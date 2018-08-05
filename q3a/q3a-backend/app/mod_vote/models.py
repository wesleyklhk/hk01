# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:47:15 2017

@author: wlau
"""

from app import db
from sqlalchemy import and_
from sqlalchemy import text
from sqlalchemy import func
from uuid import uuid1
import numpy as np
import pandas as pd


# Define a User model
class Vote(db.Model):

    __tablename__ = 't_vote'

    id = db.Column(db.String(50), primary_key=True)

    vote_date  = db.Column(db.DateTime,  nullable=True)

    candidate = db.Column(db.String(10),  nullable=True)


    @staticmethod
    def find_votes():
        query = Vote.query.group_by(Vote.candidate).with_entities(Vote.candidate,func.count(Vote.candidate).label('count'))
        return query
    

print('********** model config completed')