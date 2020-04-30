# 创建年级类
class Grade():
    # 定义初始化⽅法
    def __init__(self, grades):
        # 创建实例化属性self.grades，self.grades_name
        self.grades = str(grades)
        self.grades_name = '年级'

    # 定义str魔法⽅法
    def __str__(self):
        # str⽅法的返回值为实例属性self.grades
        return self.grades


# 创建班级类
class Banji():
    # 定义初始化⽅法
    def __init__(self, banji):
        # 创建实例化属性self.grades，self.banji，self.banji_name
        # self.grades = str(grades)
        self.banji = str(banji)
        self.banji_name = '班级'

    # 定义str魔法⽅法
    def __str__(self):
        # str⽅法的返回值为实例属性self.grades
        return self.banji


# 创建⽼师类，继承Grade类和Banji类
class Teacher(Grade, Banji):
    # 定义初始化⽅法
    def __init__(self, name, subject, grades_name, banji_name):
        # 使⽤类名调⽤⽗类Grade的init⽅法
        Grade.__init__(self, grades_name)
        # 使⽤类名调⽤⽗类Banji的init⽅法
        Banji.__init__(self, banji_name)
        # 创建实例属性name和subject
        self.name = name
        self.subject = subject

    # 定义实例⽅法run
    def run(self):
        # 进⾏格式化输出，依次进⾏接收
        print('我是⽼师%s,%s年级，%d班的%s⽼师' % (self.name, self.grades, int(self.banji), self.subject))


# 创建学⽣类，继承⽗类Grade和 Banj
class Student(Grade, Banji):
    # 定义初始化⽅法
    def __init__(self, name, age, grades_name, banji_name):
        # 使⽤类名调⽤⽗类Grade的init⽅法
        Grade.__init__(self, grades_name)
        # 使⽤类名调⽤⽗类Banji的init⽅法
        Banji.__init__(self, banji_name)
        # 创建实例属性name和subject
        self.name = name
        self.age = age

    # 定义实例⽅法run
    def run(self):
        # 格式化输出
        print('我是%s，%s年级，%s班的学⽣,今年%s岁' % (self.name, self.grades, self.banji, self.age))


# 创建实例对象grade
grade = Grade('2')  # 得到年级
# 进⾏print输出时，会调⽤str⽅法
print('年级', grade)

# 创建实例对象banji
banji = Banji('3')
# 进⾏print输出时，会调⽤str⽅法
print('班级', banji)

# 创建实例对象tea
tea = Teacher('name', 'sub', grade, banji)
# 调⽤实例⽅法
tea.run()

# 创建实例对象stu
stu = Student('⼩张', 19, grade, banji)
# 调⽤实例⽅法
stu.run()
