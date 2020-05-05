import sys                        #引入sys库体，python的信息模块
sys.path.append('D:\Pycharm-community-2019.3.1\PycharmProjects')           #系统路径中填写存放.py文件地址，然后通过import方法导入
for i in sys.path:
    print(i)
import lcx            #从.py文件加载内容
print(lcx.strtest)



