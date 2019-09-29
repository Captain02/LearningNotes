# 打开文件
file_name = 'hello/demo.txt'
#调用 open()来打开文件
file_obj = open(file_name)
#当我们读取了文件对象以后，所有对文件的操作都应该通过对象来记性
#读取文件中的内容
#read()方法，用来读取文件中的内容，它会将内容全部保存为一个 字符串返回
# cotent = file_obj.read()
# print(cotent)
#关闭文件
#调用close()方法来关闭文件
# file_obj.close()

#with ... as语句
with open(file_name) as file_obj:
    #在with语句中可以直接使用file_obj来操作文件操作
    #此时这个文件只能在with中使用，一旦with结束则文件会自动close()
    print(file_obj.read())

file_name = "hello.txy"
try:
    with open(file_name) as file_obj:
        print(file_obj.read())
except FileNotFoundError:
    print(f'{file_name} 文件不存在')