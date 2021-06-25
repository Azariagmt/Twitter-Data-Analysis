import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
'''
setup_db(app):
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    database_name ='twitter-covid-data-analysis'
    default_database_path= "postgres://{}:{}@{}/{}".format('postgres', 'Familyguy12!', 'localhost:5432', database_name)
    database_path = os.getenv('DATABASE_URL', default_database_path)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
'''
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    created_at = Column(String(100))
    source = Column(String(100))
    polarity = Column(db.Text)
    subjectivity = Column(db.Text)
    original_text = Column(db.Text)
    lang = Column(String(5))
    favorite_count = Column(db.Text)
    retweet_count = Column(db.Text)
    original_author = Column(String(30))
    followers_count = Column(db.Text)
    friends_count = Column(db.Text)
    possibly_sensitive = Column(String(5))
    hashtags = Column(db.ARRAY(String))
    user_mentions = Column(db.ARRAY(String))
    location = Column(db.String(30))
    # title = Column(String(80), unique=True)
    # release_date = Column(db.DateTime)
    def __init__(self, source, created_at, polarity, subjectivity, original_text, lang, favorite_count, retweet_count, original_author, followers_count, friends_count, possibly_sensitive, hashtags, user_mentions, location):
        self.source = source
        self.created_at = created_at
        self.polarity = polarity
        self.subjectivity = subjectivity
        self.original_text = original_text
        self.lang = lang
        self.favorite_count = favorite_count
        self.retweet_count = retweet_count
        self.original_author = original_author
        self.followers_count = followers_count
        self.friends_count = friends_count
        self.possibly_sensitive = possibly_sensitive
        self.hashtags = hashtags
        self.user_mentions = user_mentions
        self.location = location
    def details(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'source': self.source,
            'polarity': self.polarity,
            'subjectivity': self.subjectivity,
            'original_text': self.original_text,
            'lang': self.lang,
            'favorite_count': self.favorite_count,
            'retweet_count': self.retweet_count,
            'original_author': self.original_author,
            'followers_count': self.followers_count,
            'friends_count': self.friends_count,
            'possibly_sensitive': self.possibly_sensitive,
            'hashtags': self.hashtags,
            'user_mentions': self.user_mentions,
            'location': self.location
        }
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()