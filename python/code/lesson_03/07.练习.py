# 1求100以内奇数和
i = 0;
num = 0
while i <= 100:
    if i % 2 != 0:
        num += i
    i += 1
print("100以内奇数和为%d"%num)