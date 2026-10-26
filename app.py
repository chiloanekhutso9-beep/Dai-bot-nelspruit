from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return """
    <html><body style='font-family:Arial;text-align:center;padding:50px'>
    <h1>🤖 DAI BOT NELSPRUIT IS LIVE! 🇿🇦</h1>
    <h2 style='color:green'>✅ ONLINE 24/7</h2>
    <p>WhatsApp Webhook: READY</p>
    <p>Built by Khutso | Mbombela</p>
    <hr>
    <p>Your bot link: <b>dai-bot-nelspruit.onrender.com/webhook</b></p>
    </body></html>
    """
@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if mode == 'subscribe' and token == 'dai123':
            return challenge, 200
        return "Verification failed", 403
    data = request.get_json()
    print("Incoming:", data)
    return jsonify({"status":"received"}), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
