#Python 编程，从入门到实践  
# 3.1 列表（list)
# 列表是由一系列特定顺序排列的元素组成的。
# 可以创建包含字母表的所有字母，数字0-9或所有家庭成员姓名的列表
# 可以将毫无关系的元素加入到同一个列表里
# 往往给列表指定一个表示复数的名称，如letters, digits, names
# 列表用[]来表示，并且用逗号来隔开其中的元素
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

#对比第二章学习的变量
# favorite_language = 'Python ' #首先建立一个变量，并把'python '赋值给变量
# print(favorite_language) #打印变量

#3.1.1 访问列表元素
#列表是有序集合，若要访问列表里的任意元素，需要将该元素的位置（索引）告诉python
#访问列表元素三步骤：1，指出列表名称；2，指出元素索引；3，将其放在[]
# 示例：从列表中提取第一款自行车： 
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0]) #只访问第一个元素（或索引为0的元素）

print(bicycles[0].title())# 叠加将访问的这个元素的第一个字母作大写化处理的方法
# upper(), lower(), type() 等方法都可以叠加进去

# 3.1.2 索引从0而不是从1开始
# 在Python中第一个列表的元素的索引为0，而不是1.（差1原则）
# 在大多数编程语言中都是如此，这与列表操作的底层实现相关。
bicycles = ['trek','cannondale','redline','specialized']
# 索引： trek - 0, cannondale - 1, redline - 2, specialized -3;(索引从0开始)
print(bicycles[1]) #只访问第二个元素（或索引为1的元素）
print(bicycles[3]) #只访问第四个元素（或索引为3的元素）
print(bicycles[-1]) # 访问列表倒数第一个元素
print(bicycles[-2]) # 访问列表倒数第二个元素

#3.1.3 使用列表中的各个值
bicycles = ['trek','cannondale','redline','specialized']
message = f"My first bicycle was a {bicycles[0].title()}." 
#  {bicycles[0].title() 是让python访问列表中索引为0的元素，并首字母大写
print(message)
# 打印结果： My first bicycle was a Trek.

# 练习题环节
# 3-1 将一些朋友的姓名存储在一个列表中，并将其命名为names。依次访问
# 该列表中的每个元素，从而将每个朋友的姓名都打印出来。
names = ['eric', 'tom','宝器之港','1/#random name#/1']
# 索引：eric - 0, tom - 1, 宝器之港 - 2,  1/#random name#/1 - 3 ... 这是正着数
# 索引：eric - （-4）, tom - （-3）, 宝器之港 - （-2）,  1/#random name#/1 -（-1） 这是反着数
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-2])

# 3-2 问候语：：继续使用练习3-1 中的列表，但不打印每个朋友的姓名，
# 而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
names = ['eric', 'tom','宝器之港','1/#random name#/1']
# 索引：eric - 0, tom - 1, 宝器之港 - 2,  1/#random name#/1 - 3 ... 这是正着数
message = f"Hi {names[0].title()}, how are you?" 
print(message)
message = f"Hi {names[1].title()}, how are you?" 
print(message)
message = f"Hi {names[2].title()}, how are you?" 
print(message)
message = f"Hi {names[3].title()}, how are you?" 
print(message)

# 3-3 自己的列表：想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含
# 多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，
# 如“I would like to own a motorcycle”。
favorite_vehicles = ['motorcycle', 'telsa rocket','model 3','yacht' ]
message = f"I would like to own a {favorite_vehicles[0].title()}." 
print(message)
message = f"I would like to own a {favorite_vehicles[1].title()}." 
print(message)
message = f"I would like to own a {favorite_vehicles[2].title()}." 
print(message)
message = f"I would like to own a {favorite_vehicles[3].title()}." 
print(message)


