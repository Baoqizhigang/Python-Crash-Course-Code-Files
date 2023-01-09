# 第二章 变量和简单数据类型

#2.1 运行hello_world.py时发生的情况
print("Hello Python world!")
# print 是一个函数，能起到输出的作用
# ‘Hello Python world!’ 是一个字符串，是输出的内容
# 开头带井号表示这是一条注释，编译器在运行程序时会忽略它
# 文件名末尾的.py表示这是一个python程序，
# 因此编辑器将使用python解释器来运行它。编写程序时，
# 编译器会以各种方式突出程序不同的部分。例如，它知道print()的名称，
# 因此将其显示为某种颜色。


#2.2 变量(Variable)
message = "Hello Python world!" # 注意这里一定要使用引号将信息框起来
#上一句里，将文本“Hello Python world!” 作为一个值赋给了变量：message
print(message) #打印message这个变量的值
#每个变量都指向一个值，这个值是与该变量相关的信息。
#添加变量导致python解释器需要做更多的工作。
#处理第一行代码时，它将变量message与文本“Hello Python world!”关联在一起
#处理第二行代码时，编辑器将与变量message关联的值打印到屏幕上。
#实际上，在程序中可随时修改变量的值，而python将始终记录变量的最新值；
#现在就让你看看，喜新厌旧python，是如何抛弃ex的 :p 
message = "Hello Python world!" #将变量message与“Hello Python world!”关联在一起
print(message) #打印message这个变量所关联的值
# 换一个牵手 :p 
message = "I love coding in python!" #将变量message与新的值关联在一起
print(message)#将赋予了新的值的（同一个）变量打印出来

#2.2.1 变量的命名和使用
# 变量的命名要遵守一些规则和指南，这些规则能帮助我们编写的代码更容易阅读和理解
# 违反这些规则和指南话则将引发错误，python会提示你并要求你重新回到正确的道路
# 规则如下：
# 变量名只能包含字母，数字和下划线。可以以字母或下划线打头，但不能以数字打头
# 例如：message_1, _1message 是可以的，但1_message 则不可以
# 变量名不能包含空格，但能使用下划线来分隔其中的单词
# 例如：AB_AB 是可以的， 但AB AB 则不可以
# 不要将python关键字和函数名用作变量名，即不要使用python保留用于特殊用途的单词
# 例如：print,for,split,try,if,else,def,while,continue,type,dir,open......
# 若是非要用到这些单词，可以采用这样的方法：_print, _for
# 变量名应即简介又具有可描述性，如name 比n好，student_name比s_n好
# 慎用小写字母i和大写字母O，因为很可能被看错成数字1和0；

# 目前我们最好都使用小写的python变量名，虽然用大写字母也不会导致错误，但大写字母
# 在变量名中有特殊意义，我们后面会讨论这部分内容。

# 2.2.2 使用变量时避免命名错误
# 这是优秀的程序员也会犯的错，但他们也知道如何高效地消除错误
# 名称错误一般有两种情况，1，使用变量前忘记给它赋值，2，输入的变量名拼写不准确
message = "I love coding in python!"     
#mesage = "I encourage you to click the LIKE buttom! :) "
print(mesage) #将变量的名字打错

#Traceback (most recent call last):

#  File "<ipython-input-118-0e897e3d4ac2>", line 2, in <module>
#   print(mesage) #将变量的名字打错

#NameError: name 'mesage' is not defined

#将程序无法运行成功时，解释器将提供一个Traceback（回溯）
# Traceback是一条记录，指出解释器尝试运行代码时，在什么地方陷入困境
# 在这里解释器发现了一个名称错误，并告诉你打印的变量mesage没有被定义，
# python无法识别没有被定义的变量名, 也不关心单词拼法，更不会对变量名做拼写校正
#　但ｐｙｔｈｏｎ要求变量名的拼写一致
#　即前面定义的变量名和后面打印输出的变量名拼写要一致

# 2.2.3 变量是标签
# 变量常被描述为可用于存储值的盒子。
# 但更好的定义是：变量是可以赋给值的标签，也可以说变量指向特别的值。

