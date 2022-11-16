import re

# 目标字符串
s = "Alex:1994,Sunny:1996"
pattern = r'(\w+):(\d+)'

# 如果正则表达式有子组,findall则只能获取到子组的内容
# re 模块
list01 = re.findall(pattern,s)
print(list01)

# compile对象调用findall
regex = re.compile(pattern)
print(regex.findall(s,0,12))

# 按正则表达式切割
l = re.split(r'[:,]',s)
print(l)

# 替换
s = re.sub(r':','-',s)
print(s)

