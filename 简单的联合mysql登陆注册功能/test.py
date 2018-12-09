import mysql.connector
import hashlib
from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/',methods=['get','post'])
def home():
	return render_template('home.html')

def hashmd5(str):
	ming=str.encode('utf-8')
	m=hashlib.md5()
	m.update(ming)
	return m.hexdigest()

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')
	
@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    conn=mysql.connector.connect(host="39.105.116.195",port="3306",user="root",password="*******",database='test')
    cursor=conn.cursor()
    cursor.execute("select * from user where username='"+username+"'")
    row=cursor.fetchall()
    cursor.close()
    conn.close()
    if row==[]:
    	return render_template('form.html',message='还没注册呢铁子')
    else:
    	if username==row[0][0] and hashmd5(password)==row[0][1]:
    		return render_template('signin-ok.html',username=username)
    	return render_template('form.html',message='Bad username or password',username=username)


@app.route('/register',methods=['GET'])
def regesuter_form():
	return render_template('register_form.html')

@app.route('/register',methods=['POST'])
def register():
	username=request.form['username']
	password=request.form['password']
	if (check(username)):
		conn=mysql.connector.connect(host="39.105.116.195",port="3306",user="root",password="*******",database='test')
		cursor=conn.cursor()
		cursor.execute("insert into user values('"+username+"','"+hashmd5(password)+"')")
		conn.commit()
		cursor.close()
		conn.close()
		return render_template('signin-ok.html',username=username)
	else:
		return render_template('form.html',message='已经被注册了',username=username)

def check(user):
	conn=mysql.connector.connect(host="39.105.116.195",port="3306",user="root",password="*******",database='test')
	cursor=conn.cursor()
	cursor.execute("select * from user where username='"+user+"'")
	row=cursor.fetchall()
	cursor.close()
	conn.close()
	if row ==[]:
		return True
	else:
		return False



if __name__=="__main__":
	app.run(port='80')
