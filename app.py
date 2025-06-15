
from flask import Flask, render_template, send_from_directory, request, redirect, url_for

app = Flask(__name__)

BOTS = {
    "sma": {
        "name": "SMA Fast and Slow, Rise and Fall",
        "price": 20,
        "filename": "SMA_Fast_and_Slow.xml"
    },
    "digits": {
        "name": "Digits Analyzer - MG",
        "price": 20,
        "filename": "Digits_Analyzer_MG.xml"
    },
    "btc": {
        "name": "Matches or Differs - With Bitcoin",
        "price": 50,
        "filename": "Matches_or_Differs_BTC.xml"
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bots")
def bots():
    return render_template("bots.html", bots=BOTS)

@app.route("/buy/<bot_id>", methods=["GET", "POST"])
def buy(bot_id):
    bot = BOTS.get(bot_id)
    if not bot:
        return "Bot not found", 404
    if request.method == "POST":
        return redirect(url_for("success", bot_id=bot_id))
    return render_template("buy.html", bot=bot, bot_id=bot_id)

@app.route("/success/<bot_id>")
def success(bot_id):
    bot = BOTS.get(bot_id)
    if not bot:
        return "Bot not found", 404
    return render_template("success.html", bot=bot, bot_id=bot_id)

@app.route("/download/<bot_id>")
def download(bot_id):
    bot = BOTS.get(bot_id)
    if not bot:
        return "Bot not found", 404
    return send_from_directory("static/bots", bot["filename"], as_attachment=True)

if __name__ == "__main__":
   app.run(debug=True)
