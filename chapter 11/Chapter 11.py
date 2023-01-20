# 11.1 测试函数
# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     """将名和姓合并成姓名,，在名和姓之间加上一个空格，并将它们的首字母都大写，再返回结果"""
#     full_name = first + ' ' + last
#     return full_name.title()

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print("\t Neatly formatted name: " + formatted_name + '.')
    
# 11.1.1 單元測試和測試用例  - Python標準庫中的模塊unittest提供了代碼測試工具
# 單元測試用於核實函數的某個方面沒有問題；測試用例是一組單元測試，這些單元測試一起核實函數在各種情形下的行為都符合要求。
# 良好的測試用例考慮到了函數可能收到的各種輸入，包含針對所有這些情形的測試。
# 全覆蓋式測試用例包含一整套單元測試，涵蓋了各種可能的函數使用方式。對於大型項目，要實現全覆蓋可能很難。
# 通常，最初只要針對代碼的重要行為編寫測試即可，等項目被廣泛使用時再考慮全覆蓋。

# 11.1.2 可通過的測試
#　要為函數編寫測試用例，可先導入模塊unittest以及要測試的函數，再創建一個繼承unittest.TestCase的類，並編寫一系列方法對函數行為的不同方面進行測試。

import unittest # 模塊unittest

from name_function import get_formatted_name # 導入了要測試的函數get_formatted_ name()

class NamesTestCase(unittest.TestCase): #這個類用於包含一系列針對get_formatted_name()的單元測試.這個類必須繼承unittest.TestCase類,這樣Python才知道如何運行你編寫的測試
    """测试name_function.py"""
    
    # NamesTestCase只包含這一個方法，用於測試get_formatted_name()的一個方面，我們將這個方法命名為test_first_last_name()
    def test_first_last_name(self): # 運行test_name_function.py時，所有以test_打頭的方法都將自動運行
        """能够正确地处理像Janis Joplin这样的姓名"""
        formatted_name = get_formatted_name('janis','joplin') # 使用实参'janis'和'joplin'调用get_formatted_name()，并存储要测试的返回值
        # unittest類最有用的功能之一：斷言方法 - 用來核實得到的結果是否與期望的結果一致
        # assertEqual（a,b）這個斷言方法就是來核實 a == b 是否成立,在这个案例里是核實变量formatted_name的值与'Janis Joplin是否相等
        self.assertEqual(formatted_name,'Janis Joplin') # 調用unittest的方法assertEqual()，並向它傳遞formatted_name和'Janis Joplin'
        # 上一句代碼行是說：將formatted_name的值同字符串'Janis Joplin'進行比較，如果它們相等，就萬事大吉，如果它們不相等，跟我說一聲！

unittest.main()


# 輸出結果：
.  # 句點表明有一個測試通過了
----------------------------------------------------------------------
Ran 1 test in 0.001s    # 指出Python運行了一個測試，消耗的時間不到0.001秒

OK # 最後的OK表明該測試用例中的所有單元測試都通過了

# 11.1.3 不能通過的測試

import unittest # 模塊unittest

from name_function_with_middle_name import get_formatted_name # 導入了要測試的函數get_formatted_ name(),這個版本能夠正確地處理包含中間名的姓名

class NamesTestCase(unittest.TestCase): #這個類用於包含一系列針對get_formatted_name()的單元測試.這個類必須繼承unittest.TestCase類,這樣Python才知道如何運行你編寫的測試
    """測試name_function.py"""
    
    # NamesTestCase只包含這一個方法，用於測試get_formatted_name()的一個方面，我們將這個方法命名為test_first_last_name()
    def test_first_last_name(self): # 運行test_name_function.py時，所有以test_打頭的方法都將自動運行
        """能夠正確地處理像Janis Joplin這樣的姓名"""
        formatted_name = get_formatted_name('janis','joplin') # 使用實參'janis'和'joplin'調用get_formatted_name()，並存儲要測試的返回值
        # unittest類最有用的功能之一：斷言方法 - 用來核實得到的結果是否與期望的結果一致
        self.assertEqual(formatted_name,'Janis Joplin') # 調用unittest的方法assertEqual()，並向它傳遞formatted_name和'Janis Joplin'
        # 上一句代碼行是說：將formatted_name的值同字符串'Janis Joplin'進行比較，如果它們相等，就萬事大吉，如果它們不相等，跟我說一聲！
