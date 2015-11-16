from flask import Flask
app = Flask(__name__)

# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Define the WSGI application object
app = Flask(__name__)

# Load default configuration (dev)
app.config.from_object('app.config')
# Load configuration from file specified in environment
app.config.from_envvar('FLASK_CONFIG_FILE', silent=True)

# Define the database object which is imported
# by modules and controllers
# Order matters: Initialize SQLAlchemy before Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Sample HTTP error handling
#@app.errorhandler(404)
#def not_found(error):
#    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.bp_root.views import bp as bp_root
from app.bp_project.views import bp as bp_project
from app.bp_about.views import bp as bp_about
from app.bp_blog.views import bp as bp_blog
from app.bp_contact.views import bp as bp_contact

# Register blueprint(s)
app.register_blueprint(bp_root)
app.register_blueprint(bp_project)
app.register_blueprint(bp_about)
app.register_blueprint(bp_blog)
app.register_blueprint(bp_contact)

# Simple case for debugging
#@app.route('/')
#def hello_world():
#    return 'Hello World!'

# Build the database:
# import all models so that SQLAlchemy can initialize the db with create_all()
from app.bp_blog.models import Post
# This will create the database file using SQLAlchemy
# Empty url implies sqllite in-memory db which needs special handling
if app.config['DEBUG'] and app.config['SQLALCHEMY_DATABASE_URI'] != 'sqlite://':
    db.create_all()

# need to initialize sqllite in-memory db after app.run()
# https://gehrcke.de/2015/05/in-memory-sqlite-database-and-flask-a-threading-trap/
@app.before_request
def before_request():
    if app.config['DEBUG'] and app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite://':
        with app.app_context():
            # Extensions like Flask-SQLAlchemy now know what the "current" app
            # is while within this block. Therefore, you can now run........
            db.create_all()
