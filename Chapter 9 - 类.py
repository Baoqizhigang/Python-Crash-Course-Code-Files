# 9.1.1 创建Dog 类
# 根据Dog类创建的每个实例都将存储名字和年龄。
# 我们赋予每条小狗蹲下和打滚的能力

class Dog():
    # 定义一个名为Dog的类，关键字是class
    #在python中首字母大写的名称指的是类
    #定义中的括号的空的，因为要从空白创建这个类
    """一次模拟小狗的简单尝试"""#这个文档字符是对类功能的一个描述
    
    #类别中的函数被称为方法
    def __init__(self,name,age):# self,name,age 是方法_init_()的三个形参
        #_init_()是一个特殊的方法，每当根据Dog类创建实例时，python就会自动运行它
        # init两边的下划线是一种约定，让python避免默认方法与普通方法名称的冲突 
        # 形参self必不可少，且必须位于其他形参之前
        # Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self
        # 每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，
        # 让实例能够访问类中的属性和方法
        # 我们将通过实参向Dog()传递名字和年龄；
        # self会自动传递，因此我们不需要传递它。
        # 每当我们根据Dog类创建实例时，都只需给最后两个形参（name和age）提供值。
        """初始化属性name和age"""
        # 以self为前缀的变量都可供类中的所有方法使用
        # 我们可以通过类的任何实例来访问这些变量
        self.name = name # 获取存储在形参name中的值，并将其存储到变量name中，
                         # 然后该变量被关联到当前创建的实例中
        self.age = age
        # 像这样可通过实例访问的变量称为属性
    
    # Dog类还定义了另外两个方法：sit()和roll_over()
    # 由于这些方法不需要额外的信息，如名字或年龄，因此它们只有一个形参self
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

#--------------------------------------------------------  
    
class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self,name,age):
        """初始化属性name和age"""
        
        self.name = name 
        self.age = age
  
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")   
#--------------------------------------------------------  
    
# 9.1.2 根据类创建实例
# Dog类是一系列说明，让python知道如何创建表示特定小狗的实例
class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age): #init两边分别是两根下划线
        """初始化属性name和age"""
        
        self.name = name 
        self.age = age
  
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
        
my_dog = Dog('willie',6)

print("My dog's name is " + my_dog.name.title() + ".")
print("my dog is " + str(my_dog.age) + " years old.")


my_dog = Dog('willie',6) #将这个实例存储在变量my_dog中
# python使用实参'willie'和6调用Dog类中的方法__init__()
# 方法__init__()创建一个表示特定小狗的示例，并使用我们提供的值来设置属性name和age.
# 方法__init__()并未显式包含return语句，但Python自动返回一个表示这条小狗的实例。
# 命名约定：通常可以认为首字母大写的名称（如Dog）指的是类
# 命名约定：通常可以认为小写的名称（如my_dog）指的是根据类创建的实例。

# 1.访问属性 - 使用句点表示法
print("My dog's name is " + my_dog.name.title() + ".")
# 访问my_dog的属性name的值：my_dog.name
# 句点表示法在Python中很常用，这种语法演示了Python如何获悉属性的值
# my_dog.name.title()将my_dog的属性name的值'willie'改为首字母大写的
print("My dog is " + str(my_dog.age) + " years old.")
# str(my_dog.age)将my_dog的属性age的值6转换为字符串

# 2 调用方法
# 根据Dog类创建实例后，就可以使用句点表示法来调用Dog类中定义的任何方法
my_dog = Dog('willie',6)
my_dog.sit()
my_dog.roll_over()


# 要调用方法，可指定实例的名称（这里是my_dog）和要调用的方法，并用句点分隔它们
my_dog = Dog('willie',6)
my_dog.sit() # Python在类Dog中查找方法sit()并运行其代码
my_dog.roll_over()
# 请务必给属性和方法指定了合适的描述性名称，如name、age、sit()

