from flask import Flask, request
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_data(as_text=True)
    
    # Try to pretty-print if it's JSON, otherwise store raw
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
```

**`requirements.txt`**
```
flask
gunicorn
```

---

## Step 2 — Deploy to Railway

1. Push the folder to a GitHub repo
2. Go to [railway.app](https://railway.app), create a new project → **Deploy from GitHub repo**
3. Railway will auto-detect Flask and deploy it
4. In Railway's settings, set the **start command** to:
```
   gunicorn app:app
```
5. Railway gives you a public URL like `https://your-app.up.railway.app`

Your webhook URL will be: `https://your-app.up.railway.app/webhook`

---

## Step 3 — Point Skyvern at it

In Skyvern's workflow or task settings, set the webhook callback URL to:
```
https://your-app.up.railway.app/webhook