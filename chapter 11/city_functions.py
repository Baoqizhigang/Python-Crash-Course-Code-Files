#-*- coding: utf-8 -*-
# """一系列处理城市的函数"""

# def city_country(city, country):
#     """返回一个形如 'Santigo,Chile'的字符串"""
#     return f"{city.title()},{country.title()}"



#  将形参 population设置为可选的。再次运行
"""一系列处理城市的函数"""

def city_country(city, country, population = ''):
    """返回一个形如'Santiago, Chile - population 5000000'的字符串"""
    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - population {population}"
    return output_string


