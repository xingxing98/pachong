import requests
from lxml import etree


class Tieba(object):

    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2'
        print(self.url)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
        }

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        with open('temp.html', 'wb')as f:
            f.write(response.content)
        return response.content

    def parse_data(self, data):
        # 创建element对象
        data = data.decode().replace('<!--', '').replace('-->', '')
        html = etree.HTML(data)
        el_list = html.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a')
        # print(len(el_list))

        data_list = []

        for el in el_list:
            temp = {}
            temp['title'] = el.xpath('./text()')[0]
            temp['link'] = 'https://tieba.baidu.com/' + el.xpath('./@href')[0]
            data_list.append(temp)

        # 获取下一页url
        try:
            next_url = 'https:' + html.xpath('//a[contains(text(),"下一页")]/@href')[0]
        except:
            next_url = None

        return data_list, next_url

    def save_data(self, data_list):
        for data in data_list:
            print(data)

    def run(self):
        # url
        # headers
        next_url = self.url
        while True:
            # 发送请求，获取响应
            data = self.get_data(next_url)
            # 从响应中提取数据（数据和翻页用的url）
            data_list, next_url = self.parse_data(data)
            self.save_data(data_list)
            print(next_url)
            # 判断是否终结
            if next_url == None:
                break


if __name__ == '__main__':
    tieba = Tieba()
    tieba.run()
