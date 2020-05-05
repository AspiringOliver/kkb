import requests, json
from bs4 import BeautifulSoup

#登陆网页
url_login = 'http://www.renren.com/ajaxLogin/login'

data_login = {
    'email': '15304801916',
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '2b75f49911df5efdc41e6ef79cafd88c9d0f541a1318ba7a7962469822fee593',
    'rkey': '612aa01d5d684652b619e935e1661cb4',
    'f': 'http%3A%2F%2Fwww.renren.com%2F974348845'
}

header = {
    'Origin': 'http://www.renren.com',
    'Referer': 'http://www.renren.com/SysHome.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}

login_in = requests.post(url=url_login, data=data_login, headers=header)

#获取cookies
cookie = login_in.cookies
#把cookie转化为str
# cookie_dict = requests.utils.dict_from_cookiejar(cookie)
# cookie_str = json.dumps(cookie_dict)

#获取数据
url = 'http://www.renren.com/974348845'
header_url = {
    'Origin': 'http://www.renren.com',
    'Referer': 'http://www.renren.com/SysHome.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'

}
res = requests.get(url=url, headers=header_url, cookies=cookie)

#解析数据
soup = BeautifulSoup(res.text, 'html.parser')
#筛选数据
tag = soup.find('b', id='bTotalRpNum')
print(tag.text)