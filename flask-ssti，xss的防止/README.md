```
import uuid
from flask import Flask, request, make_response, session,render_template, url_for, redirect, render_template_string

app=Flask(__name__)
app.config['SECRET_KEY']=str(uuid.uuid4())

#flask只对后缀名为('.html', '.htm', '.xml', '.xhtml')的自动进行转义,所以开发的时候尽量写个单独的模板，实现代码和视图分离


#<script>alert(1)</script>需要url编码

#ssti xss都存在
#单独写了个404报错页面
@app.errorhandler(404)
def page_not_found(e):
	template='''
		{%% block body %%}
		<div class="center-content error">
		<h1>Oops! That page doesn't exist.</h1>
		<h3>%s</h3>
		</div>
		{%% endblock %%}
	'''%(request.url)
	return render_template_string(template),404

#无ssti，有xss
@app.route('/test1',methods=['GET','POST'])
def test1():
	if request.method=='GET':
		name=request.args.get("name")
		return name
	return "hello world!"  

#都有
@app.route('/test2',methods=['GET','POST'])
def test2():
	if request.method=='GET':
		name=request.args.get("name")
		template="""
		<h1>%s</h1>
		"""%(name)
		return render_template_string(template)
	return "hello world!"

#安全
@app.route('/test3',methods=['GET','POST'])
def test3():
	if request.method=='GET':
		name=request.args.get("name")
		template="""
		<h1>hello,{{name}}</h1>
		"""
		return render_template_string(template,name=name)
	return "hello world!"  

#安全，提倡的做法
@app.route('/test4',methods=['GET','POST'])
def test4():
	if request.method=='GET':
		name=request.args.get("name")
		return render_template('1.html',name=name)
	return "hello world!"
  
app.run(port=80,debug=True)
```  

>     flask有防止ssti注入和XSS的方法，默认对('.html', '.htm', '.xml', '.xhtml')为后缀的进行转义,所以写代码的时候无论代码量多少，写个单独的模板传递进去参数显示总是安全的。  
  
-----
>     但是并不会对render_template_string进行转义，这就造成了ssti和xss  
>     不管怎么说，代码和视图分离是最好的了。