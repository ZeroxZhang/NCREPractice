# 序列.py
#基础知识：
'''序列类型包含了元祖和列表，是具备先后关系的一组数据。'''

#1:序列类型操作实例
    #实例1：反向排序
ls = ["python","zerxo",23,"666",".com"]
print(ls[::-1])
string = "zerox"#因为字符串也是序列类型，所以也可以用：：-1来取反
print(string[::-1])

    #实例2：常用函数
print(len(ls))#元素个数
print(ls.index(23))#找到序列中第一次出现23的序号
print(ls.count("666"))#返回序列中出现666的次数
print(max(string))#如果序列中是字符串，则max函数和min函数是按照字母排序

#2. 元祖类型
    #实例1：常规需要使用()来定义元祖，但是可以不用小括号。
yuanzu1 = "zerox","robbie","zhang",666
yuanzu2 = ("zerox","robbie","zhang",666)
print(yuanzu1==yuanzu2)#返回的是True
    #元祖类型继承了全部序列操作，一旦生成，不可改变
print(yuanzu2[::-1])
    #元祖里的元祖,切片的时候，可以对里面元素持续切片
yuanzu3 = (yuanzu2,yuanzu1)
print(yuanzu3[-1])#返回元祖里的后面的元素，也就是元祖1
print(yuanzu3[-1][-2][-3])#返回元祖1的倒数第二个元素zhang的倒数第三个字符a

#3. 列表
    #实例1：列表的操作
liebiao = ["dog","cat","tiger",1024]
liebiao[1:2]=[1,2,3,4]#把列表的第二个元素，赋值为新的列表
# print(liebiao)
del liebiao[::3]#删除列表中以3为步长的子序列，也就是dog，3,1024
# print(liebiao)
liebiao = liebiao*3
# print(liebiao)
    #实例2：列表的操作方法
liebiao.append("monkey")
# liebiao.clear()
liebiao2 = 2*liebiao.copy()
liebiao2.insert(3,"snake")#在列表中第3位置后面！切记是后面加入元素
liebiao2.pop(4)#在列表中取出第4位的元素并删除
# liebiao2.remove(1024)#将列表中出现的第一个dog删除掉
liebiao2.reverse()#讲列表每一个元素反转
print(liebiao,liebiao2)