# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
# empty path for in memory db
SQLALCHEMY_DATABASE_URI = 'sqlite://'
# turn on query generation logging
SQLALCHEMY_ECHO=True
DATABASE_CONNECT_OPTIONS = {}
#TEST_DATA_DIR=os.path.abspath("%s/data/" % os.path.join(BASE_DIR, os.pardir))
TEST_DATA_DIR="/code/data"
