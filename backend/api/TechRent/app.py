from ast import JoinedStr
import email
from imp import init_builtin
import json
import re
from flask import Flask, jsonify, request, session
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, create_engine



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
app.config['SECRET_KEY'] = "test"
db = SQLAlchemy(app)


class Users(db.Model):
    uid = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(256), nullable = False)
    question1 = db.Column(db.String(256), nullable = False)
    question2 = db.Column(db.String(256), nullable = False)


    def __init__(self, name, email, password, question1, question2):
        self.name = name
        self.email = email
        self.password = password
        self.question1 = question1
        self.question2 = question2




@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"



# app = Flask(__name__)
# app.config.from_object(__name__)
# CORS(app,resources={r"/*":{'origins':'*'}})



# @app.route('/',methods = ['GET'])
# def check():
#     return jsonify("hello world")


# @app.route("/api/register",methods=['POST'])
# def register():
#     data = request.get_json()
#     return jsonify({'data':data})

# @app.route("/api/login",methods=['POST'])
# def register():
#     data = request.get_json()
#     return jsonify({'data':data})


@app.route("/test",methods=['GET','POST'])
def test():
    return jsonify("Hkladjfiasdjfask ")


@app.route("/register", methods = ['GET','POST'])
def register():
    data = request.json
    print(data)
    name = data['name']
    email = data['email']
    password = data['password']
    question1 = data['question1']
    question2 = data['question2']
    user = Users(name = name, email = email, password = password, question1=question1, question2=question2 )
    db.session.add(user)
    db.session.commit()
    app.logger.info(user.uid)

    # name = request.form['name']
    # email = request.form['email']
    # password = request.form['password']
    # question1 = request.form['question1']
    # question2 = request.form['question2']
    # user = Users(name = name, email = email, password = password, question1=question1, question2=question2 )
    # db.session.add(user)
    # db.session.commit()
    # app.logger.info(user.uid)
    return jsonify("User successfully registered")

    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
