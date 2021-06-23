from flask import Flask, render_template, request

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
    app.run(debug=True, port=5000)
