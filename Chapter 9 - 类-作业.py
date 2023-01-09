   
















 
#练习 9-1 餐馆：9-1 餐馆：创建一个名为Restaurant 的类，其方法__init__()设置两个属性：
# restaurant_name 和cuisine_type。创建一个名为describe_restaurant()的方法和一个
# 名为open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
# 为编写的类创建三个实例，并对每个实例调用方法describe_restaurant()。  
 
class Restaurant():
    """这是一个描述餐馆的类"""
    
    def __init__ (self, restaurant_name, cusine_type):
        """初始化描述餐馆的属性"""
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        
    def describe_restaurant(self):
        """返回一条描述餐厅名字和其所提供食物风格的信息"""
        print(self.restaurant_name.title() + " restaurant serves " + \
              self.cusine_type.title() + ".")
        
    def open_restaurant(self):
        """输出餐厅正在营业的信息"""
        print(self.restaurant_name.title() + " restaurant is open.")
        
my_restaurant = Restaurant('good food','sichuan food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant('come again', 'guangdong food')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

his_restaurant = Restaurant('bring fortune', 'shanghai food')
his_restaurant.describe_restaurant()
his_restaurant.open_restaurant()

'''
9-4 就餐人数：在为完成练习9-1 而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant 的实例；打印有
多少人在这家餐馆就餐过，然后修改这个值并再次打印它。添加一个名为set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，
然后再次打印这个值。添加一个名为increment_number_served()的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
'''

class Restaurant():
    """这是一个描述餐馆的类"""
    
    def __init__ (self, name, cusine_type):
        """初始化描述餐馆的属性"""
        self.name = name.title()
        self.cusine_type = cusine_type
        self.number_served = 0 #添加一个名为number_served的属性，并将其默认值设置为0
        
    def describe_restaurant(self):
        """返回一条描述餐厅名字和其所提供食物风格的信息"""
        print(self.name + " restaurant serves " + \
              self.cusine_type.title() +".")
        
    def open_restaurant(self):
        """输出餐厅正在营业的信息"""
        print(self.name + " restaurant is open.")
        
    def set_number_served(self, number_served): #添加一个名为set_number_served()的方法
        """让用户能够设置就餐人数"""
        self.number_served = number_served
            
    def increment_number_served(self,additional_served): #添加一个名为increment_number_served()的方法
        """让用户能够增加就餐人数"""
        self.number_served += additional_served

restaurant = Restaurant('good food','sichuan food')
restaurant.describe_restaurant()

print(f"\n{restaurant.name} restaurant just opend and has served: {restaurant.number_served} guests.") #默认值是0

restaurant.number_served = 430 #手动调整属性值
print(f"Tonigt the {restaurant.name} restaurant has served: {restaurant.number_served} guests.")

restaurant.set_number_served(1257) #设置最大可以服务的人数
print(f"The maximum number of guests that {restaurant.name} restaurant can serve is: {restaurant.number_served}.")

restaurant.increment_number_served(3) #设置超额来的人数
print(f"{restaurant.name} restaurant has served additional {restaurant.number_served} guests tonight!")

'''
9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand 的类，让它继承你为完成练习9-1 或练习9-4 而编写的Restaurant 类。这两个版本的Restaurant 
类都可以，挑选你更喜欢的那个即可。添加一个名为flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个IceCreamStand 实例，
并调用这个方法。'''

class Restaurant():
    """这是一个描述餐馆的类"""
    
    def __init__ (self, name, cusine_type):
        """初始化描述餐馆的属性"""
        self.name = name.title()
        self.cusine_type = cusine_type
        self.number_served = 0 #添加一个名为number_served的属性，并将其默认值设置为0
        
    def describe_restaurant(self):
        """返回一条描述餐厅名字和其所提供食物风格的信息"""
        print(self.name + " serves " + \
              self.cusine_type.title() +".")
        
    def open_restaurant(self):
        """输出餐厅正在营业的信息"""
        print(self.name + " restaurant is open.")
        
    def set_number_served(self, number_served): #添加一个名为set_number_served()的方法
        """让用户能够设置就餐人数"""
        self.number_served = number_served
            
    def increment_number_served(self,additional_served): #添加一个名为increment_number_served()的方法
        """让用户能够增加就餐人数"""
        self.number_served += additional_served

class IceCreamStand(Restaurant):
    """一个表示冰激凌小店的类"""
    
    def __init__(self,name,cuisine_type = 'ice cream'):#改写父类属性
        """初始化冰激凌小店"""
        super().__init__(name, cuisine_type)
        self.flavors = [] #添加属性并动态创建列表
        
    def show_flavors(self):
        """显示出售的冰激凌品种"""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
        
big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla','chocolate','black cherry']

big_one.describe_restaurant()
big_one.show_flavors()

"""9-3 用户：创建一个名为User 的类，其中包含属性first_name 和last_name，还有用户简介通常会存储的其他几个属性。在类User 中定义一个名为describe_user()的方
法，它打印用户信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化的问候。创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。"""


class User():
    """一个表示用户的简单类"""
    
    def __init__(self, first_name, last_name, username, email, location):# 六个形参，但只有五个需要传参
        """初始化用户各项属性"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
    
    def describe_user(self):
        """显示用户信息摘要"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")
    
    def greet_user(self): 
        """向用户发出个性化的问候"""
        print(f"\nWelcome back, {self.username}!")

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska') 
eric.describe_user() 
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska') 
willie.describe_user() 
willie.greet_user()

