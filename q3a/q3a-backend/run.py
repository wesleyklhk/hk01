# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:37:37 2017

@author: wlau
"""

# Run a test server.
from app import app
print("run.py __name__ = " + __name__)
app.run(host='0.0.0.0', port=8080, debug=True)