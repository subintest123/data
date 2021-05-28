#100以内能被3整除但不能被5整除的数

lists=[]
for i in range(1,101):
    if i%3==0 and i%5!=0:
        lists.append(i)
print(f'#100以内能被3整除但不能被5整除的数为:{lists}')
