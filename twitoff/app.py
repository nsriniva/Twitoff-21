"""Main app/routing file for Twitoff"""

from os import getenv
from dotenv import load_dotenv
from flask import Flask, render_template
from .twitter import add_or_update_user
from .models import DB, User, Tweet, migrate

load_dotenv() # actually load the env vars :-D

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)
    migrate.init_app(app, DB)

    #
    # ADMIN ROUTES
    #

    @app.route("/reset")
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template("base.html", title="Home")

    #
    # USER ROUTES
    #

    @app.route('/')
    def root():
        # SQL equivalent = "SELECT * FROM user;"
        return render_template("base.html", title="Home", users=User.query.all())

    @app.route("/update")
    def update_all():
        # consider moving this logic into our twitter module. we want to keep these routes "skinny"
        print("SEEDING USERS...")
        EXAMPLE_USERS = ["elonmusk", "justinbieber", "s2t2"]
        for screen_name in EXAMPLE_USERS:
            print(screen_name)
            add_or_update_user(screen_name)
        return render_template("base.html", title="Home", users=User.query.all())

    #@app.route("/update/<screen_name>")
    #def update(screen_name=None):
    #    print("UPDATING USER:", screen_name)
    #    db_user, db_tweets = add_or_update_user(screen_name)
    #    return render_template("base.html", title="Home", users=User.query.all())

    @app.route("/users/<screen_name>")
    def show(screen_name=None):
        print("SHOW USER:", screen_name)
        user = User.query.filter_by(name=screen_name).one()
        return render_template("user.html", user=user, tweets=user.tweets)

    return app
