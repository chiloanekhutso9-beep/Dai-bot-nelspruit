from flask import Flask, request, Response
import requests, os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html><head><meta name="viewport" content="width=device-width">
    <title>Dai-bot Nelspruit | Live</title>
    <style>
        body { font-family: sans-serif; text-align:center; background:#f5f5f5; }
        .card { background: white; max-width:400px; margin:50px auto; padding:20px; border-radius:12px; }
        h1 { color: #0a7d26; }
        .badge { background: #e6f9e8; color: #0a7d26; padding:4px 8px; border-radius:8px; }
        .btn { display: block; background: #25D366; color:white; padding:12px; margin:10px 0; border-radius:8px; text-decoration:none; }
        .btn2 { background: #111; }
    </style></head><body>
    <div class="card">
        <h1>🤖 DAI BOT NELSPRUIT</h1>
        <p><span class="badge">✅ ONLINE</span></p>
        <p><b>Built by Khutso | Mbombela</b></p>
        <hr>
        <p>I solve 4 problems for learners</p>
        <ul style="text-align:left;">
            <li>📐 Maths - Step by step</li>
            <li>💻 Coding - Simple Python</li>
            <li>🌱 Life Advice</li>
            <li>📈 Trading Education</li>
        </ul>
        <a class="btn" href="https://wa.me/">WhatsApp Bot</a>
        <a class="btn btn2" href="https://1win.com/?p=zxlm">1WIN LINK ?p=zxlm</a>
        <p style="font-size:12px; color:gray;">Webhook: dai-bot-nelspruit.onrender.com<br>Status: WhatsApp Webhook READY</p>
    </div></body></html>
    """

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        # For Meta verification
        return request.args.get('hub.challenge', '')

    # POST - WhatsApp message received
    data = request.get_json()
    try:
        msg_obj = data['entry'][0]['changes'][0]['value']['messages'][0]
        phone = msg_obj['from']
        text = msg_obj['text']['body'].lower()

        if any(k in text for k in ['1win','link','bonus','register']):
            reply = "🔥 1WIN SA 🇿🇦\n✅ No VPN needed\n👉 https://1win.com/?p=zxlm\n\n1. Open in Chrome\n2. Register ZAR\n3. Deposit Ozow/Capitec\n\nType HELP if link won't open\n18+ Play responsibly"
            send_whatsapp(phone, reply)
        elif 'help' in text:
            send_whatsapp(phone, "Link fix: In WhatsApp tap 3 dots top right -> Open in browser -> Chrome. Still blocked? Turn off MTN Safe Browsing in MyMTN app.")
    except:
        pass

    return Response(status=200)

def send_whatsapp(to, body):
    token = os.getenv('WHATSAPP_TOKEN')
    phone_id = os.getenv('PHONE_ID')
    if not token or not phone_id:
        return
    requests.post(f"https://graph.facebook.com/v19.0/{phone_id}/messages",
        headers={"Authorization": f"Bearer {token}"},
        json={"messaging_product":"whatsapp","to":to,"type":"text","text":{"body":body}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
