from fastapi import Flask
app = Flask(__name__)

@app.route('/hello',methods=['GET','POST'],endpoint='hello')
def hello():
    return 'hello world'

@app.route('/hi',methods=['GET','POST'],endpoint='hi')
def hi():
    return 'hi hi'

@app.route('/user/<id>')
def id(id):
    if int(id) == 1 :
        return 'superise'
    elif int(id) == 2 :
        return 'python'
    else :
        return 'bye'
if __name__ == '__main__':
    app.run()
