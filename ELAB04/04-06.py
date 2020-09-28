def fac(n) :
  if n==0:
    return 1
  else :
    return n * fac(n-1)
def cal(a,b):
  return int (fac(a) / (fac(b)*fac(a-b)))
t = int(input("Input: "))
for i in range(t) :
  ans = ''
  for j in range(i+1) :
    ans += str(cal(i,j)) + " "
    ###print(f"({i},{j} )",end=" ")
  print(ans)