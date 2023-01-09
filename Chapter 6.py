
#Python 编程，从入门到实践 P81-词典
#6.2.1
alien_0 = {'color':'green', 'points':'5'}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'you just earned {new_points} points!') #注意括号后紧跟字母f！！！

alien_0['x_position'] = 0  #加key & value到字典里去
alien_0['y_position'] = 25 #加key & value到字典里去
print(alien_0)

#6.2.2
Empty_Dict = {}
Empty_Dict['Apple'] = 25.3
Empty_Dict['Banana'] = 37.5
print(Empty_Dict)

#6.2.3
alien_0 = {'color':'green'}
alien_color = alien_0['color'] #将alien_0里的色彩元素单独做成一个检索表
print(f'The alien is {alien_color}.')

alien_0 = {'color':'Yellow'}
alien_color = alien_0['color']
print(f'The alien is {alien_color}.')

#6.2.4
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")
#向外移动外星人
#根据当前速度确定将外星人向右移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的移动速度肯定很快。
    x_increment = 3
    #新位置为旧位置加上移动速度
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")


#6.2.5 删除键值对
alien_0 = {'color':'green', 'points':'5'}
print(alien_0)

del alien_0['points']
print(alien_0)

#6.2.6 由类似对象组成的字典
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'eward':'c',
    'phil':'python'}

language = favorite_languages ['sarah']#.title()
#将sarah的key值赋予给language , 同时把language也做成一个词典
print(f"Sarah's favoriate language is {language}.")

#6.2.7 使用get（）来访问值
alien_0 = {'color':'green', 'speed':'slow'}
#使用get（）来指定获取词典里的值
#get（）的第一个参数用于key，是必不可少的
#get()的第二个参数为指定的key不存在时要返回的值，可不填
# 如果字典中没有对应的Key, 将返回指定的默认值
point_value = alien_0.get('points','No point value assigned.')
print(point_value)
# 如果字典中有对应的Key, 将获得与之相关联的value
point_speed = alien_0.get('speed','No point value assigned.')
print(point_speed)

#6.3 遍历字典
#6.3.1 遍历所有key&value

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'eward':'java',
    'phil':'ruby'}

for key, value in favorite_languages.items():
    #用for语句来遍历字典，可声明两个变量，用于存储键值对中的key&value
    #for语句第二部分包含字典名和方法item(),它返回一个键值对列表
    #接下来，for循环依次对每个键值对赋予指定的两个变量
    #在第一个函数调用print()中加入‘\n'是为了确保在输出每个键值对前都插入一个空行
    print(f"\nKey:{key}")
    print(f"Value:{value}")

for k, v in favorite_languages.items():
    print(f"\nName:{key}")
    print(f"language:{value}")
   
     
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'eward':'java',
    'phil':'ruby'}

#下面的代码将遍历字典中的每个键值对，并将key赋予变量name，将velue赋予变量language
#for语句第二部分（in之后)包含字典名和方法item(),它返回一个键值对列表
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#6.3.2遍历字典中的所有键
#.key()可以提取字典里所有的key，并依次赋予变量name
#遍历字典时会默认遍历所有的键
for name in favorite_languages.keys():
    print(name.title())


    
friends = ['phil','sarah'] #创建一个列表，其中包含要收到打印消息的朋友
for name in favorite_languages.keys(): # 把变量name和字典里的key一一对应赋值
    print(f"Hi {name.title()}.")#在循环中打印每个人的名字，下一句里检查当前的名字是否在列表friends中
    if name in friends: #如果在，就打印一句特殊的问候语，其中包含这朋友喜欢的语言
        #languuage = favorite_languages.value()
        language = favorite_languages[name].title() #为获悉朋友喜欢的语言，这里使用了字典名，并将变量name的当前值作为key
        #这样每个人的名字都会打印，但只对朋友打特殊的消息
        print(f"\t{name.title()}, i see you love {language}!")

#使用key()确定某个人是否接受调查，方法key()并非只用于遍历；
#实际上，key()返回一个列表，其中包含字典中的所有key。因此下面的代码只核实“erin"是否在列表中
#核实后发现它并不在列表中，所以打印出一条邀请的特殊信息；
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll")
        
apple_name = ['jade','sarah','Erin']
for name in favorite_languages.keys(): # #zichuang 
    print(f"Hi {name.title()}.")##zichuang 
    if name not in apple_name: #zichuang 
        print(f"\t{name.title()}, please take our poll") #zichuang       
        
# 6.3.3 按特定顺序遍历字典中所有键
# 对方法dictionary.keys()的结果调用函数sorted(),使输出在遍历前对列表进行排序       
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'eward':'java',
    'phil':'python'} 

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
#6.3.4 遍历字典中的所有值
#如果对字典包含的值感兴趣，可使用方法values（）来返回一个值列表，不包含任何键
#调用的函数是value()
#但这种没有考虑是否重复，重复项也会被打印出来

