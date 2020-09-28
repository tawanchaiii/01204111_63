arr = list()
sum = 0

while True:
  x = int(input("Enter a positive number: "))
  if x > 0 :
    arr.append(x)
    sum+=x
  if(len(arr)==5) :
    break
maxx = arr[0]
minn = arr[0]
for i in range(1,5) :
  if (arr[i] > maxx) :
    maxx = arr[i]
  if (arr[i] < minn) :
    minn = arr[i]
arr.sort()
print(f"sum: {sum}")
print(f"min: {minn}")
print(f"max: {maxx}")
print(f"med: {arr[2]}")