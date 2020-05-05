import requests

#登陆网页
url_login = 'https://xiaoke.kaikeba.com/example/wordpress/wp-login.php'

data_login = {
    'log': 'kaikeba',
    'pwd': 'kaikeba888',
    'wp-submit': '登录',
    'redirect_to': 'https://xiaoke.kaikeba.com/example/wordpress/2019/10/17/%e5%bc%80%e8%af%be%e5%90%a7%e6%97%a0%e6%95%8c%e5%a5%bd%e5%90%83%e7%9a%84%e9%a3%9f%e5%a0%82%e4%b8%80%e5%91%a8%e8%8f%9c%e8%b0%b1/',
    'testcookie': '1'
}

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
login_in = requests.post(url=url_login, data=data_login, headers=header)

#获取cookie
cookie = login_in.cookies   #提取cookie的方法：调用requests对象（login_in）的cookie属性获得登录的cookie，并赋值给变量cookie。

url_comment = 'https://xiaoke.kaikeba.com/example/wordpress/wp-comments-post.php'

data_comment = {
    'comment': input('请输入您的评论:'),
    'submit': '发表评论',
    'comment_post_ID': '35',
    'comment_parent': '0'
}

comment = requests.post(url_comment,headers=header,data=data_comment,cookies=cookie)

#用requests.post发起发表评论的请求，放入参数：文章网址、headers、评论参数、cookie参数，赋值给comment。

#调用cookie的方法就是在post请求中传入cookies=cookie的参数。

print(comment.status_code)

#打印出comment的状态码，若状态码等于200，则证明我们评论成功。






