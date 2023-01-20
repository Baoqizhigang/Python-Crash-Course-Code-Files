# 這是一個類的測試 - 一個幫助管理匿名調查的類

class AnonymousSurvey:
    '''收集匿名調查問卷的答案'''
    
    def __init__(self, question):
        '''存儲一個問題，並為存儲答案做準備'''
        self.question = question # 存儲一個指定的調查問題
        self.responses = [] # 創建一個空列表，用於存儲答案
        
    def show_question(self):
        '''顯示調查問卷'''
        print(self.question)
        
    def store_response(self, new_response):
        '''存儲單份調查答卷'''
        self.responses.append(new_response) # 答案列表中添加新答案
        
    def show_results(self):
        '''顯示收集到的所有答卷'''
        print('Survey results:')
        for response in self.responses:
            print('- ' + response) # 將存儲在列表中的答案都打印出來
