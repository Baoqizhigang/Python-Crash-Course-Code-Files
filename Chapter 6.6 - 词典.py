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
    'BOD4':'joe gebbia',
    }
# python 提取字典中的所有键，并依次将它们赋值给变量mangement_title
for mangement_title in board_of_directors.keys():
    print(f"{mangement_title}")
    
print(board_of_directors.keys())    

# python 提取字典中的所有值，并依次将它们赋值给变量mangement
for management in board_of_directors.values():
    print(f"Management:{management.title()}")

print(board_of_directors.values())

board_of_directors = {
    'Leader1':'elon musk',
    'Leader2':'andrew baglino',
    'Leader3':'zachary kirkhorn',
    'BOD1':'james murdoch',
    'BOD2':'robyn m. deholm',
    'BOD3':'ira ehrenpreis',
    'BOD4':'joe gebbia',
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
    'joe gebbia':'board member',
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
    'joe gebbia':'board member',
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
    'joe gebbia':'board member',
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

job_title ={'top leader','leader','leader','board member'}
print(job_title)

management ={'top leader':'elon musk','leader':'andrew baglino'}
print(management)


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

# 更符合现实的情况是，游戏中外星人杂兵应该不止三个
# 且每个外星人都是代码自动生产的
# 我们可以用range()生成30个外星人试试
# 因为是动态创建，所有首先我们来创建一个空列
# 空列表用来存储接下来将创建的外星人
aliens = [ ] 

# 创建30个绿色的外星人
# range()返回一系列的数，其唯一用途就是告诉Python需要重复循环多少次
# 每次执行这个循环的时候，都创建一个外星人
# 外星人的属性如词典中所示
# 然后将这个外星人附加到列表aliens的末尾
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

# 使用一个切片，来显示前5个外星人
# 这些外星人虽然有相同的特征，但每个外星人都是独立的
# 也就是说我们可以独立修改每一个外星人的参数
for alien in aliens [ :5]:
    print(alien)
    
print("……")

# 打印列表的长度，以证明其确实是创建了30个外星人

print(f"Total number of aliens:{len(aliens)}")

# 我们来尝试使用for循环和if语句来修改某些外星人的颜色
aliens = [ ] 

for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens [ :3]:
    if alien ['color'] == 'green':
        alien ['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens [ :5]:
    print(alien)
    
print("……")


# 还可以进一步扩展 增加复杂度
aliens = [ ] 

for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens [ :3]:
    if alien ['color'] == 'green':
        alien ['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens [ :2]:
    if alien ['color'] == 'yellow':
        alien ['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
for alien in aliens [ :5]:
    print(alien)
    
print("……")


# 在字典中存储列表
CEO = {
    'name':'elon musk',
    'parents':['errol musk','maye musk'],
    }

print(f"The CEO of Tesla is {CEO['name'].title()} and his parents are：")

for parent in CEO['parents']:
    print('\t' + parent.title())


# 当需要在一个字典将一个键关联到多个值时，都可以在字典中嵌套一个列表。
# 我们创建一个字典，里面有很多的pop star，而每个明星都有自己的歌曲
# 我们遍历字典的时候，跟每个明星关联的都是一个歌曲列表，而不只是一首歌
# 我们需要使用for循环来遍历与明星相关的歌曲列表
pop_stars = {
    'charlie puth':['see you again','attention',"we don't talk anymore"],
    'robyn rihanna fenty':['umbrella','take a bow','love the way you lie'],
    'chris martin':['fun','want','homesick','joyride'],
    'taylor swift':['love story','lover','me'],
    }


for star, songs in pop_stars.items():
    print(f"\n{star.title()}'s best hits are: ")
    for song in songs:
        print(f"\t《 {song.title()} 》")

#6.4.3 在字典中存储字典
# 在字典中嵌套字典，代码可能很快复杂
# 这时候请务必注意缩进格式和相应的标点符号
pop_stars = {
    'chris martin': {
        'height':'186cm ',
        'age': 48,
        'orgin':'London',   
        },
    'taylor swift': {
        'height':'180cm',
        'age': 35,
        'orgin':'West Reading',    
        },
    }

for pop_star,basic_info in pop_stars.items():
    print(f"\nPop Star: {pop_star.title()}")
    year = 2025 - basic_info['age']
    family_location = basic_info['orgin']
    
    print(f"\t{pop_star.title()} is born in {year}.")
    print(f"\t{pop_star.title()} is {basic_info['height']} tall.")
    print(f"\t{pop_star.title()}'s family is from {family_location}.")


# 以下为第六章额外补充内容
# --------------------------------copy() 方法---------------------------------
# copy()方法
# copy() 方法返回一个字典的拷贝，也即返回一个具有相同键值对的新字典

a = {'one':1,'two':2,'three':[1,2,3]}
b = a.copy()
print(b)

# 注意，copy() 方法所遵循的拷贝原理，既有深拷贝，也有浅拷贝。
# 拿拷贝字典 a 为例，copy() 方法只会对最表层的键值对进行深拷贝，
# 也就是说，它会再申请一块内存用来存放 {'one': 1, 'two': 2, 'three': []}；
# 而对于某些列表类型的值来说，此方法对其做的是浅拷贝，
# 也就是说，b 中的 [1,2,3] 的值不是自己独有，而是和 a 共有。

# 向a中添加新键值对，由于b已经提前将a所有键值对深拷贝过来，因此a添加键值对，不影响b
a = {'one':1,'two':2,'three':[1,2,3]}
b = a.copy()
a ['four'] = 1000
print(a)
print(b)
# 由于b和a共享[1,2,3](浅拷贝)，因此，移除a中列表的元素，也会影响b
a['three'].remove(1)
a['one'] = 111 # 不影响b
print(a)
print(b)

# 从运行结果不难看出，对 a 增加新键值对，b 不变；
# 而修改 a 某键值对中列表内的元素，b也会相应改变。

# --------------------------------update() 方法---------------------------------
# update() 方法可以使用一个字典所包含的键值对来更新己有的字典。
# 在执行 update() 方法时，如果被更新的字典中己包含对应的键值对，
# 那么原 value 会被覆盖；如果被更新的字典中不包含对应的键值对，
# 则该键值对被添加进去。

a = {'one':1,'two':2,'three':3}
a.update({'one':4.5,'four':93})
print(a)

# 由于被更新的字典中已包含key为“one”的键值对，因此更新时该键值对的 value 将被改写；
# 被更新的字典中不包含 key为“four”的键值对，所以更新时会为原字典增加一个新的键值对。

# --------------------------pop() 和 popitem() 方法---------------------------------
# pop() 和 popitem() 方法都是用来删除字典中的键值对，
#不同的是，pop() 用来删除指定的键值对，而 popitem() 用来随机删除一个键值对，
# dictname.pop(key)  -  dictname 表示字典名称，key 表示键。
# dictname.popitem()

tanscript_tom = {'数学':95,'语文':83 ,'化学':97,'物理':94 }
print(tanscript_tom)
tanscript_tom.pop('语文')
print(tanscript_tom)

tanscript_tom = {'数学':95,'语文':83 ,'化学':97,'物理':94 }
print(tanscript_tom)
tanscript_tom.popitem()
print(tanscript_tom)

# 说popitem() 随机删除字典中的一个键值对是不准确的，虽然字典是一种无序的列表，
# 但键值对在底层也是有存储顺序的，popitem() 总是弹出底层中的最后一个 key-value，
# 这和列表的 pop() 方法类似，都实现了数据结构中“出栈”的操作。
# 在这里呢就先打住，不再深入探讨什么是“出栈”，我们现在是初学，主要目标是快速上手写码
# 对于哪些技能可以暂时跳过，哪些技能可以浅尝辄止，哪些技能必须深入学习，
# 我们要有意识地做主动选择。 但是我也把这个选项放在这里，有余力的小伙伴
# 可以自行选择勇攀知识的高峰，我就先撤退了。 

# --------------------------setdefault() 方法------------------------------
# setdefault()方法用来返回某个key对应的 value，
# setdefault()方法语法格式：dictname.setdefault(key, defaultvalue)
# dictname 表示字典名称，key 表示键，defaultvalue 表示默认值（可以不写，不写的话是 None）。
# 当指定的key不存在时，setdefault()会先为这个不存在的 key设置一个默认的defaultvalue，
# 然后再返回 defaultvalue。
#也就是说，setdefault() 方法总能返回指定 key 对应的 value：
#如果key存在，那么直接返回该 key 对应的 value；
#如果key不存在，那么先为key设置默认的defaultvalue，然后再返回key对应的defaultvalue。

tanscript_tom = {'数学':95,'语文':83 ,'化学':97,'物理':94 }
print(tanscript_tom)
# key 不存在，指定默认值
tanscript_tom.setdefault('古汉语',75)
print(tanscript_tom)


tanscript_tom = {'数学':95,'语文':83 ,'化学':97,'物理':94 }
print(tanscript_tom)
# key 不存在，不指定默认值
tanscript_tom.setdefault('古汉语',)
# key 存在，指定默认值，但并不会对原键值对有任何影响
tanscript_tom.setdefault('数学',35)
print(tanscript_tom)








