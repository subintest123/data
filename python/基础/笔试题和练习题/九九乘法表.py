#九九乘法表
# 1*1=1
# 1*2=2   2*2=4
# 1*3=3   2*3=6   3*3=9
# ....
# 1*9=9   2*9=18 ......  9*9=81

#i*j=i*j
for i in range(1, 10):
    for j in range(1, i+1):
        #print('{}x{}={}\t'.format(j, i, i*j), end='')
        print(f'{j}x{i}={j*i}')
    print()



print('\n'.join(['\t'.join(['{}*{}={}'.format(i, j, i * j) for j in range(1, i + 1)]) for i in range(1, 10)]))


