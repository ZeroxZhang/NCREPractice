#习题1：
import jieba
s = "中国特色社会主义进入新时代，我国社会主要矛盾已经转化为人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾。"
n = len(s)
m = len(jieba.lcut(s))
print("中文字符数为{}，中文词语数为{}。".format(n, m))

#习题2：0x4DC0 是一个十六进制数，它对应的 Unicode 编码是中国古老的《易经》六十四卦的第一卦，
# 请输出第 51 卦（震卦）对应的 Unicode 编码的二进制、十进制、八进制和十六进制格式。
print("二进制{0:b}、十进制{0:d}、八进制{0:o}、十六进制{0:x}".format(0x4DC0+50))