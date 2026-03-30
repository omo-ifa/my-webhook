from flask import Flask, request
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_data(as_text=True)
    try:
        data = json.dumps(json.loads(data), indent=2)
    except Exception:
        pass
    with open("received.txt", "a") as f:
        f.write(f"\n\n--- {datetime.utcnow().isoformat()} ---\n")
        f.write(data)
    return "OK", 200

if __name__ == "__main__":
    app.run()
