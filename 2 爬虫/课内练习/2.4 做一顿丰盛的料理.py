# 把下厨房“本周最受欢迎菜谱”的“菜名、URL、食材”打印出来。
# 地址：http://www.xiachufang.com/explore/
import requests
from bs4 import BeautifulSoup

#未知
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

# 获取数据
res = requests.get('http://www.xiachufang.com/explore/', headers=headers)
# print(type(res))    #<class 'requests.models.Response'>

# 解析数据
bs_foods = BeautifulSoup(res.text, 'html.parser')
# print(type(bs_foods))   #<class 'bs4.BeautifulSoup'>

# 筛选数据
#初筛
fname_list = bs_foods.find_all('p', class_='name')
fmaterials_list = bs_foods.find_all('p', class_="ing ellipsis")
# print(type(fname_list))  #<class 'bs4.element.ResultSet'>
#细筛
list_ultimate = []
for i in range(len(fname_list)):
    list_food = [fname_list[i].text[18:-15],
                 fname_list[i].find('a')['href'],
                 fmaterials_list[i].text[1:-1]]
    list_ultimate.append(list_food)
for i in list_ultimate:
    print(i)
