from flask import Flask, session, redirect, url_for, escape, request, render_template
import hashlib
from database import *
from manage import app


def get_icon(email):
    return'https://s.gravatar.com/avatar/' + hashlib.md5(email.encode()).hexdigest() + '?s=52'


'''
@app.route('/', methods=['GET', 'POST'])
def index():
    sever_init()
    if request.method == 'GET':
        if not 'username' in session:
            return redirect(url_for('login'))
        return render_template('ChatRoom.html', username=session['username'],
                               icon=session['icon'],
                               entries=entries,
                               users=users,
                               title='聊天室(迫真)',
                               )
    if request.method == 'POST':
        timedata = time.localtime(time.time())
        data = {
            'username': session['username'],
            'message': request.form['message'],
            'time': str(timedata.tm_mon).zfill(2) + '/' + str(timedata.tm_mday).zfill(2) + ' ' + \
                    str(timedata.tm_hour).zfill(2) + ':' + str(timedata.tm_min).zfill(2),
        }
        entry_insert(entry_get_new_id(), data['username'], data['time'], get_icon(session['email']), data['message'])
        return redirect(url_for('index'))
'''


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'username' in session:
        redirect(url_for('logout'))
    if request.method == 'POST':
        if request.form['passwd'] != request.form['passwd_']:
            return '两次密码不一致。' + '<a href=%s>返回</a>' % url_for('signup')
        if request.form['username'] == '':
            return '用户名不能为空。' + '<a href=%s>返回</a>' % url_for('signup')
        hl = hashlib.md5(request.form['passwd'].encode()).hexdigest()
        result = user_add(request.form['username'], hl, request.form['email'].lower())
        sever_user_init()
        return result + '<a href=%s>首页</a>' % url_for('index')
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        redirect(url_for('logout'))
    if request.method == 'POST':
        hl = hashlib.md5(request.form['passwd'].encode()).hexdigest()
        result = user_check(request.form['username'], hl)
        if result != 'Success':
            return result
        session['uid'] = user_get_uid(request.form['username'])
        session['username'] = request.form['username']
        session['passwd'] = hl
        session['email'] = user_get_email(session['username'])
        session['icon'] = get_icon(session['email'])
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/get_email/<username>')
def get_email(username):
    email = user_get_email(username)
    return email + '<br><img src=\"%s\">' % (get_icon(email))


@app.route('/about')
def about():
    return redirect('http://chatroom.lanceliang2018.xyz/')


def sever_user_init():
    global users
    users = user_all_name()


def sever_init():
    sever_user_init()



