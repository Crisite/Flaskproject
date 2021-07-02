from flask import Blueprint, request, render_template, session, redirect, url_for, views
from app.models import *
import json

product_bp = Blueprint("product", __name__, url_prefix="/product", template_folder="../templates/product")


# products_see = []#存储json

@product_bp.route("/detail")
def detail():
    pid = int(request.args.get("id"))
    uid = session.get('uid')
    session['pid'] = pid
    product = Product.query.filter_by(id=pid).first()
    # if session.get('uid'):
    #     p=Product.product_json(product)
    #     products_see.append(p)
    #     json_products=json.dumps(products_see,ensure_ascii=False)
    #     print(json_products)
    #     session['products_see']=json_products
    if session.get('uid'):
        foot_print = FootPrint(uid=uid, pid=pid)
        db.session.add(foot_print)
        db.session.commit()
    return render_template('detail.html', product=product)


class addCart(views.MethodView):
    def post(self):
        print(request.form['number'])
        uid = session.get('uid')
        pid = session.get('pid')
        shop_cart = ShopCar.query.filter_by(uid=uid, pid=pid).first()
        number_new = int(request.form['number'])
        if shop_cart:  # 如果存在该商品购物记录 就只改变其数量
            number = shop_cart.number
            # print(number)
            shop_cart.number = number + number_new
            db.session.add(shop_cart)
            db.session.commit()
            return redirect(url_for('index'))
        shop_cart = ShopCar(uid=uid, pid=pid, number=number_new)  # 如果不存在该商品购物记录 就添加记录 并初始化数量为1
        db.session.add(shop_cart)
        db.session.commit()
        return redirect(url_for('index'))


product_bp.add_url_rule('/addCart', endpoint='addCart', view_func=addCart.as_view('addCart'))


@product_bp.route("/goods1")
def goods1():
    pid = int(request.args.get("id"))
    productType = ProductType.query.all()
    result = select2(pid)
    return render_template('index.html', products=result, productType=productType)


# 查询商品类别
def select2(keyword):
    data = Product.query.filter(Product.p_typeid.like(keyword)).all()
    return data
