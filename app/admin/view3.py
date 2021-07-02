from flask import Blueprint, render_template

from app import Product, ProductType

home_bp = Blueprint("home", __name__)


@home_bp.route('/')
def index():
    products = Product.query.all()
    productType = ProductType.query.all()
    print(products)
    print(productType)
    return render_template('index.html', products=products, productType=productType)
    # return "index"
