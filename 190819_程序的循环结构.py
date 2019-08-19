#程序的循环结构.py
#遍历循环

for i in range(50):
    print("\r{}".format(i+1),end="")

for n in range(6,21,3): #从10到20，步长为3，不包含21
    print(n)

for c in "PYTHON":
    print(c,end=",")

#列表遍历循环
for item in [124,"PYH","xer"]:
    print("\n{}".format(item),end="。")

# #文件的遍历
# for line in file:#file替换成具体的文件路径
#     print(line)

#无限循环：反复执行语句块，直到条件不满足的时候停止
a = 5
while a <10:
    a +=1
    print(a)
#循环控制的保留字
#break:跳出并结束当前循环，并运行循环之后的语句
#continue：跳出当次循环，继续运行后续循环
#break 和 continue都可以用在for 和 while循环中

for t in "PYTHON":
    if t =="T":
        continue
    print(t,end="）")
for t2 in "PYTHON":
    if t2 == "T":
        break
    print(t2,end=",")

s="PYTHON"
while s!="":
    for c in s:
        print(c,end="")
        if c=="T":
            break
    s = s[:-1]

#for in else,while else。else是可以用来控制循环结构