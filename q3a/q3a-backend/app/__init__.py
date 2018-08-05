#
# Import flask and template operators


from flask import Flask, render_template
import pdb

# Import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
print("__name__=" + __name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
    
    
@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)    

# Import a module / component using its blueprint handler variable (mod_auth)
#from .mod_ask import controllers as ask_module
from .mod_vote.controllers import mod_vote as vote_module


# Register blueprint(s)
app.register_blueprint(vote_module)


# Build the database:
# This will create the database file using SQLAlchemy
#db.create_all()

print('app config done')
