import requests
# from requests import utils
url = 'https://www.baidu.com'
response = requests.get(url)

print(response.cookies)

# dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
cookies_dict = requests.utils.dict_from_cookiejar(response.cookies)
dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies_dict)
print(dict_cookies)








