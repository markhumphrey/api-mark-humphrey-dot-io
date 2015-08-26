# mhumphrey/flask-app-template

This is an evolving personal base template for my Flask apps wrapped up in a Docker image for development and deployment.

## Usage

To build the docker image and launch the dev container:

```
docker-compose up web
```

By default the directory that docker-compose is run from will be mounted read-only as /code in the container and main.py run from that location. This allows for a dev workflow of changing the code without having to rebuild the container.

To attach a shell to the running docker container:

```
docker-compose run web "/bin/bash"
```

## Flask Directory Structure

Application is kicked off by:

```
main.py
```

Configuration is located in:

```
config.py
config_prod.py
```

Following the recommendations of:
http://flask.pocoo.org/docs/0.10/config/#development-production

Dependencies are listed in requirements.txt and are initially:
- Flask
- Flask-SQLAlchemy
- Flask-WTForms

This turtorial is used as a starting point for the code organization:
https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications

Each blueprint  is further broken out into it own module to better scale as the app grows larger.

Each blueprint has also has its own templates and static assets. I am following the current official recommendation for templates located in blueprint dirs:
http://flask.pocoo.org/docs/0.10/blueprints/#templates

## Docker Support

The Dockerfile builds from the python-2.7 base image and exposes port 8080 as specified here:

```
Dockerfile
```

Multi-container applications are defined for docker-compose here:

```
docker-compose.yml
```

The docker-compose extends feature is used to support different workflows:
https://docs.docker.com/compose/extends/

```
docker-common.yml
docker-dev.yml
docker-prod.yml
```
