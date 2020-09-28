arr = list(map(str,input().split()))
a = []
b = []
c = []
for i in arr :
  if ( 'A' <= i <= 'Z' or 'a' <= i <='z' ) :
    a.append(i)
  elif ( '0' <= i <= '9') :
    b.append(i)
  else :
    c.append(i)

print(f"Alphabet: {a}")
print(f"Number: {b}")
print(f"Special: {c}")
