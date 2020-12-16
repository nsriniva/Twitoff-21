# Deployer's guide


Install production dependencies:

```sh
pipenv install gunicorn psycopg2-binary
```

Make a Procfile:

    web: gunicorn twitoff:APP -t 120


## Server Management

Create the server:

```sh
heroku create twitoff-21 # you'll need to choose your own name instead of twitoff-21
```

Configure the server:

```sh
heroku config:set FLASK_ENV="production"
heroku config:set TWITTER_API_KEY="______________"
heroku config:set TWITTER_API_KEY_SECRET="__________"
```

## Deploying

```sh
git push heroku main
# git push heroku my-branch:main
```

## Database Management

Provision the database:

```sh
heroku addons:create heroku-postgresql:hobby-dev
```

Migrate the database (need to deploy first, to reference our app code):

```sh
heroku run "FLASK_APP=web_app flask db init"
#heroku run "FLASK_APP=web_app flask db stamp head"
heroku run "FLASK_APP=web_app flask db migrate"
heroku run "FLASK_APP=web_app flask db upgrade"
```