unittest.main()

# 輸出結果：
E # 指出測試用例中有一個單元測試導致了錯誤
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase) # 指出NamesTestCase中的test_first_last_name()導致了錯誤。測試用例包含眾多單元測試時，知道哪個測試未通過至關重要
能夠正確地處理像Janis Joplin這樣的姓名
----------------------------------------------------------------------
Traceback (most recent call last): # 一個標準的traceback指出函數調用get_formatted_name('janis', 'joplin')有問題，因為它缺少一個必不可少的位置實參。
  File "<ipython-input-20-1ae13875b7de>", line 11, in test_first_last_name
    formatted_name = get_formatted_name('janis','joplin') 
  File "E:\01 - coursera\python編程 從入門到實戰\chapter 11\name_function_with_middle_name.py", line 4, in get_formatted_name
    full_name = first + ' '+ middle +' ' + last
NameError: name 'middle' is not defined

----------------------------------------------------------------------
Ran 1 test in 0.156s # 運行了一個單元測試

FAILED (errors=1) # 指出整個測試用例都未通過，因為運行該測試用例時發生了一個錯誤

# 11.1.4 測試未通過時怎麽辦
# 不要修改測試，而應修復導致測試不能通過的代碼：檢查剛對函數所做的修改，找出導致函數行為不符合預期的修改。
# get_formatted_name()以前只需要兩個實參——名和姓，但現在它要求提供名、中間名和姓。新增的中間名參數是必不可少的，這導致get_formatted_name()的行為不符合預期。
# 就這裏而言，最佳的選擇是讓中間名變為可選的,這樣函數可以接受有中間名和沒有中間名的輸入。

# 來修改get_formatted_name()，將中間名設置為可選的,修改後的函數命名為get_formatted_name_with_middle_name()

import unittest # 模塊unittest

# 導入了要測試的函數get_formatted_ name(),這個版本能夠正確地處理包含与不包含中間名的姓名
from name_function_with_middle_name_as_an_option import get_formatted_name_with_middle_name 

class NamesTestCase(unittest.TestCase): #這個類用於包含一系列針對get_formatted_name()的單元測試.這個類必須繼承unittest.TestCase類,這樣Python才知道如何運行你編寫的測試
    """測試name_function.py"""
    
    # NamesTestCase只包含這一個方法，用於測試get_formatted_name()的一個方面，我們將這個方法命名為test_first_last_name()
    def test_first_last_name(self): # 運行test_name_function.py時，所有以test_打頭的方法都將自動運行
        """能夠正確地處理像Janis Joplin這樣的姓名"""
        formatted_name = get_formatted_name_with_middle_name('janis','joplin') # 使用實參'janis'和'joplin'調用get_formatted_name()，並存儲要測試的返回值
        # unittest類最有用的功能之一：斷言方法 - 用來核實得到的結果是否與期望的結果一致
        self.assertEqual(formatted_name,'Janis Joplin') # 調用unittest的方法assertEqual()，並向它傳遞formatted_name和'Janis Joplin'
        # 上一句代碼行是說：將formatted_name的值同字符串'Janis Joplin'進行比較，如果它們相等，就萬事大吉，如果它們不相等，跟我說一聲！

unittest.main()


# 輸出結果：
. # 句點表明有一個測試通過了
----------------------------------------------------------------------
Ran 1 test in 0.149s # 指出Python運行了一個測試，消耗的時間不到0.149秒

OK # 最後的OK表明該測試用例中的所有單元測試都通過了

import unittest # 模塊unittest

# 導入了要測試的函數get_formatted_ name(),這個版本能夠正確地處理包含与不包含中間名的姓名
from name_function_with_middle_name_as_an_option import get_formatted_name_with_middle_name 

