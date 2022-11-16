"""
    二进制文件存储
"""
import pymysql

db = pymysql.connect(host='localhost',port=3306,user='root',
                     password='qqq290810',
                     database='student',charset='utf8')
cur = db.cursor()

# with open('image.png','rb') as f:
#     data = f.read()
# try:
#     sql = "update class1 set image = %s where id = 2"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

# 获取图片
sql = "select image from class1 where id = 2"
cur.execute(sql)
data = cur.fetchone()
with open('new_image.png','wb') as f:
    f.write(data[0])

cur.close()
db.close()