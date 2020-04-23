import json,csv

a = {"title": "今天是学习爬虫的第n天！", "date":"2020.4.20", "content":"今天是学习爬虫的第n天！我学习了爬虫基础啦！"}
print(a)
print(type(a))
b = json.dumps(a)
print(b)
print(type(b))
c = json.loads(b)
print(c)
print(type(c))

with open("mytest1.txt", 'a')  as r:
    # wr = csv.writer(r)
    # wr.writerow(a)
    r.write(b)#a只有经过dumps(卸数据)才能在其他文本中使用
print("写入完毕！")


