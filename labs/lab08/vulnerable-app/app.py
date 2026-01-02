from flask import (
    Flask,
    request,
    make_response,
    render_template_string,
    session,
)
import sqlite3
import os
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

DB_PATH = os.environ.get("APP_DB_PATH", "app.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            role TEXT
        )
        """
    )
    cur.execute("DELETE FROM users")
    cur.executemany(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        [
            ("admin", "admin123", "admin"),
            ("user", "user123", "user"),
        ],
    )
    conn.commit()
    conn.close()


@app.after_request
def security_headers(response):
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self'; "
        "img-src 'self'; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "frame-ancestors 'none'"
    )
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Permissions-Policy"] = (
        "geolocation=(), microphone=(), camera=(), payment=()"
    )
    response.headers["Server"] = "Application"
    return response


@app.route("/")
def index():
    html = """
    <h1>DAST Demo App (Hardened)</h1>
    <ul>
      <li><a href="/echo?msg=Hello">Echo</a></li>
      <li><a href="/search">Search (POST)</a></li>
      <li><a href="/login">Login</a></li>
      <li><a href="/profile">Profile</a></li>
      <li><a href="/admin">Admin</a></li>
      <li><a href="/files/">Files</a></li>
    </ul>
    """
    resp = make_response(html)
    resp.set_cookie(
        "session_id",
        secrets.token_hex(16),
        httponly=True,
        samesite="Strict",
    )
    return resp


@app.route("/echo")
def echo():
    msg = request.args.get("msg", "")
    template = """
    <h2>Echo</h2>
    <p>Message: {{ msg }}</p>
    <a href="/">Back</a>
    """
    return render_template_string(template, msg=msg)


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template_string(
            """
            <h2>Search user</h2>
            <form method="post">
              <input name="username">
              <button>Search</button>
            </form>
            <a href="/">Back</a>
            """
        )

    username = request.form.get("username", "")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    rows = cur.execute(
        "SELECT id, username, role FROM users WHERE username = ?",
        (username,),
    ).fetchall()
    conn.close()

    return render_template_string(
        """
        <h2>Result</h2>
        {% if rows %}
          <ul>
          {% for id, u, r in rows %}
            <li>{{ id }} – {{ u }} ({{ r }})</li>
          {% endfor %}
          </ul>
        {% else %}
          <p>No results</p>
        {% endif %}
        <a href="/">Back</a>
        """,
        rows=rows,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template_string(
            """
            <h2>Login</h2>
            <form method="post">
              <input name="username">
              <input name="password" type="password">
              <button>Login</button>
            </form>
            <a href="/">Back</a>
            """
        )

    username = request.form.get("username", "")
    password = request.form.get("password", "")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    row = cur.execute(
        "SELECT username, role FROM users WHERE username=? AND password=?",
        (username, password),
    ).fetchone()
    conn.close()

    if not row:
        return "<h2>Invalid credentials</h2><a href='/login'>Try again</a>"

    session["user"] = row[0]
    session["role"] = row[1]

    return f"<h2>Welcome {row[0]}</h2><a href='/'>Home</a>"


@app.route("/profile")
def profile():
    return render_template_string(
        """
        <h2>Profile</h2>
        <p>User: {{ user }}</p>
        <p>Role: {{ role }}</p>
        <a href="/">Back</a>
        """,
        user=session.get("user", "guest"),
        role=session.get("role", "guest"),
    )


@app.route("/admin")
def admin():
    if session.get("role") != "admin":
        return "<h2>Forbidden</h2>", 403

    return """
    <h2>Admin panel</h2>
    <ul>
      <li>DEBUG: false</li>
      <li>FEATURE_FLAG: hardened</li>
    </ul>
    <a href="/">Back</a>
    """


@app.route("/files/")
@app.route("/files/<path:subpath>")
def files(subpath=""):
    base = os.path.join(os.path.dirname(__file__), "files")
    full = os.path.abspath(os.path.join(base, subpath))

    if not full.startswith(base):
        return "<h2>Forbidden</h2>", 403

    if not os.path.exists(full):
        return "<h2>Not found</h2>", 404

    if os.path.isdir(full):
        entries = os.listdir(full)
        return render_template_string(
            """
            <h2>Files</h2>
            <ul>
            {% for e in entries %}
              <li><a href="{{ e }}">{{ e }}</a></li>
            {% endfor %}
            </ul>
            <a href="/">Back</a>
            """,
            entries=entries,
        )

    with open(full, "r", errors="ignore") as f:
        return f"<pre>{f.read()}</pre>"


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8080, debug=False)
