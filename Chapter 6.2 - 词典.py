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
print(elon_musk.keys())
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

# 6.2.4 修改字典中的值
alien_0 = {'color':'green'}
print (f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print (f"The alien is now {alien_0['color']}")

alien_0 = {'x_position':0,'y_postion':25,'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")

#向右移动外星人
#根据当前速度确定将外星人向右移动多远
if alien_0 ['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的移动速度肯定很快
    x_increment = 3

# 新位置为旧位置加上移动速度
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position:{alien_0['x_position']}")


# 6.2.6 由类似对象组成的字典
favorite_cars = {
    'Michael':'model 3',
    'Charlie':'model Y',
    'Serena':'model X',
    'Mars':'model 3',
    }

car = favorite_cars['Michael'].title()
print(f"Michael's favorite car is {car}.")

# 6.2.7 使用get 来访问值
# 如果指定的键不存在，就会报错
# 假设你向要获悉elon musk的第一个女朋友名字
# 但这个信息并不存在于字典中
elon_musk = {'date of birth':'June 28,1971',
             'citizenship':'USA',
             'education':'University of Pennsylvania',
             'Title':'CEO of Tesla',
                 'partner':'Grimes',
                 }

print(elon_musk['girl friend'])#字典中无该键

#使用方法get（）在指定的键不存在时返回一个默认值，可以避免程序报错。
#方法get()的第一个参数用于指定键，是必不可少的
#方法get()的第二个参数为指定的键不存在时要返回的值，是可自定义的。

gossip = elon_musk.get('gril friend','No such information.')
print(gossip)

# 如果字典里有键'gril friend'， 就会获得与之相关联的值
# 如果没有，获得指定的默认值，虽然这里没有键'gril friend'
# 但我们获得了一条默认信息，避免了程序报错的情况
# 当指定的键有可能不存在的时候，推荐使用get()方法
# 如果get()方法没有指定第二个参数，python将返回None
# None 并非错误，而是表示所需值不存在的特殊值。

# 6.3 遍历字典

# 6.3.1 遍历所有键值对
#当你想要获取字典里所有信息时，可以使用for循环

board_of_directors = {
    'Leader1':'Elon Musk',
    'Leader2':'Andrew Baglino',
    'Leader3':'Zachary Kirkhorn',
    'BOD1':'James Murdoch',
    'BOD2':'Robyn M. Deholm',
    'BOD3':'Ira Ehrenpreis',
    'BOD4':'Joe Gebbia',
    }
# for循环中要声明两个变量，用于存储键值对中的键和值
# 这两个变量可以使用任意名称
# for 语句里第二部包含字典名和items()方法
# 它能返回一个键值对的列表
# 接下来for循环依次将每个键值对赋值给指定的两个变量
for key, value in board_of_directors.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")

# python 遍历字典中的每个键值对，并将键赋给变量title
# 将值赋给变量name. 
# 这些描述性名称能让人非常轻松地明白函数调用print()的意义
for title, name in board_of_directors.items():
    print(f"\nTitle:{title}")
    print(f"Name:{name}")
    
# 如果不是那么严谨的话，简化一下也是可以的
for k, v in board_of_directors.items():
    print(f"\nKey:{k}")
    print(f"Value:{v}")
    
# 如果持续不严谨的话，倒着来也是可以的
for v, k in board_of_directors.items():
    print(f"\nKey:{v}")
    print(f"Value:{k}")    
    
# 要是再往前走一步，这种也是可以的，但不推荐大家这么操作
for 键, 值 in board_of_directors.items():
    print(f"\n键:{键}")
    print(f"值:{值}")

print(board_of_directors.items())


# 6.2.3 遍历字典中的所有键
# 在不需要使用字典中的值的时候，方法key（）是很有用的
board_of_directors = {
    'Leader1':'elon musk',
    'Leader2':'andrew baglino',
    'Leader3':'zachary kirkhorn',
    'BOD1':'james murdoch',
    'BOD2':'robyn m. deholm',
    'BOD3':'ira ehrenpreis',
    'BOD4':'joe gebbia'
    }
# python 提取字典中的所有键，并依次将它们赋值给变量mangement_title
for mangement_title in board_of_directors.keys():
    print(f"{mangement_title}")
    
print(board_of_directors.keys())    

# python 提取字典中的所有值，并依次将它们赋值给变量mangement
for management in board_of_directors.values():
    print(f"Management:{mangement.title()}")

print(board_of_directors.values())

board_of_directors = {
    'Leader1':'elon musk',
    'Leader2':'andrew baglino',
    'Leader3':'zachary kirkhorn',
    'BOD1':'james murdoch',
    'BOD2':'robyn m. deholm',
    'BOD3':'ira ehrenpreis',
    'BOD4':'joe gebbia'
    }

my_friends = ['charlie puth','elon musk','zoe kang']
for management in board_of_directors.values():
    print(f"Hi {management.title()}")
    #print(management)

    if management in my_friends:
        print(f"\tI am so proud to be your friend!")
        #job_title = board_of_directors[management].title()
        #print(f"\t{management.title()},I see you are {job_title} in Tesla.")


board_of_directors = {
    'elon musk':'top leader',
    'andrew baglino':'leader',
    'zachary kirkhorn':'leader',
    'james murdoch':'board member',
    'robyn m. deholm':'board member',
    'ira ehrenpreis':'board member',
    'joe gebbia':'board member'
    }


my_friends = ['charlie puth','elon musk','zoe kang']
for name in board_of_directors.keys():
    print(f"Hi {name.title()}")

    if name in my_friends:
        print(f"\tI am so proud to be your friend!")
        job_title = board_of_directors[name].title()
        print(f"\t{name.title()},I see you are {job_title} in Tesla.")
        
#方法keys()并非只能用于遍历。实际上，它返回一个列表，其中包含字典中的所有值
#因此，下面的代码值合适'baoqizhigang'是否包含在这个里诶包中。
# 如果不包含，就返回一条消息。 
if 'baoqizhigang' not in board_of_directors.keys():
    print('Baoqizhigang is not a board member of Tesla.')



# 6.3.6 按特定顺序遍历字典中的所有键
# 要以特定的顺序返回元素，一种办法是在for循环中对返回的键进行排序
# 可使用函数sorted()来获得按特定顺序排列的键列表的副本
board_of_directors = {
    'elon musk':'top leader',
    'andrew baglino':'leader',
    'zachary kirkhorn':'leader',
    'james murdoch':'board member',
    'robyn m. deholm':'board member',
    'ira ehrenpreis':'board member',
    'joe gebbia':'board member'
    }

# 对dictionary.keys()的结果调用sorted()。
# 这让Python列出字典中的所有键，并在遍历前对这个列表进行排序
for name in sorted (board_of_directors.keys()):
    print(f"{name.title()}, than you for running the company!")

# 6.3.4 在遍历字典中所有的值的时候剔除重复项
# 当提取字典里的值的时候，若值之间存在重复项，可用集合（set)。
# 集合中的每个元素都必须是独一无二的
board_of_directors = {
    'elon musk':'top leader',
    'andrew baglino':'leader',
    'zachary kirkhorn':'leader',
    'james murdoch':'board member',
    'robyn m. deholm':'board member',
    'ira ehrenpreis':'board member',
    'joe gebbia':'board member'
    }

#通过对包含重复元素的列表调用，可以让Python找出列表中独一无二的元素，
# 并使用这些元素来创建一个集合。
# 这里是用set（）来提取board_of_directors.values()不同的董事类型
print("There are three types of board of directors in Tesal:")
for job_title in set(board_of_directors.values()):
    print(job_title.title())


# 集合与字典很容易混淆，因为他们都是一对花括号定义的。
# 但当花括号里没有键值对的时候，定义的很可能就是集合。
# 不同于列表和字典，集合不会以特定顺序存储元素。 
job_title ={'top leader','leader','leader','board member','board member'}
print(job_title)

# 6.4嵌套
# 嵌套：将一系列字典存储在列表中，或是将列表作为值存储在字典中
# 可以在列表中嵌套字典，在字典中嵌套列表，在字典中嵌套字典。
# 假设当你需要管理成群结对的外星人的时候，你需要创建一个外星人列表，其中每个外星人都是一个字典
# 首先创建3个字典，每个字典是一个外星人
# 然后将这些字典存储在一个aliens的列表中
# 最后遍历这个列表，将每个外星人打印出来
alien_0 = {'color':'green','points': 5 }
alien_1 = {'color':'yellow','points': 10 }
alien_2 = {'color':'red','points': 15 }

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)























