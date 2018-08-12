#https://www.youtube.com/watch?v=k-NSNUKk1Kw&list=PLXmMXHVSvS-Db9KK1LA7lifcyZm4c-rwj&index=4
from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'employee'
app.config['MONGO_URI'] = 'mongodb://ushna:ushna25@ds247587.mlab.com:47587/employee'
mongo = PyMongo(app)

@app.route("/")
def index():
    employees = []
    records = mongo.db.employee_info.find({'name':'ushna'})
    
    for record in records:
        employees.append( {'name' : record['name'], \
        'f_name' : record['f_name'] } )
    
    return jsonify ({'Employee_Info' : employees})

@app.route("/add")
def add():
    add = mongo.db.employee_info.insert({'name':'Ali'})
    return "Successfully added"

app.run(debug = True, use_reloader = True)