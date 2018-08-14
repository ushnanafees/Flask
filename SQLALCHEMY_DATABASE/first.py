import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=\
    'sqlite:///C:\\absolute\\path\\to\\foo.db' 

    #'sqlite:///' +os.path.join(basedir, 'data.sqlite')
    
    
    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)    

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column('id', db.Integer, primary_key = True) # (Column_type, Configuration for attribute)
    name = db.Column('name', db.String(64), unique = True)
    users = db.relationship('User', backref = 'role') # relationship
    
    
    def __repr__(self):
        return '<Role %r>' % self.name
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64) , unique = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles_id'))
    
    def __repr__(self):
        return '<User %r>' %self.username