from pymysql import connect


# 查询所有数据
def select_all(user, password, host, database, port, query):
    conn = connect(user=user, password=password, host=host, database=database, port=port)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()


# 查询一个
def select_one(user, password, host, database, port, query):
    conn = connect(user=user, password=password, host=host, database=database, port=port)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)
    cursor.close()
    conn.close()


# 查询几条数据
def select_many(user, password, host, database, port, query, number):
    conn = connect(user=user, password=password, host=host, database=database, port=port)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchmany(number)
    print(result)
    cursor.close()
    conn.close()


# 插入数据
def insert_data(user, password, host, database, port, query):
    conn = connect(user=user, password=password, host=host, database=database, port=port)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


# 更新数据
def update_data(user, password, host, database, port, query):
    conn = connect(user=user, password=password, host=host, database=database, port=port)
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.close()
    conn.close()


# 删除数据
def delete_data(user, password, host, database, port, query):
    conn = connect(user=user, password=password, host=host, database=database, port=port)
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.close()
    conn.close()


# select_all(user='root', password='root', host='192.168.1.40', database='project', port=3306, query='select * from dept')
# select_one(user='root', password='root', host='localhost', database='test', port=3306, query='select * from dept')
# select_many(user='root', password='root', host='localhost', database='test', port=3306, query='select * from dept', number=3)

# insert_data(user='root', password='root', host='localhost', database='test', port=3306, query='insert into dept(dname) values ("帅哥部")')
# update_data(user='root', password='root', host='localhost', database='test', port=3306, query="update dept set dname='123' where deptno=80")
# delete_data(user='root', password='root', host='localhost', database='test', port=3306, query="delete from dept where dname='R & D'")
