"""
    match 对象属性
"""
import re

pattern = r'(ab)cd(?P<pig>ef)'
regex = re.compile(pattern)
obj = regex.search('abcdefghi')  # match对象

# 属性变量
print(obj.pos)  # 目标字符串开始位置  0
print(obj.endpos)  # 目标字符串结尾位置  9
print(obj.re)  # 正则表达式
print(obj.string)  # 目标字符串
print(obj.lastgroup)  # 最后一组组名  pig
print(obj.lastindex)  # 最后一组序列号 2

# 属性方法
print(obj.span())  # 匹配内容在字符串中的位置
print(obj.start())
print(obj.end())
print(obj.groupdict())  # 有组名的组
print(obj.groups())  # 所有子组
print(obj.group(2))

