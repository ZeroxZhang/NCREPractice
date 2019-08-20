#函数的递归与复用：
#递归的实现：需要函数+分支语句
#以阶乘为例

# #阶乘
def fact(n):
    if n==0:                     #这里是基例
        return 1
    else:
        return n*fact(n-1)          #这里是链条

print(fact(10))

#利用递归实现字符串的翻转
s = "我是你爸爸"
print(s[::-1]) #常规方法，利用字符串切片

def rvs(st):
    if st == "":
        return st
    else:
        return rvs(st[1:])+st[0]#把第一个字符串放到后面
print(rvs("我是你爸爸a"))