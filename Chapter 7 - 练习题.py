-------------------------------------

#练习 7-1 汽车租赁： 编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息
#指定消息： Let me see if I can find you a Tesla Model 3. 

prompt = "What kind of car would you liek to rent?"
prompt += "\nPlease type your order here: "

car = input(prompt)

print(f"Let me see if I can find you a {car}.")


# 练习7-2 餐馆订位。询问用户有多少人用餐，如果超过8位，就打印一条消息，
# 指出这里没有空位； 否则指出有空位

prompt = "How many guests are coming to the restaurant tonight? "
prompt += "\nPlease type here: "

reservation = input(prompt)
reservation_info = int(reservation)

if reservation_info <= 8:
    print('Your reservation is confirmed.Thank you!')
else:
    print('I am sorry, the tables are all booked.')

# 练习7-3 10的整数倍
# 让用户输入一个数字，并指出该数字是否是10的整数倍

prompt = "Tell me a number and I will tell you if its multiple of ten. "
prompt += "\nPlease type here: "

num = input(prompt)
num = float(num)

if num % 10 == 0:
    print('This number is multiple of ten.')
else:
    print('This number is not multiple of ten.')


# 联系7-4：火锅配料
# 编写一个循环，提示用户输入一系列火锅配料，并在用户输入'quit'时结束循环
# 每当用户输入一种配料后，就打印一条消息，指出我们会在比萨中添加这种配料
# 在最后的结尾，把客户要添加的调料汇总打印出来
# 假设客户要加的调料是：['油泼辣子','油酥花椒','老牛油']

hotpot_flavors = [ ]
prompt = "请添加你想要的火锅配料： "

active = True

while active:
    flavor = input(prompt)
    hotpot_flavor = flavor
    
    if flavor == 'quit':
        active = False
    else:
        print(f'我们会在你的锅底中添加：{flavor}.')
        hotpot_flavors.append(hotpot_flavor)
        
#print(f'这是你锅底中添加的调料：{hotpot_flavors}')

print(f'这是你锅底中添加的调料：')
print(' '.join(hotpot_flavors))

# 练习 7-5：电影票
# 有家庭电影院根据观众的年龄收取不同的票价：
# 三岁以下免费；3~16岁的观众收费10元；16岁以上观众收费20元；
# - 在while循环中使用条件测试来结束循环
# - 使用变量active来控制循环结束的时机
# - 使用break语句在用户输入"quit"时退出循环     

# - 在while循环中使用条件测试来结束循环
prompt = "购票结束后请输入：退出"
prompt += "\n请在此输入购票者年龄或退出："
message = " "

while message != '退出': 
    message = input(prompt)
    
    if message != '退出':
        age = int(message)
      
        if age <= 3:
            print('3岁及以下无需付费')
        if 3 < age <= 16:
            print('您的票价是10元，请扫码支付。')
        else:
            print('您的票价是20元，请扫码支付。')
        print("您还需要购票吗？")
    
print("购票结束，祝您观影愉快！")   
    
    
    
    
    
    
# - 使用变量active来控制循环结束的时机
prompt = "购票结束后请输入：退出"
prompt += "\n请在此输入购票者年龄或退出："

active = True
    
while active:
    age = input(prompt)
    
    if age == '退出':
        print("购票结束，祝您观影愉快！")
        active = False
    else:
        age = int(age)
        if age <= 3:
            print('3岁及以下无需付费')
        if 3 < age <= 16:
            print('您的票价是10元，请扫码支付。')
        else:
            print('您的票价是20元，请扫码支付。')
        print("您还需要购票吗？")
        
        
        
        
        
        
        
        
 、
# - 使用break语句在用户输入"quit"时退出循环  
prompt = "购票结束后请输入：退出"
prompt += "\n请在此输入购票者年龄或退出："
message = " "

while True: 
    message = input(prompt)
    if message != '退出':
        age = int(message)
      
    if age <= 3:
        print('3岁及以下无需付费')
    if 3 < age <= 16:
        print('您的票价是10元，请扫码支付。')
    else:
        print('您的票价是20元，请扫码支付。')
    print("您还需要购票吗？")
    
    if message == '退出':
        print("购票结束，祝您观影愉快！")
        break







