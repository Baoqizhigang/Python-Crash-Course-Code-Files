# 第四章-学习遍历整个列表(list)，高效处理任何长度的列表

# 4.1 遍历整个列表
# 用for循环 遍历列表：
magicians = ['alice','david','carolina'] #建立一个含有3个名字的列表
for magician in magicians: 
    #　magician在这里是一个临时变量，在循环中被不断赋予新的值
    #　让Python打印前面存储到变量magician中的每一个名字
    #　对列表中的每一个名字，都执行下一步print()操作
    print(magician)

# 4.1.1 深入研究循环
#　还是沿用上一个魔法师名单列表的代码
#　Python首先读取这一行代码：　for magician in magicians: 
#  这行代码让Python获取列表magicians中第一个值（'alice'），并将其存储到变量magician。
#  Python读取下一行代码：print(magician)
#  它让Python打印magician的值——就是是'alice'
#  考虑到列表还包含其他值，Python返回到循环的第一行：for magician in magicians:
#　Python获取列表中的下一个名字——'david'，并将其存储到变量magician中
#　然后Python读取下一行代码：print(magician)，　当前为'david'
#　接下来Ｐｙｔｈｏｎ再一次执行整个循环，对列表中的最后一个值做同样的处理。
#　通常情况下，当引入for循环语句后，Ｐｙｔｈｏｎ会重复执行指定的步骤，
#　直到对列表中所有元素都执行完同样的步骤之后，Ｐｙｔｈｏｎ才会停止
#　如果你的列表里有１００万个元素，Ｐｙｔｈｏｎ就会重复执行指定的步骤１００万次。

#　对于用于存储列表中每个值的临时变量，建议使用选择描述单个列表元素的有意义的名称
#　使用单数和复数式名称，可帮助你判断代码段处理的是单个列表元素还是整个列表
for magician in magicians: #临时变量在程序执行中要跟列表中所有元素都牵一次手
for cat in cats:
for dog in dogs:
for item in list_of_items:
   
# 插播一个关于‘缩进’的知识点
# 在Python中缩进是有明确意义的，表示同一级别的缩进一般是四个空格
# python使用缩进来表示一个语句是否属于一个逻辑上的‘块’/同一个层级
# 也就是说列表中所有元素都被遍历了之后Python解释器才会继续下一步工作。
# 缩进的引入使得代码更加清晰易读，我们也可以清晰理解程序的逻辑过程 
   
#4.1.2 在for循环中执行更多操作
magicians = ['alice','david','carolina']
for magician in magicians:
    #临时变量每牵手一个新的元素，下面两条print()命令就要执行一次
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}.\n ")
#两个print函数都缩进了，因此他们都将针对列表中每个魔术师执行一次。
#第二个函数调用了‘\n'换行符，从而整洁地对打印消息编组
#对于每一位魔术师都打印出一条消息，并且魔术师名字首字母大写
#以上两句为一组打印出来，注意末尾的'\n' '

# 插播：花括号{} 是一个占位符，表示这里将要传入print语句里一个具体（变量）的值

#4.1.3 在for循环结束后执行一些操作
magicians = ['alice','david','carolina']
for magician in magicians:
    # 在for循环可以包含任意数量的代码
    # 每个被缩进的代码行都是循环的一部分，且针对列表中的值都执行一次。
    # 可以对列表中的每个值执行任意次数的操作
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}.\n ")
    #当列表里第一个变量被访问且被打印出来后，程序将回到列表中，找接下来的第二个变量
    #来执行同样的命令，一直到列表中所有的变量/元素都被执行过同样的命令后，
    #这个模块才会停止。 然后Python跳出这个模块，进而执行下一条命令。
    #我们可以把每一次的循环用一个热门的词来表达：迭代

print('Thank you everyone, that was a great magic show!')
#没有缩进的代码则不属于for循环语句这个模块，因此只会执行一次（就如其他所有普通代码一样）

#4.2 避免缩进错误
#4.2.1 忘记缩进
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)
# IndentationError: expected an indented block

