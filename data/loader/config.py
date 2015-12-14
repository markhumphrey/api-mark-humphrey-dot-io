# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

APP_BASE_DIR = "../../"

# Define the database - we are working with
# SQLite for this example
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
# empty path for in memory db
# SQLALCHEMY_DATABASE_URI = 'sqlite://'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123@sql/database'
# turn on query generation logging
SQLALCHEMY_ECHO = True
DATABASE_CONNECT_OPTIONS = {}

BLOG_DATA_DIR = "/code/data/raw/blog"
PROJECT_DATA_DIR = "/code/data/raw/project"
