#二分支结构.py

#简单的二分支判断结构
# guess = eval(input("请输入一个数字"))
# print("猜对了" if guess == 99 else "猜错了")

#异常处理
try:
    num = eval(input("请输入一个数字："))
    print("它的平方是：",num**2)
except:
    print("输入有误，请重新输入")
else:#如未发生异常，继续执行else
    print(num)
finally:#无论如何，都要执行这句
    print(num*2)
