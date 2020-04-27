# 爬取了豆瓣排行里的“豆瓣新片榜”的电影名，URL，电影基本信息，电影评分信息现在我们将他保存下来
import requests, openpyxl
# 引用requests库
from bs4 import BeautifulSoup

wb = openpyxl.Workbook()
# 利用openpyxl.Workbook()函数创建新的workbook（工作薄）对象，就是创建新的空的Excel文件。
sheet = wb.active
# wb.active就是获取这个工作薄的活动表，通常就是第一个工作簿，也就是我们在上面的图片中看到的sheet1。
sheet.title = '豆瓣新片榜'
# 可以用.title给工作表重命名。现在第一个工作表的名称就会由原来默认的“sheet1”改为"kaikeba"。
sheet['A1'] = '豆瓣新片榜'
# 向单个单元格写入数据
list_name = ['电影名', '网址', '基本信息', '评分']
sheet.append(list_name)
# 写入整行的数据，变量类型是一个列表


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}

res_movies = requests.get('https://movie.douban.com/chart', headers=headers)
# 获取数据
bs_movies = BeautifulSoup(res_movies.text, 'html.parser')
# 解析数据
list_movies = bs_movies.find_all('div', class_='pl2')
# 查找最小父级标签
for movie in list_movies:
    tag_a = movie.find('a')  # tag_s = list_movies[0].find('span', style='font-size:13px;')
    tag_p = movie.find('p')
    tag_s = movie.find('span', class_='rating_nums')
    # 提取第1个父级标签中的<p>标签
    film_name = tag_a.text[25:40].replace(' ', '').replace('\n', '')
    film_url = tag_a['href']
    information = tag_p.text.replace(' ', '').replace('\n', '')
    message = tag_s.text
    # 电影基本信息，使用replace方法去掉多余的空格及换行符
    print('电影名：%s\nURL:%s\n电影的基本信息为：%s\n电影评分信息:%s\n' % (film_name, film_url, information, message))
    # 输出结果
    list = [film_name, film_url, information, float(message)]
    sheet.append(list)
    # 写入整行的数据，变量类型是一个列表

wb.save('豆瓣新片榜.xlsx')
# 保存修改的Excel
wb.close()
# 关闭Excel
