import requests, openpyxl
from bs4 import BeautifulSoup
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '要问 上观'

list_name = ['标题', '内容', '作者及日期']
sheet.append(list_name)
#请求数据
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
url = 'https://www.shobserver.com/news/list?section=42&page=1'
res = requests.get(url, headers=header)
#解析数据
soup = BeautifulSoup(res.text, 'html.parser')
#筛选数据
#一筛
resultset = soup.find_all('div', class_="chengshi_wz")
#二筛
for tag in resultset:
    tag1 = tag.find('div', class_="chengshi_wz_h").text
    tag2 = tag.find('div', class_="chengshi_wz_m").text
    tag3 = tag.find('div', class_="chengshi_wz_f").text.replace(' ', '').replace('\n', '')
    list = [tag1, tag2, tag3]
    sheet.append(list)
wb.save('要问 上观.xlsx')
# 保存修改的Excel
wb.close()

    # print(tag1.find('a')['title'])
# <span class="top_label">置顶</span>