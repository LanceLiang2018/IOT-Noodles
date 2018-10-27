#!/usr/bin/python
# -*- coding:utf-8 -*-  

import json
import time
import requests


def analyze(sentence):
        f = open('words.json', encoding='utf-8')
        m = open('machines.json')
        # dat = f.read()
        dat = '''{"actions": {"关": "off", "开": "on"}, "devices": {"门": [2, "2"], "灯": [1, "1"]}}'''
        # dat = dat.decode('gbk').encode('utf-8')
        # dat = dat.encode('utf-8').decode('gbk')
        print(dat)
        # if dat.startswith(u'\ufeff'):
        #         dat = dat.encode('utf8')[3:].decode('utf8')

        # di = json.loads(dat)
        di = {"actions": {"关": "off", "开": "on"}, "devices": {"门": [2, "2"], "灯": [1, "1"]}}
        # dat = m.read()
        # dat = dat.decode().encode('utf-8')
        # ma = json.loads(dat)
        ma = {"1": "192.168.1.101", "2": "192.168.1.101"}
        machines = []
        actions = []
        for d in di['devices']:
                machines.append(d)
        for d in di['actions']:
                actions.append(d)
        m.close()
        f.close()

        #将要发送给分机的数据
        send = {'machine':None,'device':None,'action':None}
        #判断动词(actions)
        for i in actions:
            if i in sentence:
                send['action'] = di['actions'][i]
        #判断设备
        for i in machines:
            if i in sentence:
                send['device'] = di['devices'][i][0]
                send['machine'] = ma[di['devices'][i][1]]
        if send['machine'] == None or send['device'] == None or send['action'] == None:
                send = None
        return send


host = 'http://192.168.1.101:8081'


def url_for(s):
        if s[0] == '/':
                return host + s
        else:
                return host + '/' + s


def post_data(url, prames):
        res = ''
        txt = '------WebKitFormBoundary7MA4YWxkTrZu0gW'
        for d in prames:
                res = res + txt + '\r\nContent-Disposition: form-data; name=\"' + d + '\"\r\n\r\n' + str(prames[d]) + '\r\n'
        res = res + txt + '--'
        headers = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW", 'Cache-Control': "no-cache"}
        response = requests.request("POST", url, data=res, headers=headers)
        return response.text


did = 0
token = ''
form = {}


def init():
        global did, token, form
        # 先注册一个设备，获取设备id
        did = 1

        # 获取token
        form = {'did': did}
        token = post_data(url_for('/get_token'), form)

        print(token)

        # 发送心跳
        form['token'] = token
        print(post_data(url_for('/beat'), form))

        '''
        # 发送数据给设备2
        data = 'Data'
        dest = '2'
        form['dest'] = dest
        form['data'] = data
        tid = post_data(url_for('/command_new'), form)
        print(tid)
        form['tid'] = tid
        '''


#发送一个从字典转换来的str
# PORT = 10492
#端口
def send_to(send):
        '''
        import socket
        import json
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((send['machine'], PORT))
        s.send(json.dumps(send).encode('utf-8'))
        s.close()'''
        global did, token, form
        data = json.dumps(send)
        # 发送数据给设备2
        dest = '2'
        form['dest'] = dest
        form['data'] = data
        tid = post_data(url_for('/command_new'), form)
        print(tid)
        form['tid'] = tid
        print(form)
        tries = 100
        while tries > 0:
                res = post_data(url_for('/command_task_stat'), form)
                print('Waiting...\tres =', res)
                if res == "FINISH":
                        break
                tries = tries - 1
                time.sleep(1)
        if tries < 0:
                print("Time Out.")
                post_data(url_for('/command_finish'), form)
                return
        data = post_data(url_for('/command_finish'), form)
        print(data)

        print('Finish task.')


        
def main(words):
        #words = '关灯...'
        #words = words.decode('gbk').encode('utf-8')
        #words = words.decode('utf-8')
        print(words)
        send = analyze(words)
        print("send", send)
        if send != None:
                send_to(send)
