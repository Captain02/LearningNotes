print('异常出现前')
l = []
try:
    # print(c);
    print(10/0)
except NameError:
    # 如果except后不跟任何的内容，则此时它会捕获到所有的异常
    # 如果在except后跟着一个异常的类型，那么此时它只会捕获该类型的异常
    print("出现NameError异常")
except ZeroDivisionError:
    print('出现 ZeroDivisionError 异常')
finally:
    print("无论是否有异常这个语句都会执行！")
print("异常出现后")
