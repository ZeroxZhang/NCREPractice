#文件的操作.py
a = open("hamlet.txt")
s = a.readlines(10)#读出前10行，并形成列表
print(s)
a.close()

#文件的全文本操作：方法一
fname = input("请输入文件名称：")+".txt"
fo = open(fname,"r")
txt = fo.read()
    #对全文txt进行处理。一次读入，统一处理
fo.close()

#文件的全文本操作：方法二
fname = input("请输入文件名称：")+".txt"
fo = open(fname,"r")
txt = fo.read(2)
while txt !="":
    #对全文txt进行处理。
    txt = fo.read(2) #分阶段按数量读入，逐步处理的思路
fo.close()

#文件的逐行操作：方法一
fname = input("请输入文件名称：")+".txt"
fo = open(fname,"r")
for line in fo.readlines():
    print(line)
fo.close()

#文件的逐行操作：方法二
fname = input("请输入文件名称：")+".txt"
fo = open(fname,"r")
for line in fo:  #使用for line in fo，不加任何方法，可以对文本进行分行读入，逐行处理。
    print(line)
fo.close()