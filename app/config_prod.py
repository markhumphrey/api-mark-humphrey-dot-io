# Define variables based to Flask app.run
#HOST = '0.0.0.0'
#PORT = 8080
# Statement for enabling the development environment
DEBUG = FALSE

# Define the database - we are working with
# SQLite for this example
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
# empty path for in memory db
#SQLALCHEMY_DATABASE_URI = 'sqlite://'
# turn on query generation logging
SQLALCHEMY_ECHO=False