class NamesTestCase(unittest.TestCase): #這個類用於包含一系列針對get_formatted_name()的單元測試.這個類必須繼承unittest.TestCase類,這樣Python才知道如何運行你編寫的測試
    """測試name_function.py"""
    
    # NamesTestCase只包含這一個方法，用於測試get_formatted_name()的一個方面，我們將這個方法命名為test_first_last_name()
    def test_first_last_name(self): # 運行test_name_function.py時，所有以test_打頭的方法都將自動運行
        """能夠正確地處理像Janis Joplin這樣的姓名"""
        formatted_name = get_formatted_name_with_middle_name('janis','joplin',middle ='ok') # 使用實參'janis'和'joplin'調用get_formatted_name()，並存儲要測試的返回值
        # unittest類最有用的功能之一：斷言方法 - 用來核實得到的結果是否與期望的結果一致
        self.assertEqual(formatted_name,'Janis Ok Joplin') # 調用unittest的方法assertEqual()，並向它傳遞formatted_name和'Janis Joplin'
        # 上一句代碼行是說：將formatted_name的值同字符串'Janis Joplin'進行比較，如果它們相等，就萬事大吉，如果它們不相等，跟我說一聲！

unittest.main()


# 断————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# 11.1.5 添加新测试 - 再编写一个测试，用于测试包含中间名的姓名

import unittest # 模塊unittest
# 導入了要測試的函數get_formatted_ name(),這個版本能夠正確地處理包含与不包含中間名的姓名
from name_function_with_middle_name_as_an_option import get_formatted_name_with_middle_name 

class NamesTestCase(unittest.TestCase): #這個類用於包含一系列針對get_formatted_name()的單元測試.這個類必須繼承unittest.TestCase類,這樣Python才知道如何運行你編寫的測試
    """測試name_function.py"""
     
    def test_first_last_name(self): # 運行test_name_function.py時，所有以test_打頭的方法都將自動運行
        """能夠正確地處理像Janis Joplin這樣的姓名"""
        formatted_name = get_formatted_name_with_middle_name('janis','joplin') # 使用實參'janis'和'joplin'調用get_formatted_name()，並存儲要測試的返回值
        # unittest類最有用的功能之一：斷言方法 - 用來核實得到的結果是否與期望的結果一致
        self.assertEqual(formatted_name,'Janis Joplin') # 調用unittest的方法assertEqual()，並向它傳遞formatted_name和'Janis Joplin'
        # 上一句代碼行是說：將formatted_name的值同字符串'Janis Joplin'進行比較，如果它們相等，就萬事大吉，如果它們不相等，跟我說一聲！
        
    def test_first_last_middle_name(self): # 方法名必须以test_打头，这样它才会在我们运行test_name_function.py时自动运行。
    # 在TestCase类中使用很长的方法名是可以的；这些方法的名称必须是描述性的，这才能让你明白测试未通过时的输出；这些方法由Python自动调用，你根本不用编写调用它们的代码
        """能够正确地处理像Charles Otto Puth 这样的姓名吗？"""
        formatted_name = get_formatted_name_with_middle_name(
            'charles','puth','otto') # 请特别注意这里，middle name的位置是在最后一个
        # 为测试函数get_formatted_name_with_middle_name()，我们使用名、姓和中间名调用它，再使用assertEqual()检查返回的姓名是否与预期的姓名（名、中间名和姓）一致
        self.assertEqual(formatted_name, 'Charles Otto Puth')
    
unittest.main()

# 輸出結果：
..
----------------------------------------------------------------------
Ran 2 tests in 0.063s

OK

'''拓展练习
城市和国家：编写一个函数，它接受两个形参：一个城市名和一个国家名。这个函数返回一个格式为City, Country 的字符串，如Santiago, Chile。将这个函数存储在一个名为city _functions.py 的模块中。
创建一个名为test_cities.py 的程序，对刚编写的函数进行测试（别忘了，你需要导入模块unittest 以及要测试的函数）。编写一个名为test_city_country()的方法，
核实使用类似于'santiago'和'chile'这样的值来调用前述函数时，得到的字符串是正确的。运行test_cities.py，确认测试test_city_country()通过了。
'''

import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):#這個類用於包含一系列針對city_country()的單元測試.這個類必須繼承unittest.TestCase類,這樣Python才知道如何運行你編寫的測試
    '''测试city_functions.py'''
    
     # CitiesTestCase只包含這一個方法，用於測試city_country()的一個方面，我們將這個方法命名為test_city_country()
    def test_city_country(self):
        """传入简单的城市和国家可行吗"""
        santiago_chile = city_country('santiago','chile') # 使用實參'santiago'和'chile'調用city_country()，並存儲要測試的返回值
        self.assertEqual(santiago_chile, 'Santiago,Chile')# 調用unittest的方法assertEqual()，並向它傳遞santiago_chile和'Santiago, Chile'
        # 上一句代碼行是說：將santiago_chile的值同字符串'Santiago, Chile'進行比較，如果它們相等，就萬事大吉，如果它們不相等，跟我說一聲！
        