#4.2.1 忘记缩进额外的代码行
magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick,{magician.title()}.\n ")
# 第二个print语句本来应该是要缩进的，但却没有。
# Python发现for语句后面有一行代码是缩进，因此也没报告错误。
# 第二条print语句中临时变量的终值为'carolina'，因此只有她收到了这条消息
# 这是一个逻辑错误。从语法上看，这些Python代码是合法的，但由于存在逻辑错误
# 结果并不符合预期。如果你预期某项操作将针对每个列表元素都执行一次
# 但它却只执行了一次，请确定是否需要将一行或多行代码缩进。

# 4.2.3 不必要的缩进
# 在不需要缩进的地方缩进了，Python在运行时会报错
message = "Hello Python world!"
    print(message)
# IndentationError: unexpected indent

# 4.2.4 循环后不必要的缩进
# 这同样是关于逻辑错误的示例。 
magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}.\n ")
    
    print('Thank you everyone, that was a great magic show!')#这条代码不应该缩进
# 以上的代码都是符合python的语法规则的，但不符合你想表达意思的逻辑
# 所以虽然程序还是会运行，但执行的结果却是错误的。

# 4.2.5 遗漏冒号
magicians = ['alice', 'david', 'carolina']
for magician in magicians #这里应该有个冒号哦，这是很常见的错误
    print(magician)
# Spyder有内置命令帮助你自动打冒号

#练习题环节
#4-1 水果：将至少三个水果名称存储在一个列表中，使用for循环将每个名称都打印出来。
# 修改这个for 循环，使其打印包含水果名称的句子，而不仅仅是水果的名称
# 在程序末尾添加一行代码，它不在for 循环中，指出你有多喜欢水果。
fruits = ['apple','lemon','orange']
for fruit in fruits:
    print(f"I love drinking {fruit} juice after work out. ")

print('Drinking freash furit juice makes me happy! ')

#4-2
# 动物：将至少三个动物名称存储在一个列表中，使用for循环将每个名称都打印出来。
# 修改这个for 循环，针对每种动物打印一个句子
#　在程序末尾添加一行代码，指出这些动物的共同之处
pets = ['dog','cat','bird']
for pet in pets:
    print(f"我好想领养一只 {pet}. ")

print('家里有宠物的话会让我放松很多. ')


---------------------或许是时候休息一下了--------------------------------


#4.3 创建数值列表 - 列表非常适合用于存储数字集合
print(range(1,8))
#4.3.1 使用函数range() - 能产生一系列数
for value in range(1,8):
    #代码只会打印1-7，不会打印出数字8，注意两个数字是用逗号隔开哦
    # 类似于一个这样的列表：[1,2,3,4,5,6,7]   
    # 函数range()让Python从你指定的第一个值开始数，并在到达你指定的第二个值时停止
    # 差一行为
    print(value)
for value in range(8):# range(1,8) 和 range(8)是一个效果
    print(value)
   
# 4.3.2  使用函数range() 创建数字列表，
numbers = list(range(-10,8)) # 使用函数list()将range()的结果转化为列表
print(numbers)# 这次就打印出这样的列表了：[1,2,3,4,5,6,7]  

# 可以给函数第三个参数来指定步长，python将根据这个步长来生成数
even_numbers = list(range(2,11,2)) #第三个参数不可以是浮点数
print(even_numbers) # 按2的步长，只打印出[2, 4, 6, 8, 10]
# 函数range()从2开始数，然后不断加2，直到达到或超过终值（11）

squares = [] #创建一个名为square的空列表
for value in range(1,11): 
    #使用for语言让value这个临时变量把range()里的值都访问一遍
    #在循环中，计算当前值的平方，并将结果赋给变量square(如下)
    square = value**2 # value与square 在这一步牵手
    #将新计算得到的平方值附加到列表squares末尾（如下）
    squares.append(square) #当value访问到11时，循环结束，访问到11但不牵手11
    #print(squares) 
    
print(squares) #循环结束，打印列表squares:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#为了让代码更简介，可不使用临时变量square,而直接将每个计算得到的值都附加到列表末尾
squares = []
for value in range(1,11):
    #在循环中计算每一个值的平方，并立即将结果附到列表末尾（如下）
    squares.append(value**2)#append()的括号很强大，可以允许临时变量的赋值与计算
    
print(squares)

