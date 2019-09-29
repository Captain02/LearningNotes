#集合
#使用{}来创建集合
s = {10,3,5,1,2,1,2,3,1,1,1,1}
print(type(s))# <class 'set'>

s = set()
#可以通过set()来将序列和字典转换为集合
s = set([1,2,3,4,5,6,7,1,1])
print(s)
s = ('hello')
print(s)
#创建集合
s = {'a','b',1,2,3,1}
print(s)
#使用in和not in来检查集合中的元素
print('c' in s)

#使用len()来获取集合中元素的数量
print(len(s))

# add()向集合中添加元素
s.add(10)
s.add(30)
print(s)

# update()将一个集合中的元素添加到当前集合中
# update()可以传递序列或者字典作为参数，字典只会使用键
s2 = set('hello')
s.update(s2)
print(s)
s.update({10:"ab",20:"bc"})
print(s)

# pop随机删除并返回一个集合中的元素
result = s.pop()
print(result)

# remove()删除集合中指定的元素
s.add(100)
print(s)
s.remove(100)
print(s)

# # clear()清空集合
# s.clear()
# print(s)

# copy()对集合进行浅复制
b = s.copy()
print(b,type(b))
