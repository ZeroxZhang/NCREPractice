#字符串的类型及操作.py

#字符串切片高级用法
string = "字符串切片的高级用法"
print(string[0:9:2])#其中2是步长。s[N:M]表示对字符串s的切片操作，从N到M，但不包含M


print(string[::-1])#用来逆序打印
#转义符:反斜杠\
print("这里有个双(\")引号")#转义符用来表达特定字符的本意
"\b"#表示回退
"\n"#表示换行
"\r"#表示回车

#字符串操作符
print("字"+"符串")
print(2*"字符串 ","字符串"*2)
print("字" in "字符串")

#输入数字，返回星期几
# weekstr = "一二三四五六日"
# weekid = eval(input("请输入数字（1-7):"))
# print("星期",weekstr[weekid-1])

#字符串函数
len("str")
str(2.34)
hex(425) # 能够将整数x输出对应的小写16进制字符串
oct(542) # 能够将整数x输出对应的小写8进制字符串
# chr(u) #u为Unicode编码，返回其对应的字符
# ord(c) #c为字符，返回对应的Unicode编码
print(ord("→"))
for i in range(12):
    print(chr(9800+i),end="\n")

#字符串处理方法
"adfgd".upper()#变大写
"ABCSD".lower()#变小写
print("s,d,dg,d,s,te,d,tggd".split(","))#字符串的split方法，将字符串按照某个字符切割，并返回列表
print("an appele a day".count("a"))#统计字符串中某个字符的数量
print("python".replace("y","yy"))#替换字符串的某个字符为新的泽富
print("python".center(20,"_"))#将字符串居中，需要设置宽度和左右的字符
print("s.python.".strip(".s"))#将字符串中的某些字符去掉，可以一起写，不用分隔
print(",".join("12345"))#把逗号放在某一个字符后面
print("{}:计算机{}的CPU占用率为{}%".format("备注","zerox","10"))#{}在字符串中表示“槽”，用来占位，与后面format的变量一一对应