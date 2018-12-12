from flask import Flask,make_response,redirect ,request,render_template
from werkzeug.utils import secure_filename
app=Flask(__name__)

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']                #请求到文件
        f.save('d:\\' + secure_filename(f.filename))   #保存到d盘
    return render_template('upfile.html')       
app.run(port='8888')