#4.3.3 对数字列表执行简单的统计计算
#找出数字列表中的最大值，最小值和总和
digits = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(min(digits)) #min() 找出最小值
print(max(digits)) #max() 找出最大值
print(sum(digits)) #sum() 数字列表里所有数字总和

alphabet = ['eae','bere','cere','f','r','w','m','q','dfez']
print(min(alphabet)) 
print(max(alphabet)) 


#4.3.4 列表解析
# 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
# 要使用这种语法，首先指定一个描述性的列表名，如squares
# 然后指定一个左方括号，并定义一个表达式，用于生成要存储到列表中的值。
# 在这个例子中，表达式为 value**2 , 它计算平方值
# 编写一个for循环，用于给表达式提供值（注意这里的for语句末尾没有冒号）
# 最后加上一个右方括号。
# for 循环为for value in range(1,11), 它将值1~10提供给表达式value**2
squares = [value**2 for value in range(1,11)] 
print(squares)
# 打印结果：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 

# 练习4-3 使用一个for循环打印数字1-20（含）
list = [digits for digits in range(1,21)]
print(list)
#以下是不使用for 循环语句的方式
numbers = list(range(1,21)) # 使用函数list()将range()的结果转化为列表
print(numbers)

# 练习4-4 创建一个包含数1-1,000,000的列表，再使用for循环将这些数打印出来
# 如果打印时间太长，可以按ctrl+c 停止输出或关闭输出窗口
list = [num for num in range(1,1000001)]
print(list) 

# 练习4-5：创建一个包含数字1-1,000,000的列表，
# 使用min ()和max() 核实该列表是从1开始，在1000000结束
# 对这个列表调用函数sum(),看看python将一百万个数加总需要多长时间
list = [num for num in range(1,1000001)]
list_start = min(list)
list_end = max(list)
Sum_of_list = sum(list)
print(f"List starts at the number: {list_start}! ")
print(f"List ends at the number: {list_end}! ")
print(f"This is the sum number of the entire list: {Sum_of_list}! Holy Cow, that's a big number! ")
# Bonus 500000500000! 
print("I wish the sum number of the list coule be my bank account number, and I wish the same for you. <3")


# 练习4-6：通过函数range()指定第三个参数来创建一个列表，其中包含1-20的基数
# 使用for循环将这些基数打印出来
odd_numbers = list(range(1,21,2))#代码只会打印1-20，不会打印出数字21
# 按2的步长，只打印出[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(odd_numbers) 
# 这一个是没有使用for语句的；

# 这是用for语句的方法
# 为了让代码更简介，直接将每个计算得到的值都附加到列表末尾
odd_number = [] #创建一个名为odd_number的空列表
for value in range(1,21,2):
    #使用for函数让value遍历range()里的值(如上)
    #在循环中，以1为起点，按2为步长记录当前值，并将结果赋给变量value()
    #将循环中记录到的每一个value值的结果附到列表的末尾（如下）
    odd_number.append(value)
    
print(odd_number)


#也可以用列表解析的方法来解这道题
odd_number = [value for value in range(1,21,2)] 
print(odd_number)
# 打印结果：[1, 3, 5, 7, 9, 11, 13, 15, 17, 19] 
# 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
# 要使用这种语法，首先指定一个描述性的列表名，如odd_number
# 然后指定一个左方括号，并定义一个表达式，用于生成要存储到列表中的值。
# 在这个例子中，表达式为 value , 它记录列表里的值
# 编写一个for循环，用于给表达式提供值（注意这里的for语句末尾没有冒号）
# 最后加上一个右方括号。
# for 循环为for value in range(1,21), 它将值1~20的基数提供给表达式value

# 这是用for语句的方法，但是有个错误
odd_numbers = [] #创建一个名为odd_numbers的空列表
for value in range(1,6,2): 
    odd_number = [value for value in range(1,6,2)] #[1, 3, 5]
    #将value按照1-20的区间里的奇数值，赋值给odd_number
    odd_numbers.append(odd_number)
    
print(odd_numbers) #打印了20遍，如果找到了错误，欢迎在评论区里留言哦


# 练习4-7， 创建一个列表，其中包含3-30里能被3整除的数
# 再使用一个for循环将这些列表中的数打印出来
list = [num for num in range(3,31,3)]
# 创建一个列表，在列表中使用range()函数让python遍历0-30的值(如上)
# 在遍历循环中，以0为起点，按3为步长记录当前值，并将结果赋给变量num(如上)
# 最后得到赋值的变量num都留在了列表里
print(list)


