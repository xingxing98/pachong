from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url = 'http://www.baidu.com'

# 创建一个浏览器对象
driver = webdriver.Chrome()

# 访问指定的url地址
driver.get(url)

# 显示源码
# print(driver.page_source)
# 显示响应对应的url
print(driver.current_url)
# 显示响应对应的标题
print(driver.title)

# time.sleep(2)
# driver.get('http://www.douban.com')
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# driver.close()
# 保存网页快照，常用语验证是否运行或者验证码截图
driver.save_screenshot('baidu.png')
driver.quit()