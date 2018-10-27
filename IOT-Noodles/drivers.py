from flask import Flask, session, redirect, url_for, escape, request, render_template
from manage import app
from database import *
from actoken import *


@app.route('/get_token', methods=['POST', 'GET'])
def page_driver_get_token():
    if request.method == 'POST':
        if 'username' not in session:
            redirect(url_for('login'))
        did = int(request.form['did'])
        token = token_get_token(did)
        return token
    else:
        return render_template('get_token.html')


@app.route('/beat', methods=['POST'])
def page_driver_beat():
    did = request.form['did']
    token = request.form['token']
    if not token_check(did, token):
        return 'Token Error.'
    res = driver_beat(did, ip=str(request.remote_addr))
    return res


@app.route('/add_driver', methods=['GET', 'POST'])
def page_driver_add():
    if request.method == 'GET':
        return render_template('add_driver.html')
    if request.method == 'POST':
        form = request.form
        # 这里有破绽
        # if 'token' not in form and 'username' not in session:
        #     return 'No permission.'
        # elif 'username' not in session:
        #     redirect(url_for('login'))
        # name = form['name']
        # type = form['type']
        # if 'token' in form:
        #     token = form['token']
        # uid = session['uid']
        # ip = str(request.remote_addr)
        # if not token_check(uid, token) and 'username' not in session:
        #     return 'Token Error.'
        # res = driver_add(uid, name, type, ip)
        # return res
        # 网页的处理情况
        if 'username' in session:
            name = form['name']
            type_ = form['type']
            uid = session['uid']
            # 网页就不管ip了
            # ip = str(request.remote_addr)
            res = driver_add(uid, name, type_)
            return res

        return 'Error usage.'


@app.route('/del_driver', methods=['GET', 'POST'])
def page_driver_del():
    if request.method == 'GET':
        return render_template('del_driver.html')
    if request.method == 'POST':
        if not 'username' in session:
            return 'Error usage.'
        did = request.form['did']
        res = driver_del(did)
        return res
