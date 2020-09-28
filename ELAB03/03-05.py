n = int(input("input: "))
t = int((n+1)/2)
for i in range(t):
  s = ''
  for j in range(t-i,1,-1):
    s+=' '
  for j in range(1,(2*(i+1)),1):
    s+='#'
  print(s)
for i in range(n-t): ## 0 1 2 
  s = ''
  for j in range(1,i+2):
    s+=' '
  for j in range(1,n-2*i-1,1):
    s+='#'
  print(s)
    
    