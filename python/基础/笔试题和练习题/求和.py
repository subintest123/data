# 1+2+3+.....+100的和

total = 0
for i in range(1, 101):
    total = total + i  # total+=i也可以
    # print(total)
print(f'1+2+3+.....+100的和为:{total}')
