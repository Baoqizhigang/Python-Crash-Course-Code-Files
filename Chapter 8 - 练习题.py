
# 练习 8-3： T恤
# 编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。
# 这个函数打印一个句子，概要地说明T恤的尺码和字样
# 使用位置实参调用该函数来制作一件T恤
# 使用关键字实参来来调用这个函数

def make_shirt(size,texts):
    """概要说明即将制作的T恤的尺码和字样""" 
    print(f"\nThe texts on the {size} size T-shirt is:{texts} ")

make_shirt('small','I love python!') # 位置实参
make_shirt(texts='I love python!',size='large') # 关键字实参

# 练习8-4：大号T恤
# 修改函数make_shirt()，使其在默认情况下制作一件印有“I love python"字样的大号T恤
# 调用这个函数来制作：一件印有默认字样给的大号和中号T恤
# 调用这个函数来制作：一件印有其他字样的T恤（尺寸无所谓）

def make_shirt(size,texts='I love python!'):
    """概要说明即将制作的T恤的尺码和字样""" 
    print(f"\nThe texts on the {size} size T-shirt is:{texts} ")

make_shirt('medium') # 位置实参
make_shirt('large') # 位置实参
make_shirt('large',texts='Python is the best programming language!') # 修改默认值

# 练习8-5：城市
# 编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。
# 这个函数应该打印一个简单的句子，下面是一个例子：
# San Francisco is in America. 
# 给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市
# 不属于默认国家。

def describe_city(city_name,country='America'):
    """概要说明城市的名字以及该城市所属的国家""" 
    print(f"\n{city_name.title()} is in {country.title()}.")

describe_city('san francisco')
describe_city('new york')
describe_city('tokyo',country='japan') #不属于默认国家的城市

# 练习8-6： 城市名
# 编写一个名为city_country()的函数，它接受城市的名称及所属的国家。这个函数应该返回
# 一个格式类似于这样的字符串："Santiago, Chile"
# 至少使用3个城市国家对来调用这个函数，并打印它返回的值。

def city_country(city,country):
    """城市的名字以及该城市所属的国家""" 
    full_msg = city + ', '+ country
    return full_msg.title()

while True:
    #print("\nPlease tell me the city you want to travel: ")
    #print("Please tell me which country this city in: ")
    print("(enter 'quit' at any time to quit)")
    
    city_name = input("Please tell me the city you want to travel:")
    if city_name == 'quit':
        break
    
    country_name = input("Please tell me which country this city in:")
    if country_name == 'quit':
        break
    
    outcome = city_country(city_name, country_name) # 位置实参
    print("\n")
    print(outcome)


# 练习8-7：专辑
# 编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。这个函数应该接受
# 歌手的名字和专辑名，并返回一个包含这两项信息的字典。使用这个函数创建三个表示不同
# 专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
# 给函数make_album()添加一个可选形参，以便能够存储专辑包含的歌曲数。
# 如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。
# 调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
def make_album(singer_name,album_name,num_of_songs=''):
    """ 描述歌手的名字和专辑名字的字典 """
    album = {'singer':singer_name.title(),'album':album_name.title()}
    if num_of_songs:
        album['number of songs'] = num_of_songs
    return album

album1 = make_album('charlie puth','voicenotes', num_of_songs=3)
print(album1)
album2 = make_album('taylor swift','midnights')
print(album2)
album3 = make_album('mariah carey','merry christmas', num_of_songs=10)
print(album3)

# 8-8 用户的专辑：
# 在为完成练习8-7 编写的程序中，编写一个while 循环，让用户输入一个专辑的歌手和名称。
# 获取这些信息后，使用它们来调用函数make_album()，并将创建的字典打印出来。
# 在这个while 循环中，务必要提供退出途径。

def make_album(singer_name,album_name):
    """ 描述歌手的名字和专辑名字的字典 """
    album = {'singer':singer_name.title(),'album':album_name.title()}
    return album

while True:
    #print("\nPlease type the singer's name': ")
    #print("Please type the name of the album: ")
    print("(enter 'quit' at any time to quit)")
    
    singer = input("Singer:")
    if singer == 'quit':
        break
    
    album = input("Album:")
    if album == 'quit':
        break
    
    outcome = make_album(singer,album) # 位置实参
    print("\n")
    print(outcome)


-----------------------------------------------------

# 8-9 魔术师： 创建一个包含魔术师名字的列表， 并将其传递给一个名为
# show_magicians()的函数，这个函数打印列表中每个魔术师的名字。
def show_magicians(names):
    """魔术师名字的列表"""
    for name in names:
        magician = name.title()
        print(magician)

