from flask import Flask,render_template
from sqlalchemy import true
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/home')
def home1():
    return render_template("home.html")    
@app.route('/about')
def about():
    return render_template("about.html") 
@app.route('/price')
def price():
    return render_template("price.html") 

if __name__=='__main__':
 app.run(debug=true)      