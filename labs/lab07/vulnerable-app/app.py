from flask import Flask, request, make_response, abort
import sqlite3
import os
import subprocess
import logging
from pathlib import Path
import ipaddress
import ast
import operator as op

app = Flask(__name__)
app.config["DEBUG"] = True

DB_USER = "admin"
DB_PASSWORD = "SuperSecret123"
DB_PATH = "app.db"

logging.basicConfig(level=logging.DEBUG)

BASE_READ_DIR = Path("/tmp/vulnerable-app-allowed").resolve()
BASE_READ_DIR.mkdir(parents=True, exist_ok=True)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn


@app.route("/")
def index():
    return "Vulnerable lab07 app"


@app.route("/user")
def get_user():
    username = request.args.get("name", "")
    conn = get_db()
    cur = conn.cursor()
    query = f"SELECT id, name, email FROM users WHERE name = '{username}'"
    app.logger.debug("Executing query: %s", query)
    rows = cur.execute(query).fetchall()
    conn.close()
    return {"result": rows}


@app.route("/search")
def search():
    q = request.args.get("q", "")
    html = f"<h1>Results for: {q}</h1>"
    return make_response(html, 200)


@app.route("/ping")
def ping():
    """
    FIX: вместо os.system(cmd) используем subprocess.run со списком аргументов
    и валидируем host, чтобы исключить инъекции команд (RCE).
    """
    host = request.args.get("host", "127.0.0.1")

    try:
        ipaddress.ip_address(host)
    except ValueError:
        abort(400, description="Invalid host (expected IP address).")

    subprocess.run(["ping", "-c", "1", host], check=False)
    return f"Pinged {host}"


@app.route("/backup")
def backup():
    target = request.args.get("target", "/tmp/backup.sql")
    cmd = ["sh", "-c", f"pg_dump mydb > {target}"]
    subprocess.call(cmd)
    return f"Backup to {target} started"


@app.route("/read")
def read_file():
    """
    FIX: предотвращаем Path Traversal/LFI:
    - разрешаем чтение только внутри BASE_READ_DIR
    - приводим путь к realpath/resolve и проверяем, что он "под" BASE_READ_DIR
    """
    rel = request.args.get("path", "example.txt")

    if os.path.isabs(rel):
        abort(400, description="Absolute paths are not allowed.")

    candidate = (BASE_READ_DIR / rel).resolve()

    if BASE_READ_DIR not in candidate.parents and candidate != BASE_READ_DIR:
        abort(403, description="Path traversal attempt blocked.")

    if not candidate.is_file():
        abort(404, description="File not found.")

    try:
        data = candidate.read_text(encoding="utf-8", errors="replace")
        return f"<pre>{data}</pre>"
    except Exception as e:
        return str(e), 500


@app.route("/load")
def load():
    """
    FIX: убираем pickle.loads() (опасная десериализация).
    Вместо этого принимаем безопасный формат (JSON-строку) либо просто возвращаем текст.
    Для минимального изменения: принимаем hex -> bytes -> decode('utf-8') и не исполняем.
    """
    data = request.args.get("data", "")
    if not data:
        abort(400, description="Missing data.")

    try:
        raw = bytes.fromhex(data)
        text = raw.decode("utf-8", errors="replace")
        return f"Loaded data (as text): {text}"
    except ValueError:
        abort(400, description="Invalid hex-encoded data.")
    except Exception as e:
        return f"Error: {e}", 500


_ALLOWED_OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.UAdd: op.pos,
    ast.USub: op.neg,
}


def _safe_eval(expr: str) -> float:
    """
    Разрешаем только арифметику над числами: + - * / // % ** и скобки.
    Любые имена, вызовы функций, атрибуты, индексы и т.п. запрещены.
    """
    node = ast.parse(expr, mode="eval")

    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return n.value
        if isinstance(n, ast.BinOp) and type(n.op) in _ALLOWED_OPS:
            return _ALLOWED_OPS[type(n.op)](_eval(n.left), _eval(n.right))
        if isinstance(n, ast.UnaryOp) and type(n.op) in _ALLOWED_OPS:
            return _ALLOWED_OPS[type(n.op)](_eval(n.operand))
        raise ValueError("Expression contains запрещённые конструкции.")

    return _eval(node)


@app.route("/calc")
def calc():
    """
    FIX: вместо eval(expr) используем _safe_eval(),
    который допускает только арифметические AST-узлы.
    """
    expr = request.args.get("expr", "1+1")
    try:
        result = _safe_eval(expr)
        return str(result)
    except Exception:
        abort(400, description="Invalid expression.")


@app.route("/debug")
def debug():
    headers = dict(request.headers)
    env = dict(os.environ)
    return {
        "headers": headers,
        "env_sample": {k: env[k] for k in list(env)[:10]},
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
