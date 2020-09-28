arr = list(map(int,input().split()))
p = arr[0]+1
ans = ""
for i in range (1,len(arr),p) :
  ans = ans +  chr(arr[i])
print(ans)