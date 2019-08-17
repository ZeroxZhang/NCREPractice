#问题1：每天进步1‰，一年进步多少？每天退步1‰，一年退步多少？
dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("向上:{:.2f}\n向下：{:.2f}".format(dayup,daydown))

#问题2：引入变量
dayfactor = 0.05
dayup = pow(1+dayfactor,365)
daydown = pow(1-dayfactor,365)
print("向上:{:.2f}\n向下：{:.2f}".format(dayup,daydown))

#问题3：工作日每天进步1%，周末每天退步1%
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [0,6]:
        dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)
print(dayup)

#问题4：工作日模式下，需要努力多少，才能跟每天进步1%的效果一样？
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [0,6]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor +=0.001
print("工作日的努力参数应该为：{:.3f}".format(dayfactor))
