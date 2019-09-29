age = int(input('请输入你的年龄'))
if age > 200:
    print('或者可真没劲呢')
elif age > 100:
    print('你也是老大不小了')
elif age >= 60:
    print("你已经退休了")
elif age >= 30:
    print("你已经是中年了")
elif age >= 18:
    print("你已经成年了")
else:
    print("你还是个小孩")