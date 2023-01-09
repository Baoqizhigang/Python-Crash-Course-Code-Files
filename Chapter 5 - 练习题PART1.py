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
      
 









