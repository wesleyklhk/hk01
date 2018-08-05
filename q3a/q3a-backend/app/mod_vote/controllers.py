# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:46:53 2017

@author: wlau
"""
# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from flask import jsonify
from flask import Flask, current_app
# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

from .models import Vote

import pdb
from app import db
from uuid import uuid1
import datetime


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_vote = Blueprint('vote', __name__, url_prefix='/vote')

# Set the route and accepted methods
@mod_vote.route('', methods=['POST'])
def vote():
    try:
        data = request.get_json()
        vote = Vote()
        vote.id = str(uuid1())
        vote.vote_date = datetime.datetime.now()
        vote.candidate = data['candidate']
        db.session.add(vote)
        db.session.commit()
        return jsonify({'status':'SUCCESS'})
    except:
        return jsonify({'status':'FAIL'})
    

@mod_vote.route('', methods=['GET'])
def get_votes():
    try:
        result = {'status':'SUCCESS'}
        query = Vote.find_votes()
        votes = query.all()
        result['result'] = [{'candidate':v[0],'votes':v[1]} for v in votes]
        return jsonify(result)
    except:
        return jsonify({'status':'FAIL'})

@mod_vote.route('/mark', methods=['GET'])
def list_all_answers():
    unmarked = Answer.find_answer_bundle_id_by_marked(marked=False)
    return render_template('answers.html',unmarked=unmarked)

@mod_vote.route('/mark/<answer_bundle_id>', methods=['GET'])
def answer(answer_bundle_id):
    all_in_ones = AllInOne.find_by_answer_bundle_id(answer_bundle_id)
    return render_template('answer.html',all_in_ones=all_in_ones)   

