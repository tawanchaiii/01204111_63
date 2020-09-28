from datetime import date

d = int(input("d: "))
m = int(input("m: "))
y = int(input("y: "))

a = date(y, m, d)
b=  date(y, 1, 1)
delta=a-b
print(f'{delta.days+1}')