# 练习7-6：奶茶店
# 奶茶店有几种固定的奶茶供应，每次客户来都询问客户需要买什么奶
# 每一次客户下单，都打印一条消息，确认客户的订单已经接受
# 客户下单结束时，输入NO，利用break来停止循环 
# 所有奶茶制作好后，将客户的订单集中在一个列表里打印输出


prompt = "We serve: Bubble Milk Tea, Fullcream Milk Tea,Sweet Milk Tea. "
prompt += "\nPleaee type 'NO' when you finish ordering."
prompt += "\nPleaee order your milktea here:"

milktea_orders = [ ]

while True: 
    milktea = input(prompt)
    if milktea == 'NO':
        break    
    
    if milktea != 'NO':
        print(f'\nYour order: {milktea} is confirmed. ')
        milktea = milktea + ' ' 
        milktea_orders.append(milktea)  
        
print("\n")       
print(f"This is your order:{''.join(milktea_orders)} ")
print("Enjoy your milktea, thank you!")

print(f"This is your order:{milktea_orders} ")


# 练习7-7：fullcreammilk卖完了
# 接练习的7-6而创建的列表，但奶茶店‘fullcrea milk tea'卖光了
# 客户每次下单买fullcrea milk tea，都打印一条消息，指奶茶店fullcrea milk tea卖光了
# 每一次客户下单，都打印一条消息，确认客户的订单已经接受
# 客户下单结束时，输入NO，利用break来停止循环 
# 所有奶茶制作好后，将客户的订单集中在一个列表里打印输出
# 确认最终的列表milktea_orders未包含‘fullcreammilk'

prompt = "We serve: Bubble Milk Tea, Fullcream Milk Tea,Sweet Milk Tea. "
prompt += "\nPleaee type 'NO' when you finish ordering."
prompt += "\nPleaee order your milktea here:"

milktea_orders = [ ]

while True: 
    milktea = input(prompt)
    if milktea == 'NO':
        break    
    if milktea == "Fullcream Milk Tea":
        print(f'\nSorry we are out of {milktea}')
    
    else:
        print(f'\nYour order: {milktea} is confirmed. ')
        milktea = milktea + ' '
        milktea_orders.append(milktea)

print("\n")
for milktea in milktea_orders:
    print(f'I made you: {milktea}.')
print(f"\nThis is your order:{''.join(milktea_orders)} .")
print("Enjoy your milktea, thank you!")




# ---------------华丽的分割线------------------------------------

prompt = "We serve: Bubble Milk Tea, Fullcream Milk Tea,Sweet Milk Tea. "
prompt += "\nPleaee type 'NO' when you finish ordering."
prompt += "\nPleaee order your milktea here:"

milktea_orders = [ ]
milktea = ''

while True: 
    milktea = input(prompt)
    if milktea == 'NO':
        break    
    if milktea == "Fullcream Milk Tea":
        print(f'\nSorry we are out of {milktea}')
    
    if milktea != 'NO' and milktea != "Fullcream Milk Tea" :
        milktea = milktea + ' '
        milktea_orders.append(milktea)

print("\n")        
for milktea in milktea_orders:
    print(f'I made you {milktea}')      
print(f"This is your order:{''.join(milktea_orders)} ")
print("Enjoy your milktea, thank you!")



# 练习7-8：fullcreammilk卖完了
# 假设客户已经完成了下单，并都存在了列表：milktea_orders
# 客户的下单里出现了2次 Fullcream Milk Tea
# 这是后台反馈给客户：Fullcream Milk Tea 卖光了
# 模拟正在做奶茶的过程
# 打印客户最终被确认的订单，且最终的订单列表未包含‘fullcreammilk'
# 告诉客户奶茶已经做好了


milktea_orders = ['Bubble Milk Tea','Fullcream Milk Tea','Fullcream Milk Tea','Sweet Milk Tea' ]

finished_milkteaorders = []

print("I am sorry, we are out of Fullcream Milk Tea today.")
while 'Fullcream Milk Tea' in milktea_orders:
    milktea_orders.remove('Fullcream Milk Tea')

print("\n")
while milktea_orders:
    current_order = milktea_orders.pop()
    print(f"We are working on your {current_order}.")
    finished_milkteaorders.append(current_order)
    
print("\n")
print(f"This is your order:{finished_milkteaorders}")
print(" ... \n")
for milktea in finished_milkteaorders:
    print(f"\tWe made a {milktea} for you, enjoy!")





