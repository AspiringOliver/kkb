# import csv
#
# with open("mytest.csv", 'a', encoding='utf-8-sig')  as r:
#     writ = csv.writer(r)
#     writ.writerow([41, 42, 43])
#     print("写入完毕！")
# with open("mytest.csv", encoding='utf-8-sig')  as r:
#     rea = csv.reader(r)
#     # 使用csv的reader()方法，创建一个reader对象
#     for content in rea:
#         # 遍历rea对象的每一行
#         print(content)
# print("读取完毕！")



import auxiliary, time
ticks1 = time.time()
localtime1 = time.localtime(time.time())
localtime2 = time.asctime(localtime1)
print('本地时间（方式1）：', localtime2)
print('请开始输入算式:\n（每次结束一次操作请按一次回车）\n：')
sig = 'null'

while 1:
    auxiliary.number()
    if auxiliary.flag == 1:
        break
    auxiliary.signal()
    if auxiliary.flag == 1:
        break

ticks2 = time.time()
print('代码花费时间：', ticks2 - ticks1, '秒')

print('='*10, '延时一秒钟', '='*10)
time.sleep(1)
print('='*10, '延时结束', '='*10)

localtime1 = time.localtime(time.time())
print('本地时间（localtime）：', localtime1)
localtime2 = time.asctime(localtime1)
print('本地时间（方式1）：', localtime2)
localtime3 = time.strftime('%Y-%m-%d %H:%M:%S', localtime1)
print('本地时间（方式2）：', localtime3)