unittest.main()



'''拓展练习
人口数量：修改前面的函数，使其包含第三个必不可少的形参population，并返回一个格式为City, Country – population xxx 的字符串，如Santiago, Chile –
population 5000000。运行test_cities.py，确认测试test_city_country()未通过。修改上述函数，将形参population 设置为可选的。再次运行test_cities.py，确认测
试test_city_country()又通过了。再编写一个名为test_city_country_population()的测试，核实可以使用类似于'santiago'、'chile'和'population=5000000'这样的值来调用这个函数。
再次运行test_cities.py，确认测试test_city_country_population()通过了。
'''

import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):#這個類用於包含一系列針對city_country()的單元測試.這個類必須繼承unittest.TestCase類,這樣Python才知道如何運行你編寫的測試
    '''测试city_functions.py'''
    
    def test_city_country(self):
        """传入简单的城市和国家可行吗"""
        santiago_chile = city_country('santiago','chile') # 使用實參'santiago'和'chile'調用city_country()，並存儲要測試的返回值
        self.assertEqual(santiago_chile, 'Santiago, Chile')# 調用unittest的方法assertEqual()，並向它傳遞santiago_chile和'Santiago, Chile'
        # 上一句代碼行是說：將santiago_chile的值同字符串'Santiago, Chile'進行比較，如果它們相等，就萬事大吉，如果它們不相等，跟我說一聲！
        
    def test_city_country_population(self):
        """可向形参population传递值吗"""
        santiago_chile = city_country('santiago','chile', population = 5_000_000)# 使用實參'santiago','chile'和可选实参'5000000'調用city_country()，並存儲要測試的返回值
        self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')# 調用方法assertEqual()，並向它傳遞santiago_chile和'Santiago, Chile - population 5000000'
        # 上一句代碼行是說：將santiago_chile的值同字符串'Santiago, Chile - population 5000000'進行比較，如果它們相等，就萬事大吉，如果它們不相等，跟我說一聲！

unittest.main()



# 断————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 11.2.2 一个要测试的类

# 为证明AnonymousSurvey类能够正确地工作，来编写一个使用它的程序
from survey import AnonymousSurvey

#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question() # 调用show_question()来显示问题，并提示用户输入答案
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response) # 收到每个答案的同时将其存储进一个列表
    
# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

# 11.2.3 测试AnonymousSurvey 类

# 导入模块unittest以及要测试的类AnonymousSurve
import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase): # 测试用例命名为TestAnonymousSurvey，它继承了unittest.TestCase
    """针对AnonymousSurvey类的测试"""
    
    def test_store_single_response(self): # 测试方法验证调查问题的单个答案被存储后，会包含在调查结果列表中
        """测试单个答案会被妥善地存储""" # 如果这个测试未通过，我们就能通过输出中的方法名得知，在存储单个调查答案方面存在问题
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question) #　使用问题"What language did you first learnto speak?"创建了一个名为my_survey的实例
        my_survey.store_response('English')　#　使用方法store_response()存储单个答案English
        # 断言方法assertIn(item, list)的用途是： 核实item在list中
        self.assertIn('English', my_survey.responses)　#检查English是否包含在列表my_survey.responses中，以核实这个答案是否被妥善地存储了
        
unittest.main()
    

# 下面来核实用户提供三个答案时，它们也将被妥善地存储。需要在TestAnonymousSurvey中再添加一个方法
import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase): # 测试用例命名为TestAnonymousSurvey，它继承了unittest.TestCase
    """针对AnonymousSurvey类的测试"""
    
    def test_store_single_response(self): # 测试方法验证调查问题的单个答案被存储后，会包含在调查结果列表中
        """测试单个答案会被妥善地存储""" # 如果这个测试未通过，我们就能通过输出中的方法名得知，在存储单个调查答案方面存在问题
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question) #　使用问题"What language did you first learnto speak?"创建了一个名为my_survey的实例
        my_survey.store_response('English') #　使用方法store_response()存储单个答案English
        # 断言方法assertIn(item, list)的用途是： 核实item在list中
        self.assertIn('English', my_survey.responses) # 检查English是否包含在列表my_survey.responses中，以核实这个答案是否被妥善地存储了
    
    def test_store_three_responses(self):
        """测试三个答案会被妥善地保存"""
        question = "What language did you first learn?"
        my_survey = AnonymousSurvey(question) # 创建一个调查对象
        responses = ['English','Spanish','Mandarin']
        for response in responses:
            my_survey.store_response(response) # 将responses列表中的三个元素都存储到my_survey这个实例中
        
        for response in responses:
            self.assertIn(response, my_survey.responses)
        
