from flask import Flask, request, Response
import os
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html><head><meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Dai-bot Nelspruit | Live</title>
    <style>
        body { font-family: sans-serif; text-align: center; background:#f5f5f5; padding:20px; }
        .card { background: white; max-width:400px; margin:auto; padding:20px; border-radius:16px; box-shadow:0 4px 12px rgba(0,0,0,0.1); }
        h1 { color: #0a7d26; }
        .badge { background: #e6f9e8; color: #0a7d26; padding:4px 10px; border-radius:20px; }
        .btn { display: block; background: #0a7d26; color: white; padding:12px; border-radius:8px; text-decoration:none; margin:10px 0; font-weight:bold; }
        .btn2 { background: #111; }
    </style></head><body>
    <div class="card">
        <h1>🤖 DAI BOT NELSPRUIT</h1>
        <p><span class="badge">✅ ONLINE</span></p>
        <p><b>Built by Khutso | Mbombela</b></p>
        <hr>
        <p>I solve 4 problems for learners:</p>
        <ul style="text-align:left;">
            <li>📐 Maths - Step by step</li>
            <li>💻 Coding - Simple Python</li>
            <li>🌱 Life Advice</li>
            <li>📈 Trading Education</li>
        </ul>
        <a class="btn" href="https://wa.me/27684306386?text=hi">💬 Chat on WhatsApp</a>
        <a class="btn btn2" href="https://1win.com/?p=zxlm">🔥 1WIN LINK ?p=zxlm</a>
        <p style="font-size:12px; color:gray">dai-bot-nelspruit.onrender.com</p>
    </div></body></html>
    """

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        return request.args.get('hub.challenge', '')
    data = request.get_json()
    try:
        entry = data['entry'][0]['changes'][0]['value']
        if 'messages' in entry:
            msg = entry['messages'][0]
            phone = msg['from']
            text = msg.get('text', {}).get('body', '').lower()
            reply = "🤖 *DAI BOT NELSPRUIT* 🔥\n\nHere is your link 👇\n👉 https://1win.com/?p=zxlm\n\n✅ No VPN - Open in Chrome\n✅ Register ZAR\n✅ Deposit Ozow / Capitec\n\nReply HELP if blocked"
            if 'help' in text:
                reply = "Link blocked? WhatsApp > 3 dots > Open in browser > Chrome. Turn off MTN Safe Browsing. Then: https://1win.com/?p=zxlm"
            send_whatsapp(phone, reply)
    except Exception as e:
        print("Error:", e)
    return Response(status=200)

def send_whatsapp(to, body):
    token = os.getenv('WHATSAPP_TOKEN')
    phone_id = os.getenv('PHONE_ID')
    if not token or not phone_id:
        return
    url = f"https://graph.facebook.com/v19.0/{phone_id}/messages"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"messaging_product":"whatsapp","to":to,"type":"text","text":{"body":body}}
    requests.post(url, headers=headers, json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
