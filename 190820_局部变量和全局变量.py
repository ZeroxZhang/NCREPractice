#局部变量和全局变量.py
#规则1：局部变量和全局变量是不同的变量，局部变量是函数内部的占位符，即便重名也是不同的变量。函数使用结束后，变量将被释放掉
#规则2：可以使用global保留字在函数内部使用全局变量
#规则3：局部变量为组合数据类型且未被创建为全局变量，则其等同于全局变量

#全局变量和局部变量：
n,s=10,100
def fact(n):
    s = 1
    for i in range(1,n+1):
        s = s*i
    return s
print(fact(n),s) #这里的n是全局变量10，付给了函数内局部变量s。这里的s是全局变量s，s=100


#函数内使用全局变量，使用global保留字
n,s=10,100
def fact(n):
    global s
    for i in range(1,n+1):
        s = s*i
    return s
print(fact(n),s) #这里的n是全局变量10，这里的s是被函数内计算过的s，理论上等于fact（n）

#规则3：局部变量为组合数据类型且未被创建为全局变量，则其等同于全局变量

ls = ["zerox","robbie"]
def func(a):
    ls.append(a)#这里没有声明ls是引用全局变量，但是最终结果也是在全局变量ls上增加了内容。因为没有在函数内真实创建这个ls变量。
    return
func("zhang")
print(ls)

ls2 = ["zerox","robbie"]
def func2(a):
    ls2=[]  #这里在函数内真实创建了局部变量ls2，因此为局部变量。所以在函数外增加一个元素后。全局变量ls2并没有增加。
    ls2.append(a)
    return ls2
func2("zhang")
print(ls2)

#lambda函数: lambda 变量：表达式
f = lambda x,y:x+y
print(f(1,2))