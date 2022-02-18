# import requests
# url = 'https://www.baidu.com/s?&wd=Python'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
# }
# response = requests.get(url, headers=headers)
#
# with open('baidu.html', 'wb') as f:
#     f.write(response.content)


import requests
# url = 'https://www.baidu.com/s?&wd=Python'
url = 'https://www.baidu.com/s?&'
data = {
    'wd': 'Python'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}
response = requests.get(url, headers=headers, params=data)

print(response.url)
with open('baidu1.html', 'wb') as f:
    f.write(response.content)