# 3 创建多个实例 -  可按需求根据类创建任意数量的实例
# 创建了两条小狗，它们分别名为Willie和Lucy
# 每条小狗都是一个独立的实例，有自己的一组属性，能够执行相同的操作
my_dog = Dog('willie',6)
your_dog = Dog('lucy',3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()  #使用句点表示法来调用Dog类中定义的任何方法

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

# 就算我们给第二条小狗指定同样的名字和年龄，Python依然会根据Dog类创建另一个实例。
# 可按需求根据一个类创建任意数量的实例，条件是将每个实例都存储在不同的变量中,或占用
# 列表或字典的不同位置。

#9.1 使用类和实例
# 可以使用类来模拟现实世界中的很多情景
# 可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。

# 9.2.1 Car 类
# 编写一个表示汽车的类，它存储了有关汽车的信息，还有一个汇总这些信息的方法

class Car():
    """一次模拟汽车的简单尝试"""
    
    #这个方法的第一个形参为self,还包含了另外三个形参：make、model和year
    #方法__init__()接受这些形参的值，并将它们存储在根据这个类创建的实例的属性中
    def __init__(self, make, model, year): 
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self): #定义一个名为get_descriptive_name()的方法
        """返回整洁的描述性信息"""
        #这个方法使用属性year、make和model来创建一个对汽车进行描述的字符串
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        #使用了self.make、self.model和self.year来访问属性的值
        return long_name.title()
    
my_new_car = Car( 'audi', 'a4', 2016 ) #根据Car类创建一个实例，并将其存储到变量my_new_car中
print (my_new_car.get_descriptive_name()) #调用方法get_descriptive_name()

#----------------------------------------------------
class Car():
    """一次模拟汽车的简单尝试"""
    
    def __init__(self, make, model, year): 
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self): 
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
my_new_car = Car( 'audi', 'a4', 2016 )
print (my_new_car.get_descriptive_name())


print(1,2,3,4,5, sep =',', end = '.')

# 9.2.2 给属性指定默认值
# 类中的每个属性都必须有初始值，哪怕这个值是0或空字符串
# 设置默认值时，在方法__init__()内指定这种初始值是可行的；
# 如果你对某个属性这样做了，就无需包含为它提供初始值的形参。

# 给它添加一个随时间变化的属性（odometer_reading），初始值总是为0，它存储汽车的总里程
# 添加了一个名为read_odometer()的方法，用于读取汽车的里程表：

