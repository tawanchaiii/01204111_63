def union(a,b):
  if len(a) > len (b) :
    m = a.copy()
    n = b.copy()
    arr = a.copy()
  else :
    m = b.copy()
    n = a.copy()
    arr = b.copy()
  for i in n :
    if not i in m :
      arr.append(i)
  for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
      if arr[j] < arr[i] :
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
  return arr
  
a = list(map(int,input("Input set A: ").split()))
b = list(map(int,input("Input set B: ").split()))
want = union(a,b)

if len(want) == 0 :
  print(f"A union B: empty set")
else :
  print(f"A union B: {want}")
