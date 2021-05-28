from pymysql import connect

'''
查询所有数据
'''
def selectall(host,user,password,database,port,query):
    conn = connect(host,user,password,database,port)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()

'''
查询一个
'''
def selectone(host,user,password,database,port,query):
    conn = connect(host,user,password,database,port)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)
    cursor.close()
    conn.close()

'''
查询几条数据
'''
def selectmany(host,user,password,database,port,query,number):
    conn = connect(host,user,password,database,port)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchmany(number)
    print(result)
    cursor.close()
    conn.close()

'''
插入数据
'''
def insertdata(host,user,password,database,port,query):
    conn = connect(host,user,password,database,port)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

'''
更新数据
'''
def updatedata(host,user,password,database,port,query):
    conn = connect(host,user,password,database,port)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

'''
删除数据
'''
def deletedata(host,user,password,database,port,query):
    conn = connect(host,user,password,database,port)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


selectall('localhost','root','root','mtesting',3306,'select * from dept')
selectone('localhost','root','root','mtesting',3306,'select * from dept')
selectmany('localhost','root','root','mtesting',3306,'select * from dept',2)

#insertdata('localhost','root','root','mtesting',3306,'insert into dept(dname) values ("研发部")')
#updatedata('localhost','root','root','mtesting',3306,"update dept set dname='后勤部' where deptno=11")
#deletedata('localhost','root','root','mtesting',3306,"delete from dept where deptno=11")


