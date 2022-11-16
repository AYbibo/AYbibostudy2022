"""
打开exc.txt 根据服务器型号输出地址

1、根据输入的端口名称找到对应的段落
2、在该段落匹配address
"""
import re

port = input('端口:')
file = open('exc.txt','r',encoding='UTF-8')
while True:
    data = ''
    for line in file:
        if line == '\n':
            break
        data += line
    if data == '':
        print('没有该端口')
        break
    obj = re.match(port,data)  # 匹配开始位置
    if obj:
        # pattern = r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'
        pattern = r'((\d{1,3}\.){3}\d{1,3}/\d+)|Unknown'
        obj = re.search(pattern,data)
        print(obj.group())
        break


