from selenium import webdriver
import time

#设置搜索引擎是chrome,在本地打开谷歌浏览器
driver = webdriver.Chrome()

#使用get()方法请求
driver.get('https://github.com/login')
# html = driver.page_source
# print(html)
time.sleep(2)
#登陆
username = driver.find_element_by_type("passward")
input1 = 'AspiringOliver'
username.send_keys(input1)


driver.close()