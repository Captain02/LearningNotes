#返回值，返回值就是函数执行以后返回的结果
#可以通过return来指定函数的返回值
#可以之间所使用函数的返回值，也可以通过一个变量来接受函数的返回值
def sum(*nums):
    #定义一个变量，来保存结果
    result = 0
    for n in  nums:
        result += n
    print(result)
sum(123,234,345)

#return 后边跟什么值，函数就会返回什么值
# return后面可以跟任意的对象，返回值甚至可以是一个函数
def fn():

    def fn2():
        print('hello')
    return fn2
r = fn()
print(r)

# 如果仅仅写一个return 或者不写return 则相当于return None
def fn2():
    a = 10
    return
#在函数中，return后的代码都不会执行，return一旦执行函数自动结束
def fn3():
    print('hello')
    return
    print(213)
