from flask import Flask, request, jsonify, session,json
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin
from flask_session import Session
from mongoengine import *
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from datetime import datetime,timedelta,timezone
from model import User

app = Flask(__name__)
CORS(app,supports_credentials=True)
DB_URI = "mongodb+srv://root:oidc001@oidc.n90pv.mongodb.net/?retryWrites=true&w=majority"
connect(host=DB_URI)

app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this in your code!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

user=User()
@app.route("/register",methods=["GET","POST"])
def register():
    name=request.get_json()["name"]
    id = request.get_json()["id"]
    password =request.get_json()["password"]
    print("register data-->",name,id,password)
    user.user_name =name
    user.user_id = id
    user.user_password = password
    user.save()
    return request.data

@app.route("/login", methods=["POST"])
def login():
    id = request.get_json()["user_id"]
    password = request.get_json()["password"]
    p = User.objects(user_id=id,user_password=password)
    print(p)
    if len(p)==0 or p[0].user_id != id or p[0].user_password != password:
        print("로그인 실패")
        return jsonify({"msg": "Bad username or password"}), 401
    else:
        access_token = create_access_token(identity=id)
        print("토큰: ", access_token)
        return jsonify(access_token=access_token),200


@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

@app.route("/protected")
@jwt_required()
def protected():
    return jsonify(foo="bar")



if __name__ == '__main__':
    app.run(debug=True)


