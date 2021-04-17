from flask import Flask ,jsonify#Response,request,
from flask_restful import  Api,Resource,abort

import  pymongo
from pymongo import MongoClient
import bson
import json
from bson import json_util

######?k@g85)f4Zy#x*
######xy_db ,user
client = pymongo.MongoClient("mongodb+srv://username:password@y")
# db = client['xy_db']
db = client.xy_db
collection = db.user
# collection = db['user']

App = Flask(__name__)
api = Api(App)
# collection.insert_one({'}name':'jace','age':19})




@App.route('/users',methods=['GET'])
def get_users():
    # data = list(collection.find({}))
    data = list(collection.find({}))
    # return jsonify(data)   # ensure_ascii=False加入此除中文乱码
    return json.dumps(data,ensure_ascii=False,default=json_util.default) # ensure_ascii=False加入此除中文乱码

@App.route('/adduser',methods=['POST'])
def add_users():
    request_payload = request.json
    user = request_payload['user']
    return json.dumps(all_seeds,default=json_util.default)

if __name__ == '__main__':
    App.run(debug=True)
#  Mac 
# export FLASK_APP = hello.py flask run
# windows
#senv :FLASK_APP = "hello.py" flask run

# mongodb+srv://<username>:<password>@y
# myclient = pymongo.MongoClient@(y)
# print(myclient.database_names())


# @App.route('/hi')
# def Hi():
#     return 'Hi ,this is App route'

# @App.route('/tamil')
# def hello_in_temil():
#     return "hahavivi"

# @App.route('/name/<name>')
# def hello_name(name):
#     return 'Welcome (name)'

class Hello(Resource):
    def get(self):
        return {'date':'this is start...'}
# api.add_resource(Hello,'/hehe')

