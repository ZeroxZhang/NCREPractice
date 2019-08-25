#文件的写入.py
fo = open("output.txt","w+")
ls = ["CN","US","FRE"]
fo.writelines(ls)#这个时候指针在文件的最后，如果这个时候再去遍历每一行，是没有内容的。这个时候需要加一行
fo.seek(0)#让指针回到文件的最前方。1表示光标当前位置，2表示文件最后。
for line in fo:
    print(line)
fo.close()

#AutoTraceDraw.py
import turtle as t
t.title('自动轨迹绘制')
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)
#数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")
    datals.append(list(map(eval, line.split(","))))
f.close()
#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.rt(datals[i][2])
    else:
        t.lt(datals[i][2])