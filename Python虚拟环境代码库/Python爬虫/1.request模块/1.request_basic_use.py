import requests
url = 'https://www.baidu.com'
response = requests.get(url)
# response.encoding = 'utf8'
# print(response.text)
# print(response.encoding)
# print(response.content.decode())

# print(response.url)
# print(response.status_code)
# print(response.request.headers)
# print(response.headers)
# print(response.cookies)

# print(len(response.content.decode()))
# print(response.content.decode())
herders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}
response1 = requests.get(url, headers=herders)
print(response1.content.decode())
