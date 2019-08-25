#将空格分隔的文件打开
txt = open(filename).read()
ls = txt.split()
filename.close

#将特殊符号分隔的文件打开，比如逗号或者$
txt = open(filename).read()
ls = txt.split(",")
filename.close

#将列表采用空格分隔的方式，写入文件中
ls = ["中国","韩国","美国","日本"]
f = open("output.txt","w")
f.write(",".join(ls))#讲join前的字符串写入字符串的每个元素之间
f.close()
