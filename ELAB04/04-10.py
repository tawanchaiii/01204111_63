x = input()
c = True
for i in range(len(x)) :
  y = input()
  if (x[i] != y) :
    print("Fail!!")
    c = False
    break
if (c) :
  print("Succeed!!")