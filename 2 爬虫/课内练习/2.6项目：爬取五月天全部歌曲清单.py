import requests

# 引用requests模块

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

for i in range(0, 3):

    url = 'https://movie.douban.com/j/search_subjects'

    param = {'type': 'movie',

             'tag': '热门',

             'sort': 'recommend',

             'page_limit': '20',

             'page_start': i * 20}

    # print(param)

    res_movie = requests.get(url, params=param, headers=headers)

    # 调用get方法，下载电影列表

    json_movie = res_movie.json()

    # 使用json()方法，将response对象，转为列表/字典

    # print(json_movie)

    list_movies = json_movie['subjects']

    # 一层一层地取字典，获取电影名称

    for comment in list_movies:
        # list_movies，comment是它里面的元素

        print(comment['title'])

    # 输出电影名名称
