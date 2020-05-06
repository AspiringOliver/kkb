import requests, schedule, time, smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header
import sys
sys.path.append('D:\图片\刘慈欣小哥哥')           #系统路径中填写存放.py文件地址，然后通过import方法导入
from Oliver的机密信息 import myQQ_email_address as sender           #从.py文件加载内容
from Oliver的机密信息 import mySMTP_serve_password as password           #从.py文件加载内容

start_url = 'http://www.weather.com.cn/weather1d/101050101.shtml'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
res = requests.get(start_url, headers=header)


def weather_spider():
    if res.status_code == 200:
        res.encoding = 'utf-8'
        bs_res = BeautifulSoup(res.text, 'html.parser')
        # print(bs_res)
        weather = bs_res.find_all('p', class_='wea')
        wea0 = weather[0].text
        wea1 = weather[1].text
        temperature = bs_res.find_all('p', class_='tem')
        tem0 = temperature[0].text.replace(' ', '').replace('\n', '')
        tem1 = temperature[1].text.replace(' ', '').replace('\n', '')
        # print('白天天气：{}，温度{}'.format(wea0, tem0))
        # print('晚间天气：{}，温度{}'.format(wea1, tem1))
        content = '白天天气：{}，温度{}\n晚间天气：{}，温度{}'.format(wea0, tem0, wea1, tem1)
        return content


    else:
        print('请求失败')


def send_emile():
    mailhost = 'smtp.qq.com'
    # 把qq邮箱的服务器地址赋值到变量mailhost上，地址应为字符串格式
    qqmail = smtplib.SMTP()
    # 实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的方法和属性了
    qqmail.connect(mailhost, 25)
    # 连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。
    # 以上，皆为连接服务器。

    content = weather_spider()
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


schedule.every(5).seconds.do(send_emile)
# 开始执行任务
while True:  # 加循环是为了执⾏完⼀次任务后不终⽌运⾏
    schedule.run_pending()  # 运行所有可以运行的schedule任务
    time.sleep(1)  # 让程序按秒来检查，如果检查太快，会浪费计算机的资源。
