one = ['1']
two = ['3']
three = ['9']
a = '1' 
b = '3' 
c = '9'
v = [0,0,0]
for i in range(1000):
  v[0] = int(a) 
  v[1] = int(b)
  v[2] = int(c)
  for i in range(len(a)) :
    v[0] += int(a[i])
  for i in range(len(b)) :
    v[1] += int(b[i])
  for i in range(len(a)) :
    v[2] += int(c[i])
  one.append(str(v[0]))
  two.append(str(v[1]))
  three.append(str(v[2]))
  a = str(v[0])
  b = str(v[1]) 
  c = str(v[2])


n = input("N: ")
s = n
while True :
  num = int(s)
  for i in range(len(s)) :
    num +=  int(s[i])
  if str(num) in one :
    print(f"1 {num}")
    break
  '''elif str(num) in two :
    print(f"3 {num}")
    break
  elif str(num) in three :
    print(f"9 {num}")
    break'''
  s = str(num)
  