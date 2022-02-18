import requests
import re


def login():
    # session
    session = requests.session()

    # headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }

    # url1-获取token
    url1 = 'https://gitee.com/login'
    # 发送请求获取相应
    res_1 = session.get(url1, headers=headers).content.decode()
    # 正则提取
    token = re.findall('name="authenticity_token" value="(.*?)" />', res_1)[0]
    print(token)

    # url2-登录
    url2 = session
    # 构建表单数据
    data = {

    }
    # 发送请求登录

    # url3-验证


if __name__ == '__main__':
    login()


import requests
import re


def login():
    # session
    session = requests.session()

    # headers
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }

    # url1-获取token
    url1 = 'https://github.com/login'
    # 发送请求获取相应
    res_1 = session.get(url1, headers=headers).content.decode()
    # 正则提取
    token = re.findall('name="authenticity_token" value="(.*?)" />', res_1)[0]
    print(token)

    # url2-登录
    url2 = 'https://github.com/session'
    # 构建表单数据
    data = {
        'commit': 'Sign in',
        'authenticity_token': token,
        'login': 'xingxing98',
        'password': 'liuyongxing123456',
        'trusted_device': '',
        'webauthn-support': 'supported',
        'webauthn-iuvpaa-support': 'unsupported',
        'return_to': 'https://github.com/login',
        # 'allow_signup': '',
        # 'client_id': '',
        # 'integration': '',
        # 'required_field_c875': '',
        'timestamp': '1645011869078',
        'timestamp_secret': '23aaaef338a781b9a6da59ff3a8d7eefdb8c405c7568c82245e539f8c03e9d8b'
    }
    print(data)
    # 发送请求登录

    # url3-验证
    url3 = 'https://github.com/xingxing98'
    response = session.get(url3)
    with open('github.html', 'wb')as f:
        f.write(response.content)


if __name__ == '__main__':
    login()
