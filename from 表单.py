from fastapi import Flask,render_template
from wtforms import StringField,PasswordField,SubmitField  #类型
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,EqualTo #验证数据不能为空 验证数据是否相同

app = Flask(__name__)

app.route('/index')
def index():
    return render_template('index2.0.html')

if __name__ == '__main__':
    app.run()