unittest.main()

# 11.2.4 方法setUp()
# setUp()让我们只需创建这些对象一次，就能在每个测试方法中使用。如果在 TestCase 类中包含了方法 setUp()，Python 将先运行它，再运行各个以 test_打头的方法。
import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase): # 测试用例命名为TestAnonymousSurvey，它继承了unittest.TestCase
    """针对AnonymousSurvey类的测试"""
    
    def setUp(self): # 创建一个调查对象：my_survey 和一个答案列表：responses
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What Language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question) # 存储的变量名包含前缀self（即存储在属性中），因此可在这个类的任何地方使用。
        self.responses = ['English','Spanish','Mandarin'] # 存储的变量名包含前缀self（即存储在属性中），因此可在这个类的任何地方使用。
    
    def test_store_single_response(self): # 
        """测试单个答案会被妥善地存储""" # 
        self.my_survey.store_response(self.responses[0])
        # 断言方法assertIn(item, list)的用途是： 核实item在list中
        self.assertIn(self.responses[0], self.my_survey.responses) # 核实self.responses 中的第一个答案——self.responses[0]——被妥善地存储
    
    def test_store_three_responses(self):
        """测试三个答案会被妥善地保存"""
        for response in self.responses:
            self.my_survey.store_response(response) # 每一次遍历的结果都通过调用方法store_response存储到实例my_survey中
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)  # 每经历上一步代码的遍历后，都核实response是否已经通过调用方法store_response存储到实例my_survey中
        
unittest.main()



# 斷————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 11.2.2 一個要測試的類

# 為證明AnonymousSurvey類能夠正確地工作，來編寫一個使用它的程序
from survey import AnonymousSurvey

#定義一個問題，並創建一個表示調查的AnonymousSurvey對象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 顯示問題並存儲答案
my_survey.show_question() # 調用show_question()來顯示問題，並提示用戶輸入答案
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response) # 收到每個答案的同時將其存儲進一個列表
    
# 顯示調查結果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

# 11.2.3 測試AnonymousSurvey類

# 導入模塊unittest以及要測試的類AnonymousSurve
import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase): # 測試用例命名為TestAnonymousSurvey，它繼承了unittest.TestCase
    """針對AnonymousSurvey類的測試"""
    
    def test_store_single_response(self): # 測試方法驗證調查問題的單個答案被存儲後，會包含在調查結果列表中
        """測試單個答案會被妥善地存儲""" # 如果這個測試未通過，我們就能通過輸出中的方法名得知，在存儲單個調查答案方面存在問題
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)#使用問題"What language did you first learnto speak?"創建了一個名為my_survey的實例
        my_survey.store_response('English')#使用方法store_response()存儲單個答案English
        # 斷言方法assertIn(item, list)的用途是： 核實item在list中
        self.assertIn('English', my_survey.responses)#檢查English是否包含在列表my_survey.responses中，以核實這個答案是否被妥善地存儲了
        
unittest.main()
    

# 下面來核實用戶提供三個答案時，它們也將被妥善地存儲。需要在TestAnonymousSurvey中再添加一個方法
import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase): # 測試用例命名為TestAnonymousSurvey，它繼承了unittest.TestCase
    """針對AnonymousSurvey類的測試"""
    
    def test_store_single_response(self): # 測試方法驗證調查問題的單個答案被存儲後，會包含在調查結果列表中
        """測試單個答案會被妥善地存儲""" # 如果這個測試未通過，我們就能通過輸出中的方法名得知，在存儲單個調查答案方面存在問題
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question) #　使用問題"What language did you first learnto speak?"創建了一個名為my_survey的實例
        my_survey.store_response('English') #　使用方法store_response()存儲單個答案English
        # 斷言方法assertIn(item, list)的用途是： 核實item在list中
        self.assertIn('English', my_survey.responses) # 檢查English是否包含在列表my_survey.responses中，以核實這個答案是否被妥善地存儲了
    
    def test_store_three_responses(self):
        """測試三個答案會被妥善地保存"""
        question = "What language did you first learn?"
        my_survey = AnonymousSurvey(question) # 創建一個調查對象
        responses = ['English','Spanish','Mandarin']
        for response in responses:
            my_survey.store_response(response) # 將responses列表中的三個元素都存儲到my_survey這個實例中
        
        for response in responses:
            self.assertIn(response, my_survey.responses)
        