#  练习题环节
# 2-1+2 将一条消息赋给变量， 并打印；再将变量的值修改为一条新消息，再打印出来。
message_from_me = "If you like my show, please click the like buttom!"
print(message_from_me)

message_from_you = "I love your show, and I am clicking the like buttom now!"
print(message_from_you)

message_from_me = "Thank you for clicking the like buttom!"
print(message_from_me)


# 2.3 字符串（string）
# 字符串就是一系列字符，用引号括起来的都是字符串（双引号/单引号皆可）
msg_a = "This is a string."
msg_b ='This is alos a string.'
msg_c = '123 234, 3243 3234'
msg_d = " This is a mix of english & 中文"
msg_e = " WHEN you mix 中文和英文，it's STILL 字符串"
msg_f = " $%^%$# *&^&*v &*^&* is a string"
#print(msg_a)
print(type(msg_a)) # 关于type() 我们后面再来详细讲
print(type(msg_b)) # 这里主要是想演示用单/双引号括起来的都是字符串
print(type(msg_c)) # 即使是一串数字，被引号括起来后也变成了字符串
print(type(msg_d)) # 中文和英文混合的文本信息也是字符串
print(type(msg_e)) # 不管中英文比例多少，中文和英文混合的文本信息也是字符串
print(type(msg_f)) # 特殊符号被引号括起来后也是字符串

msg_h = I told my friend,"This is my favorite Python Youtube Channel!"'
msg_i = "I think 'Qiao' is the youtuber's first name."
print(type(msg_h))
print(msg_h)
# 注意双引号和单引号的运用，
print(type(msg_i))
print(msg_i)
# 注意双引号，单引号和撇号的运用，
# 当文本有阅读意义时，请既注重标点符号在英文里的规则，更要注重在python里的规则


#2.3.1 使用'方法'修改字符串大小写
name = 'eric matthes' # 把eric matthes作为一个值赋给标签（变量）name
print(name.title()) #在print()语句中，方法title()出现在变量的后面。
#  title() 这个方法是以首字母大写的方式显示每个单词，“方法”是python可对数据执行的操作
# 在name.title()中, name后面的句号点.是让python对变量name执行方法title（）指定的操作
# 因为“方法”需要额外的信息来完成其工作，所以每个方法后面都跟着一对括号
# 这种信息是括号内提供的，也是预设的，所以括号里面是空的，不需要我们再输入什么。

print(name.upper()) # upper()这个方法可以把单词/整个变量的值都以大写字母输出
print(name.lower()) # lower()这个方法可以把单词/整个变量的值都以小写字母输出
print(msg_a.upper()) # upper()这个方法可以把单词/整个变量的值都以大写字母输出
print(msg_e.lower()) # 即使是汉字和英文的混合，也不妨碍这个方法丝滑运行

# 小技巧：存储数据时，往往先全部都用lower（）转为小写，在后期需要这些信息时，
# 再将其转化为最合适的大小写方式。

message = 'hello THis is qiao trying TO tyR someThing thAt maKEs sense.'
print(message)
print(message.lower()) # lower() 函数是可以把字符串每个单词里都小写打印出来
print(message.title()) # title() 函数是可以把字符串每个单词里的首字母都大写打印出来
print(message.upper()) # upper() 函数是可以把字符串每个单词里都大写打印出来


#2.3.2 在字符串中使用变量 （合并拼接字符串）
first_name = 'eric'
last_name = 'matthes'
#full_name = 'first name' + 'last_name' 你可能会以为是这样的，其实不是
full_name = f"{first_name} {last_name}"
print(full_name.title())
# 要将字符串中插入变量的值，可在前引号前加上字母f,再将要插入的变量放在花括号内
# 这种字符串名字为f字符串 f字符串是format（设置格式）的简写，
# 这样python显示字符串时，将每个变量都替换为其值
# python通过把花括号里的变量替换为其值来设置字符串的格式


#通过拼接合并字符串来创建完整的消息。
message = f"Hello {full_name.title()}!" 
# title()方法让full_name里变量的值的首字母都大写 
# f字符串能将‘hello,’ 这个字符串和变量拼接在一起，并存储在一个新的变量中
print(message)
print('Hello, ' + full_name.title()) #这是另外一种拼接方式，注意加号的运用
print('I want to say: ' + message.lower()) #多多尝试吧，体会不同的用法
# 备注： f字符串是python3.6版本引入的，3.6之前的版本需要使用format()方法
# 希望你用的是3.6以后的版本，若你是用的3.6之前的版本，请移步谷歌查询相关用法

