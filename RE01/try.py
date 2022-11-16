import re

re01 = re.findall('ab','adgetwab')
print(re01)

re02 = re.findall('com|cn','https://www.bilibili.com/video/BV1Jv411j7oc?p=351&vd_source=a10f019f38e1d735d5b648c227ef00d6.cn')
print(re02)

re03 = re.findall('张.丰','张三丰，张思丰，张\n丰')
print(re03)

re04 = re.findall('[aei ou0-9]','hello world,aou,5738')
print(re04)

re05 = re.findall('[^aei ou0-9]','hello world,aou,5738')
print(re05)

re06 = re.findall('^0Jame,','0Jame,hello,Jame')
print(re06)

re07 = re.findall('1Jame$','Jame,hello,1Jame')
print(re07)

re08 = re.findall('wo*','woooooo~w')
print(re08)

re09 = re.findall('[0-9]*',"I'm 18")
print(re09)

re10 = re.findall('[A-Z][a-z]*',"How are you? Fine Jame")
print(re10)

re11 = re.findall('[A-Z][a-z]+',"HOW are you? Fine Jame")
print(re11)

re12 = re.findall('-?[0-9]+',"167 -28 29 -8")
print(re12)

re13 = re.findall('[^ ]+',"Port-9 Error #404# %@STD")
print(re13)

re14 = re.findall('[0-9]{11}',"13981942602")
print(re14)

re15 = re.findall('张.{3}',"张而扩大，张端口")
print(re15)

re15 = re.findall('张.{2,3}',"张而扩大，张端口")
print(re15)

re16 = re.findall('[0-9]{6,11}',"QQ:10895593")
print(re16)

re17 = re.findall('\D{1,5}',"PORT:9999,80")
print(re17)

re18 = re.findall('\w+',"server_port = 阿里嘎多")
print(re18)

re19 = re.findall('\w+\s+\w+',"hello    world")
print(re19)

re20 = re.findall('\Ahello',"hello    world")
print(re20)

# 前面要加r才行
re21 = re.findall(r'\Bis\b',"This is a test")
print(re21)

re22 = re.findall(r'\b\d+\b',"123 68 Num007")
print(re22)

re23 = re.findall('-?\\d+\\.*\\d*',"12 -36 28 1.35 -3.8")
print(re23)

# python遇到 \ 就想转义，但python没有 \$ 这个含义
re23 = re.findall('\$\d+',"日薪：$100")
print(re23)
re23 = re.findall('\\$\\d+',"日薪：$100")   # \\$\\d+ 经过python转义成 \$\d+ 然后传入正则表达式
print(re23)

s = r'hello \n world'
print(s)

re24 = re.findall('ab{3,5}?',"abbbbbbb")   # \\$\\d+ 经过python转义成 \$\d+ 然后传入正则表达式
print(re24)

s = '[花千骨],[好气哦],[新还珠格格],[十多天]'
re25 = re.findall(r'\[.+?]',s)
print(re25)

# 匹配.com邮箱格式字符串
# 匹配密码 8-12位，数字字母下划线
# 匹配一个数字 正数 负数 整数 小数 分数1/2 百分数45%
# 匹配一段文字中以大写字母开头的单词，注意文字中可能有 iPython 这种不算   H-base 这个算

re26 = re.search(r'(王|李)\w{1,3}','王者荣耀').group()
print(re26)

re27 = re.search(r'(https|http|ftp|file)://\S+',"https://www.baidu.com").group(1)
print(re27)

re28 = re.search(r'(?P<pig>ab)+','abababab').group('pig')
print(re28)


