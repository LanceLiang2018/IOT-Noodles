import sqlite3 as sql
import os

r = input('是否重新初始化数据库？enter/y/yes继续。')
if not ( r == 'y' or r == 'yes' or r == ''):
    print('取消')
    exit(0)

li = os.listdir('.')
for i in li:
    if '.db' in i:
        print('尝试删除 %s' % i)
        os.remove(i)

print('初始化用户数据')
conn = sql.connect('users.db')
c = conn.cursor()
c.execute(
    "create table users ("
    "name varchar(512), "
    "passwd char(32), "
    "email varchar(512), "
    "uid int)")
c.execute('create table token (uid int, token varchar(512))')
c.execute('create table sid (nid int, s int)')
c.execute('insert into sid values (0, 0);')
c.execute('update sid set nid = 1 where s = 0;')
conn.commit()
c.close()
conn.close()

print('建立设备表')
conn = sql.connect('drivers.db')
c = conn.cursor()
c.execute(
    "create table drivers ("
    "id int,"
    "user int,"
    "name varchar(512),"
    "type varchar(512),"
    "ip varchar(32),"
    "token varchar(32),"
    "last_beat datetime)")
c.execute('create table sid (nid int, s int);')
c.execute('insert into sid values (0, 0);')
c.execute('update sid set nid = 1 where s = 0;')
conn.commit()
c.close()
conn.close()


print('建立设备数据表')
conn = sql.connect('drivers_data.db')
c = conn.cursor()
# request.remote_addr
c.execute(
    "create table drivers_data ("
    "id int,"
    "type varchar(512),"
    "name varchar(512),"
    "ip varchar(256))")
c.execute('create table sid (nid int, s int);')
c.execute('insert into sid values (0, 0);')
c.execute('update sid set nid = 1 where s = 0;')
conn.commit()
c.close()
conn.close()
