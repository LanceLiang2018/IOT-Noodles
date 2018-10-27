import requests
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
did = 1

# 获取token
form = {'did': did}
token = post_data(url_for('/get_token'), form)

print(token)

# 发送心跳
form['token'] = token
print(post_data(url_for('/beat'), form))

# 发送数据给设备2
data = 'Data'
dest = '2'
form['dest'] = dest
form['data'] = data
tid = post_data(url_for('/command_new'), form)
print(tid)
form['tid'] = tid

while True:
    res = post_data(url_for('/command_task_stat'), form)
    time.sleep(0.1)
    if res == 'FINISH':
        break

data = post_data(url_for('/command_finish'), form)
print(data)

print('Finish task.')


