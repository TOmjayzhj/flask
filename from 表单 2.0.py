from fastapi import Flask,render_template,request
from wtforms import StringField,PasswordField,SubmitField  #类型
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,EqualTo #验证数据不能为空 验证数据是否相同

app = Flask(__name__)
app.config['SECRET_KEY'] = 'akghajdy'

class Register(FlaskForm) :
    username = StringField(label='用户名',validators=[DataRequired('用户名不能为空')])
    password = PasswordField(label='密码',validators=[DataRequired('密码不不能为空')])
    password2 = PasswordField(label='密码',validators=[DataRequired('密码不能为空'),EqualTo('password')])
    submit = SubmitField(label='提交')

@app.route('/register',methods=['GET','POST'])
def register():
    form = Register()
    if request.method == 'GET':
        return render_template('register.html',form=form)
    elif request.method == 'POST':
        #验证器
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            print(username,password)
        else:
            print('error')
            print('验证失败')
        return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run()