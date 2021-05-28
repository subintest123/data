from pymysql import connect

conn = connect(user='root',
               password='root',
               host='localhost',
               database='test',
               port=3306)
# print(conn)
cursor = conn.cursor()
# print(cursor)
# 查询
cursor.execute('select * from emp')
# result = cursor.fetchall()
# result = cursor.fetchmany(3)
result = cursor.fetchone()
print(result)


cursor.close()
conn.close()
