# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:12:36 2022

@author: Administrator
"""
  
#练习6-1 人
# 使用一个字典来存储一个人的信息，包括名，姓，年龄和居住的城市
# 该字典应当包含键first_name, last_name,born和city。 

info = {'first_name':'selena','last_name':'gomez','born':'1992','city':'Grand Prairie'}
name = info['first_name'] +' ' + info['last_name']
print(f"{name.title()} is born in {info['born']}, her family is from {info['city']}.")
        
#练习6-2 使用一个字典来存储福布斯富豪榜前五位的名字和他们所拥有的财富，国籍，年龄等信息
rich_people = { 'Jeff Bezos':{'net worth':'177B',
                              'nationality':'USA',
                              'age':'59',},
               'Elon Musk':{'net worth':'151B',
                              'nationality':'USA',
                              'age':'51',},
               'Bernard Arnault':{'net worth':'150B',
                              'nationality':'USA',
                              'age':'74',},
               'Bill Gates':{'net worth':'124B',
                              'nationality':'USA',
                              'age':'67',},
               'Mark Zuckerberg':{'net worth':'97B',
                              'nationality':'USA',
                              'age':'38',},
    }
 
for name, info in rich_people.items():
    print(f"\n{name} is {info['age']} old and is from {info['nationality']}.")
    print(f"{name} is one of the richest pepole in the world with the net worth of ${info['net worth']} or more. ")

print('\nI wish at least one of them is my Jinzhubaba. :p ')

#练习6-3 想出前面学过的5个编程术语，将其用作词汇表的键，并将他们的含义作为值存储在词汇表中
#以整洁的方式打印每个术语及其含义。 格式要求：
# 格式一：先打印术语，在它后面加上一个冒号，再打印其含义
# 格式二： 在一行打印术语，再使用换行符(\n)插入一个空行，然后在下一行以缩进的方式打印其含义。

#variable：以看成一个小箱子，专门用来“盛装”程序中的数据。
#list：列表是由一系列特定顺序排列的元素组成的
#tuple：元组也是由一系列按特定顺序排序的元素组成，但元素不可更改。
#dict：是一种无序的、可变的序列，它的元素以“键值对（key-value）”的形式存储。
#string：若干个字符的集合就是一个字符串

terms = {'variable':'以看成一个小箱子，专门用来“盛装”程序中的数据。',
         'tuple':'元组也是由一系列按特定顺序排序的元素组成，但元素不可更改。',
         'list':'列表是由一系列特定顺序排列的元素组成的.',
         'dict':'是一种无序的、可变的序列，它的元素以“键值对”的形式存储。',
         'string':'若干个字符的集合就是一个字符串.',
    }

# 格式一：先打印术语，在它后面加上一个冒号，再打印其含义
for key,value in terms.items():
    print(f"\n{key.title()}: {value}")
  
# 格式二： 在一行打印术语，再使用换行符(\n)插入一个空行，然后在下一行以缩进的方式打印其含义。
for k,v in terms.items():
    print(f"\n{k.title()}: \n")
    print(f"\t{v}")

#练习6-4 在6-3的基础上，再往字典里添加两项，然后用任意一种格式打印出来
terms['int'] = '整数。'
terms['float'] = '浮点数，也就是小数。'

# 格式一：先打印术语，在它后面加上一个冒号，再打印其含义
for key,value in terms.items():
    print(f"\n{key.title()}: {value}")
    
# 6-5 核酸检测人员名单筛查
# 创建一个应该需要接受核酸检测的人员名单，其中有些人已经包含在字典中，而有些人没有。
# 遍历这个人员名单，对于已经参与调查的人，打印一条消息表示感谢
# 对于还未参与的人，打印一条消息通知ta参与核酸检测

residents = ['尚书','吉米','翠喜','李栋梁','大卫德','陈书楠','罗斯','柔斯']

tested_residents = {'翠喜':'阴性',
                    '大壮':'阴性',
                    '尚书':'阴性',
                    '大卫德':'阴性',
                    '珍妮':'阴性',
                    '罗斯':'阴性',
                    '柔斯':'阴性',
                    }
# 格式一
for resident in residents:
    if resident in tested_residents.keys():
        print(f'你好，{resident}! 听我说，谢谢你，因为有你，世界更美丽。')
    else:
        print(f'{resident}同志，请您配合防疫工作，立刻去做核酸检测。')

# 格式二
for resident in residents:
    if resident in tested_residents.keys():
        print(f'你好，{resident}! 听我说，谢谢你，因为有你，世界更美丽。')
        
for resident in residents:
    if resident not in tested_residents.keys():
        print(f'{resident}同志，请您配合防疫工作，立刻去做核酸检测。')


#6-6 在6-1编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为People
#的列表中，遍历这个列表，将其中每个人的所有信息都打印出来。

first_person = {'name':'selena gomez','born':'1992','city':'Grand Prairie'}
second_person = {'name':'chris martin','born':'1972','city':'London'}
thrid_person = {'name':'taylor swift','born':'1986','city':'West Reading'}

people = [first_person,second_person,thrid_person]

for person in people:
    print (f"\nThis is {person['name'].title()}.")
    print(f"\t{person['name'].title()} is born in the year of {person['born']}." )
    print(f"\t{person['name'].title()}'s hometown is {person['city']}. " )










   
    
    