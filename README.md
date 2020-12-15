# Twitoff-21

Flask web application to compare a Twitter Users hypothetical tweet.

## Prerequisites

  + Python 3.8
  + Pipenv (`brew install pipenv` to install on mac)
  + SQLite (should be pre-installed on most machines)

## Setup

### Setup Environment

Install package dependencies from existing Pipfile:

```sh
pipenv install
```

Activate the virtual environment:

```sh
pipenv shell
```

### Setup Spacy

Install NLP model(s):

```sh
python -m spacy download en_core_web_sm
```

### Setup the Database

Using the [`Flask-Migrate` package](https://flask-migrate.readthedocs.io/en/latest/) to simplify database creation and migration:

```sh
#pipenv install Flask-Migrate
```

```sh
FLASK_APP=twitoff flask db init #> generates app/migrations dir
FLASK_APP=twitoff flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=twitoff flask db upgrade #> creates the specified tables
```

## Configuration

Obtain [Twitter API Keys](https://developer.twitter.com), then configure environment variables accordingly:

```sh
# first, make a copy of the example env vars:
cp dotenv .env

# remember to update the ".env" file with your own Twitter API keys!
```

## Usage

```sh
FLASK_APP=twitoff flask run
```
