#文本进度条实例.py

#不刷新
import time
scale = 10
print("------执行开始------")
for i in range(scale+1):
    a = "*" * i
    b = "." * (scale-i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------执行结束------")

#单行动态刷新
for i in range(101):
    print("\r{:3}%".format(i),end="")#end表示光标不换行，停留在当前字符串后。冒号n表示从换行后第几个字符开始显示
#     time.sleep(0.05)

#完整的文本进度条
import time
scale = 50
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in range(scale+1):
    a = "*" * i
    b = "." * (scale-i)
    c = (i/scale)*100
    dur = time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.1)
print("\n","执行结束".center(scale//2,"-"))
