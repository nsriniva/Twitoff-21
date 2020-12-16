"""Main app/routing file for Twitoff"""

from os import getenv
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request
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
        print("RESETTING THE DATABASE!")
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
        #return render_template("base.html", title="Home", users=User.query.all())
        #flash(f"Updated Users!", "success")
        return redirect("/")

    #@app.route("/update/<screen_name>")
    #@app.route("/users/<screen_name>/update")
    #def update(screen_name=None):
    #    print("UPDATING USER:", screen_name)
    #    db_user, db_tweets = add_or_update_user(screen_name)
    #    return render_template("base.html", title="Home", users=User.query.all())

    @app.route("/users/<screen_name>")
    def show(screen_name=None):
        print("SHOW USER:", screen_name)
        user = User.query.filter_by(name=screen_name).one()
        return render_template("user.html", user=user, tweets=user.tweets)

    #
    # PREDICTION ROUTES
    #

    @app.route("/predictions/new", methods=["GET"])
    def prediction_form():
        return render_template("prediction_form.html")

    @app.route("/predictions/create", methods=["POST"])
    def predict():
        print("PREDICT ROUTE...")
        print("FORM DATA:", dict(request.form))
        #> {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}
        screen_name_a = request.form["screen_name_a"]
        screen_name_b = request.form["screen_name_b"]
        tweet_text = request.form["tweet_text"]

        most_likely = "TODO" # TODO: make a prediction

        return render_template("prediction_results.html",
            screen_name_a=screen_name_a,
            screen_name_b=screen_name_b,
            tweet_text=tweet_text,
            screen_name_most_likely=most_likely
        )

    return app
