a = 'abc'+'hahah'+'哈哈'
print(a)

b = 'hello %s'%'孙悟空'
print(b)

b = "hello %s 你好 %s"%("tom","孙悟空")
print(b)

b = "hello %3.5s" %"33"
print(b)

b = "hello %s"%123.456
print(b)

b = "hello %.2f"%123.456
print(b)

b = "hello %d" %123.456
print(b)

c = f"hello {a} {b}"
print(f"a = {a}")
print(f"a = {c}")