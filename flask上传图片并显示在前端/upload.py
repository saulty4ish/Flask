from flask import Flask,render_template,request,url_for
import os,json
import time
app=Flask(__name__)


@app.route('/upload',methods=['GET','POST'])
def upload():
	if request.method=='POST':
		type=['jpeg','png','jpg','gif']
		try:
			f=request.files['myfile']
			suffix=f.filename.split('.')[-1]
			if suffix in type:
				basepath=os.path.dirname(__file__)
				name=str(int(time.time()))
				f.save(os.path.join(basepath,"static\\images\\"+name+"."+suffix))
				#return render_template('upload.html',message=str(int(time.time()))+"."+suffix)
				return "<h1>上传成功</h1><img src='./static/images/"+name+"."+suffix+"'>"
		except KeyError:                            #捕获文件没有上传就提交的异常
			a="没上传你提交你🐎呢"
			return render_template('upload.html',message=a)
		return render_template('upload.html',message="不允许上传的类型")
	return render_template('upload.html',message="上传个图片试试😀")


app.debug=True
app.run(host='0.0.0.0',port='80')