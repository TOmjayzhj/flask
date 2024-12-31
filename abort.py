#raise 主动掏出异常
#abort 在网页当中做出异常
from fastapi import Flask,abort,request,render_template
app = Flask(__name__)

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET' :
        return render_template('index2.0.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('pwd')
        if password == "1234" and name == "Tom":
            return "Weclcome!"
        else :
            abort(404)
            return none

if __name__ == '__main__':
    app.run()