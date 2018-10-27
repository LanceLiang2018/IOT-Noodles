import requests
import json
import time


host = 'http://localhost:8081'
# host = 'http://192.168.1.100:5000'


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


# 先注册一个设备，获取设备id
did = 2

# 获取token
form = {'did': did}
url = url_for('/get_token')
token = post_data(url, form)

print(token)

# 发送心跳
form['token'] = token
print(post_data(url_for('/beat'), form))

# 接收数据
while True:
    task = post_data(url_for('/command_get_task'), form)
    time.sleep(0.1)
    if task != 'No task.':
        break

task = json.loads(task)
data = task['data']
print(data)
tid = task['tid']
form['tid'] = tid
print('Get Data:', data)
data = 'Success'
form['data'] = data.encode()

# 返回数据
print(post_data(url_for('/command_fetch'), form))




