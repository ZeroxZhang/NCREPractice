#词云.py
import jieba
import wordcloud
from sci
f = open("政府工作报告.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(width=1000,height=700,background_color="white",max_words=20)
w.generate(txt)
w.to_file("wordcloud.png")
