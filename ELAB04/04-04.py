n = int(input("n: "))

for i in range(n) :
  for j in range(i) :
    print(" ",end='')
  for j in range(9 + (n-3)*2 - 2*i) : 
    print("=",end='')
  print("\n",end='')
  for j in range(i) :
    print(" ",end='')
  for j in range(9 + (n-3)*2 - 2*i) :
    x =  9 + (n-3)*2 - 2*i
    if (j == 0 or j == x-1) :
      print("=",end='')
    else :
      print("#",end='')
  print("\n",end='')

for i in range(n+1) :
  print(" ",end='')
print('=')


for i in range(n//2) :
  if n!= (n//2)-1 :
    for j in range(n-i):
      print(" ",end='')
    for j in range(3+2*i) :
      if j == 0 or  j == (3+2*i) - 1 :
        print("=",end='')
      else :
        print("#",end='')
    print("\n",end="")
    for j in range(n-i):
      print(" ",end='')
    if i != n//2-1 :
      for j in range(3+2*i) :
        print("=",end='')
    print("\n",end="")
  
  