'''9-7 管理员：管理员是一种特殊的用户。编写一个名为Admin的类，让它继承你为完成练习9-3而编写的User 类。添加一个名为privileges 的属性，用于存储一个由字符串
（如"can add post"、"can delete post"、"can ban user"等）组成的列表。编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin实例，
并调用这个方法。'''

class User():
    """一个表示用户的简单类"""
    
    def __init__(self, first_name, last_name, username, email, location):# 六个形参，但只有五个需要传参
        """初始化用户各项属性"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
    
    def describe_user(self):
        """显示用户信息摘要"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")
    
    def greet_user(self):
        """向用户发出个性化的问候"""
        print(f"\nWelcome back, {self.username}!")
    
        
class Admin(User):
    """有管理权限的用户"""
    
    def __init__(self, first_name, last_name, username, email, location):
        """初始化管理员"""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []
        
    def show_privileges(self):
        """显示当前管理员的权限"""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

eric = Admin('eric','matthes','e_matthes','e_matthes@example.com','alaska')
eric.describe_user()
eric.privileges = [ 'can reset passwords', 'can moderate discussions', 'can suspend accounts', ] 
eric.show_privileges()


"""9-8 权限：编写一个名为Privileges 的类，它只有一个属性——privileges，其中存储了练习9-7 所说的字符串列表。将方法show_privileges()移到这个类中。在Admin
类中，将一个Privileges 实例用作其属性。创建一个Admin 实例，并使用方法show_privileges()来显示其权限。"""

class User():
    """一个表示用户的简单类"""
    
    def __init__(self, first_name, last_name, username, email, location):# 六个形参，但只有五个需要传参
        """初始化用户各项属性"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
  
    def describe_user(self):
        """显示用户信息摘要"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")
    
    def greet_user(self):
        """向用户发出个性化的问候"""
        print(f"\nWelcome back, {self.username}!")
        
        
class Admin(User):
    """有管理权限的用户"""
    
    def __init__(self, first_name, last_name, username, email, location):
        """初始化管理员"""
        super().__init__(first_name, last_name, username, email, location)
        # 将权限集初始化为空
        self.privileges = Privileges() #将实参通过形参传给一个类
       
class Privileges():
    """一个存储管理员权限的类"""
    
    def __init__(self, privileges = []):
        self.privileges = privileges
        
    def show_privileges(self):
        """显示当前管理员的权限"""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")         
        else:
            print(" - This user has no privileges.")
            

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska') 
eric.describe_user()
eric.privileges.show_privileges() # 通过调用Admin类中privileges的形参来调用Privileges这个类，然后再调用这个类里的show_privileges的方法

print("\nAdding privileges...")
eric_privileges = [ 'can reset passwords', 'can moderate discussions', 'can suspend accounts', ] 

eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()