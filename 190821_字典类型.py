#字典类型

#定义一个字典
dict = {"CN":"Beijing","FR":"PRS","USA":"WDC","JP":"TKO"}
#判断某个键是否在字典中
print("CN" in dict)
#调用字典中所有的键和值
print(dict.keys(),dict.values())
#获得某个键的值，如果没有这个键，则返回一个预设的默认值
print(dict.get("FR"))#这个会返回Paris
print(dict["FR"])#常规查询键对应的值
print(dict.get("巴西","巴西利亚"))#这个会返回巴西利亚
#取出并删除某个键值对
dict.pop("USA")
#从字典中随机获取一个键值对
print(dict.popitem())
#给字典新增键值对
dict["BRA"]="BRAZIL";dict["KOREA"]="SOUL"
print(dict)
