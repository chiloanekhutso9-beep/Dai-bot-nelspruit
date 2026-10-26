from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Dai Bot Nelspruit is LIVE!"

@app.route('/webhook', methods=['GET', 'POST'])
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
    
    # Auto reply logic
    try:
        # Here you can add your Nelspruit delivery logic
        return jsonify({"status": "received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
