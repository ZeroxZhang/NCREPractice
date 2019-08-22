#文件的操作.py
#文件都是由二进制存储在计算机中，有统一编码的（如UTF-8）编码的，叫文本文件。没有统一编码的，由特定格式存储的01文件，叫做二进制文件，例如png，avi等。

#以文本形式打开文件:
tf = open("中国.txt","rt")
print(tf.readline())
tf.close()

#以二进制形式打开文件
tb = open("中国.txt","rb")
print(tb.readline())
tb.close()

#打开文件：注意：在windows下的文件路径是反斜杠\，但是在python中反斜杠有别的含义，所以要改成常规斜杠/，否则会报错。
a = open("E:/NCREPractice/中国.txt")
print(a.readlines())
a.close()

#文件的模式
f = open("中国.txt") # - 文本形式、只读模式、默认值
f = open("中国.txt","rt") # - 文本形式、只读模式、同默认值
f = open("中国.txt", "w") # - 文本形式、覆盖写模式
f = open("中国.txt", "a+") # - 文本形式、追加写模式+ 读文件
f = open("2.txt", "x") # - 文本形式、创建写模式
f.close()
f = open("中国.txt", "b") # - 二进制形式、只读模式
f = open("中国.txt","wb") # - 二进制形式、覆盖写模式