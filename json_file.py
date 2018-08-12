from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    employees=[ 
            {'name':'Ali' , 'f_name':'Raza' , 'nic':2345677 , 'designation' :'PM' },
            {'name': 'Ali', 'company_name':'axact', 'qualification': 'MBA'}
            
            ] 
    return jsonify({'Employeeinfo': employees})

app.run(debug = True, use_reloader = True)


