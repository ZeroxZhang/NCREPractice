#随机数.py
#给定种子10，那么每次出来的随机数是相同的。
import random
# random.seed(10)
# a = random.random()
# random.seed(10)
# b = random.random()
# print(a==b)

#不给定种子，每次程序默认选择当前的系统时间为种子
c = random.random()
print(c)

#整数随机数
print(random.randint(100,1000))
#randrange(m,n,k)，在m和n之间以100为步长的数。
print(random.randrange(10,1000,100))
#uniform(a,b)，生成一个a，b之间的随机小数
print(random.uniform(0,100))
#random.choice([]),在序列中随机选取一个元素
print(random.choice(["d",2,3.4,"sd"]))
#random.shuffle。讲一个序列元素随机排列，并返回随机排列后的序列
s=["sd",43,32.3,"ze","1.3"]
random.shuffle(s)
print(s)