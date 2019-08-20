#函数的定义与使用.py

#阶乘函数
def fact(n):
    s = 1
    for i in range(1,n+1):
        s = s*i
    return s
a = fact(10)
print(a)

#可选参数：放在必选参数之后，必须附一个默认值。其中p为可变参数
def fact2(n1, p=1):
    j = 1
    for i in range(1,n1+1):
        j*=i
    return j//p
a = fact2(10,2)
print(a)

#多个可变参数：其中*b表示多个变量
def fact3(n2,*b):
    s = 1
    for i in range(1,n2+1):
        s*=i
    for item in b:
        s*=item
    return s
a=fact3(10,10,10)
print(a)

#返回保留值return：return可以不返回，也可以返回多个保留值，具体方法如下
def fact4(n3, p=1):
    j = 1
    for i in range(1,n3+1):
        j*=i
    return j//p,n3,p #这里就返回三个值,返回的是元祖类型
print(fact4(10,5))