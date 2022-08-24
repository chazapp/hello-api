# hello

!insert build + coverage badges here

A Flask API that says Hello and wishes an Happy Birthday.

## Usage

### Requirements
Python 3.10+

### Development
Clone the repository, create a virtualenv and install the dependencies:

```
$ git clone git@github.com:/chazapp/hello-api && cd hello-api
$ python -m virtualenv .venv && source .venv/bin/activate
$ pip install -r requirements.txt
```

Provide the database connection URI as an environment variable, using a `.env` file:

```
$ echo "DB_URI=sqlite:///db.sqlite" >> .env
```

Migrate your database to the latest schema:

```
$ FLASK_APP=hello/app flask db upgrade
```

Should you introduce changes to the database schema, create a migration script
and commit it to this repository:

```
$ FLASK_APP=hello/app flask db migrate
$ git add hello/migrations
$ ...
```

### Production

This repository provides a Dockerfile that runs the application in Gunicorn
for production purposes.
Provide the `DB_URI` database connection string as an environment variable in
your container orchestration engine of choice, then expose port 8000 to access
the API. 




