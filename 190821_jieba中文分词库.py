#jieba.py
import jieba
#精确模式
string = "中华人民共和国是一个伟大的国家"
print(jieba.lcut(string))
#全模式
print(jieba.lcut(string,cut_all=True))
#搜索引擎模式
print(jieba.lcut_for_search(string))
#增加词库
jieba.add_word("扩列")

