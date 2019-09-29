import m
# print(m.a,m.b)
#
# # m.test2()
#
# p = m.Person()
#
# print(p.name)
#
# def test2():
#     print('这是主模块中的test2')

# 也可以只引入模块中的部分内容
#语法from 模块名 import 变量，变量..

from m import test

print(m)
# from m import * # 引入到模块中所有内容，一般不会使用

from m import *
print(_c)

# import xxx
# import xxx as yyy
# from xxx import yyy , zzz , fff
# from xxx import *
# from xxx import yyy as zz