# 列表的方法
stus = ['孙悟空','猪八戒','沙和尚','唐僧']
print('原列表：',stus)

#append()
#向列表的最后添加一个元素
stus.append('唐僧')
print(stus)

#insert()
#想列表的指定位置插入一个元素
#参数：
#1.要插入的位置
#2.要插入的元素
stus.insert(2,'唐僧')
print(stus)
#extend()
#使用新的序列来扩展当前序列
#需要一个序列作为参数，它会将该序列中的元素添加到当前列表中
stus.extend(['唐僧','白骨精'])
stus += ['唐僧','白骨精']
print(stus)

# clear()清空序列
# stus.clear()
print(stus)

#pop()
#根据索引删除并返回删除的元素

# result = stus.pop(2)#删除索引为2的元素
# print(result)
# result = stus.pop()#删除最后一个
# print(result)
# print(stus)

# remove()
# 删除指定的元素，如果相同值的元素有多个，只会删除第一个
stus.remove("猪八戒")
print(stus)

#reverse()
#用来反转列表
stus.reverse()
print(stus)

#sort()
#用来对列表中的元素进行排序，默认是升序排序
#如果需要降序排列，则需要传递一个reverse=True作为参数
my_list = list('asdadsadasdsadasdfdg')
my_list = [10,1,2,3,5,-1]
print("修改前",my_list)
my_list.sort(reverse=False)
print("修改后",my_list)



