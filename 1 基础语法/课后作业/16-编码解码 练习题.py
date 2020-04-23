# 计算机语言有一个相同之处，就是最前面都有一个字母‘b’，这是代表它是bytes(字节)类型的数据。
# myfile = open(r'D:\通信学习\考研资料\毕设\python 课\1基础语法\12编码与解码 读与写\test1.txt',encoding='utf-8')

# k = b'\xe5\x93\x88\xe5\x96\xbd\xef\xbc\x8c\xe5\xa4\xa7\xe5\xae\xb6\xe5\xa5\xbd'.decode('utf-8')
# myfile = open(r'test1.txt', 'a', encoding='utf-8')
# myfile.write(k)
# myfile.close()


with open(r'test.txt', 'r', encoding='utf-8') as myfile1:
    print(myfile1.read())

with open(r'test.txt', 'a', encoding='utf-8') as myfile2:
    myfile2.write('\n哈喽，⼩伙伴们，⼤家好，今后我们要⼀起好好学习哦')
