# 和元组一样,列表也是在新建,访问,遍历上一模一样
# 列表其实是数据结构中的链表

# 1.新建
emp = []
emp = [7788, 'caichang', 'teacher', 200, None, True, '老王']
# emp=[[1,'张飞','屠夫'],[2,'刘备','卖草鞋'],[3,'关羽','保安'],[4,'孙尚香','大小姐']]

# 访问
print(emp[2])  # 正向访问
print(emp[-5])  # 反向访问
print(emp[1:4])  # 从1开始切,切到4但不包含4  [1,4)  这个最常用
print(emp[1:-3])
print(emp[-6:4])
print(emp[-6:-3])

print(emp[3:])
print(emp[:3])

# 遍历
emp = [7788, 'caichang', 'teacher', 200, None, True, '老王']
for i in range(len(emp)):
    print(emp[i])

emp = [[1, '张飞', '屠夫'], [2, '刘备', '卖草鞋'], [3, '关羽', '保安'], [4, '孙尚香', '大小姐']]
for i in range(len(emp)):
    for j in range(len(emp[i])):
        print(emp[i][j])

#列表和元组不一样的地方是,因为列表是链表结构,所以它有自己的特殊方法,而上班后这些特殊方法才是重点

emp = [7788, 'caichang', 'teacher', 200, None, True, '老王']
emp.append('测试部')
print(emp)
emp.append((1,'凤姐','同事'))
print(emp)
emp.insert(2,'男')
print(emp)

emp.pop()
print(emp)

emp.pop(5)
print(emp)

emp.remove('老王')
print(emp)

emp.insert(3,200)
print(emp)

emp.remove(200)
print(emp)

emp=[32,15243,5,41,12,43234,423,43,1414]
emp.sort()
print(emp)

emp.sort(reverse=True)
print(emp)

emp.reverse()
print(emp)

print(emp.index(43))

emp.clear()
print(emp)

