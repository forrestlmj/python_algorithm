"""
字符串主要在day10-day11
range主要在day11提到一点
"""
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

# 中文字符三，可以被识别为数字
print("三".isnumeric())
print("了三".isnumeric())
# 其他类型字符串，判断是不是数字
print("12".isdecimal())
print("12".isdigit())

# 字符串制表,制表输出
print("id\tname\tsex\t\n1\tyck\tmale\t\n2\twsn\tfemale\t\n".expandtabs(10))

# 字符串在很多方面可以看作list操作
print("_".join("yck"))
# 字符串切片
print(s[:4])
# 中间切片
print(s[1:10])
# 隔位切片
print(s[1:10:2])
# 最后10位
print(s[-10:])

# 倒序
print(s[::-1])
#　倒序加步长
print(s[10:0:-2])


# 之后重点，生成器和迭代器，生成器与协程、迭代器与迭代器协议
i = range(10)
print(i)
c =(i for i in range(10))
a = iter(c)
print(next(a))
print(next(a))
