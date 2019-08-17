#每天进步1‰，一年进步多少？每天退步1‰，一年退步多少？
dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("向上:{:.2f}\n向下：{:.2f}".format(dayup,daydown))
