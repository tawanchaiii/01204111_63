def minus(a,b):
  arr = []
  for i in a :
    if not i in b :
      arr.append(i)
  if len(arr) == 0 :
      return 'empty set'
  else :
    return arr 
a = list(map(int,input("Input set A: ").split()))
b = list(map(int,input("Input set B: ").split()))
want = minus(a,b)
print(f"A minus B: {want}")
