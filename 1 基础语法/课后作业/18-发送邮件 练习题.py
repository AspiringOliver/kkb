from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( Header(name, 'utf-8').encode(), addr))
# 输入Email地址和口令:
from_addr = '3314677250@qq.com'
password = input('请输入密码：\n')
# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com'
# 输入收件人地址:
to_addr = []
n = int(input('您要群发几名好友？'))
for i in range(n):
    ad = input('请输入收件人邮箱地址To: ')
    to_addr.append(ad)

content = '''
    周杰伦 - 晴天
作词：周杰伦
作曲：周杰伦
故事的小黄花
从出生那年就飘着
童年的荡秋千
随记忆一直晃到现在
Re So So Si Do Si La
So La Si Si Si Si La Si La So
吹着前奏望着天空
我想起花瓣试着掉落
'''

msg = MIMEText(content, 'plain', 'utf-8')
msg['From'] = _format_addr(u'嘉兴 <%s>' % from_addr)
msg['To'] = _format_addr(u'尊敬的用户 <%s>' % to_addr)
msg['Subject'] = Header(u'来自Oliver的问候……', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()












