class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # property装饰器，用来将一个get方法，转换为一个对象的属性
    # 添加为property装饰器以后，我们就可以想嗲用属性一样使用get方法
    # 使用property装饰器的方法，必须和属性名是一样

    @property
    def name(self):
        print("get方法执行了~!!")
        return self._name

    @name.setter
    def name(self, name):
        print("setter方法调用了")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

p = Person('猪八戒',18)
p.name = '孙悟空'
p.age = 28

print(p.name,p.age)