import requests
from bs4 import BeautifulSoup

session = requests.session()

# 登陆网页
url_login = 'https://accounts.douban.com/j/mobile/login/basic'

data_login = {
    'ck': '',
    'name': '15304801916',
    'password': '8978215',
    'remember': 'false',
    'tickit': 'XE9CQrAB55W9G9SzfMY877aOcqS2hsN-MCtf3JTydEQ_9iCWD5DGLv1UAyL26-FG3kqiVKFpR04*'

}

header = {
    'Origin': 'https://accounts.douban.com',
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
# login_in = requests.post(url=url_login, data=data_login, headers=header)
# print(login_in)
session.post(url_login, headers=header, data=data_login)
print(session.cookies)

# 获取数据
# url = 'http://www.renren.com/974348845'
# header_url = {
#     'Origin': 'http://www.renren.com',
#     'Referer': 'http://www.renren.com/SysHome.do',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
#
# }
# res = session.get(url=url, headers=header_url)
