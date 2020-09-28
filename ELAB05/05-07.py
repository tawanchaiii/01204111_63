def findmax(a,n,m):
    s = []
    prepare = []
    maxx = -1
    people = []
    for i in range(n) :
        arr = []
        for j in range(1,len(a[i])):
            arr.append(int(a[i][j]))
        prepare.append(arr)
    for i in range(n):
        prepare[i].sort(reverse=True)
        rr = 0
        for j in range(m-1) :
            rr+= prepare[i][j]
        s.append(rr) 
    maxx = max(s)
    for i in range(n):
        if s[i] == maxx:
            people.append(a[i][0])
    return maxx,people

def printans(maxi,name):
    print(maxi)
    for i in name :
        print(i)
n = int(input("n = "))
m = int(input("m = "))
a = []

for i in range (0,n,1):
    k = input().split()
    a.append(k)

maxi,name = findmax(a,n,m)
printans(maxi,name)