unittest.main()

# 11.2.4 方法setUp()
# setUp()讓我們只需創建這些對象一次，就能在每個測試方法中使用。如果在 TestCase 類中包含了方法 setUp()，Python 將先運行它，再運行各個以 test_打頭的方法。
import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase): # 測試用例命名為TestAnonymousSurvey，它繼承了unittest.TestCase
    """針對AnonymousSurvey類的測試"""
    
    def setUp(self): # 創建一個調查對象：my_survey 和一個答案列表：responses
        """創建一個調查對象和一組答案，供使用的測試方法使用"""
        question = "What Language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question) # 存儲的變量名包含前綴self（即存儲在屬性中），因此可在這個類的任何地方使用。
        self.responses = ['English','Spanish','Mandarin'] # 存儲的變量名包含前綴self（即存儲在屬性中），因此可在這個類的任何地方使用。
    
    def test_store_single_response(self): # 
        """測試單個答案會被妥善地存儲""" # 
        self.my_survey.store_response(self.responses[0])
        # 斷言方法assertIn(item, list)的用途是： 核實item在list中
        self.assertIn(self.responses[0], self.my_survey.responses) # 核實self.responses 中的第一個答案——self.responses[0]——被妥善地存儲
    
    def test_store_three_responses(self):
        """測試三個答案會被妥善地保存"""
        for response in self.responses:
            self.my_survey.store_response(response) # 每一次遍歷的結果都通過調用方法store_response存儲到實例my_survey中
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)  # 每經歷上一步代碼的遍歷後，都核實response是否已經通過調用方法store_response存儲到實例my_survey中
        
unittest.main()

# 测试引发错误时会打印一个E；测试导致断言失败时打印一个F

'''
11-3 雇員：編寫一個名為Employee 的類，其方法__init__()接受名、姓和年薪，並將它們都存儲在屬性中。編寫一個名為give_raise()的方法，它默認將年薪增加5000美元，
但也能夠接受其他的年薪增加量。為Employee 編寫一個測試用例，其中包含兩個測試方法：test_give_default_raise()和test_give_custom_raise()。
使用方法setUp()，以免在每個測試方法中都創建新的雇員實例。運行這個測試用例，確認兩個測試都通過了。
'''

import unittest

from employee import Employee

class TestEmployee (unittest.TestCase):
    """測試模塊employee"""
    
    def setUp(self):
        """創建一個Employee實例，以便在測試中使用"""
        self.eric = Employee('eric','matthes', 65_000)
    
    def test_give_default_raise(self):
        '''測試使用默認的年薪增加量是否可行'''
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 70000)
        
    def test_give_custom_raise(self):
        """測試自定義年薪增加量是否可行"""
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.salary, 75000)
        
unittest.main()

    




'''
11-3 雇员：编写一个名为Employee 的类，其方法__init__()接受名、姓和年薪，并将它们都存储在属性中。编写一个名为give_raise()的方法，它默认将年薪增加5000美元，
但也能够接受其他的年薪增加量。为Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_raise()和test_give_custom_raise()。
使用方法setUp()，以免在每个测试方法中都创建新的雇员实例。运行这个测试用例，确认两个测试都通过了。
'''

import unittest

from employee import Employee

class TestEmployee (unittest.TestCase):
    """测试模块employee"""
    
    def setUp(self):
        """创建一个Employee实例，以便在测试中使用"""
        self.eric = Employee('eric','matthes', 65_000)
    
    def test_give_default_raise(self):
        '''测试使用默认的年薪增加量是否可行'''
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 70000)
        
    def test_give_custom_raise(self):
        """测试自定义年薪增加量是否可行"""
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.salary, 75000)
        
unittest.main()
    








