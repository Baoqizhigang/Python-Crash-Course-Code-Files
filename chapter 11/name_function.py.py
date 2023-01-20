def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    """將名和姓合並成姓名,，在名和姓之間加上一個空格，並將它們的首字母都大寫，再返回結果"""
    full_name = first + ' ' + last
    return full_name.title()
