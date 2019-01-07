from flask import Flask,session,render_template,request,url_for,make_response,redirect,abort
from werkzeug.exceptions import HTTPException
import os,json,werkzeug.exceptions
import time
app=Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def index():
	if 'username' in session:
		return session['username']
	return render_template("login.html",message="你还没登陆")

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='POST':
		session['username']=request.form['username']
		return request.form['username']
	if 'username' in session:
		return "已经登陆"
	return render_template('login.html')

@app.route('/loginout',methods=['GET','POST'])
def loginout():
	if request.method=='GET':
		session.pop('username',None)
		return render_template('login.html',message="你已经退出了")


	return(render_template('login.html'))



app.debug=True
app.run(host='0.0.0.0',port='8080')