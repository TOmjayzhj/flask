from fastapi import Flask ,render_template
from datetime import datetime
app = Flask(__name__)

def datetime_format(value,format="%Y-%d-%m %H:%M"):
    return value.strftime(format)

app.add_template_filter(datetime_format,"dformat")
@app.route('/')
def index():
    data = {
        'name' : '张三',
        'age' : '789',
        'list' : [1,2,3,4,5,6]
    }
    mytime = datetime.now()
    age2 = 17
    books = [
        {'name' : '三国演义',
         'author' : '罗贯中',
         'price' : 100},
        {'name': '西游记',
         'author': '吴承恩',
         'price': 101},
        {'name': '红楼梦',
         'author': '曹雪芹',
         'price': 100},
        {'name': '水浒传',
         'author': '施耐庵',
         'price': 101},
    ]
    return render_template('template-test.html',data=data,mytime=mytime,age2=age2,books=books)

@app.route('/base1')
def base1():
    return render_template('child 1.html')

@app.route('/base2')
def base2():
    return render_template('child 2.html')

if __name__ == '__main__':
    app.run()