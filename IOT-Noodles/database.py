import sqlite3 as sql
import os

conn_user = sql.connect('users.db', check_same_thread=False)
conn_dri = sql.connect('drivers.db', check_same_thread=False)


def user_get_new_id():
    c = conn_user.cursor()
    c.execute('select nid from sid')
    data = c.fetchall()
    nid = data[0][0]
    c.execute('update sid set nid = ? where s = 0;', (nid + 1, ))
    conn_user.commit()
    c.close()
    return nid


def user_add(name, passwd, email):
    c = conn_user.cursor()
    c.execute('select * from users where name = ?;', (name,))
    data = c.fetchall()
    if len(data) != 0:
        return 'Name used'
    nid = user_get_new_id()
    try:
        c.execute('insert into users values (?, ?, ?, ?);', (name, passwd, email, nid))
    except Exception as e:
        conn_user.commit()
        c.close()
        return 'Fail, ' + str(e)
    conn_user.commit()
    c.close()
    return 'Success'


def user_del(name, passwd):
    c = conn_user.cursor()
    c.execute('select * from users where name = ?;', (name, ))
    data = c.fetchall()
    if len(data) == 0:
        conn_user.commit()
        c.close()
        return 'No such of user'
    if data[0][1] != passwd:
        conn_user.commit()
        c.close()
        return 'Password error'
    c.execute('delete from users where name = ?;', (name, ))
    conn_user.commit()
    c.close()
    return 'Success'


def user_check(name, passwd):
    c = conn_user.cursor()
    c.execute('select * from users where name = ?;', (name, ))
    data = c.fetchall()
    c.close()
    if len(data) == 0:
        return 'No such of user'
    if data[0][1] != passwd:
        return 'Password error'
    return 'Success'


def user_get_email(name):
    c = conn_user.cursor()
    conn_user.commit()
    c.execute('select email from users where name = ?;', (name, ))
    data = c.fetchall()
    if len(data) == 0:
        return 'Get None'
    c.close()
    return data[0][0]


def user_all_name():
    c = conn_user.cursor()
    c.execute('select name from users')
    data = c.fetchall()
    c.close()
    if len(data) == 0:
        return []
    return data


def user_get_name(uid):
    c = conn_user.cursor()
    c.execute('select name from users where uid = ?', (uid, ))
    c.close()
    data = c.fetchall()
    if len(data) == 0:
        return []
    return data


def user_get_uid(name):
    c = conn_user.cursor()
    c.execute('select uid from users where name = ?', (name, ))
    data = c.fetchall()
    c.close()
    if len(data) == 0:
        return 0
    return data[0][0]


def user_all():
    c = conn_user.cursor()
    c.execute('select name, email from users')
    data = c.fetchall()
    c.close()
    if len(data) == 0:
        return []
    return data


def token_get_new_token(length=8):
    return ''.join([('0'+hex(ord(os.urandom(1)))[2:])[-2:] for x in range(length)])


def driver_get_new_id():
    c = conn_dri.cursor()
    c.execute('select nid from sid')
    data = c.fetchall()
    nid = data[0][0]
    c.execute('update sid set nid = ? where s = 0;', (nid + 1, ))
    conn_dri.commit()
    c.close()
    return nid


def driver_check(uid, token):
    c = conn_dri.cursor()
    c.execute('select drivers')
    actoken = c.fetchall()[0][0]
    c.close()
    conn_dri.commit()


def driver_add(uid, name, type_, ip='0.0.0.0'):
    c = conn_dri.cursor()
    nid = driver_get_new_id()
    token = token_get_new_token()
    try:
        c.execute("insert into drivers (id, user, name, type, ip, token) values (?, ?, ?, ?, ?, ?)",
                  (nid, uid, name, type_, ip, token))
    except Exception as e:
        conn_dri.commit()
        c.close()
        return 'Fail, {0}'.format(str(e))
    conn_dri.commit()
    c.close()
    return 'Success'


def driver_beat(uid, ip='0.0.0.0'):
    c = conn_dri.cursor()
    c.execute("select datetime('now', 'localtime')")
    datetime = c.fetchall()[0][0]
    try:
        c.execute('update drivers set last_beat = ?, ip = ? where id = ?', (datetime, ip, uid))
    except Exception as e:
        c.close()
        conn_dri.commit()
        return 'Fail to beat: {0}'.format(str(e))
    c.close()
    conn_dri.commit()
    return 'Success'


def driver_get_all(did):
    c = conn_dri.cursor()
    c.execute('select * from drivers where id = ?', (did,))
    data = c.fetchall()[0]
    print(data)
    c.close()
    conn_dri.commit()
    return data


def driver_del(did):
    c = conn_dri.cursor()
    c.execute('select * from drivers where id = ?', (did, ))
    data = c.fetchall()
    if len(data) == 0:
        conn_dri.commit()
        c.close()
        return 'No such of driver'
    c.execute('delete from drivers where id = ?', (did, ))
    conn_dri.commit()
    c.close()
    return 'Success'


def driver_get_user(uid):
    c = conn_dri.cursor()
    c.execute('select id from drivers where user = ?', (uid, ))
    data = c.fetchall()
    # print(data)
    c.close()
    conn_dri.commit()
    return data


if __name__ == '__main__':
    # driver_add(1, 'Dri1', 'comm')
    driver_beat(1)
    driver_get_all(1)