# 3.2 修改，添加和删除元素
# 大多数列表都将是动态的，这意味着列表创建后，将随着程序的运行增删元素。
# 创建一个游戏，要求玩家射杀飞机；为此，可在开始时将一些飞机存储在列表里
# 每当有飞机被射杀时，都将被射杀的飞机从列表中删除。
# 每次有新飞机出现在屏幕上时，都将新飞机添加到列表中。
# 在整个游戏运行期间，飞机列表的长度将不断变化。

#3.2.1 修改列表元素
# 修改列表元素的语法与访问列表元素的语法类似。
# 要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。
motorcycles = ['honda','yamaha','suzuki'] 
# 首先用[]定义一个摩托车列表，并将列表里的值都赋给变量motorcycles
# 也就是说这个变量motorcycles 是代表的一系列的值；（脚踏N只船，时间管理大师）
# 索引：honda - 0，yamaha - 1, suzuki - 2; 
print(motorcycles)

print(motorcycles[2])
motorcycles[2] = 'ducati' #将第一个元素(第0号索引对应的元素）修改为ducati
print(motorcycles) # 第一个元素的值变了，但列表其他元素的值没变：
# 可以修改任何列表元素的值，而不仅仅是第一个元素的值。

#3.2.2 在列表中添加元素
# 你可能希望你的游戏中出现新的敌人，或添加可视化数据或给网站添加新注册的用户。
# 这时我们就需要在列表中添加新的元素。
# 1. 在末尾添加元素，用方法append()
motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati') # 1. 在末尾添加元素，用方法append()
print(motorcycles)
# 还记得我们前面学习过的方法吗？
# 有：title(),upper(),lower(),len(),type(),strip(),rstrip(),lstrip()....

# 用方法append()可以实现动态创建列表的目的
motorcycles = [] #先创建一个空列表
motorcycles.append('honda') # 逐步在空列表中添加元素
motorcycles.append('yamaha') # 新添加的元素总是在上一个元素之后
motorcycles.append('suzuki')
print(motorcycles) #最终列表元素排列方式与前述示例中完全相同
print(motorcycles[0].title())# 只访问第一个元素，且第一个字幕大写
# 这种创建列表的方式很常见，因为我们经常要等程序运行后，
# 才知道用户要在程序中存储哪些数据。为控制用户，可首先创建一个空列表，
# 用于存储用户将要输入的值，然后将用户提供的每个新值附加到列表中。

# 2.在列表中插入元素
# 使用insert()方法可以在列表中的任何位置添加元素
# 这个方法的括号里的内容不能为空，需要指定新元素的索引和值
motorcycles = ['honda','yamaha','suzuki']
# 索引：honda - 0，yamaha - 1, suzuki - 2; 
motorcycles.insert(1,'ducati')
#上一句代码的括号中，数字1表示在索引1的位置，ducati表示添加的元素
#通过insert()方法在指定的位置添加元素后，该元素索引后序的元素往后顺移
print(motorcycles)
# 新的索引：honda - 0，ducati - 1, yamaha - 2, suzuki - 3; 

#3.2.2 在列表中删除元素
# 1. 使用del语句在列表中删除元素
# 当你游戏中的一个角色死亡时，这个角色就应该从存活着的角色列表中删除；
# 当用户在你创建的网站中注销账户时，这个用户就该从活跃用户列表中删除；
# 我们可以根据位置或值来删除列表中的元素
motorcycles = ['honda','yamaha','suzuki']
# 索引：honda - 0，yamaha - 1, suzuki - 2; 
print(motorcycles)
del motorcycles[1] # 删除索引为1对应的元素的值（第二个元素）
print(motorcycles) 
# 元素一旦被删除后，我们将无法再访问这个元素（除非再把它添加到列表中）
# 要不要试一下删除索引-1对应的元素呢

# 下面是一个错误的示范
del motorcycles[5] # 删除索引为5对应的元素的值（第六个元素）
# 但列表并没有那么多元素，所以会报错。 
print(motorcycles) #报错：list assignment index out of range

---------------------或许是时候休息一下了--------------------------------

