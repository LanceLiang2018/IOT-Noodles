import requests

url = "http://localhost:8080/command_new"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"did\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"dest\"\r\n\r\n2\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data\"\r\n\r\ndata_to_send\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    'Postman-Token': "80a82416-85cb-4b36-87f4-b89cd84af320"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)


import requests

url = "http://localhost:8080/command_task_stat"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"tid\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    'Postman-Token': "1d081004-3be7-4789-9fe6-ae55d37b66d1"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)


import requests

url = "http://localhost:8080/command_get_task"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"did\"\r\n\r\n2\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"token\"\r\n\r\nff36b4d4e14b7ed1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    'Postman-Token': "56e3ebca-341b-4944-89de-5fc6a39a65df"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)


import requests

url = "http://localhost:8080/command_fetch"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"did\"\r\n\r\n2\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"token\"\r\n\r\nff36b4d4e14b7ed1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"tid\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data\"\r\n\r\nresponse_data\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    'Postman-Token': "081da287-ed50-4bf3-b611-1c3f90d76f15"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

import requests

url = "http://localhost:8080/command_finish"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"did\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"token\"\r\n\r\n46c7f01c9548c7da\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"tid\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    'Postman-Token': "1a77b48c-ba7f-400d-9b86-fa6d22e7a554"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

import requests

url = "http://localhost:8080/command_task_stat"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"tid\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
