a = list(map(int,input("Input: ").split()))
a.sort()
s = list()
for i in range(len(a)) :
  for j in range(i+1,len(a)) :
    if not (a[i]+a[j]  in s )  and (abs(a[i]+a[j])  <= 100) : 
      s.append(a[i]+a[j])
s.sort()
for i in s :
  print(f"{i} ",end = '')