import requests
url = 'https://www.baidu.com'
# response = requests.get(url)
# print(response.text)
# response = requests.get(url)
proxies = {
    'http': 'https://61.133.87.228:55443',
    # 'https': 'https://14.215.212.37:9168',
}
response = requests.get(url, proxies=proxies)
print(response.content.decode())
