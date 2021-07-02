from flask import Blueprint, views, render_template, request, session, redirect, url_for

from app.models import *
import json
import hashlib

from app.forms import LoginForm, RegisterForm






user_bp = Blueprint("user", __name__, url_prefix='/user', template_folder='../templates/user')


class loginUrl(views.MethodView):
    def get(self):
        if session.get('uid'):
            return redirect(url_for('index'))
        return render_template('login.html')
        # return 'hello'

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            pwd = md5(password)
            user = User.query.filter(User.username == username, User.password == pwd).first()
            if user is not None:
                session['uid'] = user.id
                session['username'] = user.username
                return redirect(url_for('index'))
        return render_template("login.html", msg="用户名或者密码错误")
        # return 'hello'


user_bp.add_url_rule('/login', endpoint='login', view_func=loginUrl.as_view('login'))


class registerUrl(views.MethodView):

    def get(self):
        return render_template('register.html')

    def post(self):
        form = RegisterForm(request.form)
        if form.validate():
            username = form.username.data
            usernames = User.query.filter_by(username=username).all()
            if len(usernames) != 0:
                return render_template('register.html', msg='用户名重复，请更换用户名')
            password = form.password.data
            str_md5 = md5(password)
            telephone = form.telephone.data
            address = form.address.data
            user = User(username=username, password=str_md5, telephone=telephone, address=address)
            db.session.add(user)
            db.session.commit()
        else:
            return render_template('register.html', msg='注册信息有误')
        return render_template('login.html', msg='你已成功注册用户信息，请登录')


user_bp.add_url_rule('/register', endpoint='register', view_func=registerUrl.as_view('register'))


@user_bp.route("/main")
def main():
    uid = session.get('uid')
    if uid is None:
        return render_template('login.html')
    # products_see=session.get('products_see')
    # products_see=json.loads(products_see)
    # print(products_see)
    footprints = FootPrint.query.order_by(FootPrint.id.desc()).filter_by(uid=uid).all()  # 最后浏览的展示在最前边
    if footprints:
        return render_template('main.html', footprints=footprints)
    return '<h4>你还没有浏览过商品哦，快去浏览吧~<h4>'


@user_bp.route("/showCart")
def showCart():
    if session.get('uid'):
        uid = session.get('uid')
        shopcarts = ShopCar.query.filter_by(uid=uid).all()  # 找出与该用户有关的购物记录
        if shopcarts:
            return render_template('cart.html', shopcarts=shopcarts)
        else:
            return '<h4>购物车空空如也哦，快去添加宝贝吧~</h4>'
    return redirect(url_for('user.login'))


# 删除一件商品
@user_bp.route("/deleteFromCart")
def deleteFromCart():
    pid = int(request.args.get("id"))
    uid = session.get('uid')
    shopcart = ShopCar.query.filter_by(uid=uid, pid=pid).first()
    db.session.delete(shopcart)
    db.session.commit()
    return redirect(url_for('user.showCart'))


# 批量删除商品
@user_bp.route("/batchDeletes")
def batchDeletes():
    uid = session.get('uid')
    items = request.args.get("delitems")
    strs = items.split(",")
    for str in strs:
        shopcart = ShopCar.query.filter_by(uid=uid, pid=str).first()
        db.session.delete(shopcart)
        db.session.commit()
    return "true"


@user_bp.route("/logout")
def logout():
    uid = session.get('uid')
    if uid is None:
        return redirect(url_for('index'))
    session.clear()
    return redirect(url_for('index'))


def md5(password):
    m = hashlib.md5()

    # Tips
    # 此处必须encode
    # 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
    # 因为python3里默认的str是unicode
    # 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
    b = password.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    # 另一种写法：b‘’前缀代表的就是bytes
    return str_md5
