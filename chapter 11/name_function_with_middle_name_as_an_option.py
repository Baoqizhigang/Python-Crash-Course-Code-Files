def get_formatted_name_with_middle_name(first, last, middle = ''): # 要将中间名设置为可选的，可在函数定义中将形参middle移到形参列表末尾，并将其默认值指定为一个空字符串
    """Generate a neatly formatted full name."""
    """將名,姓和中間名三者合並成姓名,且各自之間加上一個空格，並將它們的首字母都大寫，再返回結果"""
    if middle: # 添加一個if測試，以便根據是否提供了中間名相應地創建姓名
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
