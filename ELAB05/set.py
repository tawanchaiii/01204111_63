a = list(map(int,input("Input setA: ").split()))
b = list(map(int,input("Input setB: ").split()))
inter = []
amb = []
bma = []
union = []
if len(a) > len(b) :
    union  = a.copy()
else :
    union  = b.copy()

for i in a :
    for j in b :
        if i == j:
            inter.append(i)
        
for i in b :
    if not i in a :
        bma.append(i)
for i in a :
    if not i in b :
        amb.append(i)

if len(a) > len(b) :
    for i in b :
        if not i in a :
            union.append(i)
else :
    for i in a :
        if not i in b :
            union.append(i)
inter.sort()
amb.sort()
bma.sort
union.sort()

if (len(inter)!=0)  :
  print("A intersect B:",end="")
  for i in inter :
    print(f" {i}",end="")
else :
  print("A intersect B: empty set",end='')

if (len(amb)!=0)  :
  print("\nA minus B:",end="")
  for i in amb :
    print(f" {i}",end="")
else :
  print("\nA minus B: empty set",end='')

if (len(bma)!=0)  :
  print("\nB minus A:",end="")
  for i in bma :
    print(f" {i}",end="")
else :
  print("\nB minus A: empty set",end='')

if (len(union)!=0)  :
  print("\nA union B:",end="")
  for i in union :
    print(f" {i}",end="")
else :
  print("\nA union B: empty set",end='')