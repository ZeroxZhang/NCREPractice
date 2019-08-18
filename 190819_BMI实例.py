#BMI.py

height,weight=eval(input("请输入你的身高(m)和体重(kg),并用逗号隔开："))
bmi = weight/pow(height,2)
print("您的BMI值为：{:.2f}".format(bmi))
who,nat= "",""
if bmi<18.5:
    who,nat="偏瘦","偏瘦"
elif 18.5<=bmi<24:
    who,nat="正常","正常"
elif 24<=bmi<25:
    who,nat="正常","偏胖"
else:
    who,nat="肥胖","肥胖"
print("您的BMI指数在国际上为：{}，在国内上为：{}".format(who,nat))