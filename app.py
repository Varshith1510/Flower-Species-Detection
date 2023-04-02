# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 21:58:57 2023

@author: Varshith
"""

import numpy as np
import pymysql
from flask import Flask,render_template,url_for,request,redirect
import pickle

model = pickle.load(open("model.pkl","rb"))

app = Flask(__name__)

def verify(username,password):
    connection = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = 'cherryontop',db = 'login')
    cur = connection.cursor()
    
    cur.execute(f'select pwd from login_detail where username = "{username}";')
    passwd = cur.fetchone()
    
    if(passwd[0] == password):
        return True
    else:
        return False
        
    
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signin',methods = ["POST"])
def signin():
       name = request.form.get("Username")
       password = request.form.get("Password")
       if(verify(name,password)):
            return redirect(url_for('home'))
       else:
            return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict',methods = ["POST"])
def predict():
    if request.method =="POST":
        input1 = request.form["slength"]
        input2 = request.form["swidth"]
        input3 = request.form["plength"]
        input4 = request.form["pwidth"]
        inputs = np.array([[input1,input2,input3,input4]])
        print(inputs)
        pred = model.predict(inputs)
        return render_template('predict.html',data = pred)


if __name__ == "__main__":
    app.run(debug = True)



