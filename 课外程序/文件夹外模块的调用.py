import sys                        #引入sys库体，python的信息模块
sys.path.append('D:\图片\刘慈欣小哥哥')           #系统路径中填写存放.py文件地址，然后通过import方法导入
for i in sys.path:
    print(i)
from Oliver的机密信息 import mySMTP_serve_password as ps           #从.py文件加载内容
print(ps)



