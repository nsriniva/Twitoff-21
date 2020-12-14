"""Main app/routing file for Twitoff"""

from flask import Flask, render_template
from .models import DB, User, Tweet, insert_example_users


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)

    # TODO - make rest of application

    @app.route('/')
    def root():
        DB.drop_all()
        DB.create_all()
        insert_example_users()

        # SQL equivalent = "SELECT * FROM user;"
        users = User.query.all()
        return render_template('base.html', title="Home", users=users)

    return app