# 练习4-8， 创建一个列表，其中包含前10个整数（1~10）的立方
# 再使用一个for语句将这些立方数打印出来

cubic_numbers = [] #创建一个名为square的空列表
for value in range(1,11): 
    #使用for()语句让临时变量遍历1~10的值(如上)
    #在循环中，计算当前值的立方，并将结果赋给临时变量cubic_number(如下)
    cubic_number = value**3
    #将新计算得到的平方值附加到列表squares末尾（如下）
    cubic_numbers.append(cubic_number )
    
print(cubic_numbers)


# 练习4-9 使用列表解析生成一个列表，其中包含前10个整数（1~10）的立方
cubic_numbers = [value**3 for value in range(0,11)] #[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
print(cubic_numbers)
# 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
# 要使用这种语法，首先指定一个描述性的列表名，如cubic_numbers
# 然后指定一个左方括号，并定义一个表达式，用于生成要存储到列表中的值。
# 在这个例子中，表达式为 value**3（数值的立方）, 它将列表里的值都做立方计算
# 编写一个for循环，用于给表达式提供值（注意这里的for语句末尾没有冒号）
# 最后加上一个右方括号。
# for 循环为for value in range(0,11),
# 它将值1~10作为基础数据赋值给value,并进一步提供给表达式value**3

---------------------或许是时候休息一下了--------------------------------

#4.4 使用列表的一部分 - 切片功能

#4.4.1 切片：要创建切片，可指定要使用的第一个元素和最后一个元素的索引。
# 与函数range()一样，python在到达第二个索引之前的元素后停止。（访问却不牵手）
# 要输出列表中的前三个元素，需要指定索引0和3，这将返回索引为0,1,2的元素

# 一个处理运动队成员列表的案例：
players = ['charles', 'martina','michael','eli']
print(players[0:3])
print(players[::2])
# 各变量对应索引：charles - 0, martina - 1, michael - 2, eli - 3
#切片功能中[0:3] 和[:3]输出的同样的结果，都是输出列表中前3个元素
print(players[:2]) #取列表中索引0和索引1的元素
print(players[1:3]) #取列表中索引1和索引2的元素
print(players[1:4]) #取列表中索引1，索引2和索引3的元素
print(players[1:]) #取列表中索引1，索引2和索引3的元素
# [1:4]切片中的4是指不包含索引4
#切片功能中[1:4] 和[:4]输出的同样的结果，都是输出列表中第二个到第四个的变量值
print(players[:]) #取整个列表中的所有变量，切片切了个寂寞
print(players[0:4:2]) #从列表中第一个值开始，每隔2个元素提取一个元素值


players = ['charles', 'martina','michael','florence','eli']
# 索引：charles - 0, martina - 1, michael - 2, florence - 3，eli - 4
print(players[-3:]) #切片从列表最后一个变量开始，分别取索引4,3,2的值
print(players[-3:5]) #切片功能中[-3:] 和[-3:5]输出的同样的结果
print(players[-3:-1]) # 这里的切片是没有包含最后一个元素的值的
print(players[-3:0]) 
print(sorted(players[-5:-2],reverse = True)) # 打印出来一个空列表
print(players[-1:]) #取列表中最后一个索引的值
print(players[-5:]) #取列表中所有的值。切片切了个寂寞
print(players[:5]) #取列表中所有的值。切片切了个寂寞
print(players[:]) #取列表中所有的值，切片切了个寂寞
print(players[0:5:2]) #从列表中第一个值开始，每隔2个三元素提取一个只
# 都是一些很琐碎的知识点，需要死记硬背

#4.4.2 遍历切片
# 在for循环语句中使用切片来遍历列表的部分元素
players = ['charles', 'martina','michael','florence','eli']
# 列表各变量对应索引：charles - 0, martina - 1, michael - 2, florence - 3, eli - 4
print("Here are the first three players on my team:")
for player in players[:3]:# 遍历列表中索引0-索引3的值（但不包含3）
    print(player.title())#遵行上一条准则输出变量，且变量首字母大写

