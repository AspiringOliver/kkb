import requests
from bs4 import BeautifulSoup

# # 获取数据
# res = requests.get('https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc')
#
# # 解析数据
# soup = BeautifulSoup(res.text, 'html.parser')
# # print(type(soup))
#
# # 一筛
# list = soup.find_all('span', class_="bjh-p")  # 标签与属性应在同级别
# # print("想找选段文本都在这里了：")
# # for item in list1:
# #     print(item) # 打印item
#
# # 二筛
# for i in range(len(list)):
#     print(list[i].text)
# # print(len(list[0].text))

#==================================================================
# 获取数据
res = requests.get('http://www.shicimingju.com/book/sanguoyanyi.html')

# 解析数据
soup = BeautifulSoup(res.text, 'html.parser')
# print(type(soup))  #<class 'bs4.BeautifulSoup'>

# 一筛
Rset1 = soup.find_all('div', class_="book-mulu")  # 标签与属性应在同级别，
# print("想找选段文本都在这里了：")
# for item in Rset1:
#     print(item) # 打印item

# 二筛
for list in Rset1:
    Rset2 = list.find_all('a')#find_all可省略作为对朝左对象简略版

    # #三筛1：
    # goal_list = []
    # for list in Rset1:
    #     goal =list.text
    # 三筛2：
    for i in range(len(Rset2)):
        goal = Rset2[i].text
        print(goal)
        with open('三国演义目录.txt', 'a', encoding='utf-8-sig') as book:
            book.write(goal)
            book.write('\n')
