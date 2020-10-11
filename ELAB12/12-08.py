maxx = 0
A = list()
while True:
    x = input()
    if x == '':
        break
    A.append(x.split())

def reflection(mirror, status):
    if ((mirror == "\\") and (status == 'left')) or ((mirror == "/") and (status == 'right')):
        return 'up'
    elif ((mirror == "\\") and (status == 'down')) or ((mirror == "/") and (status == 'up')):
        return 'right'
    elif ((mirror == "\\") and (status == 'right')) or ((mirror == "/") and (status == 'left')):
        return 'down'
    elif ((mirror == "\\") and (status == 'up')) or ((mirror == "/") and (status == 'down')):
        return 'left'

def mirrored(status):
    if status == 'up'       : return -1,0
    elif status == 'right'  : return 0,1
    elif status == 'down'   : return 1,0
    elif status == 'left'   : return 0,-1

def dfs(i, j, count, status):
    if i < 0 or j < 0 or i >= len(A) or j >= len(A[0]):
        return count
    if A[i][j] == "\\" or A[i][j] == "/":
        xx, yy = mirrored(reflection(A[i][j], status))
        return dfs(i+xx, j+yy,count+1, reflection(A[i][j], status))
    else :
        xx, yy = mirrored(status)
        return dfs(i+xx, j+yy,count, status)
p = list()

for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] == "\\" or A[i][j] == "/":
            maxx = max(maxx,dfs(i,j,0,'right'))
            break
for i in range(len(A)):
    for j in range(len(A[0])-1,-1,-1):
        if A[i][j] == "\\" or A[i][j] == "/":
            maxx = max(maxx,dfs(i,j,0,'left'))
            break
for i in range(len(A[0])):
    for j in range(len(A)):
        if A[j][i] == "\\" or A[j][i] == "/":
            maxx = max(maxx,dfs(j,i,0,'down'))
            break
for i in range(len(A[0])):
    for j in range(len(A)-1,-1,-1):
        if A[j][i] == "\\" or A[j][i] == "/":
            maxx = max(maxx,dfs(j,i,0,'up'))
            break
print(f"Maximum saitron is {2**maxx} particle(s)")

'''
O / \ \ O
/ O O O \
\ O \ O /
O \ \ / O 

Maximum saitron is 16384 particle(s)
'''