magician_names = ['chrlie puth','taylor swift','mariah carey']
show_magicians(magician_names)

# 8-10 了不起的魔术师：在你为完成练习8-9 而编写的程序中，编写一个名为
# make_great()的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样
# “the Great”。调用函数show_magicians()，确认魔术师列表确实变了。
def show_magicians(names):
    """魔术师名字的列表"""
    for name in names:
        magician =  name.title()
        print(magician)

def make_great(magician_names,modified_names):
    """魔术师名字前加上'The great '"""
    while magician_names:
        current_names = magician_names.pop()
        modified_magician = 'The great ' + current_names.title()
        print(modified_magician)
        modified_names.append(modified_magician)
        

magician_names = ['chrlie puth','taylor swift','mariah carey']
show_magicians(magician_names)

modified_names = [ ] 
make_great(magician_names,modified_names) 

print(modified_names)
print(magician_names)

show_magicians(magician_names)
make_great(magician_names,modified_names) 

# 8-11 不变的魔术师：修改你为完成练习8-10 而编写的程序，在调用函数
# make_great()时，向它传递魔术师列表的副本。由于不想修改原始列表，请返回修改后
# 的列表，并将其存储到另一个列表中。分别使用这两个列表来调用show_magicians()，
# 确认一个列表包含的是原来的魔术师名字，而另一个列表包含的是添加了字样
# “the Great”的魔术师名字。
def show_magicians(names):
    """魔术师名字的列表"""
    for name in names:
        magician =  name.title()
        print(magician)

def make_great(m_names):
    """魔术师名字的列表"""
    for magician in magician_names:
        magician = 'The great ' + magician.title()
        print(magician)

magician_names = ['chrlie puth','taylor swift','mariah carey']

show_magicians(magician_names)

make_great(magician_names) #只改变了输出形式，未改变原列表内容

#-----------------------------------------------------------

def show_magicians(names):
    """魔术师名字的列表"""
    for name in names:
        magician =  name.title()
        print(magician)

def make_great(magician_names,modified_names):
    """魔术师名字前加上'The great '"""
    while magician_names:
        current_names = magician_names.pop()
        modified_magician = 'The great ' + current_names.title()
        print(modified_magician)
        modified_names.append(modified_magician)
        

magician_names = ['chrlie puth','taylor swift','mariah carey']
show_magicians(magician_names)

modified_names = [ ] 
make_great(magician_names[:],modified_names) 

print(modified_names)
print(magician_names)

show_magicians(magician_names)
make_great(magician_names,modified_names) 


# 8-12 三明治：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个
# 函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点
# 的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。

def make_sandwich(*items): 
    # 形参名*items中的星号是让Python创建一个名为items的空元组
    # 函数调用时实参的值统统都装进这个空元组
    """使用指定的食材制作三明治"""
    print("\nI'll make you  a great sandwich:")
    for item in items:
        print(f"...adding {item} to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef','cheddar chess','lettuce','honey dijon')
make_sandwich('turkey','apple slices','honey mustard')
make_sandwich('peaunt butter','strawberry jam')


# 8-14 汽车：编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接
# 受制造商和型号，还接受任意数量的关键字实参。这样调用这个函数：
# 1,提供必不可少的信息，以及两个名称—值对，如颜色和选装配件。
# 2,这个函数必须能够像下面这样进行调用：
# car = make_car('tesla', 'model 3', color='blue', tow_package=True)
# 打印返回的字典，确认正确地处理了所有的信息。

def make_car (manufacturer,model,**options):
    # 在函数定义时，*代表收集参数，在函数调用时将提供的所有值放进一个元组
    # 在函数定义时，*号并不会收集关键字参数
    # 在函数定义时，**代表收集关键字参数,在函数调用时把提供的所有名称键值对放进字典
    """创建一个表示汽车的字典"""
    car_dict = {
        'manufacturer':manufacturer.title(),
        'model':model.title(),
        } # 'manufacturer' 和 'model' 在字典里是键，函数里对应的实参是值
    for option, value in options.items(): #option和value分别代表实参里的键值对
        car_dict[option]=value #每次遍历将实参里的关键字参数值对加入到字典
        
    return car_dict #返回字典

my_outback = make_car('tesla', 'model 3', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda','accord', year=1991, color='White',\
                         headlight='popup') #可提供任意数量的关键字实参
print(my_old_accord)



