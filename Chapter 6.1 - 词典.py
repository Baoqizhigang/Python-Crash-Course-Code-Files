# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:12:36 2022

@author: Administrator
"""
  
# 6.1 一个简单字典
#最简单的字典只有一个键值对
elon_musk = {'date of birth':'June 28,1971'}

# 字典放在花括号里的一系列键值对表示
# 键和值之间用冒号来分割
# 键值对之间用都好分隔开
# 与键值相关联的值可以是数，字符串，列表乃至字典。
# 字典里的可以存储任意数量的键值对。
elon_musk = {'date of birth':'June 28,1971',\
             'citizenship':'USA',\
             'education':'University of Pennsylvania',\
             'Title':'CEO of Tesla'}
    
print(len(elon_musk))
print(list(elon_musk))
print(list(reversed(elon_musk)))
print(elon_musk.values())
print(elon_musk.items())

# 6.2.1 访问字典里的值
elon_musk = {'date of birth':'June 28,1971',\
             'citizenship':'USA',\
             'education':'University of Pennsylvania',\
             'Title':'CEO of Tesla',\
                 'partner':'Grimes'}
    
print(elon_musk['citizenship'])

#print(lover[,default])

new_partner = elon_musk['partner'] # 访问字典里的值
print (f"Elon Musk's new partner is {new_partner} ." )
print (f"Elon Musk's new partner is {elon_musk['partner']} ." )

# 6.2.2 添加键值对
# 字典是这一种动态结构，可以随时添加键值对
# 要添加键值对，可依次指定字典名，用方括号括起的键和相关联的值
elon_musk = {'date of birth':'June 28,1971'}

elon_musk['citizenship'] = 'USA'
elon_musk['Title'] = 'CEO of Tesla'

print(elon_musk)

# 6.2.3 先创建一个空字典
#使用字典来存储用户提供的数据或在编写能自动生成大量键值对的代码时
#通常需要先定义一个空字典
elon_musk = { }

elon_musk['citizenship'] = 'USA'
elon_musk['Title'] = 'CEO of Tesla'

print(elon_musk)

# 对于字典中不需要信息。使用del语句将相应的键值对彻底删除。 
# 使用del语句时，必须指定字典名和要删除的键。
# 删除的键值对将会永久的消失，除非你再把它们添加回去。
del elon_musk['citizenship']
print(elon_musk)



