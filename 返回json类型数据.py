from fastapi import Flask,make_response,json

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'name' : '张三'
    }
    return make_response(data)
if __name__ == '__main__':
    app.run(  )