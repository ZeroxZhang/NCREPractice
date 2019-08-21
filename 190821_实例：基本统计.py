#序列类型的实例：基本统计
#个数，均值，求和，方差，中位数

#第一步：获取用户输入的不确定个数输入

def getNum():
    nums = []
    iNumStr = input("请输入数字(回车退出): ")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(回车退出): ")
    return nums
#第二步：求平均值函数

def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s + num
    return s/len(numbers)

#第三步：计算方差

def dev(numbers,mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)

#第四步：中位数
def median(numbers):
    sorted(numbers)#对列表进行排序的函数
    size = len(numbers)
    if size%2 ==0:
        med = (numbers[size//2-1]+numbers[size//2])/2
    else:
        med = numbers[size/2]
    return med

n = getNum()
m = mean(n)
print("平均值:{},方差:{:.2f},中位数:{}.".format(m, dev(n,m),median(n)))