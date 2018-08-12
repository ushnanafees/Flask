from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return '''
       <h1> User Form</h1> 
    <form action = "/info" method = "GET">
    <input type = "text"  name = "user"  placeholder = "Full Name">
    <input type = "email" name = "email"  placeholder = "Email">
    <input type = "password" name = "password"  placeholder = "password">
    <input type = "submit" value = "Send">
    </form>
    '''
@app.route("/about")
def about():
    return '''
    <h1> About Form </h1>
    <form action = "/about" method = "GET">
    <input type = "text"  user="comment"  placeholder = "Comment">
    <input type = "text" user="review" placeholder = "Review">
    <input type = "submit" value = "Enter">
    
    </form>

        '''

@app.route("/info",methods=['GET','POST'])
def info():
    if request.method == "GET":
        return "<h1>GET Method</h1>Hello "+ request.args.get('user') + \
    " Your Email:"+request.args.get('email')
    else:
        return "<h1>POST Method</h1>Hello "+ request.form['user'] + \
    " Your Email:"+request.form['email']
    
app.run(debug=True, use_reloader = False,  port = 2000 )    