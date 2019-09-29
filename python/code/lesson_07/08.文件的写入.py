file_name="demo5.txt"

# 使用open()打开文件时必须要指定打开文件所要做的操作（读、写、追加）
# 如果不指定操作类型，则默认是 读取文件 ， 而读取文件时是不能向文件中写入的
# r 表示只读的
# w 表示是可写的，使用w来写入文件时，如果文件不存在会创建文件，如果文件存在则会截断文件
#   截断文件指删除原来文件中的所有内容
# a 表示追加内容，如果文件不存在会创建文件，如果文件存在则会向文件中追加内容
# x 用来新建文件，如果文件不存在则创建，存在则报错
# + 为操作符增加功能
#   r+ 即可读又可写，文件不存在会报错
#   w+
#   a+
# with open(file_name,'w',encoding="utf-8") as file_obj:
# with open(file_name,'r+',encoding='utf-8') as file_obj:
with open(file_name,'a',encoding='utf-8') as file_obj:
    # r = file_obj.write("aaaaaaaaaaaaaaaaaabbbbbbaa")
    # print(r)
    # content = file_obj.readline()
    file_obj.write("axzcxzczc")
    # print(content)
