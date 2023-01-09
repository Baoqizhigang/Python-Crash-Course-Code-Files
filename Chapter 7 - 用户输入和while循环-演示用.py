

# 7.1.3 求模运算符（%） - 将两个数相除并取得余数

number = input("Enetr a number, and I will tell you if it's even or odd：")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even. ")
else:
    print(f"\nThe number {number} is odd. ")

# 7.2 While 循环简介
# for 循环是针对集合中的每个元素都执行一个代码块
# while 循环不断地运行，直到指定的条件不再满足为止

#7.2.1 使用while循环来数数

current_number = 1 # 将1赋值给变量current_number
while current_number <=5: # 只要current_number小于等于5，就执行下方代码
    print(current_number)
    current_number += 1 # 每次循环，current_number都再加1
    #一旦current_numberd大于5，循环就停止


# 7.2.2 让用户选择何时退出
# 可以使用while循环让程序在用户愿意时不断运行
# 需要定义一个退出值，只要用户输入的不是这个值，程序就将接着运行：
prompt = "\nTell me something, and I will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program." # 退出值 = quit
#print(prompt)
# 以上两条代码表示：用户有2个选择，要么输入一条信息，要么输入退出值‘quit'
message = " " 
# 变量message用于记录用户输入的值。我们将变量初始值设置为空字符串
# 让Python首次执行代码的时候有供检查的东西。
# Python首次执行while语句时，需要将message的值与'quit'进行比较，但此时用户还没输入。
# 如果没有供可以比较的东西，Python将无法继续运行程序。
# 为解决这个问题，必须给变量message指定初始值，即使初始值是个空字符串，也符合要求。
# 空字符串能够让Python执行while循环所需要的比较，只要初始值不是quit，循环就会不断运行。
while message != 'quit':
    #首次遇到这个循环，message是个空字符串，因此Python进入循环
    message = input(prompt) #python显示提示消息，并等待用户输入信息
    print(message) #不管用户输入的什么信息，都打印出来
    # 接下来Python重新检查while语句中的条件，只要用户输入的不是quit,循环就继续运行。
    # 在新的循环中，python会再一次显示提示消息并等待用户输入。 


prompt = "\nTell me something, and I will repeat it back to you. "
prompt +="\nEnter 'quit' to end the program." 
message = " " 
while message != 'quit':
    message = input(prompt) 
    print(message) 



# 7.2.3 使用标志
# 在要求很多条件都满足才能继续运行的程序中，可定义一个变量用于判断整个成都是否处于活动状态。
# 这个变量称为标志（flag),充当程序的交通信号灯。可以让程序在标志为True时继续运行。
# 当任何事件导致标志的值为False时，程序停止运行。这样，在while语句中，就只需要检查一个条件：
# 那就是标志的当前值是否给True. 
# 然后将所有其他测试（是否发生了应将标志设为False的事件）都放在其他地方，让代码更整洁。

prompt = "\nTell me something, and I will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program." 

active = True # 将active设置为True,让程序处于活跃状态。 这样做简化了while语句，因为不需要做任何其他的比较 - 相关的逻辑由其程序其他部分来处理。
while active: # 只要变量active 为True，循环就持续运行。
    message = input(prompt)# 用户输入信息后使用if语句来检查变量的值。
    
    if message == 'quit': #如果用户输入的是quit,则active变为False.循环停止
        active = False
    else:
        print(message)# 如果用户输入的不是quit,则将输入的信息打印出来。 


prompt = "\nTell me something, and I will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program." 

active = True
while active: 
    message = input(prompt)
    
    if message == 'quit': 
        active = False
    else:
        print(message)









# 7.2.4 使用break退出循环
# 要立即退出while循环，不再运行循环中余下的代码，也不管条件测试如何，可使用break语句。
# break语句用于控制程序流程，可用控制哪些代码将执行，哪些代码不执行，
# 从而让程序按你的要求执行你要执行的代码。

#在用户输入'quit'后使用break语句来立即退出while循环
prompt = "\nPlease enter the name of a city you want to visit:"
prompt +="\n(Enter 'quit' when you are finished.)" 

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
        
        
        
        
        
        
        
        
        
        
        







        
        
        
# 7.2.5 在循环中使用continue
# 要返回循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue语句。
# 它不象break语句那样不再执行余下的代码并退出整体循环

