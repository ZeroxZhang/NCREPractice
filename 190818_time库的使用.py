#time库的使用.py
import time
time.time()
print(time.ctime())#获取人类易读的时间格式
print(time.gmtime())#其他程序可以利用的时间格式

#strftime(tpl,ts)，tpl是格式化模板字符串，用来定义输出效果，ts是计算机内部时间类型变量
t = time.gmtime()
print(time.strftime("%b %a %H %Y-%m-%d %H:%M:%S",t))#所有的控制符都是%+字母

# #strptime(时间字符串，时间格式）
# timeStr = "2019-08-10 12 12:55:23"
# time.strptime(timeStr,"%Y-%m-%d %H:%M:%S")

#程序计时
a = print(time.perf_counter())#perf_counter函数返回一个CPU级别的精确时间技术支持，单位为妙。由于这个计数值起点不确定，连续调用差值才有用

#休眠函数
def wait():
    time.sleep(3.3)#休眠3.3秒后退出