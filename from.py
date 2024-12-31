from fastapi import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
         return render_template('index2.0.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('pwd')
        print(name,password)
        return 'this is a post'

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/hi')
def hi():
    return 'hi'

if __name__ == '__main__':
    app.run()