class Car():
    
    def __init__ (self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #创建一个odometer_reading的属性，初始值设置为0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        #这个方法使用属性year、make和model来创建一个对汽车进行描述的字符串
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        #使用了self.make、self.model和self.year来访问属性的值
        return long_name.title()
        
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        # 定义一个名为read_odometer()的方法，它让你能够获悉汽车的里程
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
my_new_car = Car('audi', 'a4', 2016)
# 出售时里程表读数为0的汽车并不多，因此我们需要一个修改该属性的值的途径
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# ----------------------------------------------
class Car():
    
    def __init__ (self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 9.2.3 修改属性的值
# 可以以三种不同的方式修改属性的值：
# 直接通过实例进行修改；
# 通过方法进行设置；
# 通过方法进行递增（增加特定的值）。

# 1. 直接修改属性的值 - 最简单的方式是通过实例直接访问它
class Car():
    
    def __init__ (self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
  

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

#使用句点表示法来直接访问并设置汽车的属性odometer_reading
#Python在实例my_new_car中找到属性odometer_reading，并将该属性的值设置为23
my_new_car.odometer_reading = 23 
my_new_car.read_odometer()


# 2. 通过方法修改属性的值
# 将值传递给一个方法，由它在内部对值进行更新。

class Car():
    
    def __init__ (self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
    # 这个方法接受一个里程值，并将其存储到self.odometer_reading中。
        """将里程表读数设定为指定的值"""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

#调用update_odometer()，并向它提供实参23（该实参对应于方法定义中的形参mileage）
my_new_car.update_odometer(23) # 可以理解为新的值覆盖了旧的/默认的值
# 方法read_odometer()打印23这个读数：
my_new_car.read_odometer()


# 可对方法update_odometer()进行扩展，使其在修改里程表读数时做些额外的工作
# 添加一些逻辑，禁止任何人将里程表读数往回调：
class Car():
    
    def __init__ (self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 12
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
    # 这个方法接受一个里程值，并将其存储到self.odometer_reading中。
        """将里程表读数设置为指定的值，禁止将里程表读数往回调"""
        if mileage >= self.odometer_reading :
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")
            print("This is a scam!")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# update_odometer()在修改属性前检查指定的读数是否合理
# 如果新指定的里程（mileage）大于或等于原来的里程（self.odometer_reading），
# 就将里程表读数改为新指定的里程,否则就发出警告，指出不能将里程表往回拨
my_new_car.update_odometer(5) 
my_new_car.read_odometer()

# 3. 通过方法对属性的值进行递增

class Car():
    
    def __init__ (self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 12
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
    # 这个方法接受一个里程值，并将其存储到self.odometer_reading中。
        """将里程表读数设置为指定的值，禁止将里程表读数往回调"""
        if mileage >= self.odometer_reading :
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")
        
    def increment_odometer(self,miles):
        #接受一个单位为英里的数字，并将其加入到self.odometer_reading中
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
        
#my_new_car = Car('audi', 'a4', 2016)
#print(my_new_car.get_descriptive_name())

my_used_car = Car('subaru', 'outback', 2013) #创建一辆二手车:my_used_car
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500) #调用方法update_odometer()并传入23500，
my_used_car.read_odometer()

my_used_car.increment_odometer(100) #调用increment_odometer()并传入100
my_used_car.read_odometer()


# ___________________________________

class Car():
    
    def __init__ (self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 12
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):

        """将里程表读数设置为指定的值，禁止将里程表读数往回调"""
        if mileage >= self.odometer_reading :
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")
        
    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# 9.3 继承  
# 当要编写的类是另一个现成类的特殊版本，可使用继承  
# 一个类继承另一个类时，它将自动获得另一个类的所有属性和方法
# 原有的类称为父类，而新类称为子类。
# 子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。

# 9.3.1 子类的方法  __init__()
# 创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值

#创建一个简单的ElectricCar类版本，它具备Car类的所有功能
class Car():
    """一次模拟汽车的简单尝试"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
     
    def increment_odometer(self, miles):
        self.odometer_reading += miles
   
    def fill_gas_tank(self):
        """给车的油箱加满"""
        print("Please fill the gas tank!")

my_new_car = Car('audi', 'a4', 2016)
my_new_car.fill_gas_tank()


# 创建子类时，父类必须包含在当前文件中，且位于子类前面。    
class ElectricCar(Car): #定义子类ElectricCar,必须在括号内指定父类的名称
    """电动汽车的独特之处"""
    #方法__init__()接受创建Car实例所需的信息
    def __init__(self,make, model, year):
        """初始化父类的属性"""
        # super()是一个特殊函数，帮助Python将父类和子类关联起来
        # 这行代码让Python调用ElectricCar的父类的方法__init__()，让ElectricCar实例包含父类的所有属性
        # 父类也称为超类（superclass），名称super因此而得名
        super().__init__(make, model, year)

# 创建ElectricCar类的一个实例，并将其存储在变量my_tesla中
# ElectricCar类中__init__()方法会调用父类Car中定义的方法__init__()        
my_tesla = ElectricCar('tesla','model s',2023) #调用ElectricCar类中定义的方法__init__()
print(my_tesla.get_descriptive_name())
    
# 9.3.3 给子类定义属性和方法
# 让一个类继承另一个类后，可添加区分子类和父类所需的新属性和方法   
# 添加一个电动汽车特有的属性（电池），以及一个描述该属性的方法    
# 存储电瓶容量，并编写一个打印电瓶描述的方法：   
class Car():
    --为展示方便，此处省略所有跟Car类的代码--
    
class ElectricCar(Car): 
    """电动汽车的独特之处"""
 
    def __init__(self,make, model, year):
        """
        电动汽车独特之处
        初始化父类的属性
        再初始化点电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70 # 添加新属性self.battery_size，并设置其初始值(70)
        # 根据ElectricCar类创建的所有实例都将包含这个属性，但所有Car实例都不包含它。

    def describe_battery(self): # 添加一个名为describe_battery()的方法，它打印有关电瓶的信息
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
    
my_tesla = ElectricCar('tesla','model s',2023)
print(my_tesla.get_descriptive_name())    
my_tesla.describe_battery()    
    
# 9.3.4 重写父类的方法    
# 对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写    
# 可在子类中定义一个这样的方法，即它与要重写的父类方法同名。
# Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。    
class Car():
    --为展示方便，此处省略所有跟Car类的代码--
    
class ElectricCar(Car): 
    """电动汽车的独特之处"""
 
    def __init__(self,make, model, year):
        """
        电动汽车独特之处
        初始化父类的属性
        再初始化点电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70 # 添加新属性self.battery_size，并设置其初始值(70)
        # 根据ElectricCar类创建的所有实例都将包含这个属性，但所有Car实例都不包含它。

    def describe_battery(self): # 添加一个名为describe_battery()的方法，它打印有关电瓶的信息
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
        
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla','model s',2023)
#print(my_tesla.fill_gas_tank())  
my_tesla.fill_gas_tank()
# 如果有人对电动汽车调用方法fill_gas_tank()， Python将忽略Car类中的方法fill_gas_tank()，转而运行上述代码。

# 9.3.5 将实例用作属性
# 当给类添加的细节越来越多：属性和方法清单以及文件也会越来越长
# 在这种情况下，可能需要将类的一部分作为一个独立的类提取出来。
# 可以将大型类拆分成多个协同工作的小类。

class Car():
    --为展示方便，此处省略所有跟Car类的代码--
    
class Battery(): # 定义一个名为Battery的新类，它没有继承任何类
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size = 70): #形参battery_size是可选的,如果没有给它提供值，电瓶容量将被设置为70
        """初始化电瓶的属性"""
        self.battery_size = battery_size
        
    def describe_battery(self): #方法describe_battery()也移到了这个类中
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-Kwh battery.")
       
class ElectricCar(Car): 
    """电动汽车的独特之处"""
    def __init__(self,make, model, year):
        """电动汽车独特之处,初始化父类的属性,再初始化点电动汽车特有的属性"""
        super().__init__(make, model, year)
        # 添加一个名为self.battery的属性
        # Python创建一个新的Battery实例（由于没有指定尺寸，因此为默认值70），并将该实例存储在属性self.battery中
        # 每当方法__init__()被调用时，都将执行该操作
        # 每个ElectricCar实例都包含一个自动创建的Battery实例
        self.battery = Battery () 
        
my_tesla = ElectricCar('tesla','model s',2023)

print(my_tesla.get_descriptive_name())
# Python在实例my_tesla中查找属性battery，并对存储在该属性中的Battery实例调用方法describe_battery()。
my_tesla.battery.describe_battery()


# 再给Battery类添加一个方法，它根据电瓶容量报告汽车的续航里程：

class Car():
    --为展示方便，此处省略所有跟Car类的代码--
    
class Battery(): 
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size = 70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
        
    def describe_battery(self): 
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-Kwh battery.")
        
    def get_range(self): #新增的方法get_range()做了一些简单的分析
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270 
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
       
class ElectricCar(Car): 
    """电动汽车的独特之处"""
    def __init__(self,make, model, year):
        """电动汽车独特之处,初始化父类的属性,再初始化点电动汽车特有的属性"""
        super().__init__(make, model, year)
        # 添加一个名为self.battery的属性
        # Python创建一个新的Battery实例（由于没有指定尺寸，因此为默认值70），并将该实例存储在属性self.battery中
        # 每当方法__init__()被调用时，都将执行该操作
        # 每个ElectricCar实例都包含一个自动创建的Battery实例
        self.battery = Battery () 

my_tesla = ElectricCar('tesla','model s',2023)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 9.3.6 模拟实物

# 9.4.1 导入单个类
# 将Car类存储在一个名为car.py的模块中，该模块将覆盖前面使用的文件car.py
# 从现在开始，使用该模块的程序都必须使用更具体的文件名，如my_car.py

# 该部分内容详见文件car.py 和 my_car.py

# 9.5 Python 标准库
# 字典让你能够将信息关联起来，但它们不记录你添加键—值对的顺序
# 要创建字典并记录其中的键—值对的添加顺序，可使用模块collections中的OrderedDict类
# OrderedDict实例的行为几乎与字典相同，区别只在于记录了键—值对的添加顺序。

#从模块collections中导入了OrderedDict类
from collections import OrderedDict

#创建了OrderedDict类的一个实例，并将其存储到favorite_languages中
#这里没有使用花括号，而是调用OrderedDict()来创建一个空的有序字典，并将其存储在favorite_languages中
favorite_languages = OrderedDict()

#以每次一对的方式添加名字—语言对
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

# 遍历favorite_languages，但知道将以添加的顺序获取调查结果：
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
    

    
    