# 在考试中，你可以统计所有考生的分数，并按降序排列该列表
# 再创建一个只包含前三个得分的切片；


#4.4.3 复制列表
#-首先采用同时省略“起索引”和“终止索引”的方式，来创建一个包含整个列表的切片；
#-同时省略“起索引”和“终止索引”的方式的表达式为： ([:])
#-这种方式就等于创建了一个始于第一个元素，终止于最后一个元素的切片，即整个列表的副本；
#-副本：在电子文档编辑中对文档内容的复制，作为对原文本内容的备份。实质为电子文档的复制品

#-假设有一个列表Ａ包含你喜欢的四种食物，而你想再创建一个列表Ｂ，
#-这个列表Ｂ中包含你朋友喜欢的所有食品，不过你喜欢的食物你朋友也喜欢

my_foods = ['鱼香肉丝','宫保鸡丁','蒜香排骨']
#因为我朋友喜欢食物和我喜欢的食物是一样的
#因此就把我喜欢的食物的列表创建一个副本，来作为我朋友喜欢的食物的列表
friend_foods = my_foods[:] 
#在不指定任何索引下，在my foods列表中提取一个包含所有元素的切片，
#从而创建my foods列表的副本，
#将副本里的变量都赋值到friend_foods列表中去

print("我喜欢吃的菜有:")
print(my_foods)

print("\n我朋友喜欢吃的菜有:") #'\n'为换行符
print(friend_foods)

#在每个列表里都添加一种食品，以核实每个列表都记录了相应人员喜欢的食物
my_foods = ['鱼香肉丝','宫保鸡丁','蒜香排骨']
friend_foods = my_foods[:] 
#将my_foods的副本存储到friend_foods
#将my_foods的元素复制到到friend_foods，但这是一个独立的列表

my_foods.append('松茸烤鸭')#在my_foods列表末尾添加‘松茸烤鸭'
friend_foods.append('豆沙烧白')#在friend_foods列表末尾添加'豆沙烧白'

print("我喜欢吃的菜有:")
print(my_foods)

print("\n我朋友喜欢吃的菜有:") #'\n'为换行符
print(friend_foods)
#输出结果显示，两种食品都分别进入到两个列表，证明副本是一个独立的列表

#下面演示一种不适用切片的情况下赋值列表的情况：
my_foods = ['鱼香肉丝','宫保鸡丁','蒜香排骨']
#friend_foods = my_foods[:] #这是创建副本的方式，放在这里做对比记忆
friend_foods = my_foods # 直接将my_foods中的变量完全赋值给frirnd_food列表
#这种语法是将新变量friend_foods关联到已与my_foods相关联的列表
#因此两变量同时指向一个列表（可以理解为：存在一个列表，两个名字）
#我们将新变量'松茸烤鸭'添加到my_foods中时，它也将出现friend_foods里
#同理，新变量'豆沙烧白'添加到friend_foods中时，它也将出现my_foods里
#如下两条语法所示：
my_foods.append('松茸烤鸭')#在my_foods列表末尾添加‘松茸烤鸭'
friend_foods.append('豆沙烧白')#在friend_foods列表末尾添加'豆沙烧白'

print("我喜欢吃的菜有:")
print(my_foods)

print("\n我朋友喜欢吃的菜有:") #'\n'为换行符
print(friend_foods)

#练习题环节
# 4-10.0 打印消息"The first three items in the list are:"
# 4-10.1 使用切片打印列表的前三个元素
# 4-10.2 使用切片打印列表的中间三个元素
# 4-10.3 使用切片打印列表的末尾三个元素

# 4-11.0 创建一个my_fruits列表，包含：apple, lemon, grape, pear
# 4-11.1 创建my_fruits列表的副本，并将变量赋予friend_fruits
# 4-11.2 在my_fruits列表中添加一种水果
# 4-11.3 在friend_fruits列表中添加另一种水果
# 4-11.4 核实有两个不同的列表，为此打印"My fruits are:",再使用一个for循环
#打印第一个列表； 
# 4-11.4 打印"My friend's fruits are:",再使用一个for循环打印第二个列表； 
# 核实打印结果，确认新增的水果都进入到正确的列表里。 