print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title()) #只打印出字典favorite_languages中的value

#为了剔除重复项，可调用函数集合set()
for language in set(favorite_languages.values()):
    print(language.title())
    
# 6.4 嵌套 
#将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套

# 6.4.1 字典列表
# 之前创建的外星人字典，一次只包含一个外星人的信息，如何管理更多外星人呢？
#一种办法是创建一个外星人列表，其中每个外星人都是一个字典，包含该外星人的各种信息

alien_0 = {'color':'green', 'points':'5'}
alien_1 = {'color':'yellow', 'points':'10'}
alien_2 = {'color':'red', 'points':'15'}
#首先创建三个字典，其中每个字典都表示一个外星人
#然后将这些字典都存储到一个名为aliens的列表里
#最后遍历这个列表，并将每个外星人都打印出来
aliens = [alien_0, alien_1, alien_2]      
for alien in aliens:
    print(alien)
        
# 当外星人数量庞大（且是由数码自动生成）时，可使用range（）工具 

aliens = []  # 首先 创建一个存储外星人的空列表
for alien_number in range(30): # 创建30个绿色的外星人- 
#上一步是告诉python要重复这个循环多少次
#下一步是告诉python，每次执行这个循环时，都要创建一个外星人，并将其附加到列表aliens末尾
    new_alien = {'color':'green', 'points':'5','speed':'slow'}
    aliens.append(new_alien)   
#显示前5个绿色的外星人
for alien in aliens[:5]:#使用一个切片来打印前5个外星人
    print(alien)
print("...")
#显示创建了多少个外星人
print(f"Total number of aliens: {len(aliens)}") #打印列表长度，证明确实创建了30个外星人
     
#在上面的例子中打印出来的外星人看起来是一样，但python还是会按照独立的个体来识别每一个外星人       
#必要时，可使用for循环和if语句来修改某些外星人的颜色     
aliens = []  # 首先 创建一个存储外星人的空列表
for alien_number in range(30): # 创建30个绿色的外星人- 
#上一步是告诉python要重复这个循环多少次
#下一步是告诉python，每次执行这个循环时，都要创建一个外星人，并将其附加到列表aliens末尾
    new_alien = {'color':'green', 'points':'5','speed':'slow'}
    aliens.append(new_alien)   
     
for alien in aliens[:3]: #创造一个切片， 把aliens里前三个元素选出来
    if alien['color'] == 'green': 
       #如果这三个元素的‘color'== green，则这三个元素将会发生以下改变
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
  

for alien in aliens[:2]: #创造一个切片， 把aliens里前两个元素选出来
    #针对在上一个循环中被修改成黄色的外星人，做如下的修改
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15    

#显示前5个外星人
for alien in aliens[:5]:#使用一个切片来打印前5个外星人
    print(alien)
print("...")

# 6.4.2 在字典中存储列表
#在下面的案例中，存储了列表的2个方面：外皮类型和配料列表
#配料列表是一个与键'toppings'相关联的值
#要访问该列表，我们使用字典名和键’toppings'，就像访问字典中的其他值一样
#这将返回一个配料列表，而不是单个值

pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }     #存储所点披萨的信息
#注意词典中第二个键值 - topping 对应的value 是一个列表
#下一步中打印出pizza这个词典中curst这个键值对应的value，同时铺垫topping的出场
print(f"You ordered a {pizza['crust']} - crust pizza with the following toppings:")
#编写一个for循环，为访问配料列表，使用键toppings，这样python就将从字典中提出配料列表
for topping in pizza ['toppings']:
    print("\t" + topping)        

# 小结：每当在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表
favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c','excel','chinese','other words'],
    'eward':['java'],
    'phil':['ruby',"sth hasn't been created"],
    }

#下面的代码将遍历字典中的每个键值对，并将key赋予变量name，将velue赋予变量language
#for语句第二部分（in之后)包含字典名和方法item(),它返回一个键值对列表
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are :")
    for language in languages:
        print(f"\t{language.title()}")

# 6.4.3 在字典中存储字典
#在下面的程序中，存储每个用户的三项信息：名，姓和居住地
#为访问这些信息，我们遍历所有的用户名，并访问与每个用户名相关的信息字典
# users字典里有两个键值： aeinstein & mcurie，这两个键直分别对应的value是独立的字典
users = {
    'aeinstein':{
    'first':"albert",
    'last':'einstein',
    'location':'princenton',
    },
    'mcurie':{
    'first':"marie",
    'last':'curie',
    'location':'paris',
    },
    
    }
# 用for循环遍历字典users，让python依次将每个键赋予给变量username,
# 并依次将与当前键相关联的字典赋予给变量user_info
# 在第一个循环，将用户名打印出来，并且开始访问改用户名内部的字典
# 变量user_info包含用户信息字典，该字典包含三个键：first,last,location
# 对于每个用户，都使用这些信息来打印用户的简要信息
for username, user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocation:{location.title()}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





