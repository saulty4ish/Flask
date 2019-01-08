from flask import Flask,session,render_template,request,url_for,make_response,redirect,abort,flash,g,current_app
from werkzeug.exceptions import HTTPException
import os,json,werkzeug.exceptions
import time

app=Flask('zaq')

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



#装饰器运行函数是会自动运行装饰器
#func就是index()函数
#wrapper()里面可以加参数
def login_session(func):
	def wrapper():
		if not 'username' in session:
			return "未登录"
		return func()
	return wrapper


@app.route('/login')
def sets():
	session['username']='qwerty'
	return "session设置为:"+session['username']


#运行index()函数相当于运行login_session(index())
@app.route('/admin')
@login_session
def index():
	return "welcome,admin"


app.run(host='0.0.0.0',port='80',debug=True)


