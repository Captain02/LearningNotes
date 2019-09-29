# 元组 tuple
# 元组是一个不可变的序列
# 它的操作的方式基本上和列表时一致的
# 所以你在操作元组时，就把元组当成是一个不可变的列表就ok了
#一般我们希望数据不可改变时，就是用元组，其余的其概况都是用列表

#创建元组
#是用()来创建元组
my_tuple = ()#创建了一个空元组
print(my_tuple,type(my_tuple))

# my_tuple = (1,2,3,4,5)#创建了一个5个元素的元组
# 元组是不可变对象，不能尝试为元组中的元素重新赋值
# my_tuple[3] = 10 #TypeError: 'tuple' object does not support item assignment
# print(my_tuple)

#当元组不是空元组时，括号也可以省略
#如果元组不是空元组，它里面至少要有一个
my_tuple = 10,2,0
# print(my_tuple)
# my_tuple = 10
# print(my_tuple)

#元组的解包（结构）
# 解包指的就是将元组当中每一个元素都赋值给一个变量,但是变量数和元素数要相等
a,b,c = my_tuple
print(a)

a = 100
b = 300
print(a,b)

a,b = b,a
print(a,b)

my_tuple = 10,20,30,40

#在对一个元组进行解包时，变量的数量必须和元组中的元素的数量一致
#也可以在变量前添加一个*，这样变量将会获取元组中所有剩余的元素
a,b,*c = my_tuple
print(c)
a,*b,c = my_tuple
print(b)
*a,b,c = my_tuple
print(a)
a,b,*c = [1,2,3,4,5,6,7]
print(c)
a,b,*c = "asdasdasd"
print(c)
#不能同时穿线两个或两个以上的*变量
*a,*b ,c = "adsa"
#SyntaxError: two starred expressions in assignment

