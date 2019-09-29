#range()是一个函数，可以用来生成一个自然数的序列
r = range(5)
# print(list(r))#[0, 1, 2, 3, 4]
r = range(1,10,2)
# print(list(r))#[1, 3, 5, 7, 9]
r = range(10,0,-1)
# print(list(r))#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#改函数需要三个参数
#1.起始位置(可以省略，默认是0
#2.结束位置
#3.步长(可以省略，默认是1)

#通过range()可以创建一个执行指定次数的for循环
#for()循环除了创建方式以外，其余的都和while一样，
#包括else、包括break continue都可以在for循环中使用，并且for循环使用也更加简单
#将之前使用while循环做的练习，再使用for循环完成一次！
for i in  range(30):
    print(i)