____这里是休息的分割线_____________________________________________________________________

# 补充内容  1  
# 打印变量名 VS 打印变量名的值
message = 'Hello world!' # 值 为 'Hello world!' , 变量 是 message
print(message)   # 打印变量名的值
print('message') # 打印变量名 
print("any_variable")
print('任意变量名/文本字符串')

# 补充内容 2 注意一定要区分双单引号到底是为python服务的，还是为你字符串的文法服务的
# 即这个标点辅导到底是给电脑读的，还是要给人读的。 
msg_h = 'I told my friend,"This is my favorite Python Youtube Channel!"'
msg_i = "I think 'Qiao' is the youtuber's first name."
print(type(msg_h))
print(msg_h)
# 注意双引号和单引号的运用，
print(type(msg_i))
print(msg_i)
# 注意双引号，单引号和撇号的运用，
# 当文本有阅读意义时，请既注重标点符号在英文里的规则，更要注重在python里的规则

# 补充内容  3
_print = '不要将python关键字和函数名用作变量名'
print(_print)

# 补充内容  4
# Ctrl + 1: 注释/反注释


#2.3.3 使用制表符或换行符来添加空白
# 在编程中，空白泛指任何非打印字符，如空格、制表符和换行符
# 在字符串中添加制表符，可使用字符组合\t
print('Python')
print('    Python')
print('\tPython') #前面加了一个缩进
# Tab/Shift + Tab: 代码缩进/反缩进
#要在字符串中添加换行符，可以使用字符组合 \n
print("I love Languages such as:\nPython\nJava\nC\nC++") # 换行
print("I love Languages such as:Python，Java，C，C++.") # 换行
print("I love Languages such as:\n\tPython\n\tJava\n\tC\n\tC++")  # 换行+缩进


#2.3.4 删除空白
#'python ' 和‘python ’ 看起来差不多，打印出来貌似也一样，但在python眼里不一样
x = 'python'
y = 'python '
print(x)
print(y) 
print(type(x))
print(len(x)) #len()函数是输出变量的字符串长度
print(len(y))

#确保字符串末尾没有多余的空白，可使用方法rstrip()
favorite_language = 'Python ' #首先建立一个变量，并把'python '赋值给变量
print(favorite_language) #打印变量
print(len(favorite_language)) #打印变量字符串长度
modified = favorite_language.rstrip() #对原始变量调用方法rstrip(), 删除末尾空格
# favorite_language被执行了这个方法后，其变量就变成了'Python'
# modified = 'Python'
print(modified) # 在上一步中原始变量的值已经修改（空格被删除了），并赋给新的变量
print(len(modified)) #打印新变量的长度

# 这样的删除是暂时的，favorite_language 这个变量里还是包含了一个空格

#要永久删除这个字符串中的空白，必须要将删除操作的结果关联到变量
favorite_language = 'Python '
favorite_language = favorite_language.rstrip() #将修改后的值重新赋给原始变量
# favorite_language被执行了这个方法后，其变量就变成了'Python'
print(favorite_language) #打印原始变量
print(len(favorite_language)) #打印原始变量字符串长度
# 碎碎念：利用你自己将你完全的改变，这可能就是程序界的杀人诛心吧
# 在编程中，经常需要修改变量的值，再将新值关联到原来的变量，
# 这就是变量的值可随程序的运行或用户输入数据而发生变化的原因所在。

# 使用方法lstrip() 和 strip() 可以剔除字符川开头的空白或同时剔除字符串两边的空白。
favorite_language = '   python    '
print(len(favorite_language))
print(favorite_language.rstrip()) #剔除字符串末尾的空白
print(len(favorite_language.rstrip()))
print(favorite_language.lstrip()) #剔除字符串开头的空白
print(len(favorite_language.lstrip()))
print(favorite_language.strip())  #剔除字符串两边的空白
print(len(favorite_language.strip()))

