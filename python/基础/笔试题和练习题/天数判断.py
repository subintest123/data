#输入某年某月某日，判断这一天是这一年的第几天
#1990-02-18
year=int(input('年份:'))
month=int(input('月份(1-12):'))
day=int(input('天(1-31):'))

total_for_months=0

months_list_value=[31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(month-1):
    total_for_months = months_list_value[i]+total_for_months

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    total=total_for_months+day+1
else:
    total=total_for_months+day

print(f'今天是整年的第{total}天')
