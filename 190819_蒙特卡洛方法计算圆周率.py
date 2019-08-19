#蒙特卡洛方法计算圆周率.py
import random
from time import perf_counter
DARTS = 2000*2000
hits = 0.0
start = perf_counter()
for i in range(1,DARTS+1):
    x,y = random.random(),random.random()
    distance = pow(x**2 + y**2,0.5)
    if distance <= 1.0:
        hits = hits+1
pi = 4*(hits/DARTS)
print("圆周率={}".format(pi))
print("程序运行时间是：{:.5f}s".format(perf_counter()-start))