from selenium import webdriver
import time

# #静默模式
# from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
# chrome_options = Options()                          #实例化Option对象
# chrome_options.add_argument('--headless')           #把Chrome浏览器设为静默模式
# driver = webdriver.Chrome(options=chrome_options)   #设置引擎为Chrome,在后台打开

#设置搜索引擎是chrome,在本地打开谷歌浏览器
driver = webdriver.Chrome()

#使用get()方法请求
driver.get('https://github.com/login')
# html = driver.page_source #爬取网页源代码
# print(html)
time.sleep(2)
#登陆
username = driver.find_element_by_id("login_field")
input1 = 'AspiringOliver'
username.send_keys(input1)
time.sleep(2)
password = driver.find_element_by_name("password")
input2 = input('请输入密码：')
password.send_keys(input2)
time.sleep(2)

#点击登陆
signin = driver.find_element_by_name("commit")
signin.click()
time.sleep(1)


driver.close()