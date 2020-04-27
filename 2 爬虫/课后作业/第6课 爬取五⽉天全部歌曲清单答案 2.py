import requests
from bs4 import BeautifulSoup

# keyword = input(":")
# try:
#     k = {'ie': 'utf-8', 'fr': 'none', 'src': 'home_none', 'q': keyword}
#     r = requests.get('http://so.com/s', params=k)
#     print(len(r.text))
#     # print(r.text)
# except:
#     print("爬取失败")<div class="ask-list-detials">
for i in range(1, 11):
    url0 = 'https://www.guokr.com/ask/highlight/?page={}'.format(i)
    res = requests.get(url0)
    html = BeautifulSoup(res.text, 'html.parser')
    a = html.find_all('div', class_='ask-list-detials')
    for i in a:
        res_data = i.find('a')
        print('标题：', res_data.text)
        url = res_data['href']
        print(url)

