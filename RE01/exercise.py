import re

# 匹配.com邮箱格式字符串
re01 = re.findall(r'\d+\D+\.com','邮箱：1014895593@edcu.com')
print(re01)

# 匹配密码 8-12位，数字字母下划线
re02 = re.findall(r"\w{8,12}","密码：3452_qqh")
print(re02)

# 匹配一个数字 正数 负数 整数 小数 分数1/2 百分数45%

re03 = re.findall(r'-?[0-9]+\.?/?[0-9]*%?',"34,-54,34.65,1/2,34%")
print(re03)

# 匹配一段文字中以大写字母开头的单词，注意文字中可能有 iPython 这种不算   H-base 这个算
s = 'iPython Hello H-base BIM'
re04 = re.findall(r'\b[A-Z][-_a-zA-Z]*',s)
print(re04)

# 匹配身份证号
re05 = re.findall(r'\d+',"身份证：510132111111110011")
print(re05)
re05 = re.search(r'\d{17}(\d|x)',"身份证：51013211111111001x").group()
print(re05)