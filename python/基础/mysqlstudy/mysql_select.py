from pymysql import connect

#1.connect()
#2.alt+enter进行引包
#3.跟踪源代码,写入对应信息(按住ctrl键并指向方法)
conn = connect('localhost','root','root','mtesting')
#4.开游标
cursor = conn.cursor() #cursor是Cursor类的对象
#5.用参数去接收这个execute的返回
query='select * from dept'
cursor.execute(query)#执行sql语句
result = cursor.fetchall()#返回出所有的执行结果
#result = cursor.fetchmany(2)
#result = cursor.fetchone()
print(result)

cursor.close()#用完后关闭游标
conn.close()#用完后要关闭连接

