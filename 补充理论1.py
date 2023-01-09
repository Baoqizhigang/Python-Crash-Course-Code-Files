# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 02:02:02 2222

@author: Administrator

"""
you = me = we = all_of_us = 168_668

number_of_my_fans = 1_000_000;

number_of_my_fans = '刚刚达到100万，且在持续增加'

print(number_of_my_fans)


a = 1
print(a) # 打印结果 = 1
print(-a) # 打印结果 = 1
print(3%2) # 计算结果 = 1
print(3//2) # 计算结果 = 1
print(-3//2) # 计算结果 = -2
print(2.3 + True + 2.7) # 计算结果 = 6.0 
#True被当做整数1参与运算，在操作数中有浮点数字，表达式结果也是浮点类型

import math 
#首先要导入Python自带的math模块

print(math.sqrt(900))
#求900的平方根
print(math.pi)
print(math.e)
print(math.ceil(3.9))
print(math.ceil(-3.9))
print(math.floor(3.9))
print(round(-3.9)) 
#非math模块函数，故函数前面不需要加math
print(abs(-3.14))
#非math模块函数，故函数前面不需要加math
print(math.fabs(-3.9))

1.0 == 1
1.0 != 1
True == 1

me = 'Baoqizhigang'
i = 'Baoqizhigang'
me == i

me = 'Baoqizhigang' # 这是在比较字符编码大小
you = 'fans of Baoqizhigang'
you > me

me = 'Baoqizhigang'
fans = [ ] # 空列表，还没有粉丝 ：（
fans > me


fans_from_mars = ['哒喂嘚','螺丝'] 
fans_from_moon = ['翠喜','截锐','肉丝' ] 
fans_from_mars > fans_from_moon

fans_from_mars = ['哒喂嘚','螺丝'] 
fans_from_moon = ['翠喜','截锐','肉丝' ] 
fans_from_mars < fans_from_moon

fans_from_mars = [1,2,3] 
fans_from_moon = ['1','2','3' ] 
fans_from_mars > fans_from_moon

fans_from_mars = [1,2,3] 
fans_from_moon = ['1','2','3' ] 
fans_from_mars != fans_from_moon

fans_from_mars = [1,2,3] 
fans_from_moon = [3,2,1 ] 
fans_from_mars  fans_from_moon

me = 'Baoqizhigang' 
me[0]
me = 'Baoqizhigang' 
me[-1] = 'a'
print(me[-1] )
me = 'Baoqizhigang' 
me[:3]
me = 'Baoqizhigang' 
me[3:5]
me = 'Baoqizhigang' 
me[::-1]# 步长为负值，从右往左获取元素（即原始序列元素的倒置）

me = 'Baoqizhigang' 
me[::2]# 步长为2，从左到右,每隔2个元素获取一个元素
me = 'Baoqizhigang' 
max(me)
me = 'Baoqizhigang' 
min(me)
me = 'baoqizhigang' 
min(me)

len(me)

list('请订阅我的频道')


fans_from_mars = ['哒喂嘚','螺丝'] 
fans_from_moon = ['翠喜','截锐','肉丝' ] 

fans_from_mars += fans_from_moon

print(fans_from_mars)

fans_from_mars = ['哒喂嘚','螺丝'] 
fans_from_moon = ['翠喜','截锐','肉丝' ] 

fans_from_mars.extend(fans_from_moon)

print(fans_from_mars)

message = 'Dog\\s food!'
print(message)

message = 'Hello\u0009 World!'
print(message)

message = 'Dog\'s food!'
print(message)

message = r'Dog\'s food!'
print(message)

the_song_i_learned_today = """

        《谢谢你之歌》
        
听我说：                    听我说：
谢谢你，因为有你，           谢谢你，因为有你，
温暖了四季；                世界更美丽

"""

print(the_song_i_learned_today)

print('I encourage you')
print('to click the LIKE buttom!')

message1= 'I encourage you'
message2= 'to click the LIKE buttom! \n'
message3 = message1 + message2 #变量与变量直接粘贴
print(message3*3) #重要的事情说三遍

type(True)

5 == (2+3)
5 != (2+3)

print(a == a)

print(a > a)

import keywords
import keyword
keyword.kwlist



x = 0 # 设公鸡的初始值是0
y = 0 # 设母鸡的初始值是0

for x in range (0,21):
    for y in range(0,34):
        z = 100 - x - y
        if z%3 == 0  and 5*x + 3*y + z//3 == 100:
            print('公鸡数量：',x,'母鸡数量',y,'小鸡数量',z)
