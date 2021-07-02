# from flask import Flask


# # from run import app
# from app import DevelopmentConfig
#
# app = Flask(__name__)
# app.config.from_object(DevelopmentConfig)
# from app import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.settings import DevelopmentConfig
# from run import app

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    telephone = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(255), nullable=True)


class ProductType(db.Model):
    __tablename__ = "product_type"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, nullable=False)


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pname = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    images = db.Column(db.Text)
    p_typeid = db.Column(db.Integer, db.ForeignKey("product_type.id"))
    product_type = db.relationship("ProductType", backref=db.backref("products"))

    def product_json(self):
        product_json = {}
        product_json["id"] = self.id
        product_json["pname"] = self.pname
        product_json["price"] = self.price
        product_json["images"] = self.images
        return product_json


class ShopCar(db.Model):
    __tablename__ = "shop_cart"
    uid = db.Column(db.String(50), db.ForeignKey("user.id", ondelete='cascade'), primary_key=True)
    user = db.relationship("User", backref=db.backref("shopcarts"))
    pid = db.Column(db.String(50), db.ForeignKey("product.id"), primary_key=True)
    product = db.relationship('Product', backref=db.backref("shopcarts"))
    number = db.Column(db.Integer, default=0)


class FootPrint(db.Model):
    __tablename__ = "foot_print"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.String(50), db.ForeignKey("user.id", ondelete='cascade'))
    user = db.relationship("User", backref=db.backref("footprints"))
    pid = db.Column(db.String(50), db.ForeignKey("product.id"))
    product = db.relationship('Product', backref=db.backref("footprints"))


# 删除表
# db.drop_all()

# 创建表
# db.create_all()
