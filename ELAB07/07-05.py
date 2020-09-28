r,c = input("City Size: ").split()
r = int(r)
c = int(c)
A = []

for i in range(r):
    A.append([int(y) for y in input().split()])

maxinrow = [] ## index
maxincol = [] ## index
maxinrow2 = [] ## index
maxincol2 = [] ## index
# max in row
for i in range(r):
    maxx = A[i][0] 
    ind = 0 
    for j in range(c):
        if A[i][j] > maxx:
            maxx = A[i][j]
            ind = j
    maxinrow.append(ind)

for i in range(c):
    maxx = A[0][i] 
    ind = 0 
    for j in range(r):
        if A[j][i] > maxx:
            maxx = A[j][i]
            ind = j
    maxincol.append(ind)

for i in range(r):
    maxx = A[i][c-1] 
    ind = c-1
    for j in range(c-1,-1,-1):
        if A[i][j] > maxx:
            maxx = A[i][j]
            ind = j
    maxinrow2.append(ind)

for i in range(c):
    maxx = A[r-1][i] 
    ind = r-1
    for j in range(r-1,-1,-1):
        if A[j][i] > maxx:
            maxx = A[j][i]
            ind = j
    maxincol2.append(ind)




ans = list()
#check N
sum = 0
for i in range(c):
    minn = A[0][i] 
    if maxincol[i] != 0 :
        sum+=2
    else :
        sum+=1
    for j in range(maxincol[i]):
        if A[j][i] > minn : 
            sum+=1
            minn = A[j][i]
ans.append(sum)
sum = 0
# check S
for i in range(c):
    minn = A[r-1][i] 
    if maxincol2[i] != r-1 :
        sum+=2
    else :
        sum+=1
    for j in range(r-1,maxincol2[i],-1):
        if A[j][i] > minn : 
            sum+=1
            minn = A[j][i]
ans.append(sum)
sum = 0

#check E
for i in range(r):
    minn = A[i][c-1] 
    if maxinrow2[i] != c-1 :
        sum+=2
    else :
        sum+=1
    for j in range(c-1,maxinrow2[i],-1):
        if A[i][j] > minn : 
            sum+=1
            minn = A[i][j]
ans.append(sum)
sum = 0

#check W
for i in range(r):
    minn = A[i][0] 
    if maxinrow[i] != 0 :
        sum+=2
    else :
        sum+=1
        
    for j in range(maxinrow[i]):
        if A[i][j] > minn : 
            sum+=1
            minn = A[i][j]
ans.append(sum)
sum = 0
way = ['N','S','E','W']
m = max(ans)
for i in range(len(way)):
    if m == ans[i]:
       print(way[i])
        