# 从1数到10，但只打印其中奇数的循环
current_number = 0 #current_number设置为0，小于10，能直接进入到while循环里
while current_number < 10:
    current_number += 1 #每次循环给current_number+1（以步长为1的方式往上数数）
    if current_number % 2 == 0: #if语句检查求模运算结果，若能被整除，执行continue
        continue #当执行这个时，python返回到while循环开头（但此时变量已经完成+1了）
    
    print(current_number)


# 7.2.6 避免无限循环
x = 1
while x<= 5:
    print(x)
    x += 1 # 如果不小心遗漏了这个代码，这个循环将无限执行下去

#在循环的退出条件比较微妙时，尤其要注意避免进入无限循环。
#可以按ctrl + C，也可以关闭显示程序输出的终端窗口。

# 7.3 使用while循环处理列表和字典
# 若要记录大量的用户和信息，需要在while循环中使用列表和字典
# for循环是一种遍历列表的有效方式，但不应在for循环中修改列表，否则将导致Python难以跟踪元素
# 要在遍历列表的同时对其修改，可使用while循环。 
# 通过将while循环同列表和字典结合起来使用，可收集，存储并组织大量输入，供以后查看。

# 7.3.1 在列表之间移动元素
# 假设有一个列表包含新注册但还未验证的网站用户
# 我们需要在验证这些用户后把他们移动到另外一个已验证的用户列表中
# 可以使用while循环，在验证用户的同时将未验证的用户从列表里提取出来，再将其加入另外一个已验证列表中


# 首先创建一个待验证用户列表和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice','brian','candace'] 
confirmed_users = [ ] #用于存储已验证用户的空列表

# 验证用户的同时将其从未验证用户列表中提取出来，再将其加入另一个已验证用户列表中
while unconfirmed_users: #这里将不断循环，直到unconfirmed_users列表为空
    current_user = unconfirmed_users.pop()
    #每次循环都把unconfirmed_users列表末尾元素删除
    #每次unconfirmed_users列表里被删除的元素都被赋值给变量current_user
    
    print(f"Verifying user:{current_user.title()}")
    #这条消息打印出来是为了模拟这个用户验证的过程
    confirmed_users.append(current_user)
    #每次current_user被赋新值后都添加到confirmed_users列表里
    
#显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
 
 
    
#7.3.2 删除为特定值的所有列表元素
# 在第三章我们使用函数remove()来删除列表中的特定值，
# 这之所以可行，是以为要删除的值只在列表里出现一次（列表里可以包含重复的元素）
# 若要删除列表中所有为特定值的元素，可不断运行while循环，直到列表中不再包含这个特定值

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets: #每次循环都执行下一步，直到逻辑假出现
    pets.remove('cat') #每次循环都删除掉列表里的一个'cat‘元素，然后返回到循环的开头
    
print(pets)


pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets: 
    pets.remove('cat') 
    
print(pets)


# 7.3.3 使用用户输入来填充字典
# 可使用while 循环来提示用户输入任意多的信息
# 创建一个调查程序，其中的循环每次执行时都提示输入被调查者的名字和回答
# 我们将收集的数据存储在一个字典中，以便将回答同被调查者关联起来。

responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active: #在首次执行循环时为逻辑真，于是执行下一句代码
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name?")
    #提示用户输入名字
    response = input("Which city would you like to visit someday?")
    #提示用户输入相关信息
    
    #将回答存储在字典中
    responses[name] = response #name和response成为键值对，进入responses这个字典
    
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond?(yes/no)")
    #如果输入'yes'，程序再次进入while循环
    if repeat == 'no':
        polling_active = False #此时标志为逻辑假，循环停止

# 调查结果，显示结果
print("\n---Poll Results ---")
for name,response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")




polling_active = True

while polling_active: 
    
    name = input("\nWhat is your name?")
   
    response = input("Which city would you like to visit someday?")

    

    responses[name] = response 
    
   
    repeat = input("Would you like to let another person respond?(yes/no)")
    
    if repeat == 'no':
        polling_active = False #


print("\n---Poll Results ---")
for name,response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")








n_1 = 0
while n_1<3:
    for n_2 in range (3):
        print('n_1=',n_1,'n_2=',n_2)
    n_1 += 1














        

















