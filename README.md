# Python Backend Take-home assignment

This application implements an Endpoint API, for the purpose of finding the risk profile based on the user's information
sent by a JSON.

## Endpoints documentation

All information regarding the endpoints, are documented within the API on the route [/docs](http://localhost:8080/docs)

## Initialization of the development environment

There are two ways to rotate the environment, a docker life and another using a virtualenv. Instructions on how to
perform each is described below:

Both versions will upload a service to the url [localhost:8000](http://localhost:8000). Practical way of checking
whether the service is working is to access the url: [localhost:8000/docs](http://localhost:8000/docs)

### Docker

First, check if you have [Docker](https://docs.docker.com/get-docker/) installed on the machine and
the [Docker-compose](https://docs.docker.com/compose/install/).

In the project's root folder, run the following code:

```shell
foo@bar: $ docker-compose up -d --build
```

### Virtualenv

To start the environment with using a virtualenv, you just need to check if it has installed
[Python 3.9](https://www.python.org/downloads/) or higher and the [Pipenv](https://pypi.org/project/pipenv/) tool. If
you do not have pipenv installed, simply run the following command:

```shell
foo@bar: $ pip install pipenv
```

After installed, in the root folder, run the command:

```shell
foo@bar: $ pipenv install --dev
```

After installed, this command to start the service:

```shell
foo@bar: $ pipenv run dev
```

or

```shell
foo@bar: $ pipenv shell && python main.py
```

## Good practices in development

This project is set up with some hooks to streamline and maintain the code standard during development, but for that you
need to configure [git-hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks).

##### Installing the git-hooks

Before anything else, make sure you have installed the plugin [pre-commit](https://pre-commit.com/#install). If you have
initialized the environment via **Virtualenv**, it must already be installed.

---
**NOTE**

It may be necessary to access your environment with the command `pipenv shell` to make available the
`pre-commit` command
---

After it is installed, run the command to install the hooks into your repository:

```shell
foo@bar: $ pre-commit install
```

With that configured, whenever a commit is made, the pre-commit will execute the tests, check the staging files, analyze
code patterns and correct them, in addition to checking the typing hints.

### MyPy

Also configured in the project is the plugin called [mypy](https://mypy.readthedocs.io/), where it assists in checking
**TypeHints**.
It will be executed automatically on every commit, if it has been configured
o [pre-commit](https://pre-commit.com/#install), but it can also be run manually with the command:

```shell
foo@bar: $ mypy .
```

### Tests

Tests will be performed automatically on every commit, if configured the [pre-commit](https://pre-commit.com/#install),
but it can also be executed manually by running the command:

```shell
foo@bar: $ pytest
```

## Technical decisions

The use of the framework called FastAPI, brings some benefits to the project, for example:

- High performance;
- API documentation generated automatically;
- Induces the use of TypeHints;

### TypeHints

This new feature available in Python 3.6+ facilitates development and reduces the time for debugging applications, as
apply weak typing. It also helps new programmers who are not used to the project. More goes up this resource
here: https://docs.python.org/3/library/typing.html
