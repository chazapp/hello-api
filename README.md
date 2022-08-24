# Hello API

![Test workflow](https://github.com/chazapp/hello-api/actions/workflows/tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/chazapp/hello-api/branch/master/graph/badge.svg?token=R8F37BGZZM)](https://codecov.io/gh/chazapp/hello-api)

A Flask API that says Hello and wishes an Happy Birthday.

Currently available methods:

```
GET /hello/<username>
PUT /hello/<username> + {"birthday": "YYYY-MM-DD"}
GET /health
GET /metrics
```


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

Run the application:
```
$ FLASK_APP=hello/app.py flask run
```

Run the test suite:

```
$ pytest
```

### Production

This repository provides a Dockerfile that runs the application in Gunicorn
for production purposes. The production system should use a Postgres > v14 database.  
The Docker container is freely available at `ghcr.io/chazapp/hello-api:<release>`.  

Provide the `DB_URI` database connection string as an environment variable in
your container orchestration engine of choice, then expose port 8000 to access
the API. 
  
A Kubernetes `kustomize` package is available in this repository's `k8s/` directory.