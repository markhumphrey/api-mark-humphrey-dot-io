# Define variables based to Flask app.run
HOST = '0.0.0.0'
PORT = 8080
# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
# empty path for in memory db
#SQLALCHEMY_DATABASE_URI = 'sqlite://'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123@mysql/database'
# turn on query generation logging
SQLALCHEMY_ECHO=True
DATABASE_CONNECT_OPTIONS = {}
TEST_DATA_DIR=os.path.abspath("%s/data/" % os.path.join(BASE_DIR, os.pardir))

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
