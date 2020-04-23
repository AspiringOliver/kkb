import requests
# 引用requests库
res = requests.get('https://careers.tencent.com/tencentcareer/api/post/Query'     #访问网页地址
                   '?timestamp=1585450579819&countryId=&cityId=&bgIds='           #请求参数，？和网址链接分开
                   '&productId=&categoryId=&parentCategoryId=&attrId=&keyword='   #请求参数，键与值之间使用=
                   '&pageIndex=1&pageSize=10&language=zh-cn&area=cn')             #请求参数，对与对用&
#调用get方法，下载这个字典

json = res.json()
# 使用json()方法，将res对象，转为列表/字典

list_post = json['Data']['Posts']
# 一层一层地取字典，获取歌单列表
print('第一页共有 {}个岗位\n'.format(len(list_post)))


for post in list_post:
# list_post是一个列表，post是它里面的元素
    print(post['RecruitPostName'])
    # 以RecruitPostName为键，查找岗位名称-
