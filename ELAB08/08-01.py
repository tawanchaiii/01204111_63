def findmax():
    s = []
    prepare = []
    for i in range(len(a)):
        rr = []
        for j in range(1,len(a[0])):
            rr.append(int(a[i][j]))
        prepare.append(rr)
    for i in range(len(a)) :
        prepare[i].sort(reverse = True)
        t = 0
        for j in range(1,len(prepare[0])-1) :
            t += prepare[i][j]
        s.append(t) 
    maxx = max(s)
    print(maxx)
    for i in range(len(a)):
        if s[i] == maxx :
            print(a[i][0])

name = input("File name: ")
f = open(name, "r")
a = []
for line in f:
    line = line.strip().split()
    a.append(line)
f.close()
findmax()