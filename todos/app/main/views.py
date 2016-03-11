from datetime import datetime
import json
from flask import render_template, redirect, url_for, abort, flash, request, current_app, make_response, jsonify, session
from flask.ext.sqlalchemy import get_debug_queries
from flask.ext.httpauth import HTTPBasicAuth
from . import main
#from .from import TodoForm
from .. import db
from ..models import Todo
#from app.exceptions import CalidationError

auth = HTTPBasicAuth()

@main.route('/', methods=['GET'])
def index():
    return render_template('show_entries.html')


@main.route('/todos/api/login/todos', methods=['GET','POST'])
def login():
    if not request.json or not 'username' in request.json:
        abort(400)
    message = {
        'username': request.json.get('username'),
        'password': request.json.get('password'),
        'done': False
    }
    ps = {
        'done': False,
        'message': None,
        'title': None,
        'body': None
    }
    user = Todo.query.filter_by(user=message['username']).first()
    if user is None:
        ps['message'] = 'Invalid username or Invalid password'
    else:
        user_password = Todo.query.filter_by(user=message['username']).first().password
        if user_password == message['password']:
            ps['message'] = 'Login success!'
            ps['done'] = True
            session['log_up'] = True
            session['username'] = message['username']
            session['password'] = message['password']
        else:
            ps['message'] = 'Invalid usernaem or Invalid password'
    return jsonify({'json':ps})


@main.route('/todos/api/logup/todos', methods=['GET','POST'])
def logup():
    #print type(request.json)
    if not request.json:
        abort(400)
    #import pdb;pdb.set_trace()
    inform = {
        'username': request.json['username'],
        'password': request.json['password'],
        'done': False
    }
    fs = {
        'done': False,
        'message': None
    }
    user = Todo.query.filter_by(user=inform['username']).first()
    if user is None:
        user = Todo(user=inform['username'],password=inform['password'])
        db.session.add_all([user])
        db.session.commit()
        fs['message'] = 'Logup success'
        fs['done'] = True
    else:
        fs['message'] = 'Sorry username had exit'
    return jsonify({'logup': fs})

@main.route('/todos/api/logout/todos', methods=['GET','POST'])
def logout():
    if not request.json:
        abort(400)
    result = {
        'done': False
    }
    if request.json['done']:
        result['done'] = True
    return jsonify({'logout':result})

@main.route('/todos/api/update/todos', methods=['GET','POST'])
def update():
    if session.get('log_in'):    
        message = {
            'title': None,
            'body': None,
            'done': False
        }
        results = {
            'done':False
        }
        if request.json['done']:
            message['title'] = request.json['title']
            table_title = Todo.query.filter_by(title=message['title']).first()
            if table_title is None:
                message['body'] = request.json['body']
                message['done'] = True
                article = Todo(title=message['title'],body=message['body'],done=message['done'])
                db.session.add_all([article])
                db.session.commit()
                results['done'] = True
    return jsonify({'update':results})
@main.route('/todos/api/change/todos',methods=['GET','POST'])
def change():
    if session.get('log_in'):
        message = {
            'title':None,
            'change_title':None,
            'change_body':None,
            'done':False,
            'which':None
        }
        results = {
            'done':False
        }
        if request.json['done']:
            message['title'] = request.json['title']
            table_title = Todo.query.filter_by(title=message['title']).first()
            if table_title:
                if message['which'] == "change_title":
                    change_title = request.json['change_title']
                    db.session.query.filter_by(title=message['title']).update({"title":change_title})
                    db.session.commit
                    results['done'] = True
                elif message['which'] == "change_body":
                    change_body = request.json['change_body']
                    db.session.query.filter_by(title=message['title']).update({"body":change_title})
                    db.session.commit
                    results['done'] = True
    return jsonify({'change':results})

@main.route('/todos/api/delete/todos',methods=['GET','POST'])
def delete():
    if session.get('log_in'):
        message = {
            'title':None
        }
        results = {
            'done':False
        }
        if request.json['done']:
            message['title'] = request.json['title']
            table_title = Todo.query.filter_by(title=message['title']).first()
            if table_title:
                db.session.delete(message['title'])
                db.session.commit()
                results['done'] = True
    return jsonify({'delete':results})
