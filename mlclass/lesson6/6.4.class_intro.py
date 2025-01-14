#!/usr/bin/python
#  -*- coding:utf-8 -*-

"""
    python面向对象(OOP)的简单介绍
     __init__（self,*args） 初始化函数，类似java的构造函数

"""
class People:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.__score = s
        self.print_people()
        # self.__print_people()   # 私有函数的作用

    def print_people(self):
        str = u'%s的年龄：%d，成绩为：%.2f' % (self.name, self.age, self.__score)
        print str

    __print_people = print_people


class Student(People):
    def __init__(self, n, a, w):
        # print "Student.__init__"
        People.__init__(self, n, a, w)
        self.name = 'Student ' + self.name

    def print_people(self):
        # print "Student.print_people"
        str = u'%s的年龄：%d' % (self.name, self.age)
        print str


def func(p):
    p.age = 11


if __name__ == '__main__':
    p = People('Tom', 10, 3.14159)
    func(p)     # p传入的是引用类型
    p.print_people()
    print

    # # 注意分析下面语句的打印结果，是否觉得有些“怪异”？
    j = Student('Jerry', 12, 2.71828)
    print
    #
    # # 成员函数
    p.print_people() #继承
    j.print_people()
    print
    #
    People.print_people(p) #多态
    People.print_people(j)