#2.3.5 使用字符串时避免语法错误
# 在单引号括起的字符串里，如果包含撇号，就会导致错误（python会把第一个单引号和撇号
# 视为一个字符串，而将余下的文本视为python代码
msg_a = "One of life's joys is to learn Python."
print(msg_a)
# mag_b = 'One of life's joys is to learn Python.'  
# 注意，编译器已经在通过不同颜色告诉里这里有问题了，应该引起我们的警惕
print(msg_b)
# 温馨提示：当看到python代码以普通句子对颜色显示，或普通句子以python代码的颜色显示
# 这可能意味着文件中存在引号不匹配现象

#练习题环节
# 2-3 个性化消息：将用户的姓名存到一个变量中，并向该用户显示一条消息。显示
# 的消息应非常简单，如“Hello Eric, would you like to learn some Python today?”。

# 2-4 调整名字的大小写：将一个人名存储到一个变量中，再以小写、大写和首字母
# 大写的方式显示这个人名。

# 2-5 名言：找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出
# 来。输出应类似于下面这样（包括引号）：
# Albert Einstein once said, “A person who never made a mistake never tried 
# anything new.”

# 2-6 名言2：重复练习2-5，但将名人的姓名存储在变量famous_person 中，再创建
# 要显示的消息，并将其存储在变量message 中，然后打印这条消息。
#
# 2-7 剔除人名中的空白：存储一个人名，并在其开头和末尾都包含一些空白字符。
# 务必至少使用字符组合"\t"和"\n"各一次。
# 打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip()、
# rstrip()和strip()对人名进行处理，并将结果打印出来。




# 解题环节
# 2-3 个性化消息：将用户的姓名存到一个变量中，并向该用户显示一条消息。显示
# 的消息应非常简单，如“Hello Eric, would you like to learn some Python today?”。
first_name = 'eric'
msg = f"Hello {first_name.title()}, would you like to lear some Python today?" 
print(msg)
print('Hello ' + first_name.title() + ' ' + first_name.title() + ', would you like to lear some Python today? ')
# 温馨提示：从一开始就要建立算法优化的概念

# 2-4 调整名字的大小写：将一个人名存储到一个变量中，再以小写、大写和首字母
# 大写的方式显示这个人名。
name_a = 'eRIc maTThes'
print(name_a.title()) #首字母大写，其余小写 - 神奇的命令
print(name_a.lower())
print(name_a.upper())
print(msg.upper())

# 2-5 名言：找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出
# 来。输出应类似于下面这样（包括引号）：
# Albert Einstein once said, “A person who never made a mistake never tried 
# anything new.”
mingyan = 'Albert Einstein once said, “A person who never made a mistake never tried anything new."'
print(mingyan)

# mingyan_2 = "He said, "Using double quotation marks is not gonna work!""
# print(mingyan_2)

# 2-6 名言2：重复练习2-5，但将名人的姓名存储在变量famous_person 中，再创建
# 要显示的消息，并将其存储在变量message 中，然后打印这条消息。
famous_person = 'eric matthes'
msg = f"Hi {famous_person.title()}, how are you today?"  #花括号是结界
print(msg)

# 2-7 剔除人名中的空白：存储一个人名，并在其开头和末尾都包含一些空白字符。
# 务必至少使用字符组合"\t"和"\n"各一次。
# 打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip()、
# rstrip()和strip()对人名进行处理，并将结果打印出来。
famous_person = '    eric matthes       '
msg = f"Hi {famous_person.title()}, how are you today?" 
print(msg)
modified_1 = famous_person.lstrip() #这是暂时修改的方法，原变量里仍然有空格
modified_2 = famous_person.rstrip()
modified_3 = famous_person.strip()

msg_1 = f"Hi {modified_1.title()}, how are you today?" 
print(msg_1)
msg_2 = f"Hi {modified_2.title()}, how are you today?" 
print(msg_2)
msg_3 = f"Hi {modified_3.title()}, how are you today?" 
print(msg_3)
msg_4 = f"Hi {modified_3.title()}, \thow are you today?" 
print(msg_4)
msg_5 = f"Hi {modified_3.title()}, \nhow are you today?" 
print(msg_5)
msg_6 = f"Hi {modified_3.title()}, \n\thow are you today?"  #注意打印结果细节
print(msg_6)
msg_7 = f"Hi {modified_3.title()}, \t\nhow are you today?"  #注意打印结果细节
print(msg_7)

