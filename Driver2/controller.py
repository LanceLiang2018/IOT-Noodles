try:    import requestsexcept:    import urequests as requestsimport networkimport jsonimport timehost = 'http://192.168.1.101:8081'def url_for(s):    if s[0] == '/':        return host + s    else:        return host + '/' + sdef post_data(url, prames):    res = ''    txt = '------WebKitFormBoundary7MA4YWxkTrZu0gW'    for d in prames:        res = res + txt + '\r\nContent-Disposition: form-data; name=\"' + d + '\"\r\n\r\n' + str(prames[d]) + '\r\n'    res = res + txt + '--'    headers = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW", 'Cache-Control': "no-cache"}    response = requests.request("POST", url, data=res, headers=headers)    return response.textform = {}def init():    global form    # 先注册一个设备，获取设备id    did = 2    # 获取token    form = {'did': did}    url = url_for('/get_token')    token = post_data(url, form)    print(token)    # 发送心跳    form['token'] = token    print(post_data(url_for('/beat'), form))def get():    global form    while True:        task = post_data(url_for('/command_get_task'), form)        time.sleep(1)        if task != 'No task.':            break    print(task)    task = json.loads(task)    data = task['data']    form['tid'] = task['tid']    print('Data:', data)    form['data'] = 'Success'    res = post_data(url_for('/command_fetch'), form)    print('res of fetch:', res)    return datadef ctrl(dat):    import json    table = {'on' : True, 'off' : False}    dat = json.loads(dat)    if dat['device'] == 1:        set_led(table[dat['action']])def set_led(action):    from machine import Pin    led = Pin(2, Pin.OUT)    led.value(1)    if action:        led.value(0)if __name__ == '__main__':    ctrl(get())