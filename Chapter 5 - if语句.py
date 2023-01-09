# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:12:36 2022

@author: Administrator
"""

#Python 编程，从入门到实践  - 第五章 - if语句
# 5.1 一个简单的例子 
my_cars = ['bm-别摸我-w','tes-铁丝拉-la','ha-哈佛','w-武陵虹光-lhg','byyade-比丫嘚']
# 下面的操作将首先检查当前的汽车名字是否是'byyady-比丫蒂'
# 如果是，就以全大写的方式打印（不影响中文字符）
# 若不是，就以首字母大写的方式打印（不影响中文字符）
for my_car in my_cars:
    if my_car == 'byyade-比丫嘚':
        print(my_car.upper())
    else:
        print(my_car.title())
        
my_cars = ['biemowo','tiesila','ha-ha-fo','wuninglanguang','byyade']

for my_car in my_cars:
    if my_car == 'byyade':
        print(my_car.upper())
    else:
        print(my_car.title())
       
        
# 5.2 条件测试
# 每条if语句的核心都是一个值为True/False的表达式，这种表达式即为条件测试。 
# Python根据条件测试的值为True/False来决定是否执行if语句中的代码
# 如果条件测试的结果为True，Python就执行紧跟在if语句后面的代码；
# 如果条件测试的结果为False，Python就不会执行紧跟在if语句后面的代码；

# 5.2.1 检查是否相等
# 大多数条件是将一个变量的当前值跟特定值进行比较。
my_car = 'byyade' # 声明变量且赋值（但是在C++里这两步可以分开）
# 一个等号是一个称述，可理解为将变量my_car的值设置为'byyade'
my_car == 'byyade' # 两个等号是相等运算符，在左右两边相等时返回True值
# 两个等号是发问，可理解为：变量my_car的值是'byyade'吗？

# 5.2.2 检查是否相等时忽略大小写
my_car = 'ByYAde' 
my_car == 'byyade' #大小写不同的值被视为不同

my_car = 'ByYAde' 
my_car.lower() == 'byyade'#这个算是耍个小聪明
# 上一句是在问：变量my_car的值的全小写格式，是否是'byyade'？
# 如果大小写无关紧要，只想检查变量的值，可将变量的值转化为小写后再比较
print(my_car)# 函数lower()不会修改最初赋给变量my_car的值，这种比较不影响原来的变量。

# 5.2.3 检查是否相等
# 要检查两个值是否不相等，需要使用 != 的组合
requested_hotpot_condiment = '黄冰糖' #客人想要吃偏回甜儿的火锅
if requested_hotpot_condiment != '油泼辣子': #但本店只支持微辣和重辣
    # 这里不等于为True， 所以Python立刻执行紧跟在后面的代码。
    print("跟客户反馈本店没有这个配料")
    
# 5.2.4 数值比较
your_age = 18 
your_age == 18


# 当你让被人来猜你的年龄的时候，如果对方的answer为18
answer = 18
if answer == 18:
    print('好眼力，本人18，貌美如花')
    
# 当你让被人来猜你的年龄的时候，如果对方的answer不是18    
answer = 78
if answer != 18:
    print('趁老娘还在微笑的时候，请你见好就收') 

age = 18
age < 22 # Python返回 True
age <= 22  # Python返回 True
age > 19  # Python返回 False
age >=19  # Python返回 False

# 5.2.5 检查多个条件 
# 当你需要两个条件同时为True时才执行相应的操作，需要引入关键字and 和 or
# 5.2.5.1 使用 and 检查多个条件
age_you = 19 #大学生
age_me = 16  #中学生
age_you >=19 and age_me >=19 # Python返回 False
(age_you <22) and (age_me <22) # Python返回 True
# 加上圆括号，可读性更好
#5.2.5.2 使用 or 检查多个条件，只要有至少一个条件满足，则Python返回True；
age_you = 19 #大学生
age_me = 16  #中学生
(age_you >=19) or (age_me >=19) # Python返回 True
(age_you <=16) or (age_me <=16) # Python返回 True

# 5.2.6 检查条件值是否包含在列表中 - 使用关键字in 
''' 叮咚-小知识
python 中，in 与 not in 是用来作为逻辑判断的另一种方式。可以理解成这样：
in 右侧的内容里，是否包含了左侧的内容。 包含返回真-True，不包含返回假-False。       
not in  右侧的内容里是否不包含左侧的内容。不包含返回真，包含返回假
返回真时，Python立刻执行紧随其后的代码，否则不执行。 
in 与 not in 可以放在任何允许添加条件判断的位置。如while  、 if 等。
'''
standard_hotpot_condiment = ['油泼辣子','油酥花椒','老牛油']
#本店的火锅锅底配料只支持微辣和重辣
request_from_customerA = '黄冰糖' #客人想要吃偏回甜儿的火锅 
request_from_customerA  in standard_hotpot_condiment
# Python返回 False, 店家无法执行这样的配料要求，请顾客移步隔壁省
request_from_customerB = '棉花糖' #这是什么奇葩要求
request_from_customerB  in standard_hotpot_condiment
# Python返回 False, 店家回应：鸽屋嗯

binary_digits = ['0','1'] # 这是一个事实

for digit in binary_digits:
    if digit == '0': 
        #这一步会用'0.5'这个数字去遍历匹配表格里是两个元素，做一个匹配度的条件测试
        #如果匹配成功，那就返回真-True， 系统打印结果：这确实是一个二进制的基数
        #如果匹配不成功，则系统返回逻辑假的结果，并告诉你：You are fooling yourself!
        print('这确实是一个二进制的基数')
    else:
        print('You are fooling yourself!')
#最后系统再一次告诉你，在二进制的世界里只有0和1的存在。        
print(f"This's a world only for digits:{binary_digits[0]} & {binary_digits[1]}.")
#这里有个bug， 我们在后面来解决

# 5.2.7 检查特定值是否不包含在列表中 - 使用关键字 not in
# 比如你的微信朋友圈里，刚刚哪个说你像78岁的朋友，你把ta拉黑了

blacklist = ['俊熙','恩熙','悯熙'] 
wechatfriend_1 = '钟嘉良'
# 假设你开发了了一款聊天软件
# 当对法打开你的微信，且对方不在你的黑名单内，那ta的屏幕上自动显示如下信息：
if wechatfriend_1 not in blacklist:
    # 如果确实不在黑名单内，Python返回 True，并执行下面这条代码
    print(f'{wechatfriend_1},快来跟我打个招呼吧！')





----------------------- 或许是时候休息一下了 ---------------------------




# 5.3 if语句
# python里 if条件语句是流程控制语句
# if语句的核心作用是控制程序走向哪一个逻辑分支。

# 5.3.1 简单的if 语句
# 假设进入医院的门诊部需要你持有48小时内有效核酸报告
hours = 49
if hours <= 48: # 这一行是测试的条件，检查你的HS报告时间是否在48小时内
    #若条件测试结果为True，Python会立刻执行下面这条代码 
    print('你可以进入医院的门诊部。')
    #在if语句中，缩进的作用与在for循环中一致
    #如果条件测试通过，将执行if 语句后面的所有缩进的代码
    print('在门诊部期间请全程佩戴好口罩。')

# 5.3.2 if-else 语句
# 有时候需要在条件测试通过时执行一种操作，未通过时执行另一种操作；
# if-else语句类似简单的if语句，其中的else语句让指定条件测试未通过时执行另一种操作

# 假设进入医院的门诊部需要你持有48小时内有效核酸报告
hours = 49
if hours <= 48: # 这一行是测试的条件，检查你的HS报告时间是否在48小时内
    #若条件测试结果为True，Python会立刻执行下面这条代码 
    print('你可以进入医院的门诊部。')
    #在if语句中，缩进的作用与在for循环中一致
    #如果条件测试通过，将执行if 语句后面的所有缩进的代码
    print('在门诊部期间请全程佩戴好口罩。')
else:#若测试结果为False,就执行以下代码
    print('很抱歉，您需要持有48小时内核酸阴性检测结果才能进入门诊部区域。')
    print('请移步医院大门外核酸检测点完成检测。')
# 在这样的简单if-else结构中，总是会执行两个操作中的一个。

# 5.3.3 if-elif-else 结构
# 当我们需要检查两种以上的情形时，需要使用if-elif-else结构。
# Python只需要执行if-elif-else结构中的一个代码块。
# Python会依次检查每个条件测试，直到遇到通过了的条件测试。
# 一旦遇到了通过了的条件测试，Python立刻执行它后面的代码，并忽略余下的测试。

# 假设进入医院的住院部需要你持有24小时内有效核酸报告
# 假设进入医院的门诊部需要你持有48小时内有效核酸报告
# 如果你设计了一个小程序
# 这个小程序会自动计算你上次核酸检测的时间
# 并更具最新的公共防疫政策，给你发送信息
# 告诉你是否可以去医院（的某些区域）

hours = 49 #这是距离你最近一次做核酸（且是阴性结果）后经过的小时数

if hours <= 24: # 若这条测试通过，则立刻执行下一条代码，并忽略掉剩余测试。
    print('您可以进入医院的住院部和门诊部。')
elif hours <= 48: # eilf 仅在前面的测试未通过时，才会运行.
    # 若elif测试通过，则立刻执行下一条代码，并忽略掉剩余测试。
    print('您只可以进入医院的门诊部。')
else: # else 仅在前面的测试未通过时，才会运行
    print('由于您没有48小时内核酸阴性结果报告，很抱歉您不能进入医院的任何区域。')

# 也可以换一种方式来设计这个小程序
hours = 49 #这是距离你最近一次做核酸（且是阴性结果）后经过的小时数

if hours <= 24: # 若这条测试通过，则立刻执行下一条代码，并忽略掉剩余测试。
    message = '您有24小时内核酸阴性报告，您可以进入医院的住院部和门诊部。'
elif hours <= 48: # eilf 仅在前面的测试未通过时，才会运行.
    # 若elif测试通过，则立刻执行下一条代码，并忽略掉剩余测试。
    message = '您有48小时内核酸阴性报告，您只可以进入医院的门诊部。'
else: # else 仅在前面的测试未通过时，才会运行
    message = '由于您没有48小时内核酸阴性结果报告，很抱歉您不能进入医院的任何区域。'

print(f'根据最新防疫政策，请遵守如下要求，谢谢配合：\n{message}')

# 5.3.4 使用多个elif代码块
# 假设进入医院的住院部需要你持有24小时内有效核酸报告
# 假设进入医院的门诊部需要你持有48小时内有效核酸报告
# 假设这个城市疫情加重了，城市要求市民至少每周（168小时）做一次核酸检测
# 如果你设计了一个小程序
# 这个小程序会自动计算你上次核酸检测的时间
# 并更具最新的公共防疫政策，给你发送信息
# 告诉你是否可以去医院（的某些区域）

hours = 72 #这是距离你最近一次做核酸（且是阴性结果）后经过的小时数

if hours <= 24: # 若这条测试通过，则立刻执行下一条代码，并忽略掉剩余测试。
    message = '您有24小时内核酸阴性报告，您可以进入医院的住院部和门诊部。'
elif hours <= 48: # eilf 仅在前面的测试未通过时，才会运行.
    # 若elif测试通过，则立刻执行下一条代码，并忽略掉剩余测试。
    message = '您有48小时内核酸阴性报告，您只可以进入医院的门诊部。'
elif hours <= 144: # else 仅在前面的测试未通过时，才会运行
    message = '由于您没有48小时内核酸阴性结果报告，很抱歉您不能进入医院的任何区域。'
    # 若elif测试通过，则立刻执行下一条代码，并忽略掉剩余测试。
else:  # else 仅在前面的测试未通过时，才会运行
    message = '尊敬的市民，根据本市防疫要求，市民每周至少要做一次核酸检测。\
请您配合防疫工作，立即做核酸检测, 否则您将无法使用健康码。珍爱健康，保住绿码！'
    
    
print(f'根据最新防疫政策，请遵守如下要求，谢谢配合：\n{message}')


binary_digits = ['0','1']

for digit in binary_digits:
    if digit == '1': 
        #这一步会用'1'这个数字去遍历匹配表格里的两个元素作为测试条件
        #如果匹配成功，那就返回真-True， 系统打印结果：这确实是一个二进制的基数
        #如果匹配不成功，则系统返回逻辑假的结果，不做任何执行
        message = '这确实是一个二进制的基数'
    else:
        message = 'You are fooling yourself!'
        
print(message)
#最后系统再一次告诉你，在二进制的世界里只有0和1的存在。        
print(f"This's a world only for digits:{binary_digits[0]} & {binary_digits[1]}.")

#5.3.5 省略else代码块
# Python并不强制要求if-else结构后面必须是有else代码块
# 有时候我们就只用elif语句也很清晰

hours = 169 #这是距离你最近一次做核酸（且是阴性结果）后经过的小时数

if hours <= 24: # 若这条测试通过，则立刻执行下一条代码，并忽略掉剩余测试。
    message = '您有24小时内核酸阴性报告，您可以进入医院的住院部和门诊部。'
elif hours <= 48: # eilf 仅在前面的测试未通过时，才会运行.
    # 若elif测试通过，则立刻执行下一条代码，并忽略掉剩余测试。
    message = '您有48小时内核酸阴性报告，您只可以进入医院的门诊部。'
elif hours <= 144: # else 仅在前面的测试未通过时，才会运行
    message = '由于您没有48小时内核酸阴性结果报告，很抱歉您不能进入医院的任何区域。'
    # 若elif测试通过，则立刻执行下一条代码，并忽略掉剩余测试。
elif hours >= 168:  # elif 仅在前面的测试未通过时，才会运行
    message = '尊敬的市民，根据本市防疫要求，市民每周至少要做一次核酸检测。\
请您配合防疫工作，立即做核酸检测, 否则您将无法使用健康码。珍爱健康，保住绿码！'
# 这样的连续elif的结构更加的严格。只有满足相应的测试，代码才会执行
# else是一条包罗万象的语句，只要不满足任何if 或 else 中的测试，其后的代码块就会执行。  
# 这位引入无效甚至恶意的数据留下隐患。    
print(f'根据最新防疫政策，请遵守如下要求，谢谢配合：\n{message}')





----------------------- 或许是时候休息一下了 ---------------------------




# 5.3.6 测试多个条件
# if-elif-else虽然功能强大，能高效测试一个特定条件，但只适用于满足只有一个条件的情况。
# 当有可能有多个条件为True且需要在每个条件为True时采取相应的措施。
 
standard_hotpot_condiments = ['碎米牙菜','油泼辣子','油酥花椒','泡椒火锅红油']
#这只是举个例子，表示火锅店的锅底可以增加这些额外的配料
#但这条代码并不需要存在，即使是删除了，也不影响下面的代码执行。 
print(f'标准火锅底料已包含食材：{standard_hotpot_condiments}。')
print('客户可根据口味偏好添加配料。\n')

# 假设火锅店的顾客想要在标准锅底里多加两种配料
requested_extra_hotpot_condiments_from_customer = ['油泼辣子','油酥花椒']

if '泡椒火锅红油' in requested_extra_hotpot_condiments_from_customer:
    print('客户要求在标准锅底里额外再加一份：泡椒火锅红油')
    #客户并没有要求这个配料，所以不会执行这条代码
    #这条测试没有通过，Python顺势执行后面的测试
if '油泼辣子' in requested_extra_hotpot_condiments_from_customer:
    print('客户要求在标准锅底里额外再加一份：油泼辣子')
if '油酥花椒' in requested_extra_hotpot_condiments_from_customer:
    print('客户要求在标准锅底里额外再加一份：油酥花椒')
if '碎米牙菜' in requested_extra_hotpot_condiments_from_customer:
    print('客户要求在标准锅底里额外再加一份：碎米牙菜')
    #客户并没有要求这个配料，所以不会执行这条代码
    #但不管前两个条件测试是否通过，Python都将进行这一条测试

print('\n根据以上信息完成火锅底料')

# 当想要执行多个代码块的时候，就要使用一系列独立的if语句；
# 如果只想执行一个代码块，就使用if-elif-else结构。

# 5.4 使用if语句处理列表

#5.4.1 检查特殊元素
# 假设客户每添加一种配料都打印一条消息，通过一系列信息把客户要求的额外配料都加进去。
# 使用一个循环来指出添加到标准锅底里的额外配料
# 假设客户要求的一项配料在火锅店里已售罄
# 假设火锅店里已经有2种配料售罄

requested_extra_hotpot_condiments_from_customer = ['油泼辣子','油酥花椒','胡辣子']

for requested_condiment in requested_extra_hotpot_condiments_from_customer:
    if requested_condiment == '油酥花椒':
        print ('抱歉，油酥花椒今日已售罄。请选择其他配料。')
    elif requested_condiment == '碎米牙菜': 
        #因为条件里没有这个测试，所以Python就忽略这个代码块里的代码
        print ('抱歉，碎米牙菜今日已售罄。请选择其他配料。')
    else:
        print(f'额外添加的调理是：{requested_condiment}')

print(f'在标准锅底里已添加以上调料。') #貌似类似这样的信息在外卖单上能看到

# 5.4.2 确定列表不是空的
# 在运行for 循环时有必要确认列表不是空的
# 假设你为一个火锅底料配送业务做了一个订单小程序
# 下面在配送锅底前，先检查顾客是否有添加额外配料的要求
# 如果顾客额外添加配料的列表为空，就在结账前向顾客确认是否确认只要标准配料的锅底
# 如果顾客额外添加配料的列表不为空，就想前面的例子那样执行锅底的制作；

requested_extra_hotpot_condiments_from_customer = [ ]
# 客户并没有要求额外配料，所以这个列表是空的

# requested_extra_hotpot_condiments_from_customer = ['油泼辣子','油酥花椒','胡辣子']

# 在这一步先做简单的检查，而不是直接执行for循环。 
# 在if 语句里将列表名用作条件语句表达时，Python将在列至少包含一个元素时返回True
# 如果列表为空，则返回False，并忽略紧随其后的执行代码
if requested_extra_hotpot_condiments_from_customer: # 这一步算是一个隐含条件
# 隐含条件是：如果该列表存在，并且列表里有元素，基于这一条件，运行下面的for循环
    for requested_condiment in requested_extra_hotpot_condiments_from_customer:
        print(f'额外添加的调理是：{requested_condiment}')
    print('\n在标准锅底里已添加以上调料。')
#若确实列表为空，上一个for循环里的代码块的print指令都不会执行  

#接下来就给客户发一个确认信息
else:
    print('您确定只需要标准配料组合的锅底吗？')

# 5.4.3 使用多个列表

# 当顾客提出及其怪异的配料需求时，我们可以使用列表和if语句礼貌地告知客户~歌屋恩
# 假设火锅店供应的配料是固定的，我们用元组来代替列表    
available_condiments = ('碎米牙菜','油泼辣子','油酥花椒','泡椒火锅红油',\
'牛油','滋粑海椒','郫县豆瓣','冰糖醪糟','葱姜蒜','八角','茴香','茅草' )
# print(available_condiments)

requested_condiments_from_customer = ['风油精','油泼辣子','牛油','棉花糖']

#在下面这一步里遍历顾客点的配料表
#在这个循环里，对顾客点的每种配料都在每一次的循环中赋值给临时遍历
for requested_condiment_from_customer in requested_condiments_from_customer:
    #在下一个条件测试里，对每个临时变量都做一次in条件测试
    if requested_condiment_from_customer in available_condiments:
    #若临时变量通过in条件测试，就执行下一条print语句，若没通过则进入到下一个条件测试。
        print(f'根据客户需求额外添加配料：{requested_condiment_from_customer}')
    #若上一个条件测试没通过，则进入到这个一个条件测试
    else:# else是一条包罗万象的语句，可以理解为最后的执行人
         #只要是没有通过if或elif中的条件测试，else中的代码都将执行。
        print(f'\n抱歉，本店无法提供您要求的:\
{requested_condiment_from_customer}。:( 请选择其他配料。\n')
 
print('\n在标准锅底里已添加以上调料。')   
print('若您喜欢本店的火锅底料，请留言订阅点赞转发，让更多的朋友知道。谢谢您！')   


 
    
lst = [1, 3, 6, 9]
for digit in lst:
      digit = digit + 1
      print(digit)

for i in range(1001):
    if i % 2 == 0 and i % 3 == 0:
        print(i)    
 
for i in range(0, 1001, 3):
    if i % 2 == 0:
        print(i)
    
 
 for i in range(0,100_000_001):
     i = i**2
     print(i)z
      
 









