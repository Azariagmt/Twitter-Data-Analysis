from flask import Flask, render_template, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Tweet, db_drop_and_create_all
import os
import re


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    """ uncomment at the first time running the app """
    # db_drop_and_create_all()
    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')


    @app.route('/tweet/<int:page_num>')
    def tweet(page_num):
        tweet = Tweet.query.paginate(per_page=20, page=page_num, error_out=True)
        return render_template('tweets.html', tweet=tweet)
    
    
    @app.route("/tweets")
    def get_tweets():
        try:
            tweets = Tweet.query.order_by(Tweet.created_at).all()
            tweet=[]
            tweet=[tweet.created_at for tweet in tweets]
            return jsonify(
                {
                    "success": True,
                    "tweet name": tweet
                }
            ), 200
        except:
            abort(500)
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "server error"
        }), 500
    return app




# app = Flask(__name__)
app = create_app()

def regex_replace(text):
    return re.search("(?<=\>)(.*?)(?=\<)", text).group(0)


app.add_template_filter(regex_replace)

@app.route("/users")
def users():
    return "Users"


@app.route("/tweet-sentiments")
def sentiments():
    return render_template('sentiments.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0',debug=True, port=port)