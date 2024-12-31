from  fastapi import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/index')
def index():
    return redirect(url_for('hello'))

@app.route('/')
def hello():
    return 'this is a joy'
if __name__ == '__main__':
    app.run()