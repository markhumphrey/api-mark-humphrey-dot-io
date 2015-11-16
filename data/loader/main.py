from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import sys

# Define the WSGI application object
app = Flask(__name__)

# Load default configuration (dev)
app.config.from_object('config')
# Load configuration from file specified in environment
app.config.from_envvar('FLASK_CONFIG_FILE', silent=True)

# TODO: Adding relative path to module path
sys.path.append(app.config["APP_BASE_DIR"])

# Build the database:
# import all models so that SQLAlchemy can initialize the db with create_all()
from app.bp_blog.models import Post
from app.bp_project.models import Project

from blog_loader import BlogLoader
from project_loader import ProjectLoader

# Define the database object which is imported
# by modules and controllers
# Order matters: Initialize SQLAlchemy before Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

if __name__ == "__main__":
    with app.app_context():
        # delete existing tables
        # need to call reflect() first for drop_all() to work
        db.reflect()
        db.drop_all()

        # initialize database
        db.create_all()

        # create all loader objects
        loaders = []
        loaders.append(BlogLoader(app.config["BLOG_DATA_DIR"]))
        loaders.append(ProjectLoader(app.config["PROJECT_DATA_DIR"]))

        # read in raw data into db models
        for loader in loaders:
            models = loader.load_models()
            for m in models:
                db.session.add(m)

        # commit records to the database
        db.session.commit()
