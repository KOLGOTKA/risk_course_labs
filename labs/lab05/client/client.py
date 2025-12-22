import sys
import time
import requests

SERVER_URL = "http://server:8000"
RETRIES = 30
SLEEP_S = 1.0
TIMEOUT_S = 3.0


def colorful_print(text):
    colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m"]
    reset = "\033[0m"
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(color + char + reset)
        sys.stdout.flush()
        time.sleep(0.02)
    print()


def wait_for_server():
    health_url = SERVER_URL.rstrip("/") + "/health"

    for _ in range(RETRIES):
        try:
            r = requests.get(health_url, timeout=TIMEOUT_S)
            if r.status_code == 200:
                return True
        except requests.RequestException:
            pass

    return False


if __name__ == "__main__":
    if not wait_for_server():
        print(f"ERROR: server is not reachable: {SERVER_URL}", file=sys.stderr)
        sys.exit(1)

    response = requests.get(SERVER_URL.rstrip("/") + "/", timeout=TIMEOUT_S)
    response.raise_for_status()
    colorful_print(response.text)
