from fastapi import FastAPI
from flask import Flask, render_template, request, jsonify,json,flash
from urllib import parse
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import text
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'akghajdy'
app.secret_key = 'akghajdy'

HOSTNAME = "127.0.0.1"

PORT = 3306

USERNAME = "root"

DB_PASSWORD = "@Ab1008611"

DATABASE = "database_learn"

PASSWORD = parse.quote(DB_PASSWORD)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

db = SQLAlchemy(app)

migrate = Migrate(app, db)

with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text("select 1"))
        print(rs.fetchone())

class Users(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(100),primary_key=True)
    email = db.Column(db.String(100),nullable=False)


#with app.app_context():
     #db.create_all()

class Form(FlaskForm):
    username = StringField(label="用户名",validators=[DataRequired("用户名不能为空")])
    email = StringField(label="电子邮箱",validators=[DataRequired("电子邮箱不能为空")])
    submit = SubmitField(label="提交")

@app.route('/login',methods=['POST','GET'])
def login():
    form = Form()
    if request.method == 'GET':
        return render_template('from 3.0.html',form=form)
    elif request.method == 'POST':
        username = form.username.data
        email = form.email.data
        data = {
            "username":form.username.data,
            "email": form.email.data
        }
        #

        user_count = db.session.query(Users).filter(
            Users.name == username,
            Users.email == email
        ).count()
        if user_count > 0:
            flash('用户早已存在', 'success')
            return '用户早已存在'
            #return f"{username}\n{email}"
        else:
            user1 = Users(name=username,email=email)

            db.session.add(user1)
            db.session.commit()
        return jsonify(data)
        #return render_template('from 3.0.html',form=form)

@app.route('/')
def hello_word():
    return 'hello world'

if __name__ == '__main__':
    app.run()