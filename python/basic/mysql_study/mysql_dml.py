from pymysql import connect

conn = connect(user='root',
               password='root',
               host='localhost',
               database='test',
               port=3306)
# print(conn)
cursor = conn.cursor()
# print(cursor)

# # 插入
# query = r"insert into dept(deptno,dname,loc) values(90,'幼儿园','深圳')"
# cursor.execute(query)

# # 更新
# query = r"update dept set deptno='80' where dname='技术部'"
# cursor.execute(query)

# # 删除
# query = r"delete from dept where dname='美女部'"
# cursor.execute(query)

conn.commit()
cursor.close()
conn.close()
