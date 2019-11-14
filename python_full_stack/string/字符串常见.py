# 培训课中主要讲的关于字符串的方法
s = "yangchengkai like fitness,never give up."
# find　字符或字符串查找，
print(s.find("fitness"))
print(s.find("k"))
# find　字符串查找时候可以指定位置
print(s.find("k",7,12))
print(s.find("k",12))
print(s.find("k",12,15))

# 判断是否是小写
print(s.islower())
#　转换为小写
print(s.lower())
# 转换为大写
print(s.upper())
# 转换为首字母大写
print(s.title())
# 形成成一个字典
c = s.maketrans("ne","12")
print(type(c))
# 按照一个字典进行翻译
print(s.translate(c))
# 按照第一个分区，分成三个，并保留like
print(s.partition("like"))
print(s.rpartition("e"))
# 划分
print(s.split("i"))
# 按照换行符切割
print("ni\n,\na new line".splitlines())
print("ni\n,\na new line".splitlines(True))
# 直接输出，不转义字符
print("%r"%"ni\n,\na new line")
# 输出字符串，转义
print("%s"%"ni\n,\na new line")