class Nefu_grades(object):
    def __init__(self, grade):
        print('年级：%s'%grade)

class Nefu_class(object):
    def __init__(self, n_class):
        print('班级：%s'%n_class)

class Teacher(Nefu_grades, Nefu_class):
    def __init__(self, gr, n_c):
        self.gr = gr
        self.n_c = n_c
        print('以下展示教师类')
    def run(self, subject, name):
        Nefu_grades.__init__(self, self.gr)
        Nefu_class.__init__(self, self.n_c)
        print('讲授学科：%s'%subject)
        print('教师姓名：%s\n' %name)
class Student(Nefu_grades, Nefu_class):
    def __init__(self, gr, n_c):
        self.gr = gr
        self.n_c = n_c
        print('以下展示学生类')

    def run(self, subject, name):
        Nefu_grades.__init__(self, self.gr)
        Nefu_class.__init__(self, self.n_c)
        print('学生年纪：%s'%subject)
        print('学生姓名：%s' %name)

zhangping = Teacher(3, '六班')
zhangping.run('math', '小张')

liu = Student(3, '六班')
liu.run(18, '小刘')


