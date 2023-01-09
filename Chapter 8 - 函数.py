# 8.1 定义函数
def greet_user():
    """ 显示简单的问候语. """
    print( "Hello" )
    print( "Hello" )
    print( "Hello" )
    print( "Hello" )
    print( "Hello" )
    print( "Hello" )
    
greet_user()

# 8.1.1 向函数传递信息
def greet_user(username):
    """ 显示简单的问候语."""
    print(f"Hello,{username.title()}!")
    
greet_user('david')

#------------------
def favorite_book(bookname):
    """ 显示最喜欢的书籍 """
    print(f"My favorite book is {bookname.title()}!")
    
favorite_book('python crash course')


#8.2 传递实参
def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息. """
    print( f"\nI have a {animal_type}." )
    print( f"My {animal_type}'s name is {pet_name.title()}."  )

describe_pet('er-ha', 'zhaocai')

# 8.2.1多次调用函数
def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息. """
    print( f"\nI have a {animal_type}." )
    print( f"My {animal_type}'s name is {pet_name.title()}."  )

describe_pet( 'er-ha' , 'zhaocai' )
describe_pet( 'dog' , 'wangfu' )
describe_pet( 'cat' , 'miaoxingren' )

# 8.2.2 关键字实参
def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息. """
    print( f"\nI have a {animal_type}." )
    print( f"My {animal_type}'s name is {pet_name.title()}."  )

describe_pet( animal_type='er-ha' , pet_name='zhaocai' )
describe_pet( pet_name='wangfu' , animal_type='dog' )

#8.2.3 默认值
def describe_pet( pet_name,animal_type = 'dog' ):
    """ 显示宠物的信息. """
    print( f"\nI have a {animal_type}." )
    print( f"My {animal_type}'s name is {pet_name.title()}."  )

describe_pet( pet_name= 'zhaocai' )

describe_pet( 'zhaocai' )

describe_pet( animal_type='cat' , pet_name='zhaocai' )

#8.2.5 避免实参错误
def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息. """
    print( f"\nI have a {animal_type}." )
    print( f"My {animal_type}'s name is {pet_name.title()}."  )

describe_pet()

#8.3 返回值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name( 'charlie' , 'puth' )
print(musician)

#8.3.2 让实参变成可选的
def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name( 'charlie' , 'otto' , 'puth' )
print(musician)

#----------------------------------

def get_formatted_name( first_name, last_name, middle_name = '' ):
    """返回整洁的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    """返回整洁的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician_1 = get_formatted_name( 'charlie' , 'puth' , 'otto' )
print(musician_1)

musician_2 = get_formatted_name( 'charlie' , 'puth' )
print(musician_2)

#8.3.3 返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = { 'first':first_name, 'last':last_name }
    return person

musician = build_person( 'charlie', 'puth' )
print(musician)

#------------------------------------------------------
def build_person( first_name, last_name, age=None ):
    """返回一个字典，其中包含有关一个人的信息"""
    person = { 'first':first_name, 'last':last_name }
    if age:
        person ['age'] = age
    return person

musician = build_person( 'charlie', 'puth', age = 31 )
print(musician)

#8.3.4 结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# 这是一个无限循环
while True:
    print( "\nPlease tell me your name:" )
    f_name = input( "First name: " )
    l_name = input( "Last name: " )
    
    formatted_name = get_formatted_name (f_name,l_name)
    print(f"\nHello, {formatted_name}!")
    
 
#给这个无限循环增加一个退出条件：
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print( "\nPlease tell me your name:" )
    print( "\nPlease enter 'done' at any time to quit:" )
    f_name = input( "First name: " )
    if f_name == 'done':
        break

    l_name = input( "Last name: " )
    if l_name == 'done':
        break
    
    formatted_name = get_formatted_name (f_name,l_name)
    print(f"\nHello, {formatted_name}!")   
    
# 8.4 传递列表
def greet_users(names):
    """向列表中的每位用户发出简单的问候"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
        
usernames = ['charlie puth','selena gomez','eric matthes']
greet_users(usernames) 

# 8.4.1 在函数中修改列表
#首先创建一个列表，其中包含一些要打印的设计。
unprinted_designs = [ 'phone case', 'robot pendant', 'ribbon' ] 
completed_models = [ ]

# 模拟打印每个设计，直到没有未打印的设计为止。
# 打印每个设计后，都将其移到列表completed_models中。
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print( f"Printing model: {current_design}" )
    completed_models.append(current_design)
    
# 显示打印好的所有模型
print( "\nThe following models have been printed:" )
for completed_model in completed_models:
    print(completed_model)


# 为了重组以上代码，可以编写两个函数，每个都做一件具体的工作。
# 第一个函数负责处理打印设计的工作
# 第二个函数概述打印了哪些设计
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止；
    打印每个设计后，都将它移动到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print( f"Printing model: {current_design}" )
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型。"""
    print( f"\nThe following models have been printed:" )
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = [ 'phone case', 'robot pendant', 'ribbon' ] 
completed_models = [ ]

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 8.4.2 禁止函数修改列表
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止；
    打印每个设计后，都将它移动到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print( f"Printing model: {current_design}" )
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型。"""
    print( f"\nThe following models have been printed:" )
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = [ 'phone case', 'robot pendant', 'ribbon' ] 
completed_models = [ ]

print_models(unprinted_designs[:], completed_models)#创建列表的副本
show_completed_models(completed_models)


# 8.5 传递任意数量的实参
# 形参名*toppings中的星号是让Python创建一个名为toppings的空元组
# 并将收到的所有值都封装到这个元组中
def make_pizza( *toppings ): 
    """打印顾客点的所有配料"""
    print(toppings)
    
make_pizza( 'pepperoni' )
make_pizza( 'mushrooms', 'green peppers', 'extra cheese' )


def make_pizza( *toppings ):
    """概述要制作的比萨"""
    print( "\nMaking a pizza with the following toppings:" )
    for topping in toppings:
        print( f"-{topping}" )

make_pizza( 'pepperoni' )
make_pizza( 'mushrooms', 'green peppers', 'extra cheese' )


# 8.5.1 结合使用位置实参和任意数量实参
def make_pizza( size,*toppings ):
    """概述要制作的比萨"""
    print( f"\nMaking a {size}-inch pizza with the following toppings:" )
    for topping in toppings:
        print( f"-{topping}" )

make_pizza ( 16, 'pepperoni')
make_pizza( 12, 'mushrooms', 'green peppers', 'extra chesse' )

# 8.5.2 使用任意数量的关键字实参
# 有时候需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，
# 可将函数编写成能够接受任意数量的键值对 - 调用语句提供了多少就接受多少

# 形参名**user_info中两个的星号是让Python创建一个名为user_info的空字典
# 并将收到的所有名称键值对都放到这个字典中
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info[ 'first_name' ] = first
    user_info[ 'last_name' ] = last
    return user_info

user_profile = build_profile ( 'albert', 'einstein',\
                             location='princenton',\
                                 field = 'physics')
print(user_profile)


#8.6.2 导入特定的函数

#导入模块中的特定函数
from module_name import function_name 
#通过用都好分隔函数，可根据需要从模块中导入任意数量的函数
from module_name import function_0,function_1,function_2
















