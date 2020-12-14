"""SQLAlchemy models and utility functions for Twitoff"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


# User Table (in relational database the table is "user")
class User(DB.Model):
    """Twitter users corresponding to Tweets"""
    # primary id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    # name column
    name = DB.Column(DB.String, nullable=False)

    def __repr__(self):
        return "<User: {}>".format(self.name)


# Tweet Table (in relational database the table is "tweet")
class Tweet(DB.Model):
    """Tweet Text and Data"""
    # primary id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    # text column of character length 300 (unicode)
    text = DB.Column(DB.Unicode(300))
    # foreign key - user.id
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey(
        'user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return "<Tweet: {}>".format(self.text)


def insert_example_users():
    """Will get error if ran twice since data already exist"""
    nick = User(id=1, name="nwdelafu")
    elonmusk = User(id=2, name="elonmusk")
    DB.session.add(nick)  # adds nick User
    DB.session.add(elonmusk)  # adds elon User
    DB.session.commit()  # commits all
