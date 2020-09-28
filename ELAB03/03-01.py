n = 1
a = list()
while n!= 0 :
  n = int(input())
  if(n!=0):
    a.append(n)
for i in range(len(a)-1,-1,-1):
  print(f"{a[i]}",end = " ")