#解题环节
# 4-10.0 打印消息"The first three items in the list are:"
message = ("The first three items in the list are:")
print(message)
# 4-10.1 使用切片打印列表的前三个元素
print(message[ :3]) #这里把每个字母作为一个元素来考虑
words = message.split('t') 
#以“空格”为分割符，将message这个字符串切割成由独立单词组成的列表
print(words[:]) #这里是把每个单词作为一个元素来考虑
# 4-10.2 使用切片打印列表的中间四个元素
print(len(message))
print(message[17:21]) #这里把每个字母作为一个元素来考虑
words = message.split(' ') 
#以“空格”为分割符，将message这个字符串切割成由独立单词组成的列表
print(words[2:6]) #这里是把每个单词作为一个元素来考虑
# 4-10.3 使用切片打印列表的末尾三个元素
print(message[-3:]) #这里把每个字母作为一个元素来考虑
print(message[35:]) #这里把每个字母作为一个元素来考虑
words = message.split(' ') 
#以“空格”为分割符，将message这个字符串切割成由独立单词组成的列表
print(words[-3:]) #这里是把每个单词作为一个元素来考虑
print(words[5:8])
print(words[5:20])  
print(words[5:]) 

# 4-11.0 创建一个my_fruits列表，包含：apple, lemon, grape, pear
my_fruits = ['apple','lemon','grape','pear']
# 4-11.1 创建my_fruits列表的副本，并将变量赋予friend_fruits
friend_fruits = my_fruits[:] 
# 4-11.2 在my_fruits列表中添加一种水果
my_fruits.append('orange')#在my_foods列表末尾添加‘orange'
# 4-11.3 在friend_fruits列表中添加另一种水果
friend_fruits.append('banana')#在my_foods列表末尾添加‘banana'
# 4-11.4 核实有两个不同的列表，为此打印"My fruits are:",再使用一个for循环
#打印第一个列表； 
print("My fruits are:")
for my_fruit in my_fruits[:]:
    print(my_fruit)   
# 4-11.4 打印"My friend's fruits are:",再使用一个for循环打印第二个列表；
print("\nMy friend's fruits are:")
for friend_fruit in friend_fruits[:]:
    print(friend_fruit)   
    
# 核实打印结果，确认新增的水果都进入到正确的列表里。 



---------------------或许是时候休息一下了--------------------------------



# 4.5 元组(tuple)
# 列表适合用于存储在程序期间运行可能变化的数据里；
# 列表可修改，这对处理网站用户列表或游戏中的角色列表至关重要
# 但有时候需要创建一系列不可修改的元素，元组可以满足这个需求
# python将不可修改的值称为不可变的（immutable)，而不可变的列表就被称为元组
# 所以，元组其实是列表的一种特殊形式，其自身包含的值不可被编辑，不可被修改
# 当需要存储的一组值在程序的整个生命周期内都不会改变，则可调用元组命令

# 4.5.1 列表用[]来表示，元组用()来表示。
# 定义元组后，可使用索引来访问其元素（但不可被修改），就像是访问列表元素一样
# 假设游戏中有一个大小不应该被改变的矩形，可将其长度和宽度储存在一个元组中
dimension = (200,50) #用()定义dimension这个元组，
# 元组中各元素索引： 200 - 0， 500 - 1；
# dimension = '200,500' # 这是把字符串作为值赋给变量dimesion
# dimension = [200,500] # 这是创建了一个叫dimesion的列表，里面包含元素200，500
print(dimension[0]) #打印元组中0号索引元素，就是第一个元素
print(dimension[1]) #打印元组中1号索引元素，就算第二个元素
dimension[0] = 250 #尝试修改元组中0号索引元素的值
print(dimension[0]) #打印元组中0号索引元素
#由于试图修改元组元素的操作是禁止的，在这一步编辑器会报错；
#碎碎念：元素在元组中成为不可变的值

dimension = 200,500
print(dimension)
#扩展备注：严格来说，元组是由逗号标示的，圆括号只是让元组看起来更整洁。

