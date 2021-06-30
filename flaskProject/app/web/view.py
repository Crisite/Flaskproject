from flask import Blueprint, render_template

sign = Blueprint('sign', __name__)


@sign.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('登录页面.html')


@sign.route('/logout')
def logout():
    pass


@sign.route('/register', methods=('GET', 'POST'))
def register():
    return 'register'
