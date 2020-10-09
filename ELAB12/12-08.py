maxx = 0
A = list()
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

for k in range(1, 5):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == "\\" or A[i][j] == "/":
                maxx = max(maxx,dfs(i,j,0,k) )
print(f"Maximum saitron is {2**maxx} particle(s)")
