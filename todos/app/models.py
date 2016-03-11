from datetime import datetime
from . import db

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column('id',db.Integer,primary_key = True)
    user = db.Column(db.String(24),unique=True,index=True)
    password = db.Column(db.String(20),index=True)
    users = db.relationship('Page', backref='tod')



class Page(db.Model):
    __tablename__ = 'page'
    id = db.Column('id',db.Integer,primary_key=True)
    title = db.Column(db.String(100),unique=True,index=True)
    body = db.Column(db.String(10000))
    done = db.Column(db.Boolean)
    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'))