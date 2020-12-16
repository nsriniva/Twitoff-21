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

Add python buildpack before deploying?

New pipfile?


```sh
pipenv install flask flask-sqlalchemy flask-migrate
pipenv install python-dotenv tweepy spacy
pipenv install gunicorn psycopg2-binary
```


Using requirements.txt?

```sh
pipenv lock --requirements > requirements.txt
```

Different version?

No spacy?



Deploy:

```sh
git push heroku main
# git push heroku my-branch:main
```

## Testing the Model Download

```sh
heroku run "python -m twitoff.nlp_helper"
```

## Database Management

Provision the database:

```sh
heroku addons:create heroku-postgresql:hobby-dev
```

Migrate the database (need to deploy first, to reference our app code):

```sh
heroku run "FLASK_APP=twitoff flask db init"
#heroku run "FLASK_APP=twitoff flask db stamp head"
heroku run "FLASK_APP=twitoff flask db migrate"
heroku run "FLASK_APP=twitoff flask db upgrade"
```


```sh
heroku run bash

FLASK_APP=twitoff flask db init #> generates app/migrations dir
FLASK_APP=twitoff flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=twitoff flask db upgrade #> creates the specified tables
```

## Viewing

```sh
heroku open
```

## Logs

```sh
heroku logs --tail
```



Errs:

"psycopg2.errors.StringDataRightTruncation: value too long for type character varying(300)"
