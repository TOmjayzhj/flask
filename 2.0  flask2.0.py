from fastapi import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/hello/<name>')
def hello_name(name):
    return "Hello %s" % name

@app.route('/blog/<int:email>')
def blog_email (email):
    return "BLOG NUMBER %d" % email

@app.route('/rev/<float:id>')
def rev_id(id):
    return "rev is %f" % id

if __name__ == "__main__":
    app.run(debug=True)