#2.使用pop()方法删除元素
# 有时候，你要将元素从列表中删除，并接着使用它的值
# 你可能需要获取刚被射杀的外星人的x和y坐标，以便在相应的位置显示爆炸效果
# 在Web应用程序中，你可能要将用户从活跃成员列表中删除，
# 并将其加入到非活跃成员列表中. 
# 使用pop()方法删除元素能帮助我们达到以上的目标。 
# 方法pop()可删除列表末尾的元素，并让你能够接着使用它。
# 列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。
# 栈（stack): 存储货物或供旅客住宿的地方,可引申为仓库、中转站，
# 所以引入到计算机领域里，栈就是指数据暂时存储的地方
motorcycles = ['honda','yamaha','suzuki'] # 首先定义列表
print(motorcycles)

popped_motorcycle = motorcycles.pop()
# 从列表中弹出一个值（末尾的值），并将其存储到变量popped_motorcycle中
print(motorcycles) #打印列表， 核实其中有一个值已经被删除
print(popped_motorcycle) # 打印弹出的值，证明依然能够访问被删除的值
#列表末尾被删除的元素已经被赋予到popped_motorcycle这个变量中
#这个值并没有从系统中彻底被删除，而是换了一个存在的形式和地方

# 假设列表中的摩托车是按购买时间存储的，就可使用方法pop()打印一条消息，
# 指出最后购买的是哪款摩托车：
motorcycles = ['honda','yamaha','suzuki'] # 首先定义列表
print(motorcycles)
last_owned = motorcycles.pop()
print(last_owned)
print(f"The last motorcycle I owned was a {last_owned.title()}.")
print("The last motorcycle I owned was a " + last_owned.title() + ".")
print(motorcycles)
# 做一个很有趣的实验，就是先把上面7句代码执行一次，
# 然后再把上面五句代码再反复执行三次，试试看结果有什么不同

# 3. 利用pop()方法弹出列表中任何位置处的元素
# 也可以使用pop()这个命令来删除列表中的任意位置的元素，
# 只需要在()中指定要删除元素的索引即可
motorcycles = ['honda','yamaha','suzuki']
# 索引：honda - 0，yamaha - 1, suzuki - 2; 
first_owned = motorcycles.pop(1) #弹出索引1对应的元素(第二个元素)
#当使用pop()这个命令时，被弹出的元素就不在列表中了
# 但我们仍然可以通过其他方式访问到这个元素（这是跟del 删除不一样的地方）
print(f"The first motorcycle i owned was a {first_owned.title()}")
print(motorcycles)

# 4. 根据值删除元素 - remove()办法
# 当你不知道要从列表中删除的值所处的位置，但只知道要删除的元素的值
# 可使用方法remove()办法。 假设我们要从列表motorcycles中删除值'ducati'。
motorcycles = ['honda','ducati','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati') #将ducati这个值从列表中删除
print(motorcycles)
# remove()会首先删除在列表里寻找到的第一个值
# 方法remove()只删除列表中出现的第一个指定的值。如果要删除的值在列表中出现多次，
# 就需要使用循环来判断是否删除了所有这样的值。我们将在第7章学习如何这样做。

# 区分使用del语句在列表中删除元素和remove()办法删除列表元素
# 使用remove()从列表中删除元素时，也可接着使用它的值。这点跟pop()类似
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati' #将列表中'ducati'这个值赋给变量too_expensive
motorcycles.remove(too_expensive) 
#用too_expensvie这个变量来告诉Python应该删除‘ducati’这个值
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')
print('\nA ' + too_expensive.title() + ' is too expensive for me.')



# 练习题环节
# 3-4 嘉宾名单：请创建一个列表，其中包含至少3 个你想邀请的嘉宾；
# 使用这个列表打印消息，邀请这些人来与你共进晚餐。
list_of_guests = ['eric','tom','bob']
msg_1 = f'Hi {list_of_guests[0].title()}, u r invited to dinner tonight!'
print(msg_1)
msg_2 = f'Hi {list_of_guests[1].title()}, u r invited to dinner tonight!'
print(msg_2)
msg_3 = f'Hi {list_of_guests[2].title()}, u r invited to dinner tonight!'
print(msg_3)

