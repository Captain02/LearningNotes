# 创建一个循环来控制图形的高度
# 循环嵌套时，外层循环每执行一次，内循环执行一圈
i = 0
while i < 5:
    # 创建一个内循环来控制图形的宽度
    j = 0
    while j <5 :
        print("* ",end=" ")
        j += 1
    print()
    i += 1