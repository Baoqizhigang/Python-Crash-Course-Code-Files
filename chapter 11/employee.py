# -*- coding: utf-8 -*-
class Employee():
    '''一个表示雇员的类'''
    
    def __init__(self, f_name, l_name, salary):
        '''初始化雇员'''
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary
        
    def give_raise(self, amount = 5000):
        '''给雇员加薪'''
        self.salary += amount
        