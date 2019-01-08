from flask import Flask,session,render_template,request,url_for,make_response,redirect,abort,flash,g,current_app
from werkzeug.exceptions import HTTPException
import os,json,werkzeug.exceptions
import time
import views#必须导入views.py
app=Flask('zaq')

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



app.add_url_rule('/foo1', view_func=views.foo1)
app.add_url_rule('/foo2', view_func=views.foo2)
app.add_url_rule('/foo3', view_func=views.foo3)#('/foo3'是访问路径，views.foo3是views.py的foo3函数)


app.run(host='0.0.0.0',port='80',debug=True)


