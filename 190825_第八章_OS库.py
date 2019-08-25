#OS库.py

import os
print(os.path.abspath("output"))#返回一个文件的绝对路径
print(os.path.isfile("hamlet.txt"))#判断是否存在文件
print(os.path.isdir("D:/NCREPractice"))#判断是否存在目录
print(os.path.getsize("threekingdoms.txt"))#获得文件大小
#os.system("E:/NCREPractice/threekingdoms.txt")#打开文件
print(os.getlogin())#获取当前系统的登录
print(os.cpu_count())#返回cpu核心数
print(os.urandom(10))#获得n个字节长度的随机字符串