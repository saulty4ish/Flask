from flask import Flask,make_response,redirect ,request,render_template
from werkzeug.utils import secure_filename
app=Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']                #请求到文件
        f.save(secure_filename(f.filename))   #保存到d盘
    return render_template('upfile.html')       
app.run(port='6888')