#如果你要定义只包含一个元素的元组，必须在变量后面加上逗号，（如下）:
the_tuple_only_has_one_varialbe = (3,)  # 这是创建一个只包含一个元素的元组，并赋值给变量
the_tuple_only_has_one_varialbe = (3) # 这是把3这个数字（digit)赋值给变量
print(the_tuple_only_has_one_varialbe )
#the_element = （3,） # 这是创建一个只包含一个元素的元组，并赋值给变量the_elenment
#the_element = 3, # 这是创建一个只包含一个元素的元组，并赋值给变量the_elenment
#the_element = 3 # 这是把3这个数字（digit)赋值给变量the_elenment
#the_elenment = '3' # 这是创建一个只包含3这个数字的字符串，并赋值给变量the_elenment
#创建只包含一个变量的元组通常没有意义，但自动生成的元组有可能只有一个变量
print(the_element)   

# 4.5.2 遍历元组中的所有值（ 用for循环语句）
dimensions = (200,50) #用（）定义dimension这个元组，
for dimension in dimensions: #没有括号
#for value in range(1,11): 注意这一条，做一个对比，你看出差异了吗
#for my_fruit in my_fruits[1:10]: 注意这一条，做一个对比，你看出差异了吗
    print(dimension)
    
    
# range()是数值列表，  [:]表示是访问列表全集


# 4.5.3 修改元组变量 （ 0><0 ) -- 是不是晕菜了，哈哈哈
# 虽然不能修改元组的元素，但可以给存储元组的变量赋新的值
# 因为如果要修改矩形的尺寸，可重新定义整个元素组： 
# 其实就是用创造一个新的元组，但用的是旧的变量名（老瓶装新酒）
# eg: 与其给茅台兑水，不如换低度数白酒 --  嘻嘻
dimensions = (200,50) #用（）定义dimension这个元组，
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,400) #用新的变量重新定义dimension这个元组
# 也就是说，给一个元组变量重新赋予新的值是符合python语法规定的
# 请不要纠结为什么这样是符合语法规定的，就像小伙伴们最开始学英文时会遇到固定搭配的问题
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    
# 碎碎念：感觉这个修改方式，挺鸡肋的。若你非要去修改元组值，可以用这个方式

# 恭喜大家，进入到我们最喜欢的做题环节，哦耶~
# 练习题环节
# 有一家自助餐厅提供五种简单的食品，请想出五种简单食品并存储在一个元组中
# 使用一个for循环将五种食品都打印出来
# 尝试以提取索引的方式修改其中一个食品，核实python是否会拒绝
# 给元组变量赋新的值，让餐厅替换两种新食品，来形成餐厅新的菜单，
# 用for循环将新的菜单打印出来

#BOUNUS: 补充内容（来自另外一本书）
t1 = ()
t2 = (1,) #逗号不能省略 否则会报错
t3 = (10,20,30,40)

print(type(t1),type(t2),type(t3))

print('t1的长度：',len(t1),'; ','t2的长度：',len(t2),'; ''t3的长度： ',len(t3),';')

print('t3中元素的最大值：',max(t3),';')
print('t3中元素的最小值：',min(t3),';')
print('t3中元素的总和：',sum(t3),';')

a_a = (3.14, 500, '宝器之港好棒棒', True, [1,2,3],[])

print('第一个元素是：',a_a[0],', 它的类型是：', type(a_a[0]))
print('第二个元素是：',a_a[1],', 它的类型是：', type(a_a[1]))
print('第三个元素是：',a_a[2],', 它的类型是：', type(a_a[2]))
print('第四个元素是：',a_a[3],', 它的类型是：', type(a_a[3]))
print('第五个元素是：',a_a[4],', 它的类型是：', type(a_a[4]))
print('第六个元素是：',a_a[5],', 它的类型是：', type(a_a[5]))

a_a = ['fans: 我要对宝器之港的所有节目都点赞订阅转发！ ']
b_b = ['不做完这个我就不睡觉！','我绝对是认真的！']
c_c = a_a + b_b
print(c_c)

a_a = ['fans: 我要对宝器之港的所有节目都点赞订阅转发！ ']
b_b = ['不做完这个我就不睡觉！','我绝对是认真的！']
a_a += b_b
print(a_a) 

a_a = ['fans: 我要对宝器之港的所有节目都点赞订阅转发！ ']
b_b = ['不做完这个我就不睡觉！','我绝对是认真的！']
a_a.append(b_b[0])
a_a.append(b_b[1])
print(a_a) 

