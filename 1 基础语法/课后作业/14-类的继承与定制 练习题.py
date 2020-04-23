class Father(object):
    height = 180
    blood_t = 'A'
    weight = 140
class Son(Father):
    edu = '本科'
    def stu(self):
        print('继续深造')
xl = Son()
print('''身高%s,
血型%s,
体重%s
学历%s
''' % (xl.height, xl.blood_t, xl.weight, xl.edu))
xl.stu()

# class Computer(object):
#     color = '蓝色'
#     price = 7600
#
#
# class Huawei(Computer):
#     def __init__(self, brank, color, prize):
#         print('品牌是%s' % brank)
#         print('''在初始化函数中，
#         颜色是%s,
#         价格是%s''' % (color, prize))
#         self.color = '红色'
#         self.price = 5000
#
#
# liu = Huawei('华为','蓝色','3400')
# print('''但实例化后调用属性，
# 颜色依然是%s,
# 价格依然是%s'''%(liu.color,liu.price))