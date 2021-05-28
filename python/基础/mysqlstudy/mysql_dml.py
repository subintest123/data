from pymysql import connect

conn = connect('localhost','root','root','mtesting')

cursor = conn.cursor()

#query=r"insert into dept(deptno,dname,loc) values (50,'测试部','深圳')"
# = r"update dept set dname='研发部' where deptno=50"
query =r"delete from dept where dname='研发部'"
cursor.execute(query)
conn.commit()
cursor.close()#用完后关闭游标
conn.close()#用完后要关闭连接
