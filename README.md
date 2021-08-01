![Header](.github/Header.svg)

# FRDP [![CodeFactor](https://www.codefactor.io/repository/github/bnademoverflow/frdp/badge/main)](https://www.codefactor.io/repository/github/bnademoverflow/frdp/overview/main)

Boilerplate code for quick docker implementation of REST API with JWT Authentication using FastAPI, PostgreSQL and PgAdmin ⛏.

## Getting Started

### Features

| Auth              | Description                                                                     |
|-------------------|---------------------------------------------------------------------------------|
|Login Access Token | OAuth2 compatible token login, get an access token for future requests          |
|Check Session      | Test if a user is logged in by checking if a valid access token is in the header|
|Recover Password   | Password Recovery                                                               |
|Reset Password     | Reset your password                                                             |

| User                               | Description                                      |
|------------------------------------|--------------------------------------------------|
|Create New User                     | Create a new user                                |
|Get Current User By Id              | Get current user                                 |
|Update Current User                 | Update own user                                  |
|Update Other User (SuperUser)       | Update a user                                    |
|Create User (Without Authentication)| Create new user without the need to be logged in.|

### Prerequisites

* [FastAPI](https://fastapi.tiangolo.com)
* [PostgreSQL - postgres12](https://hub.docker.com/_/postgres)
* [PgAdmin](https://hub.docker.com/r/dpage/pgadmin4)
* [jwt](https://jwt.io)

### Project setup

```sh
# clone the repo
$ git clone https://github.com/BnademOverflow/FRDP

# move to the project folder
$ cd FRDP
```

### Creating virtual environment

* Install `pipenv` a global python project `pip install pipenv`
* Create a `virtual environment` for this project

```shell
# creating pipenv environment for python 3
$ pipenv --three

# activating the pipenv environment
$ pipenv shell

# if you have multiple python 3 versions installed then
$ pipenv install -d --python 3.8

# install all dependencies (include -d for installing dev dependencies)
$ pipenv install -d
```

### Configured Enviromment

#### Database

* Using SQLAlchemy to Connect to our PostgreSQL Database
* Containerization The Database.
* Drop your PostgreSQL Configuration at the `.env.sample` and Don't Forget to change the Name to `.env`

```conf
# example of Configuration for the .env file

# Generate secret key using openssl rand -hex 32
SECRET_KEY= 4yi87D8FHRucoVyKXFUcMC/yb5YpLxz6PRX6YHm4kLU

# Email Defaut Intiger ex. 30, 60, 90
EMAIL_RESET_TOKEN_EXPIRE_HOURS= 60

# Server Default
SERVER_NAME=API
SERVER_HOST=http://localhost:8900

# Postgres default username and password
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=admin
POSTGRES_PORT=5500
POSTGRES_SERVER=localhost

PGADMIN_LISTEN_PORT=5050
PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=admin
```

### Running the Application

* To run the [Main](main.py) we need to use [uvicorn](https://www.uvicorn.org/) a lightning-fast ASGI server implementation, using uvloop and httptools.

```sh
# To run the Application under a reload enviromment use -- reload
$ uvicorn main:app --reload
```

## Running the Docker Container

* We have the Dockerfile created in above section. Now, we will use the Dockerfile to create the image of the FastAPI app and then start the FastAPI app container.

```sh
docker build
```

* list all the docker images and you can also see the image `frdp:latest` in the list.

```sh
docker images
```

* run the application at port 5000. The various options used are:

> * `-p`: publish the container's port to the host port.
> * `-d`: run the container in the background.
> * `-i`: run the container in interactive mode.
> * `-t`: to allocate pseudo-TTY.
> * `--name`: name of the container

```sh
docker container run -p 5000:5000 -dit --name FRDP frdp:latest
```

* Check the status of the docker container

```sh
docker container ps
```

## Preconfigured Packages

Includes preconfigured packages to kick start FRDP by just setting appropriate configuration.

| Package                                                      | Usage                                                            |
| ------------------------------------------------------------ | ---------------------------------------------------------------- |
| [uvicorn](https://www.uvicorn.org/)        | a lightning-fast ASGI server implementation, using uvloop and httptools.           |
| [Python-Jose](https://github.com/mpdavis/python-jose) | a JavaScript Object Signing and Encryption implementation in Python.    |
| [SQLAlchemy](https://www.sqlalchemy.org/)  | is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. |
| [starlette](https://www.starlette.io/)   | a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services.    |
| [passlib](https://passlib.readthedocs.io/en/stable/)  | a password hashing library for Python 2 & 3, which provides cross-platform implementations of over 30 password hashing algorithms         |
| [bcrypt](https://github.com/pyca/bcrypt/)               | Good password hashing for your software and your servers.    |
| [python-jose](https://python-jose.readthedocs.io/en/latest/) | The JavaScript Object Signing and Encryption (JOSE) technologies - JSON Web Signature (JWS), JSON Web Encryption (JWE), JSON Web Key (JWK), and JSON Web Algorithms (JWA).   |
| [jinja2](https://jinja.palletsprojects.com/en/3.0.x/) | a very fast and easy to use stand-alone template engine for Python.  |
| [psycopg2](https://www.psycopg.org/) | a Python PostgreSQL database adapter.  |

## [Contributing](docs/CONTRIBUTING.md)

* Join the FRDP Creator and Contribute to the Project if you have any enhancement or add-ons to create a good and Secure Project, Help any User to Use it in a good and simple way.
* See the [open issues](https://github.com/BnademOverflow/FRDP/issues) for a list of proposed features (and known issues) or [open pull request](https://github.com/BnademOverflow/FRDP/pulls) before starting work on a new feature.
* Check also [Docs](docs/README.md) for more information about FRDP.
* Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b hello/world`)
3. Commit your Changes (`git commit -m 'Add hello world'`)
4. Push to the Branch (`git push origin feature/helloworld`)
5. Open a Pull Request

## License

This project is licensed under the terms of the [Apache-2.0 License](LICENSE).
