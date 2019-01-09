from flask import Flask,session,render_template,request,render_template_string

app=Flask(__name__)
app.config['SECRET_KEY']="HELLO WORD!"#session必须用到的密钥，伪造身份的关键。


@app.route('/')
def index():
    try:
        username=session['username']
        return "hello,"+username    #判断session里面是否有username的值，有的话就直接登陆状态。
    except KeyError:     #捕获异常，如果没有session的值，会出现KeyError错误
        return render_template('login.html') #如果没有session就跳转登录界面

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form['username']
        if username=='admin' and not password =="8sudehd7eageaade54":        #用户是不知道admin密码的，这里考虑session伪造。
            return "密码不对"
        session['username']=username
        return "hello,"+username
    return render_template("login.html")  
#ssti注入点
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
app.run(debug=True,port=8091)