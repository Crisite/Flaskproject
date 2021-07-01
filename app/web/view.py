from _md5 import md5

from flask import Blueprint, render_template, session, url_for, flash, request, views
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect

from app.forms import LoginForm
from app.models import User

sign_bp = Blueprint('sign', __name__, url_prefix="/sign")


class LoginUrl(views.MethodView):
    def get(self):
        if session.get('uid'):
            return redirect(url_for('index'))
        return render_template('login.html')

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


sign_bp.add_url_rule('/login', endpoint='login', view_func=LoginUrl.as_view('login'))


@sign_bp.route('/logout')
def logout():
    pass


@sign_bp.route('/register', methods=('GET', 'POST'))
def register():
    return 'register'
