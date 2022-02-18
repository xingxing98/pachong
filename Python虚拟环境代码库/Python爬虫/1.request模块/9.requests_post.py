# import requests
# import json
#
#
# class King(object):
#
#     def __init__(self, word):
#         self.url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=c86e10c2b42727c3'
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/96.0.4664.93 Safari/537.36'
#         }
#         self.data = {
#             'from': 'zh',
#             'to': 'en',
#             'q': word
#         }
#
#     def get_data(self):
#         # 使用post方法发送一个请求，data为请求体的字典
#         response = requests.post(self.url, data=self.data, headers=self.headers)
#         return response.content
#
#     # def parse_data(self, data):
#     #     # loads方法将json字符串转换成python字典
#     #
#     #     dict_data = json.loads(data)
#     #
#     #     try:
#     #         print(dict_data['content']['out'])
#     #
#     #     except:
#     #         print(dict_data['content']['word_mean'])
#
#     def run(self):
#         # 爬虫逻辑
#         # url
#         # headers
#         # data字典
#         # 发送请求获取响应
#         response = self.get_data()
#         print(response)
#         # 数据解析
#         # self.parse_data(response)
#
#
# if __name__ == '__main__':
#     # word = input('请输入要翻译的单词或句子：')
#     king = King('字典')
#     king.run()


# import requests
# import json
#
#
# class King(object):
#
#     def __init__(self, word):
#         self.url = 'https://fanyi.baidu.com/v2tr'
#         self.headers = {
#             'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
#         }
#         self.data = {
#             'from': 'auto',
#             'to': 'auto',
#             'q': word
#         }
#
#     def get_data(self):
#         # 使用post方法发送一个请求，data为请求体的字典
#         response = requests.post(self.url, data=self.data, headers=self.headers)
#         return response.content
#
#     def parse_data(self, data):
#         # loads方法将json字符串转换成python字典
#
#         dict_data = json.loads(data)
#
#         try:
#             print(dict_data['content']['out'])
#
#         except:
#             print(dict_data['content']['word_mean'])
#
#     def run(self):
#         # 爬虫逻辑
#         # url
#         # headers
#         # data字典
#         # 发送请求获取响应
#         response = self.get_data()
#         # print(response)
#         # 数据解析
#         self.parse_data(response)
#
#
# if __name__ == '__main__':
#     word = input('请输入要翻译的单词或句子：')
#     king = King(word)
#     king.run()
import json
import sys
import requests


class King(object):
    def __init__(self, word):
        self.url = 'https://ifanyi.iciba.com/index.php?c=trans'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
        }
        self.data = {
            'from': 'auto',
            'to': 'auto',
            'q': word
        }

    def get_data(self):
        response = requests.post(self.url, data=self.data, headers=self.headers)
        return response.content

    def pase_data(self, data):
        dict_data = json.loads(data)
        print(dict_data['out'])

    def run(self):
        response = self.get_data()
        print(response)
        self.pase_data(response)


if __name__ == '__main__':
    word = input('请输入要翻译的单词或句子：')
    # word = sys.argv[-1]
    king = King(word)
    king.run()