# 3-5 修改嘉宾名单：有1位嘉宾无法赴约，需要另外邀请一位嘉宾。
# 以3-4 嘉宾名单为基础，在末尾添加一条print 语句，指出哪位嘉宾无法赴约。
# 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# 再次打印一系列消息，向名单中的每位嘉宾发出邀请。
list_of_guests = ['eric','tom','bob']
print(list_of_guests)
guest_cannot_come = list_of_guests[2]
msg_from_guest = f'Sorry, {guest_cannot_come.title()} cannot come. '
print(msg_from_guest)
list_of_guests.remove(guest_cannot_come) #也可以用pop()方法
#list_of_guests.remove(list_of_guests[2])
#list_of_guests.remove('bob')
#list_of_guests.pop(2)
#list_of_guests.pop()
#del(list_of_guests[2])
print(list_of_guests)

list_of_guests.append('jerry') #把jerry这个值粘贴在list_of_guests列表的末尾
print(list_of_guests)
msg_1 = f'Hi {list_of_guests[0].title()}, u r invited to dinner tonight!'
print(msg_1)
msg_2 = f'Hi {list_of_guests[1].title()}, u r invited to dinner tonight!'
print(msg_2)
msg_3 = f'Hi {list_of_guests[2].title()}, u r invited to dinner tonight!'
print(msg_3)

# 3-6 添加嘉宾：今晚实际可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
# 以完成练习3-4 或练习3-5 时编写的程序为基础，在程序末尾添加一条print 语句，
# 指出你找到了一个更大的餐桌。
# 使用insert()将一位新嘉宾添加到名单开头。
# 使用insert()将另一位新嘉宾添加到名单中间。
# 使用append()将最后一位新嘉宾添加到名单末尾。
# 打印一系列消息，向名单中的每位嘉宾发出邀请。
list_of_guests.insert(0,'lucy') # 使用insert()将一位新嘉宾添加到名单开头。
list_of_guests.insert(1,'mary') # 使用insert()将另一位新嘉宾添加到名单中间。
list_of_guests.append('jessica') # 使用append()将最后一位新嘉宾添加到名单末尾。
print(list_of_guests )
msg_1 = f'Hi {list_of_guests[0].title()}, u r invited to dinner tonight!'
print(msg_1)
msg_2 = f'Hi {list_of_guests[1].title()}, u r invited to dinner tonight!'
print(msg_2)
msg_3 = f'Hi {list_of_guests[2].title()}, u r invited to dinner tonight!'
print(msg_3)
msg_4 = f'Hi {list_of_guests[3].title()}, u r invited to dinner tonight!'
print(msg_4)
msg_5 = f'Hi {list_of_guests[4].title()}, u r invited to dinner tonight!'
print(msg_5)
msg_6 = f'Hi {list_of_guests[5].title()}, u r invited to dinner tonight!'
print(msg_6)


#　3-7 缩减名单：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
# 以完成练习3-6 时编写的程序为基础，在程序末尾添加一行代码，
# 打印一条你只能邀请两位嘉宾共进晚餐的消息。
# 使用pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。
# 每次从名单中弹出一位嘉宾时，都打印一条消息，
# 让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
# 使用del 将最后两位嘉宾从名单中删除，让名单变成空的。
# 打印该名单，核实程序结束时名单确实是空的。
print(list_of_guests)
popped_list_of_guest = list_of_guests.pop() #删除掉列表中最末尾的元素
print(list_of_guests)
print(popped_list_of_guest) #被删除的客人是 jessica
print(f'\nSorry {popped_list_of_guest.title()}, I can only invite two people over for dinner.')
print(f'{popped_list_of_guest.title()}, I will invite you next time.')