a_a = ['fans: 我要对宝器之港的所有节目都点赞订阅转发！ ']
b_b = ['不做完这个我就不睡觉！','我绝对是认真的！']
a_a.append(b_b) # 这个是粘贴列表进来
print(a_a) 


# 解题环节
# 有一家自助餐厅提供五种简单的食品，请想出五种简单食品并存储在一个元组中
menu = ('sweet-beef','fried-apple','salty-pancake','rice-soup','tea')
# 使用一个for循环将五种食品都打印出来
print("The cafeteria provides you unlimited food such as: ")
for food in menu: #注意哦 menu元组后面没有括号
    print(food)
# 尝试以提取索引的方式修改其中一个食品，核实python是否会拒绝
menu[0] = ('diamond-cut-beef')
print("The cafeteria provides you unlimited food such as: ")
for food in menu:
    print(food) # TypeError: 'tuple' object does not support item assignment
# 给元组变量赋新的值，让餐厅替换两种新食品，来形成餐厅新的菜单，
menu = ('diamond-cut-beef','fried-diamond','salty-pancake','rice-soup','tea')
# 用for循环将新的菜单打印出来
print("The cafeteria provides you unlimited food such as: ")
for food in menu:
    print(food)

#4.6.2 缩进
# Tab/Shift + Tab: 代码缩进/反缩进
# Tab：空行前是代码缩进；在输入一个字母后，按Tab健会自动补全或者代码提示。
    
#4.6.3 行长 - 建议每行不超过80个字符
b=("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print(len(b))

motorcycles = ('honda', 'yamaha', 'suzuki')
print(motorcycles.index('yamaha'))

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles.index('yamaha'))


# 做一个小结：
'''
---------------------以下函数只适用于列表，不适用于元组：-------------------------

list.append(x)
在列表的末尾，添加一个元素x;

list.insert(index,x)
在列表的下标位置index处插入元素x；

list.pop()
当列表非空时，删除并返回列表的最后一个元素；

list.pop(index)
当列表非空时，删除并返回列表下标位置为index的那个元素；

list.remove(x)
删除列表中的x元素；

list.reverse()
把列表的各个元素按照倒序排列，例如 [a,1,c] 变成 [c,1,a]；

list.sort()
如果列表中的各个元素可以比较大小，把它们按照特定顺序排列；直接修改原列表

list.sorted()
如果列表中的各个元素可以比较大小，把它们按照特定顺序排列；同时不影响原列表里的排序

list_1.extend(list_2)
把列表2中的元素添加到列表1最后一个元素的后面；

---------------------以下函数即适用于列表，也适用于元组：-------------------------
list.index(x)
计算元素x在列表中的下标位置；
motorcycles = ('honda', 'yamaha', 'suzuki')
print(motorcycles.index('yamaha'))
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles.index('yamaha'))

list*number
把原来的列表重复number次，得到一个新的列表，number是一个正整数，原来的列表长度不变；
message = [' 请点赞，订阅，留言，转发，谢谢啦 。祝生活愉快，转码顺利!']
举例：print(message * 30)

list[index]
读取列表中位置等于index的元素，index是一个从0开始的整数，当index=-1时，表示读取列表
倒数第一个元素；当index=-2时，表示读取列表中倒数第二个元素，以此类推。

list[ start : end ]
列表的切片操作，从下标 start 到下标 end - 1 处取出这些相邻的元素

len(list)
计算列表的长度（即列表里元素的个数）

min(list)
在列表中元素可以比较大小的情况下，取出列表中值最小的哪个元素；

max(list)
在列表中元素可以比较大小的情况下，取出列表中值最大的哪个元素；

sum(list)
在列表中元素可以进行加法运算的情况下，求出列表中元素的总和；

'''


---------------------呼啦，本章结束啦，恭喜各位小伙伴们！--------------------------

                                    >O<

#补充小技巧，看到就是赚到

import keyword
keyword.kwlist

#小伙伴们，推荐你试试看哦



print('请点赞，订阅，留言，转发，谢谢啦 ：）祝生活愉快，转码顺利!\n' * 30)

message = ['请点赞，订阅，留言，转发，谢谢啦 。祝生活愉快，转码顺利!']
print(message * 30)

















