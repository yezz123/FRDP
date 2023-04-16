# FRDP

Boilerplate code for quick docker implementation of REST API with JWT Authentication using FastAPI, PostgreSQL and PgAdmin.

## Project setup

```shell
# clone the repo
$ git clone https://github.com/yezz123/FRDP

# move to the project folder
$ cd FRDP
```

## Getting Started

### Features

| Auth              | Description                                                                     |
|-------------------|---------------------------------------------------------------------------------|
|`Login Access Token` | OAuth2 compatible token login, get an access token for future requests          |
|`Check Session`      | Test if a user is logged in by checking if a valid access token is in the header|
|`Recover Password`   | Password Recovery                                                               |
|`Reset Password`     | Reset your password                                                             |

| User                               | Description                                      |
|------------------------------------|--------------------------------------------------|
|`Create New User`                     | Create a new user                                |
|`Get Current User By Id`              | Get current user                                 |
|`Update Current User`                 | Update own user                                  |
|`Update Other User (SuperUser)`       | Update a user                                    |
|`Create User (Without Authentication)`| Create new user without the need to be logged in.|

## Environment variables

- [x] Using PostgreSQL as database server.
- [x] Using PgAdmin as database client.
- [x] Dockerized the Boilerplate code.

- Drop your own Configuration at the `docker-compose.env` file.

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

## Development 🚧

### Features

- use `hatch` to manage dependencies.
- use `pytest` to run tests.
- GitHub Actions to run tests, lints.
- Use `Dependabot` to keep dependencies up to date.
- use `pre-commit` to manage formatting and linting.
  - use `black` to format code.
  - use `ruff` to lint code.
  - use `isort` to sort imports.

### Setup environment 📦

You should create a virtual environment and activate it:

```bash
python -m venv venv/
```

```bash
source venv/bin/activate
```

And then install the development dependencies:

```bash
# Install dependencies
pip install -e .[test,lint]
```

### Run tests 🌝

You can run all the tests with:

```bash
bash scripts/test.sh
```

### Format the code 🍂

Execute the following command to apply `pre-commit` formatting:

```bash
bash scripts/format.sh
```

## License

This project is licensed under the terms of the MIT license.
