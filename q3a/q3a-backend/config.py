# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:37:44 2017

@author: wlau
"""

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
import pdb
from pathlib import Path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
# SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join('home','wes','Documents','hk01-offsite-test','hk01','q3a','q3a-backend','q3a.sqlite')
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'q3a.sqlite'))

DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = False

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"