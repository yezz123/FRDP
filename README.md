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

* Create a virtual environment using virtualenv.

```shell
# creating virtual environment
$ virtualenv venv

# activate virtual environment
$ source venv/bin/activate

# install all dependencies
$ pip install -r requirements.txt
```

### Environment variables

* [x] Using PostgreSQL as database server ⛏.
* [x] Using PgAdmin as database client ⛏.
* [x] Dockerized the Boilerplate code ⛏.

* Drop your own Configuration at the `.env.sample` and Don't Forget to change the Name to `.env` (`$ cp .env.sample .env`).

```conf
# Backend API Configuration
PROJECT_NAME=
DOMAIN=

# Security Configuration
SECRET_KEY=
USERS_OPEN_REGISTRATION=
EMAIL_RESET_TOKEN_EXPIRE_HOURS=

# Server Settings
SERVER_NAME=
SERVER_HOST=

# Postgres default username and password
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
POSTGRES_PORT=
POSTGRES_SERVER=

# PGADMIN_LISTEN_PORT=
PGADMIN_DEFAULT_EMAIL=
PGADMIN_DEFAULT_PASSWORD=
```

## Running the Docker Container

* We have the Dockerfile created in above section. Now, we will use the Dockerfile to create the image of the FastAPI app and then start the FastAPI app container.
* Using a preconfigured `Makefile` tor run the Docker Compose:

```sh
# Pull the latest image
$ make pull

# Build the image
$ make build

# Run the container
$ make start
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
