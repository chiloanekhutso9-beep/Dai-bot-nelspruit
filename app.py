from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Dai-bot Nelspruit | Live</title>
        <style>
            body { font-family: sans-serif; background: #f5f7f5; text-align: center; padding: 20px; }
            .card { background: white; max-width: 400px; margin: 30px auto; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
            h1 { color: #0a7d26; }
            .badge { background: #e6f9e8; color: #0a7d26; padding: 8px 15px; border-radius: 20px; font-weight: bold; }
            .btn { display: block; background: #25D366; color: white; padding: 15px; margin: 12px 0; border-radius: 12px; text-decoration: none; font-weight: bold; }
            .btn2 { background: #111; }
            ul { text-align: left; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🤖 DAI BOT NELSPRUIT</h1>
            <p><span class="badge">✅ ONLINE 24/7</span></p>
            <p><b>Built by Khutso | Mbombela 🇿🇦</b></p>
            <hr>
            <p>I solve 4 problems for learners:</p>
            <ul>
                <li>📐 Maths - Step by step</li>
                <li>💻 Coding - Simple Python</li>
                <li>🌱 Life Advice</li>
                <li>📈 Trading Education (with safety warnings)</li>
            </ul>
            <a class="btn" href="https://wa.me/YOURNUMBER">Chat on WhatsApp</a>
            <a class="btn btn2" href="https://github.com/chiloanekhutso9-beep/Dai-bot-nelspruit">View on GitHub</a>
            <p style="font-size:12px; color: #777; margin-top:20px;">
                Webhook: dai-bot-nelspruit.onrender.com/webhook<br>
                Status: WhatsApp Webhook READY
            </p>
        </div>
    </body>
    </html>
    """

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return request.args.get('hub.challenge', '')
    return Response(status=200)

if __name__ == '__main__':
    app.run()
    """

After you paste, Render will auto-redeploy in 2 mins and then your link will look BEAUTIFUL instead of just text.

Tell me when you've pasted — I'll check if it updated!
