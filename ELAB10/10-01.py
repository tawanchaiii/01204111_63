import json 
def ans(m):
    if m == 1: print(f"{len(A)}")
    elif  m == 2:
        sum = 0
        for i in range(len(A)):
            sum += int(A[i]['population'])
        print(f"{sum}")
    elif m == 3:
        frontC = 0
        five = 0
        for i in range(len(A)):
            if A[i]['country'][0] == 'C' : frontC +=1
            if len(A[i]['country']) > 5 : five += 1
        print(frontC)
        print(five)
    elif m == 4:
        w = [0,0,0]
        for i in range(len(A)):
            if  int(A[i]['population']) > 500e6 : w[0]+=1
            if  250e6 < int(A[i]['population']) < 750e6 :  w[1]+=1
            if  int(A[i]['population'])  < 10e6 :  w[2]+=1
        for i in w : print(i)
    elif m == 5:
        lis = []
        for i in range(len(A)):
            lis.append(float(A[i]['World']))
        lis.sort(reverse=True)
        s1,s2 = 0.0,0.0
        for i in range (0,20) : s1 += lis[i]
        for i in range (49,150) : s2 += lis[i]
        print(f"{s1*100:.2f}")
        print(f"{s2*100:.2f}")
file =  input("File Name: ")
menu = int(input("Input : "))
f = open(file,) 
A = json.load(f) 
f.close()
ans(menu)
#print(f"{A[0]['country']}")