"""Retrieve Tweets, embeddings, and push to our database"""
from os import getenv
from dotenv import load_dotenv
import tweepy  # to interact with the twitter API
import spacy  # will use later
from .models import DB, Tweet, User

load_dotenv() # actually load the env vars :-D

TWITTER_AUTH = tweepy.OAuthHandler(getenv("TWITTER_API_KEY"), getenv("TWITTER_API_KEY_SECRET"))
TWITTER = tweepy.API(TWITTER_AUTH)

nlp = spacy.load("my_model")

def vectorize_tweet(tweet_text):
    return nlp(tweet_text).vector

def add_or_update_user(screen_name):

    twitter_user = TWITTER.get_user(screen_name)
    print("USER:", screen_name, type(twitter_user))

    statuses = TWITTER.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    print("STATUSES COUNT:", len(statuses))

    # get existing user from the db or initialize a new one:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user.name = screen_name
    if statuses:
        db_user.newest_tweet_id = statuses[0].id
    DB.session.add(db_user)
    DB.session.commit()

    for status in statuses:
        print(status.full_text)
        # get existing tweet from the db or initialize a new one:
        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
        db_tweet.user_id = status.author.id # or db_user.id
        db_tweet.text = status.full_text
        db_tweet.vect = vectorize_tweet(status.full_text)
        DB.session.add(db_tweet)

    DB.session.commit()
