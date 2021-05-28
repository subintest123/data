#只要你给我业务,我函数的表现形式可以是4种,至于你采用哪一种,没有定论
#完全是根据你业务的具体性来决定

def total():
    total = 0
    for i in range(1,101,1):
        total = total + i
    print(total)

total()


def total2(start,end,step=1):
    total = 0
    for i in range(start,end,step):
        total = total + i
    print(total)
total2(1,101,1)


def total3():
    total = 0
    for i in range(1,101,1):
        total = total + i
    return total

t=total3()
print(t)


def total4(start,end,step=1):
    total = 0
    for i in range(start,end,step):
        total = total + i
    return total

t2=total4(1,101)
print(f'总数为:{t2}')