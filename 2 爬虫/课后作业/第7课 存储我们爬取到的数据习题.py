import requests, csv
from bs4 import BeautifulSoup

r = open("第7课.csv", 'a', newline='', encoding='utf-8-sig')
writ = csv.writer(r)
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
        writ.writerow([res_data.text, url])
r.close()
