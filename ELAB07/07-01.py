str = input("Input sentence: ")
ans=''
t = int(input("Input row: "))
arr = [['0']*100 for i in range(t)]
status = True
r = -1
c = 0
for i in str:
    if status :
        r+=1
        arr[r][c] = i
    else :
        r-=1
        c+=1
        arr[r][c] = i
    if (r == t-1)  or  ( (r == 0) and (c != 0) ) :
        status = not status
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] != '0':
            ans = ans + arr[i][j]
print(ans)