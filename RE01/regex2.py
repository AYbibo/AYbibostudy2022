"""
    生成match对象的函数
"""

import re

s = '今年是2022年，建国73周年'
pattern = r'\d+'

# 返回迭代对象
it = re.finditer(pattern,s)
for i in it:
    print(i.group())  # 生成match对象，通过.调用方法<re.Match object; span=(3, 7), match='2022'>

# 完全匹配
m = re.fullmatch(r'\S+',s)
print(m.group())

# 匹配开始位置
m = re.match(r'\w+',s)
print(m.group())

# 匹配第一个符合内容
m = re.search(r'\d+',s)
print(m.group())

