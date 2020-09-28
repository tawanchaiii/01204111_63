num = list(map(int,input().split()))
re = list(map(str,input().split()))
sum = 0
for i in range(9) :
  s = re[i]
  if s == "Ea" :
    sum += num[i] - 2
  elif s == "Bi" :
    sum += num[i] - 1
  elif s == "Pa" :
    sum += num[i] 
  elif s == "Bo" :
    sum += num[i] + 1
  elif s == "DB" :
    sum += num[i] + 2
  
print(sum)