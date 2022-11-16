"""
    flags 扩展功能
"""
import re

s = """Hello
北京
"""

# 只能匹配ASCII编码
# regex = re.compile(r'\w+',flags=re.A)

# 不区分大小写
# regex = re.compile(r'[a-z]+',flags=re.IGNORECASE)

# .匹配换行
# regex = re.compile(r'.+',flags=re.DOTALL)

# ^$每一行开头结尾
# regex = re.compile(r'^北京',flags=re.MULTILINE)

# 给正则分行注释
pattern = """\w+ # hello
\s+ # 匹配换行
\w+ # 北京
"""
regex = re.compile(pattern,flags=re.X | re.I)

l = regex.findall(s)
print(l)

