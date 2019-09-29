# help()是python中的内置函数
#通过help()函数可以查询python中的函数的用法
#语法：help(函数对象)
#help(print)#获取print()函数的使用说明

#文档字符串(doc str)
#在定义函数时，可以在函数内部编写文档字符串，文档字符串就是函数的说明
#   当我们编写了文档字符串时，就可以通过help()函数来查看函数的说明
#   文档字符串非常简单，其实直接在函数的第一行写一个字符串就是文档字符串
def fn(a:int,b:bool,c:str='hello')->int:
    '''
    这是文档字符串
    :param a:
    :param b:
    :param c:
    :return:
    '''
    return 10
help(fn)