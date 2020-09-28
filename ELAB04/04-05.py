x = float(input("Input Gold: "))
x = int(x)//1000
if x == 0 :
  print("Not enough gold.")
else :
  for i in range(3+2*x):   ## line 
    for j in range(9 + 3*(x-1)):
      if (j == 0 or j == (9 + 3*(x-1) )-1) and (i == 0 or i == (3+2*x)-1)   :
        print(" ",end = '')
      else :
        print("o",end = '')
    print("\n",end="")
  for i in range(2+x):
    for j in range(3+x):
      print(" ",end='')
    for j in range(x) :
      print("o",end = '')
    print("\n",end="")  
  for i in range(x):
    for j in range(2+x):
      print(" ",end='')
    for j in range(x+2) :
      print("o",end = '')
    print("\n",end="") 
  
  for j in range(3+x):
      print(" ",end='')
  for j in range(x) :
      print("o",end = '')
    