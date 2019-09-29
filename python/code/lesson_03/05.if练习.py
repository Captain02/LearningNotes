# 练习1：
# 编写一个程序，获取一个用户输入的整数。然后通过程序显示这个数是奇数还是偶数。
#获取用户输入的证书
# num = int(input('请输入一个任意的数字'))
#
# #显示是奇数还是偶数
# if num %2 == 0:
#     print("偶数")
# else :
#     print("奇数")
#     编写一个程序，获取用户输入的狗的年龄，然后通过程序显示其相当于人类的年龄。
#     如果用户输入负数，请显示一个提示信息
dog_age = float(input("请输入狗的年龄："))
like_persion = 0
if dog_age < 0:
    print("您输入的数值不合法")
elif dog_age <= 2:
    like_persion = dog_age * 10.5
else:
    like_persion = 2*10.5
    like_persion += (dog_age - 2) * 4

print("狗狗的年龄",like_persion)
print("狗狗的年龄%f"%like_persion)