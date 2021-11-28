from flask import Flask,jsonify
from books import Builds
# jsonify can let return a char format

app = Flask(__name__)   #initical a class and send a viriable '__name__' to this class
app.config['JSON_AS_ASCII']=False

@app.route('/',methods=['GET','POST'])    #app init class and this class has a function ----route   URL
def hello_world():  # this URL is processed by this function
    build=Builds()
    arrData=build.get_build_infos_limit()    # find info in mysql
    print(arrData)
    return jsonify(arrData)


if __name__ == '__main__':   # whether user is runing this file?
    app.run(host='127.0.0.1',port=5501,debug=True)
#1.if we do : run thisfile.py  __name__=__main__
#2.if we do : run others __name__='this file's name'