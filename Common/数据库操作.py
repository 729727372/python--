import pymysql

# 建立连接
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password = "123456",
    database="moms",
    charset ="utf8",
    cursorclass= pymysql.cursors.DictCursor
)
# 创建游标
cusor = conn.cursor()

sql = "select * from class_demo"
rows = cusor.execute(sql)
print(rows)

result = cusor.fetchall()
print(result)

cusor.close()
conn.close()

