#meaning of status
# 1 = up
# 2 = right
# 3 = down
# 4 = left
maxx = 0
maxinrow ,maxincol,maxinrow2,maxincol2 = [],[],[],[]
A = list()
class Point:
    def __init__(self,row,col):
        self.row = row 
        self.col = col
    def getPoint(self):
        return self.row,self.col
while True:
    x = input()
    if x == '':
        break
    A.append(x.split())

def reflection(mirror, status):
    
    if ((mirror == "\\") and (status == 4)) or ((mirror == "/") and (status == 2)):
        return 1
    elif ((mirror == "\\") and (status == 3)) or ((mirror == "/") and (status == 1)):
        return 2
    elif ((mirror == "\\") and (status == 2)) or ((mirror == "/") and (status == 4)):
        return 3
    elif ((mirror == "\\") and (status == 1)) or ((mirror == "/") and (status == 3)):
        return 4

def mirrored(status):
    if status == 1: return -1,0
    elif status == 2: return 0,1
    elif status == 3: return 1,0
    elif status == 4: return 0,-1

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
            p.append(Point(i,j))
            maxinrow.append(j)
            break
        if j == len(A[0])-1 : maxinrow.append(j)
for i in range(len(A)):
    for j in range(len(A[0])-1,-1,-1):
        if A[i][j] == "\\" or A[i][j] == "/":
            p.append(Point(i,j))
            maxinrow2.append(j)
            break
        if j == 0 : maxinrow2.append(0)
for i in range(len(A[0])):
    for j in range(len(A)):
        if A[j][i] == "\\" or A[j][i] == "/":
            p.append(Point(j,i))
            maxincol.append(j)
            break
        if j == len(A)-1 : maxincol.append(j)
for i in range(len(A[0])):
    for j in range(len(A)-1,-1,-1):
        if A[j][i] == "\\" or A[j][i] == "/":
            p.append(Point(j,i))
            maxincol2.append(j)
            break
        if j == 0 : maxincol2.append(j)
for i in p:
    row,col = i.getPoint()
    if row >= maxincol2[col] : maxx = max(maxx,dfs(row,col,0,1))
    if col <= maxinrow[row]  : maxx = max(maxx,dfs(row,col,0,2))   
    if row <= maxincol[col]  : maxx = max(maxx,dfs(row,col,0,3))   
    if col >= maxinrow2[row] : maxx = max(maxx,dfs(row,col,0,4))   
print(f"Maximum saitron is {2**maxx} particle(s)")
