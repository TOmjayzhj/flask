from fastapi import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('also from 菜鸟html', title='Welcome Page', name='John Doe')

if __name__ == '__main__':
    app.run(debug=True)