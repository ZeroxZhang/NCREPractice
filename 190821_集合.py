# #集合.py
# a = {"13",14,("python",33)}
# print(a)
#
# #通过set函数建立空集合,并拆分每个元素，无序。同时会去掉相同的元素
b = set("ZEROXZHANG")
print(b)

#集合会去掉相同的元素
c = {"python",123,"python",123}
print(c)

#集合操作符：|,-,&,^并差交补，<=或<判断子集关系。>=或>,判断包含关系

A = {"p","y",123}
B = set("pypy123")
print(A - B)
print(B - A)
print(A&B)
print(A|B)
print(A^B) #A和B的补运算，不同时在A和B中的

#集合的处理
A.add("t")
A.discard("p")#去除一个元素，如果元素不在集合中，不会报错
# # A.remove("c")#去除一个元素，如果元素在集合中，会报错
# A.clear()#清除所有元素
A.add("zerox")
A.pop()#从集合中随机取出一个元素，并更新集合，如果集合为空则产生异常
print(A)