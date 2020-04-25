#爬取猫眼电影信息，将电影名称，主演，上映时间爬取下来
import requests
from bs4 import BeautifulSoup

url = 'https://maoyan.com/board'
header = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'

    }
# 获取
res = requests.get(url, headers=header)
# 解析
soup = BeautifulSoup(res.text, 'html.parser')
# 一筛
soup_list = soup.find_all('div', class_='movie-item-info')
# 二筛
for h in soup_list:
    # film_name = h.find('p', class_='name').text
    film_name = h.find('a')['title']
    film_star = h.find('p', class_='star').text
    film_date = h.find('p', class_='releasetime').text
    print(film_name, film_star[10:], film_date , '\n')