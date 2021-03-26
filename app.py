from flask import Flask, render_template ,request
import time
import smtplib
import os
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")
    

    

@app.errorhandler(404)  
def not_found(e): 
  return render_template("404.html") 

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True)