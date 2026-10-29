from flask import Flask, request
import requests

app = Flask(__name__)

PHONE_NUMBER_ID = "1321460681061618"
ACCESS_TOKEN = "EAAZAqI1HNwH0BSZBkdYZBLLdfUxWu2ZAtWzEZB9ZC9ZC9ZC"  # PASTE YOUR FULL TOKEN HERE
VERIFY_TOKEN = "Khutso123"

@app.route("/", methods=["GET"])
def home():
    return "Dai bot live - 1win"

@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    chall = request.args.get("hub.challenge")
    if mode == "subscribe" and token == VERIFY_TOKEN:
        return chall, 200
    return "Forbidden", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    try:
        if data.get("object") == "whatsapp_business_account":
            for entry in data.get("entry", []):
                for change in entry.get("changes", []):
                    msgs = change.get("value", {}).get("messages", [])
                    if msgs:
                        frm = msgs[0].get("from")
                        url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
                        hdr = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}
                        payload = {
                            "messaging_product": "whatsapp",
                            "to": frm,
                            "type": "text",
                            "text": {"body": "Dai 🔥 Join 1win: https://1win.com/?p=zxlm"}
                        }
                        requests.post(url, headers=hdr, json=payload)
    except Exception as e:
        print(e)
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
