import re

secretcode = "asdasdxxixxasj5dxxlovexxfk34dasxxyouxx"

# .的使用，(不能匹配换行符 '\n')
# .就是占位符
a = 'xy123'
b = re.findall('x...',a)
print(b)


# *的使用 匹配任意字符 0次或者无限次
a = 'xyxy123'
b = re.findall('x*',a)
print(b)


# ?的使用 匹配任意字符0次或者1次
a = 'xy123'
b = re.findall('x?',a)
print(b)

# .* 贪心算法
b = re.findall('xx.*xx',secretcode)
print(b)

# .*? 非贪心
b = re.findall('xx.*?xx',secretcode)
print(b)

# （）括号内的数据作为返回结果
b = re.findall('xx(.*?)xx',secretcode)
print(b)

# \d+ 匹配纯数字
a = "jhdjaskdhj439878293jfkl"
b = re.findall('(\d+)',a)
print(b)