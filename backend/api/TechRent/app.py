from ast import JoinedStr
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify, request, session, current_app, Blueprint
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, func, create_engine
## for JWT
from functools import wraps
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import jwt


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TechRent.sqlite3'
app.config['SECRET_KEY'] = "randostring"
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(256), nullable = False)
    question1 = db.Column(db.String(256), nullable = False)
    question2 = db.Column(db.String(256), nullable = False)
    items = db.relationship('Items', backref="creator", lazy = False)

    def __init__(self, name, email, password, question1, question2):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password, method='sha256')
        self.question1 = question1
        self.question2 = question2

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        if not email or not password:
            print('Ivalid email:', email)
            print('Or invalid pword:', password)
            return None
        
        user = cls.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            print('User not found')
            return None

        return user

    def to_dict(self):
        return dict(uid=self.uid, email=self.email)


class Items(db.Model):
    __tablename__ = 'items'

    # id, item_name, rating, brand, price, location, seller, image_url, posted_at
    id = db.Column(db.Integer, unique = True, primary_key=True)
    item_name = db.Column(db.String(50), nullable = False)
    rating = db.Column(db.Integer, nullable = True)
    brand = db.Column(db.String(50), nullable = True)
    price = db.Column(db.Float, nullable = False)
    location = db.Column(db.Text, nullable = False)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.uid'))
    image_url = db.Column(db.Text, nullable = False)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text, nullable = False)
    seller_email = db.Column(db.Text, nullable=True)
    seller_phone = db.Column(db.Text, nullable=True)

    def to_dict(self):
      return dict(id=self.id,
                  item_name=self.item_name,
                  posted_at=self.posted_at.strftime('%Y-%m-%d %H:%M:%S'),
                  seller_id=self.seller_id,
                  location=self.location,
                  price=self.price,
                  rating=self.rating,
                  brand=self.brand,
                  image_url=self.image_url,
                  description=self.description,
                  seller_email=self.seller_email,
                  seller_phone=self.seller_phone
                  )

## decorator
def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = Users.query.filter_by(email=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            print("Token Expired")
            return jsonify(expired_msg), 401 
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            print("Invalid Token")
            return jsonify(invalid_msg), 401

    return _verify


@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"


@app.route("/test",methods=['GET','POST'])
def test():
    return jsonify("Hkladjfiasdjfask ")


@app.route("/register", methods = ['GET','POST'])
def register():
    data = request.get_json()
    print('Request data: ', data)
    name = data['name']
    email = data['email']
    password = data['password']
    question1 = data['question1']
    question2 = data['question2']
    user = Users(name = name, email = email, password = password, question1=question1, question2=question2)
    db.session.add(user)
    db.session.commit()
    app.logger.info(user.uid)

    return jsonify(user.to_dict()), 201

@app.route('/login', methods=('POST',))
def login():
    data = request.get_json()
    user = Users.authenticate(**data)

    if not user:
        return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401

    token = jwt.encode({
        'sub': user.email,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    return jsonify({ 'token': token })
    
@app.route('/items', methods=('POST',))
@token_required
def create_item(current_user):
    data = request.get_json()
    name = data['item_name']
    brand = data['brand']
    price = data['price']
    location = data['location']
    seller_id = current_user
    image_url = data['image_url']
    posted_at = data['posted_at']
    description = data['description']
    seller_email = data['email']
    seller_phone = data['phone']
    item = Items(name=name, brand=brand, price=price, location=location, seller_id=seller_id, image_url=image_url, posted_at=posted_at, description=description, seller_email=seller_email, seller_phone=seller_phone)
    db.session.add(item)
    db.session.commit()
    app.logger.info(item.id)

    return jsonify(item.to_dict()), 201
    
@app.route('/items', methods=('GET',))
def fetch_items():
    items = Items.query.all()
    return jsonify([i.to_dict() for i in items])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
