def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    """將名,姓和中間名三者合並成姓名,且各自之間加上一個空格，並將它們的首字母都大寫，再返回結果"""
    full_name = first + ' '+ middle +' ' + last
    return full_name.title()
