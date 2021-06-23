from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/users")
def users():
    return "Users"


@app.route("/tweet-sentiments")
def sentiments():
    return render_template('sentiments.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0',debug=True, port=port)