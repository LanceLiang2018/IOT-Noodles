from flask import Flask, session, redirect, url_for, escape, request, render_template
from manage import app
from database import *


@app.route('/', methods=['GET'])
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    drivers = []
    uid = int(session['uid'])
    data = driver_get_user(uid)
    for d in data:
        driver = {}
        dd = driver_get_all(d[0])
        driver['id'] = dd[0]
        driver['name'] = dd[2]
        driver['type'] = dd[3]
        driver['ip'] = dd[4]
        driver['last_beat'] = dd[6]
        drivers.append(driver)
    return render_template('index.html', text='Login as %s' % session['username'],
                           user={"name": session['username'], "uid": session['uid'], "img": session['icon']},
                           drivers=drivers)


@app.route('/favicon.ico')
def get_ico():
    return redirect(url_for('static', filename='favicon.ico'))

