name = input("File name: ")
file = open(name, "r")
a = []
c = 0
for line in file:
    line = line.strip().split(',')
    a.append(line)
    c = c+1
file.close()


def findIndex(str):
    for i in range(len(a[0])):
        if a[0][i] == str:
            return int(i)


def func(menu):

    if menu == 1:
        print(c)
    elif menu == 2:
        B = []
        for i in range(len(a[0])-1):
            s = 0
            for j in range(1, c):
                s += int(a[j][i])
            B.append(s)
        maxx = max(B)
        for i in range(len(a[0])-1):
            if B[i] == maxx:
                print(a[0][i])
    elif menu == 3:
        x = findIndex('blueplanet')
        B = []
        for i in range(1, c):
            B.append(int(a[i][x]))
        B.sort(reverse=True)
        for i in range(3):
            print(B[i], end=" ")
    elif menu == 4:
        B = []
        for i in range(1, c):
            s = 0
            for j in range(len(a[0])-1):
                s += int(a[i][j])
            B.append(s)

        maxx = max(B)
        for i in range(len(B)):
            if B[i] == maxx:
                r = len(a[1])
                print(f"{a[i+1][r-1]} {maxx}")

    elif menu == 5:
        maxx = int(a[1][0])
        ind = -1
        x = findIndex('tvshow')
        for i in range(2, c):
            if int(a[i][x]) > int(maxx):
                maxx = a[i][x]
                ind = i
        r = len(a[1]) - 1
        print(f"{a[ind][r]} {maxx}")
    elif menu == 6:
        cnt = 0
        x = findIndex('korea')
        for i in range(1, c):
            if int(a[i][x]) > 500:
               cnt += 1

        print(f"{cnt}")
    elif menu == 7:
        cnt = 0
        x = findIndex('siam')
        y = findIndex('food')
        for i in range(1, c):
            if int(a[i][x]) > int(a[i][y]):
               cnt += 1
        print(f"{cnt}")
    elif menu == 8:
        x = findIndex('rajdumnern')
        B = []
        for i in range(1, c):
            s = 0
            for j in range(len(a[0])-1):
                s += int(a[i][j])
            B.append(s)
        maxx = -1.0
        ind = -1
        for i in range(1, c):

            e = float(int(a[i][x]) / int(B[i-1]))
            if e > maxx:
                maxx = e
                ind = i
        r = len(a[1]) - 1
        # print(ind)
        print(f"{a[ind][r]}")
    elif menu == 9:
        r = len(a[1]) - 1
        B = []  # 0 คือช่องที่ 1
        cnt = 0
        for i in range(1, c):
            s = 0
            for j in range(len(a[0])-1):
                s += int(a[i][j])
            B.append(s)
        
        for k in range(1, c):
            check = []
            for j in range(r):
                check.append(int(a[k][j]))
            check.sort(reverse=True)
            if (check[0]+check[1])/B[k-1] >= 0.7 :
                cnt+=1
        print(cnt)
    elif menu == 10 :
        cnt = 0
        x = findIndex('pantip')
        for i in range (1,c):
            if int(a[i][x]) == 0   : 
               cnt+=1
        print(f"{cnt}")
     
        


menu = int(input("enter number: "))
func(menu)

