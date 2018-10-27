import requests


def post_data(url, prames):
    res = ''
    txt = '------WebKitFormBoundary7MA4YWxkTrZu0gW'
    for d in prames:
        res = res + txt + '\r\nContent-Disposition: form-data; name=\"' + d + '\"\r\n\r\n' + str(prames[d]) + '\r\n'
    res = res + txt + '--'
    headers = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW", 'Cache-Control': "no-cache"}
    response = requests.request("POST", url, data=res, headers=headers)
    return response.text


if __name__ == '__main__':
    prames = {'did': 1, 'dest': 2, 'data': 'data_to_send'}
    print(post_data('http://localhost:8080/command_new', prames))
    prames = {'tid': 1}
    print(post_data('http://localhost:8080/command_task_stat', prames))
    prames = {'tid': 1}
    print(post_data('http://localhost:8080/command_task_stat', prames))

