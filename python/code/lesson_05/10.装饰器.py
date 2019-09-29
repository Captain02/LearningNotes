# 创建几个函数
def add(a, b):
    '''
    求任意两个数的和
    :param a:
    :param b:
    :return:
    '''
    r = a + b
    return r


def mul(a, b):
    '''
    求任意两个数的积
    :param a:
    :param b:
    :return:
    '''
    r = a * b
    return r


# 希望函数可以在计算前，打印开始计算，计算结束后打印计算完毕
# 我们可以直接通过修改函数中的代码来完成这个需求，但是会产生以下一些问题
# 1.如果要修改的函数过多，修改起来比较麻烦
# 2.并且不方便后期的维护
# 3.并这样做会违反开闭原则(OCP)
#   程序的设计，需要开发对程序的扩展，需要关闭对程序的修改

r = add(123, 345)


# print(r)

# 我们希望在不修改原函数的情况下，来对函数进行扩展
def fn():
    print('我是fn函数....')


def fn2():
    print('函数开始执行！！')
    fn()
    print('函数执行完毕！！')


def new_add(a, b):
    print('计算开始~~~')
    r = add(a, b)
    print('计算结束~~~')
    return r


r = new_add(111, 222)
print(r)


# 上边的方式，已经可以在不修改源代码的情况下对函数进行扩展了
#   但是，这种方式要求我们每扩展一个函数就要手动创建一个新的函数，实在是太麻烦了
#   为了解决这个问题，我们创建一个函数，让这个函数可以自动的帮助我们生产函数
def begin_end(old):
    '''
    用来对其他含糊进行扩展，是其他函数可以再执行前打印开始执行，执行后打印执行结束

    参数：
    old 要扩展的函数对象
    :param old:
    :return:
    '''

    # 创建一个新函数
    def new_function(*args, **kwargs):
        print("开始执行~~~")
        # 调用被扩展的函数
        result = old(*args, **kwargs)
        print('执行结束~~~~')
        # 返回函数的执行结果
        return result

    # 返回新函数
    return new_function


f = begin_end(fn)
f2 = begin_end(add)
f3 = begin_end(mul)

r = f()
r = f2(123, 456)
r = f3(123, 456)
print(r)


# 想begin_end这种函数我们就称它为装饰器
# 通过装饰器，可以再不修改原来函数的情况下来对函数进行扩展
# 在开发中，我们都是通过装饰器来扩展函数的功能的
# 在定义函数时，可以通过@装饰器，来使用这种

def fn3(old):
    '''
    用来对其他函数进行扩展，使其他函数可以在执行前打印开始执行，执行后打印执行结束

    :param old:要扩展的函数对象
    :return:
    '''

    # 创建一个新的函数
    def new_function(*args, **kwargs):
        print('fn3装饰~开始执行~~~~')
        # 调用被扩展的函数
        result = old(*args, **kwargs)
        print('fn3装饰~执行结束~~~~')
        # 返回函数的执行结果
        return result

    # 返回新函数
    return new_function


@fn3
@begin_end
def say_hello():
    print('大家好~~~~')


say_hello()
