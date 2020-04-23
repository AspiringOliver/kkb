#self的作用：self会在类的实例化中接收传入的数据， 在代码中运行。
#类中的一个类方法需要调用另一个类方法或类属性，都需要使用self。
#总结：类方法中调用类内部属性或者是其他方法时，需要使用self来代表实例。


#1.1.0
# class Information(object):    #object是所有类的父类
#     def __init__(self, name):
#     #初试化方法无需调用，对象实例化时自动执行
#         print(name)
#         self.n = name
#         #此时的self.n可以理解为Information这个类的‘全局变量’
#
#     def other(self, constellation, age):#累赘
#         print('''
#         My name is %s,
#         my constellation is %s,
#         Im %s years old.
#         ''' % (self.n, constellation, age))
#
#
# liu = Information('Oliver')
# liu.other( 'virgo', 18)   #self属性只会在方法创建的时候出现，方法调用时就不需出现


#1.2.0
# class Information(object):       #object是所有类的父类
#     def __init__(self, name, constellation, age):
#     #初试化方法无需调用，对象实例化时自动执行
#     #利用init初始化方法的特点，我们可以在初始化方法中完成类属性的创建及类属性的赋初值。
#         print(name)             #此时name不算类属性
#         self.n = name           #‘类属性’的赋初值
#         self.c = constellation  #‘类属性’的赋初值
#         self.a = age            #‘类属性’的赋初值
#
#     def other(self):
#         print('''
#         My name is %s,
#         my constellation is %s,
#         Im %s years old.
#         ''' % (self.n, self.c, self.a))
#         #只要在othor()方法内部调用类属性(在初始化方法中)
#         # ，就可以实现同样的功能，没有必要把参数再传递一遍。
#
# liu = Information('Oliver', 'virgo', 18)
# liu.other()



class Inf(object):       #object是所有类的父类
    def __init__(self, name, age):
        self.n = name           #‘类属性’的赋初值
        self.a = age            #‘类属性’的赋初值


    def na(self):
        print('''
        My name is %s,
        '''%self.n)


    def ag(self):
        print('''
        Im %s years old.
        '''%self.a)


ol = Inf('Oliver', 23)
ol.na(),ol.ag()
