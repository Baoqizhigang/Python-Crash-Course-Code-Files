# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:12:36 2022

@author: Administrator
"""
  
# 练习： 5-1 条件测试
# 编写一系列条件测试，将每个测试以及对其结果的预测和实际结果打印出来。
# 条件1 ：熊猫是国宝
# 条件2 ：棕熊是不是国宝
# 条件测试： 判断熊猫是否是国宝，判断棕熊是否不是国宝

bears = ['熊猫','棕熊','北极熊','大灰熊']
guobao = ['熊猫',]

for bear in bears:
    if bear in guobao:
        print(f'{bear}是国宝。')
# -----------option2----------------------------
bears = ['熊猫','棕熊','北极熊','大灰熊']
guobao = ['熊猫',]

for bear in bears:
    if bear in guobao:
        print(f'{bear}是国宝。')
    else:
        print(f'{bear}不是国宝。')

# 练习： 5-1 条件测试
# 编写一系列条件测试，将每个测试以及对其结果的预测和实际结果打印出来。
# 假设1 ： Charlie Puth 是一位Pop – Star
# 假设1 ： 图男崖少是一位人民艺术家
# 条件测试： 分别判断 Charlie Puth 和图男崖少是否都归属于Pop – Star
pop_star = ['charlie puth',]
rmartist = ['图男崖少',]

for i in pop_star:
    if i == 'charlie puth':
        print(f'{i.title()} is a pop star.' )
for i in pop_star:
    if i != '图男崖少':
        print(f'{i.title()} is not a rmartist.' )

for i in rmartist:
    if i == '图男崖少':
        print(f'{i.title()} is a rmartist.' )
for i in rmartist:
    if i != 'charlie puth':
        print(f'{i.title()} is not a pop star.' )


# 练习： 5-2 更多条件测试
# 使用关键字 and  和 or 的测试。
# 假设1 ： Charlie Puth 是一位Pop – Star
# 假设1 ： 图男崖少是一位人民艺术家
# 条件测试： 分别判断 Charlie Puth 和图男崖少是否都归属于Pop – Star

charlie_puth = 'pop star'
tulanyashao = 'rmartist'

if charlie_puth == 'pop star' and tulanyashao == 'pop star':
    print('They both are pop stars.')
else: 
    print('At least one of them is not pop star.')

if charlie_puth == 'pop star' or tulanyashao == 'pop star':
    print('At least one of them is  pop star.')
else: 
    print('None of them is pop star.')


# 练习： 5-2 更多条件测试
# 测试特定值是否包含在列表中。
# 假设1 ： 你喜欢的Pop – Star是 Charlie Puth 是一位Pop – Star
# 假设2 ： 这次被选入的年度Pop – Star行列的有：
#                 赛灵娜，火星哥，Charlie Puth ，霉霉，牛姐，碧姐
# 条件测试： 判断 Charlie Puth 是否被选入了年度Pop – Star行列
pop_stars = ['赛灵娜','火星哥','Charlie Puth','霉霉','牛姐','碧姐']
pop_star = 'charlie puth'
if pop_star.title() in pop_stars:
    print(f'{pop_star.title()}已入选本年度Pop – Star行列')


# 练习： 5-2 更多条件测试
# 测试特定值是未否包含在列表中。
# 假设1 ： 你喜欢的Pop – Star是 Charlie Puth, 他是一位Pop – Star
# 假设2 ： 这次被选入的翻车阿提斯特行列的有：
#                 天下无铅，一亿一爽，旺利鸿图，移风易俗，TimeManagementMaster
# 条件测试： 判断 Charlie Puth 是否落选翻车阿提斯特行列
fanche_atisite = ['天下无铅','一亿一爽','旺利鸿图','移风易俗','TimeManagementMaster']
pop_star = 'charlie puth'
if pop_star.title() not in fanche_atisite:
    print(f'{pop_star.title()}不属于翻车阿提斯特行列。') #何其有幸
    
# 练习： 5 - 3  用if语句针对不同的商品折扣作出反应 
# 想象你做了一个外挂，全年无休的监测你放进购物篮的商品降价涨价的信息。
# 条件1 ： 检查你喜欢的商品是否到三折，如果是就通知你下单。
# 条件2 ： 如果没有到三折（假设是五折，或八折），则不会给你发任何通知。

dicount = 0.2 #这里不能用30%

if dicount <= 0.3:
    message ='乡亲们，终于等到这个价格，赶紧起来割商家韭菜.'
else:
    message ='现在只能看，不能买.'
    
print (message)


#练习： 5 - 4  用if-else语句针对不同的商品折扣作出反应 
#想象你做了一个外挂，全年无休的监测你放进购物篮的商品降价涨价的信息
#条件1 ： 检查你喜欢的商品是否到三折，如果是就通知你下单。
#条件2 ： 如果没有到三折（假设是五折，或八折），则给你发让你耐心等待的通知。
#用两种方式来完成以上条件测试：1，简单if语句；2, if-else语句。
discounts = [0.3,0.5,0.8]

for discount in discounts:
    if discount == 0.3:
        message = f'乡亲们，现在的折扣是{discount*10}折，赶紧起来割商家韭菜.'
        print(message)
    if discount > 0.3:
        message = f'{discount*10}的折扣，性价比不高啊，要不再熬一熬，看哪个商家先低头。'
        print(message)
        
print('已对所有折扣情况完成测试')


discounts = [0.3,0.5,0.8]

for discount in discounts:
    if discount == 0.3:
        message = f'乡亲们，现在的折扣是{discount*10}折，赶紧起来割商家韭菜.'
        print(message)
    else :
        message = f'现在的折扣是{discount*10}折。折扣不到位，坚决不下单。'
        print(message)
        
print('已对所有折扣情况完成测试')


#  ----------------------option2----------------------------

import random
# random模块是python自带的模块，用于生成随机数，
# 需要注意的是random()是不能直接访问的，需要导入 random 模块，
# 然后通过 random 静态对象调用该方法。
# random() 函数返回随机生成的一个实数，它在[0,1]范围内
# random()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法
a = random.random() # 产生  0 到 1 之间的随机浮点数
print(a)

discount = random.random() # 产生  0 到 1 之间的随机浮点数
print('Discount is',discount,'.')
zhekou =round(discount * 10,2) # 只保留结果的两位数
print(zhekou)
print(f'现在的折扣是{zhekou}折')

if discount <= 0.3:
    message ='乡亲们，终于等到这个价格，赶紧起来割商家韭菜.'
else:
    message = f'{zhekou}的折扣，性价比不高啊，要不再熬一熬。'

print (message)

# 练习： 5 - 5  将上一题中if-else结构改为if – elif – else 结构。
# 想象你做了一个外挂，全年无休的监测你放进购物篮的商品降价涨价的信息
# 条件1 ：如果商品价格一旦三折，就通知你下单。
# 条件2 ：如果商品价格高于三折，就通知勤俭节约，不要舵手。
# 条件3 : 如果商品价格涨价到120%，就通知你放弃该店铺并建议你寻找其他类似产品。

discounts = [0.3,0.5,0.8,1.2,1.5]

for discount in discounts:
    if discount <= 0.3:
        message = f'乡亲们，现在的折扣是{discount*10}折，赶紧起来割商家韭菜.'
        print(message)
    elif discount >= 0.3 and discount < 1.2:
        message = f'乡亲们，现在的折扣是{discount*10}折，勤俭节约，忍住剁手。'
        print(message)
    else: #折扣应该不会是负数
        message = f'现在的价格是原价的{discount}倍。换一个店铺，这个商家想钱想疯了。'
        print(message)
        
print('已对所有折扣情况完成测试')


# 练习： 5 - 6  判断基金经理的投资收益表现
# 声明变量annual_growth, 再编写一个if-elif-else结构，根据annual_growth的值判断这个基金尽力处在哪个水平。 
# 条件1 ：若annual_growth 为100%，则评为韭菜投资家。
# 条件2 ：若annual_growth 在小于100%，则评为还不如韭菜投资家。
# 条件2 ：若annual_growth 在100%~110%之间，则评为还算是一个韭菜投资家。
# 条件3 :  若annual_growth 大于等于110%，则评为比韭菜厉害的投资家。
# 条件4 :  若annual_growth 大于等于120%，则评为接近巴菲特的韭菜投资家。
# 条件5 :  若annual_growth 大于等于130%，则评为超越巴菲特的韭菜投资家。
# 条件6:   若annual_growth 大于等于140%，则评为运气远超实力的韭菜投资家。

import random
# random模块是python自带的模块，用于生成随机数，
# 需要注意的是random()是不能直接访问的，需要导入 random 模块，
# 然后通过 random 静态对象调用该方法。
# random() 函数返回随机生成的一个实数，它在[0,1]范围内
# random.uniform(0,3) # 产生0到3之间的随机浮点数，区间可以不是整数

annual_growth = random.uniform(0,2) # 产生  0 到 2 之间的随机浮点数，区间可以不是整数
print(f'annual_growth={annual_growth}')
approx_growth = round(annual_growth,2)
# 将annual_growth通过round函数处理后赋值给approx_annual_growth
# 括号中的2代表保留两位小数（若改为3则代表保留三位小数）
print(f'approx_growth={approx_growth}')

if approx_growth < 1: #如果近似年华收益小于100%
    approx_growth = str(approx_growth*100)+'%' 
    # 上一步中将近似年化收益由浮点数形式调整为带百分符号的形式
    message =f'\n这个投资经理今年投资收益{approx_growth}，还不如韭菜投资家.'
    print(message)
elif approx_growth >= 1 and approx_growth < 1.1:
    approx_growth = str(approx_growth*100)+'%' 
      # 上一步中将近似年化收益由浮点数形式调整为带百分符号的形式
    message =f'\n这个投资经理今年投资收益{approx_growth}，算是一个韭菜投资家.'
    print(message)
elif approx_growth >= 1.1 and approx_growth < 1.2:
    approx_growth = str(approx_growth*100)+'%' 
      # 上一步中将近似年化收益由浮点数形式调整为带百分符号的形式
    message =f'\n这个投资经理今年投资收益{approx_growth}，是一个比韭菜厉害的投资家.'
    print(message)    
elif approx_growth >= 1.2 and approx_growth < 1.3:
    approx_growth = str(approx_growth*100)+'%' 
    # 上一步中将近似年化收益由浮点数形式调整为带百分符号的形式
    message =f'\n这个投资经理今年投资收益{approx_growth}，算是一个接近巴菲特的韭菜投资家'
    print(message)    
elif approx_growth >= 1.3 and approx_growth < 1.4:
    approx_growth = str(approx_growth*100)+'%' 
    # 上一步中将近似年化收益由浮点数形式调整为带百分符号的形式
    message =f'\n这个投资经理今年投资收益{approx_growth}，算是一个超越巴菲特的韭菜投资家。'
    print(message) 
else:
    approx_growth = str(approx_growth*100)+'%' 
    # 上一步中将近似年化收益由浮点数形式调整为带百分符号的形式
    message =f'\n这个投资经理今年投资收益{approx_growth}，TA是运气远超实力的韭菜投资家。'
    print(message) 
     
print('\n投资有风险，下笔如有神！')



---------------------或许是时候休息一下了--------------------------------



# 练习： 5 - 7  代码人群的共同焦虑
# 假设你为了保住你的头发，你知道有一组产品套装能帮助你保住发际线，保住发量。
# 这时你写了一个外挂，这个外挂每天都在网上帮你搜索任何能同时提供这个产品套装的店铺，
# 并推送给你。 如果找到这个店铺，就立刻给你发一条通知信息，
# 并告诉你可以这个店铺可以包邮，并享受店铺满100减30的折扣。

# 你的这组产品套装包含：头皮按摩器，生姜水，发膜，护发膏
# 店铺A的套装包含：头发按摩膏，生姜水，发膜，护发素
# 店铺B的套装包含：头皮按摩器，生姜水，发蜡，护发素
# 店铺C的套装包含：头皮按摩器，生姜水，发膏，护发乳
# 店铺D的套装包含：头皮按摩器，生姜水，发膜，护发膏

# 简单版 ------------------------------------------------------------
my_products = ['头皮按摩器','生姜水','发膜']

shop_a = ['头发按摩膏','生姜水','发膜','护发素']
shop_b = ['头皮按摩器','生姜水','发蜡','护发素']
shop_c = ['头皮按摩器','生姜水','发膏','护发乳']
shop_d = ['头皮按摩器','生姜水','发膜','护发素']

tmp_shop = shop_d 

if my_products [0] in tmp_shop[:] and my_products [1] in tmp_shop[:] \
    and my_products [2] in tmp_shop[:]  :
    print('这个店里有我想要的所有商品，单店购买的话\
店铺可以包邮，并享受店铺满100减30的折扣')

# 复杂版 --------------------------------------------------------------
my_products = ['头皮按摩器','生姜水','发膜']

shop_a = ['头发按摩膏','生姜水','发膜','护发素']
shop_b = ['头皮按摩器','生姜水','发蜡','护发素']
shop_c = ['头皮按摩器','生姜水','发膏','护发乳']
shop_d = ['头皮按摩器','生姜水','发膜','护发素']

tmp_shop = shop_b 

if my_products[0] in tmp_shop[:]:
    print(f'在商店确认有：{my_products[0]} ')
else:
    print(f'这个店没有：{my_products[0]}')
if my_products[1] in tmp_shop[:]:
    print(f'在商店确认有：{my_products[1]}')
else:
    print(f'这个店没有：{my_products[1]}')
if my_products[2] in tmp_shop[:]:
    print(f'在商店确认有：{my_products[2]}')
else:
    print(f'这个店没有：{my_products[2]}')

if my_products [0] in tmp_shop[:] and my_products [1] in tmp_shop[:] \
    and my_products [2] in tmp_shop[:]  :
    print('这个店里有我想要的所有商品，单店购买的话\
店铺可以包邮，并享受店铺满100减30的折扣')
else:
    print('这个店不能提供我想要的所有护发产品，如果不能在单店购买的话\
就不能享受店铺包邮和满100减30的折扣。我需要换一个商店再试试。')

# if my_products [:] in tmp_shop[:] :
#     print('这个店里有我所有想要的商品，单店购买的话\
# 店铺可以包邮，并享受店铺满100减30的折扣')
# else:
#     print('这个店不能提供我想要的所有护法产品，如果不能在单店购买的话\
# 就不能享受店铺包邮和满100减30的折扣。我需要换一个商店再试试。')


# 练习： 5 – 8 年度Pop – Star评选 
# 假设1 ： 这次被选入的年度Pop – Star行列的有：
#         赛灵娜，火星哥，Charlie Puth ，霉霉，牛姐，碧姐
# 假设2 ： 你为本年度的评选大会做了一个网站，
#         当明星们用自己的名字登陆这个网站查评选结果的时候，
#         若是入选的明星，则打印一条恭喜TA入选的消息，否则打印一条普通的问候语。 
# 条件测试：判断登陆的明星是否入选年度Pop – Star行列

pop_stars = ['赛灵娜','火星哥','Charlie Puth','霉霉','牛姐','碧姐']
user_name = '赛灵娜'
if user_name.title() in pop_stars:
    print(f'恭喜您，您已入选本年度Pop – Star行列！请带上身份证到会场领奖。')
else:
    print('Welcome! If you see this message,it means you are not\
in the Pop - Star List of this year! so~~~rry~~~!')


# 练习： 5 - 9  处理没有粉丝的情况
# 假设1 ： ‘翻车阿提斯特’的粉丝列表为空
# 假设2 ： 若为空，就打印一条价值观正确的信息。

# 条件测试：判断列表是否为空。

#fans_of_fanche_atisite = ['王大柱','丁美君','陈翠桦']

fans_of_fanche_atisite = []
if fans_of_fanche_atisite:
    for fan in fans_of_fanche_atisite:
        print(f'原来{fan}还坚守在爱豆这里。')
    print('粉丝名单里剩余人数为：',len(fans_of_fanche_atisite))
    print('以上就是现存的所有粉丝.')
else:
    print('粉丝名单里剩余人数为：',len(fans_of_fanche_atisite))
    print('已经没有粉丝了。看来他们都不是脑残粉，为他们正确的选择点赞。')



# 练习： 5 - 10  共同的粉丝 VS 单独的粉丝
# 假设1 ：赛灵娜的粉丝有：张大壮，李大辉，王大柱，张丽红，陈根苗，董有学，向庆有
# 假设2 ：Charlie Puth的粉丝有：李秀兰，张丽红，蒋雪莲，董有学，丁美君，吴艳红，陈翠桦
# 假设3：两位明星要邀请共同的粉丝来参加他们的私人爬梯。
# 条件测试：判断列表里那些是共同粉丝，并提取出来，分别给他们发邀请信息。
fans_of_selina = ['张大壮','李大辉','王大柱','张丽红','陈根苗','董有学','向庆有']
fans_of_charlie = ['李秀兰','张丽红','蒋雪莲','董有学','丁美君','吴艳红','陈翠桦']

fans = ['李秀兰','张丽红','蒋雪莲','董有学','丁美君','吴艳红','陈翠桦',\
        '张大壮','李大辉','王大柱','陈根苗','向庆有']
    
for fan in fans:
    if fan in fans_of_selina and fan in fans_of_charlie:
        print(f'Hi {fan}, 请今晚一定要来参加赛琳娜和查理为粉丝共同举办的私人爬梯.')


练习： 额外赠送1
条件 ： 传统生肖中有十二种动物，分别是：鼠，牛，虎，兔，龙，蛇，马，羊，猴，鸡，狗，猪。
测试 ：当别人说出TA的出生年份时（4个数字），立刻算出TA的生肖。
提示：传统生效有12种动物，每12年轮回一次。 可以把4位的年份数和12求余数，
例如： zodiac = year % 12， 得到的结果按表里的对应关系就可以找到生肖。
属相/序号对应关系：0/猴，1/鸡，2/狗，3/猪。 4/鼠，5/牛，
属相/序号对应关系：6/虎，7/兔，8/龙，9/蛇，10/马，11/羊，


练习： 额外赠送2
1. 输入一个不多于3位（可包含3位）的正整数，求出他们相乘的结果是几位数？
2. 把相乘结果各个数位上的数分离出来，按照从高到底的顺序显示出来。
例如：相乘的结果是158， 则最终显示为：8,5,1

练习： 额外赠送3
有一个正方形ABCD，在平面直角坐标系里，它的四个角的坐标分别是

A(-2，2)
B ( 2,  2）
C ( 2, -2）
D (-2, -2）

测试：输入X和Y点的坐标，判断该点是否落在正放心内（包含边界上）。
如果是，就输出“该点在图形内”，否则就输出“该点在图形外”。


练习： 额外赠送4 – 判断一个人身材是否合理
假设一个人的身高是XX米，一个人的体重是XX千克
身体BMI指数 = 体重 / （身高*身高）
若BMI小于18.5，则该人体重过轻
若BMI在18.5~24.9之间，则该人体重正常
若BMI在24.9~29.9之间，则该人体重过重
若BMI超出29.9，则该人属于肥胖体型




    
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
      
 









