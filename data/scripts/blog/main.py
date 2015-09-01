from flask import Flask
app = Flask(__name__)

# Import flask
from flask import Flask

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Define the WSGI application object
app = Flask(__name__)

# Load default configuration (dev)
app.config.from_object('config')
# Load configuration from file specified in environment
app.config.from_envvar('FLASK_CONFIG_FILE', silent=True)

# Define the database object which is imported
# by modules and controllers
# Order matters: Initialize SQLAlchemy before Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Build the database:
# import all models so that SQLAlchemy can initialize the db with create_all()
#import sys
#sys.path.append('C:/full/path')
#from foo import util,bar

#import imp
#util = imp.load_source('util', 'C:/full/path/foo/util.py')

#from app.bp_blog.models import Post

from os import listdir
from os.path import isdir, isfile, join

def drop_all_years():
    pass

def insert_all_years():
    datadir = "%s/blog/" % app.config["TEST_DATA_DIR"]
    years = [ join(datadir, f) for f in listdir(datadir) if isdir(join(datadir, f)) ]
    for y in years:
        insert_year(y)

def insert_year(dir):
    posts = [ join(dir, f) for f in listdir(dir) if isfile(join(dir, f)) ]
    for p in posts:
        insert_post(p)

def insert_post(filename):
    print filename
    jsonstr = open(filename).read();
    #post_schema = PostSchema()
    #post = post_schema.loads(jsonstr).data;
    print jsonstr;

if __name__ == "__main__":
    #app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
    with app.app_context():
        #db.create_all()
        insert_all_years()
