"""Main app/routing file for Twitoff"""

from os import getenv
from flask import Flask, render_template
from .twitter import add_or_update_user
from .models import DB, User, Tweet, migrate


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)
    migrate.init_app(app, DB)

    # TODO - make rest of application

    @app.route('/')
    def root():
        # SQL equivalent = "SELECT * FROM user;"
        users = User.query.all()
        return render_template('base.html', title="Home", users=users)

    @app.route("/update")
    def update():
        add_or_update_user("elonmusk")
        return render_template("base.html", title="Home", users=User.query.all())

    @app.route("/reset")
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template("base.html", title="Home")

    return app
