# 煎饼果⼦⽼师傅配⽅
class Master(object):  # Master⼤师 师傅
    def __init__(self):
        self.kongfu = "古法煎饼果⼦配⽅"

    def make_cake(self):
        print("[古法] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)
        # 煎饼果⼦培训学校配⽅


class School(object):  # 学校 培训班（新东⽅，你懂得）
    def __init__(self):
        self.kongfu = "现代煎饼果⼦配⽅"

    def make_cake(self):
        print("[现代] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)


class Damao(School, Master):
    def __init__(self):
        self.kongfu = "猫氏煎饼果⼦配⽅"

    def make_cake(self):
        self.__init__() #调用本类初始化函数括号中无self
        print("[猫氏] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)

    def old_cake(self):
        Master.__init__(self) #调用父类初始化函数括号中self
        print("[古法] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)

    def new_cake(self):
        School.__init__(self) #调用父类初始化函数括号中self
        print("[现代] 按照 <%s> 制作了⼀份煎饼果⼦..." % self.kongfu)


lisi = Damao()
print(lisi.kongfu)
lisi.old_cake()
lisi.new_cake()
lisi.make_cake()
