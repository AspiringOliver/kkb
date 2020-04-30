# 创建年级类
class Gradee():
    # 定义初始化⽅法
    def __init__(self, grades):
        # 创建实例化属性self.grades，self.grades_name
        self.grades = str(grades)


    # 定义str魔法⽅法
    def __str__(self):
        # str⽅法的返回值为实例属性self.grades
        return self.grades



l = Gradee('222')
print(type(l))
print('af', l)