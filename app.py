from fastapi import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from urllib import parse
from flask_migrate import Migrate
app = Flask(__name__)

HOSTNAME = "127.0.0.1"

PORT = 3306

USERNAME = "root"

db_PASSWORD = "@Ab1008611"

DATABASE = "database_learn"

PASSWORD = parse.quote_plus(db_PASSWORD)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

db = SQLAlchemy(app)

migrate = Migrate(app, db)

with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text("select 1"))
        print(rs.fetchone())

#一个ORM模型与数据库中的一个表对应
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)

# user = User(username="法外狂徒张三",password="123456")
#sql : insert user(username,password) values('法外狂徒张三‘，’123456‘);
#映射到数据库中

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    email = db.Column(db.String(100),nullable=False)
    signature = db.Column(db.String(100),nullable=False)
    fnumber = db.Column(db.Integer,nullable=False)
'''
    # 添加外键
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship("User",back_populates="article")

article = Article(title="Flask",content="Falseidjfaadfe")
'''

#with app.app_context():
        #db.create_all()
migrate = Migrate(app, db)

@app.route("/user/add")
def add_user():
    #创建一个ORM对象
    user = User(username="法外狂徒张三",password="123456")
    #将ORM对象添加到db.session中
    db.session.add(user)
    #将db.session中的改变同步到数据库中
    db.session.commit()
    return "用户创建成功"

@app.route("/user/query")
def query_user():
    #get查找：根据主键（1）查询1条数据
    user1 = User.query.get(1)
    print(f"{user1.id}:{user1.username}:{user1.password}")
    #filter_by查找
    users = User.query.filter_by(username="法外狂徒张三")
    print(type(users))
    for user in users:
        print(user.username)
    return "查找成功"

@app.route("/user/update")
def update_user():
    user = User.query.filter_by(username="法外狂徒张三").first()
    user.password = "112233"
    db.session.commit()
    return "修改成功"

@app.route('/user/delete')
def delete_user():
    user = User.query.get(2)
    #从session中删除
    db.session.delete(user)
    db.session.commit()
    return "删除成功"
@app.route('/')
def hello_world():
    return 'Hello World!'



if __name__ == '__main__':
    app.run()


