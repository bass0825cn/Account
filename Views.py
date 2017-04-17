# -*- coding: utf-8 -*-
# 上面用于python支持中文
from run import app, db
from flask import render_template, redirect, url_for, session, g, flash
from flask import request, jsonify
import models
from forms import UserForm


def execute_sql(sql):
    cur = g.db.cursor()
    cur.execute(sql)
    g.db.commit()
    return cur


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if 'user_name' in session and session['user_name'] == name:
        return render_template('hello.html', name=name)
    else:
        return redirect(url_for('login'))


def valid_login(user, password):
    u = models.User.query.get(user)
    if not u:
        return None
    if u.password != password:
        return None
    return u.user_name


@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = None
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        username = valid_login(user_id, password)
        if username:
            session['user_id'] = user_id
            session['user_name'] = username
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            msg = '登录失败'.decode("utf-8")
    return render_template('login.html', msg=msg)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.pop('logged_in')
    return redirect(url_for('login'))


@app.route('/user_list')
def user_list():
    if not session.get("logged_in"):
        return redirect(url_for('login'))
    users = models.User.query.all()
    return render_template('user_list.html', users=users)


@app.route('/user_edit', methods=['GET', 'POST'])
@app.route('/user_edit/<user_id>')
# @app.login_required
def user_edit(user_id=None):
    if not session.get("logged_in"):
        return redirect(url_for('login'))
    form = UserForm()
    if form.validate_on_submit():
        g.user = models.User.query.get(form.user_id.data)
        if not g.user:
            g.user = models.User()
        g.user.user_id = form.user_id.data
        g.user.user_name = form.user_name.data
        g.user.password = form.password.data
        try:
            db.session.add(g.user)
            db.session.commit()
            flash("维护用户成功！".decode("utf-8"))
        except Exception, e:
            print Exception, ":", e
        return redirect(url_for('user_list'))
    else:
        if user_id:
            g.user = models.User.query.get(user_id)
            form.user_id.data = g.user.user_id
            form.user_name.data = g.user.user_name
            form.password.data = g.user.password
        else:
            form.user_id.data = ''
            form.user_name.data = ''
            form.password.data = ''
        return render_template('user_edit.html', form=form)


@app.route('/user_delete/<user_id>')
def user_delete(user_id=None):
    if not session.get("logged_in"):
        return redirect(url_for('login'))
    g.user = models.User.query.get(user_id)
    try:
        db.session.delete(g.user)
        db.session.commit()
        flash("用户删除成功！".decode("utf-8"))
    except Exception, e:
        print Exception, ":", e
    return redirect(url_for('user_list'))


@app.route('/test_bootstrap')
def test_bootstrap():
    return render_template('test_bootstrap.html')


@app.route('/AjaxCheckUser', methods=['GET', 'POST'])
def ajax_check_user():
    msg = ''
    if request.method == 'POST':
        user = models.User.query.get(request.form['user_id'])
        if not user is None:
            msg = '该用户已存在！'
    return jsonify(msg=msg)
