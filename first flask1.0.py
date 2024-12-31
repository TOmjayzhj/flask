from fastapi import Flask,request,jsonify

app = Flask(__name__)


#http://127.0.0.1:5000/index?age=195&pwd=789        -> 执行index GET
#http://127.0.0.1:5000/index?age=195&pwd=789
# 请求体： xx=123&yy=999                             -> 执行index POST
#http://127.0.0.1:5000/index?age=195&pwd=789
# 请求体： {"xx":123,"yy":999}  json                           -> 执行index POST
@app.route("/index",methods=["POST","GET"])
def index():
    #age = request.args.get("age")
    #pwd = request.args.get("pwd")
    #print(age,pwd)

    #xx = request.form.get("xx")
    #yy = request.form.get("yy")
    #print(xx,yy)

    #print(request.json)
    #return "成功"

    return jsonify({"status": True,'data':"what the fuck now"})
   # return jsonify({"status": True,'error':"oh shit"})

@app.route("/home")
def home():
    return "失败"

if __name__ == '__main__':
    app.run()