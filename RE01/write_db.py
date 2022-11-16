"""
    write_db 写操作
"""
import pymysql
db = pymysql.connect(host='localhost',port=3306,
                     user='root',password='qqq290810',
                     charset='utf8',database='student')

cur = db.cursor()

try:
    # name = input('name:')
    # age = input('age:')
    # score = input('score:')
    # 注意'%s'
    # sql = "insert into class1 (name,age,score) values ('%s',%d,%f)" % (name,age,score)

    # 列表直接给values传值，不用加‘’了
    # sql = "insert into class1 (name,age,score) values (%s,%s,%s)"
    # cur.execute(sql,[name,age,score])

    # 修改
    # sql = "update interest set price = 11800 where name = 'Didi'"
    # cur.execute(sql)

    # 删除
    sql = "delete from class1 where score < 80 limit 1"
    cur.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()  # 退回到commit执行之前的数据库
    print(e)

cur.close()
db.close()