popped_list_of_guest = list_of_guests.pop()#被删除的客人是 jerry
print(f'\nSorry {popped_list_of_guest.title()}, I can only invite two people over for dinner.')
print(f'{popped_list_of_guest.title()}, I will invite you next time.')

popped_list_of_guest = list_of_guests.pop()#被删除的客人是 tom
print(f'\nSorry {popped_list_of_guest.title()}, I can only invite two people over for dinner.')
print(f'{popped_list_of_guest.title()}, I will invite you next time.')

popped_list_of_guest = list_of_guests.pop()#被删除的客人是 eric
print(f'\nSorry {popped_list_of_guest.title()}, I can only invite two people over for dinner.')
print(f'{popped_list_of_guest.title()}, I will invite you next time.')

print(list_of_guests)#列表中只剩下2位客人了
msg_1 = f'Hi {list_of_guests[0].title()}, u r invited to dinner tonight!'
print(msg_1)
msg_2 = f'Hi {list_of_guests[1].title()}, u r invited to dinner tonight!'
print(msg_2)

del list_of_guests[0] #删除列表中0号索引对应的值
del list_of_guests[0] #再一次删除列表中0号索引对应的值
print(list_of_guests) #此时是一个空的列表，因为所有的值都被删除了

---------------------或许是时候休息一下了--------------------------------

# 3.3 组织列表
# 当列表中的数据由别人输入时，我们往往不能控制列表中数据输入顺序时，
# 也就不能控制列表中元素的排列顺序。但又经常需要以特定的顺序来呈现信息。
# 有时候，你希望保留列表元素最初的排列顺序，而有时候又需要调整排列顺序。
# Python提供了很多组织列表的方式，可根据具体情况选用。

# 3.3.1 使用方法sort()对列表进行永久性排序
# 假设有一个汽车列表，并要让其中的汽车按字母顺序排列（列表中所有的值的开头都是小写）
cars = ['bmw', 'h-哈FO', 'w-午零红光', 'tesla'] #建立列表
cars.sort() # 把cars这个列表里的元素按字母（正向）顺序来重新排列
print(cars)
# 方法sort() 永久性地修改了列表元素的排列顺序，该列表再也无法恢复到原来的排列顺序 
# 还可以用sort()方法传递参数reverse=True的方式，按与字母顺序相反的顺序排列列表元素
cars = ['bmw', 'h-哈FO', 'w-午零红光', 'tesla']
cars.sort(reverse = True) #注意True这个单词的大小写。reverse = True： 反向为真；
# sort()方法默认情况下是正向排列为真；
# reverse = True: 降序， reverse = False:升序（默认）
print(cars)
# 方法sort(reverse = True)对列表元素的排列顺序的修改也是永久性的

#3.3.2 使用函数sorted()对列表进行临时排序
# sorted()：即保留列表元素原来的排列顺序，同时以特定的顺序呈现它们
cars = ['bmw', 'h-哈FO', 'w-午零红光', 'tesla']
print("Here is the original list:")
print(cars) #按原始顺序打印列表
print("\nHere is the sorted list:")
print(sorted(cars)) #这个临时性的修改方式只在这个一行打印命令中执行
print(sorted(cars, reverse = True)) #注意最里面的括号中，是用的逗号，不是句号
# cars.sorted() #这是个错误的示范
print(cars) #按字母顺序显示列表
print("\nHere is the original list again:")
print(cars) #再一次按原始顺序打印列表（列表中的原始排列顺序并未受到任何影响）
# cars_reversed = cars.sort(reverse = True)  #这是个错误的示范
# print(cars_reversed)  #这是个错误的示范
# print(cars) #这是个错误的示范

