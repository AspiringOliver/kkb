import requests, schedule, time, smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header
import sys
sys.path.append('D:\图片\刘慈欣小哥哥')           #系统路径中填写存放.py文件地址，然后通过import方法导入
from Oliver的机密信息 import myQQ_email_address as sender           #从.py文件加载内容
from Oliver的机密信息 import mySMTP_serve_password as password           #从.py文件加载内容






def movie_spider():
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
    url = 'https://movie.douban.com/chart'
    res_movies = requests.get(url, headers=header)
    bs_movies = BeautifulSoup(res_movies.text, 'html.parser')
    list_movies = bs_movies.find_all('div', class_='pl2')
    list_all = []
    for movie in list_movies:
        tag_a = movie.find('a')
        name = tag_a.text.replace(' ', '').replace('\n', '')
        # 电影名，使用replace方法去掉多余的空格及换行符
        url = tag_a['href']
        # 电影详情页的链接
        tag_p = movie.find('p', class_='pl')
        # 提取父级标签中的<p>标签
        information = tag_p.text.replace(' ', '').replace('\n', '')
        # 电影基本信息，使用replace方法去掉多余的空格及换行符
        tag_div = movie.find('div', class_='star clearfix')
        # 提取父级标签中的<div>标签
        rating = tag_div.text.replace(' ', '').replace('\n', '')
        # 电影评分信息，使用replace方法去掉多余的空格及换行符
        list_all.append(name+url+information+rating)
        # 将电影名、URL、电影基本信息和电影评分信息，封装为列表，用append方法添加进list_all
    return list_all


def send_emile():
    mailhost = 'smtp.qq.com'
    # 把qq邮箱的服务器地址赋值到变量mailhost上，地址应为字符串格式
    qqmail = smtplib.SMTP()
    # 实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的方法和属性了
    qqmail.connect(mailhost, 25)
    # 连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。
    # 以上，皆为连接服务器。

    movie_list = movie_spider()
    content = '\n'.join(movie_list) #join()函数，列表转字符串
    print(content)
    qqmail.login(sender, password)
    # 登录邮箱，第一个参数为邮箱账号，第二个参数为邮箱密码
    # 以上，皆为登录邮箱。

    receiver = input('请输入收件人的邮箱：')
    # 获取收件人的邮箱。
    # content = input('请输入邮件正文：')
    # 输入你的邮件正文，为字符串格式
    message = MIMEText(content, 'plain', 'utf-8')
    # 实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码
    subject = input('请输入你的邮件主题：')
    # 输入你的邮件主题，为字符串格式
    message['Subject'] = Header(subject, 'utf-8')
    # 在等号的右边是实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码，然后赋值给等号左边的变量message['Subject']。
    # 以上，为填写主题和正文。
    try:
        qqmail.sendmail(sender, receiver, message.as_string())
        print('邮件发送成功')

    except:
        print('邮件发送失败')
    qqmail.quit()


schedule.every(1).seconds.do(send_emile)
# 开始执行任务
while True:  # 加循环是为了执⾏完⼀次任务后不终⽌运⾏
    schedule.run_pending()  # 运行所有可以运行的schedule任务
    time.sleep(1)  # 让程序按秒来检查，如果检查太快，会浪费计算机的资源。