# 2.4 数（Num): 记录得分，表示可视化数据，存储web应用信息等

#2.4.1 整数 integer
print(2+3)
print(2*3)
print(2**3) #2的3次方（python使用**表示乘方运算）
print(2**2) #2的平方（python使用**表示乘方运算）
print(2-3)

print(2+3*4) # python支持运算次序
print((2+3)*4) # 四则混合运算
print((7-(2+3))*4) # 圆括号套圆括号就是中括号
print(((7-(2+3))+1)*4) # 括号套括号 
print([7-(2+3)]*4) # [] 是列表，我们将在下一章遇到

# 2.4.2 浮点数 float
print(0.2+0.3)
print(0.2**3)
print(0.2**0.3)
print(0.1*0.1) #末尾的小数我们暂时忽略，这是任何程序语言都存在的现象。
#我们会在第二部分的项目中学习如何处理多余的小数位方式。

#2.4.3 整数和浮点数 
# 将任意两个数相除时，结果总是浮点数，即便两个数都是整数且能整除
# print(4/2)
print(type(4/2))
print(type(2.0))
# 在其他任何运算中，当一个整数和一个浮点数做计算时，结果也总是浮点数
print(1+2.0)
print(type(1+2.0))

#2.4.4 数中的下划线(会被python忽略）)
universe_age = 14_000_000_000 #大数目的时候可以用这个方法
print(universe_age) #打印结果：14000000000
# 在python眼里，1000,1_000, 10_00, 100_0, 都是同一个数字，不信你可以试试看
# 还是我来试吧，您歇着
print(1000 + 1)
print(10_00 + 1)
print(100_0 + 1)

#2.4.5 同时给多个变量赋值
x,y,z = 0,2,5 # 把数字0赋值给字母x，把数字2赋值给字母y,把数字5赋值给字母z
# 我管这种赋值方式叫做： 打批发
print(y)
print(x+y)
print(y/z)
print(y**z)
print(y**5)

# 2.4.5 常量 constant（quantity）
# 常量类似于变量，但其值在程序整个生命周期内保持不变
# python没有内置的常量类型
# 但python程序员会使用全大写来指出应将某个变量视为常量
MIN_SUBSCRIBERS = 1_000_000
# 碎碎念：请多多订阅，让我尽快达到一百万的粉丝量，谢谢各位老板


# 练习题环节
# 2-8 数字8：编写4 个表达式，它们分别使用加法、减法、乘法和除法运算，但结
# 果都是数字8。为使用print 语句来显示结果，务必将这些表达式用括号括起来，也就
# 是说，你应该编写4 行类似于下面的代码：print(5 + 3)
# 输出应为4行，其中每行都只包含数字8。
print(2+6)
print(14-6)
print(2*4)
print(16/2) #请不要纠结，浮点数8.0也是数字8

# 2-9 最喜欢的数字：将你最喜欢的数字存储在一个变量中，再使用这个变量创建一
# 条消息，指出你最喜欢的数字，然后将这条消息打印出来。
favorite_num = '168'
msg = f"I like number '{favorite_num}' the most!" #注意单双引号的运用
# 这里的单引号是给人看的，有或没有都不影响Python执行命令
print(msg)

# 2.5 注释

# 2.5.1 如何编写注释
# 如果现在我们还需要解释如何编写注释的话，那前面那么多真的白看了 >0<

# 2.5.2 该编写什么样的注释
# Follow your heart~! 

# 2.6 python之禅 - 清晰，高效，不做作
# 代码应当漂亮而优雅，编程是为了解决问题，编写高效漂亮简介的代码是美德
# 能用简单的代码解决问题就最好不要用复杂的代码
# 即便是复杂的代码，也要让它易于理解。（为代码编写有益理解的注释）
# 不要企图一来就编写完美的代码，而是首先完成能行之有效的代码
# 等有能力后再考虑算法优化的问题


