# 3.3.3 倒着打印列表 - 直接调用方法reverse()
# 特别注意，方法reverse()不是指按与字母顺序相反的顺序排列列表元素，
# 而只是反转列表元素的排列顺序：
cars = ['bmw', 'h-哈FO', 'w-午零红光', 'tesla']
print(cars)
cars.reverse() #只是反转列表元素的排列顺序
print(cars)
print(sorted(cars, reverse = True)) #按列表中字母降序排列
# 一定要区分‘用sort()方法传递参数reverse=True的方式’ 跟‘直接调用方法reverse()’ 
# 用sort()方法传递参数reverse=True的方式：cars.sort(reverse = True) 
# 用sorted()方法传递参数reverse=True的方式：print(sorted(cars, reverse = True)) 
# 直接调用方法reverse()： cars.reverse()

# 3.3.4 确定列表的长度： len()
cars = ['bmw', 'h-哈FO', 'w-午零红光', 'tesla']
len(cars)
print(len(cars)) #列表包含4个元素，所以长度为4
a = 'ok'
len(a)
print(len(a))

# 练习题环节：
#3-8 
# 想出至少5个你渴望去旅游的地方，将它们存储在一个列表中，且元素不是按字母顺序排列的。
# 按原始排列顺序打印该列表。
# 使用sorted()按字母顺序打印这个列表，同时不要修改它。
# 再次打印该列表，核实排列顺序未变。
# 使用sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它
# 使用reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
# 使用reverse()再次修改列表元素的排列顺序。打印列表，核实已恢复到原来的排列顺序。
# 使用sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
# 使用sort()修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表。

# 3-9 晚餐嘉宾：
# 在练习3-4到7宾客列表中，使用len()打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。

# 3-10
# 尝试使用各个函数：想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或
# 你喜欢的任何东西。编写一个程序，在其中创建一个包含这些元素的列表，
# 然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。


#解题环节


#3-8 
# 想出至少5个你渴望去旅游的地方，将它们存储在一个列表中，且元素不是按字母顺序排列的。
favoriate_places = ['moon','sun','venus','pluto','mars']
# 按原始排列顺序打印该列表。
print(favoriate_places)
# 使用sorted()按字母顺序打印这个列表，同时不要修改它。
print(sorted(favoriate_places))
# 再次打印该列表，核实排列顺序未变。
print(favoriate_places)
# 使用sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它
print(sorted(favoriate_places, reverse = True))
# 使用reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
favoriate_places.sort(reverse = True)
print(favoriate_places)
# 使用reverse()再次修改列表元素的排列顺序。打印列表，核实已恢复到原来的排列顺序。
favoriate_places.reverse() 
print(favoriate_places)
# 使用sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
favoriate_places.sort
print(favoriate_places)
# 使用sort()修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表。
favoriate_places.sort(reverse = True)
print(favoriate_places)

# 3-9 晚餐嘉宾：
# 在练习3-4到7宾客列表中，使用len()打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
list_of_guests = ['eric','tom','bob']
len(list_of_guests)
# number_of_list = len(list_of_guests)
# print(f'I have invited {number_of_list} people to dinner tonight.')
print(f'I have invited {len(list_of_guests)} people to dinner tonight.')

# 3-10
# 尝试使用各个函数：想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或
# 你喜欢的任何东西。编写一个程序，在其中创建一个包含这些元素的列表，
# 然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。

# 3.4 使用列表时避免索引错误
# 不能要求访问超过列表范围的索引/元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3]) # IndexError: list index out of range
# 索引错误意味着Python无法理解你指定的索引。 
# 每当需要访问最后一个列表元素时，都可使用索引-1
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])
# 但是当列表为空时，这种访问最后一个元素的方式会导致错误：
motorcycles = []
print(motorcycles[-1]) #IndexError: list index out of range
# 列表motorcycles不包含任何元素，因此Python返回一条索引错误消息：

---------------------呼啦，本章结束啦，恭喜各位小伙伴们！---------------------

                                    >O<
                                                              
motorcycles = ('honda', 'yamaha', 'suzuki')
print(motorcycles.index('yamaha'))











