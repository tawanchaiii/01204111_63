n = int(input("n: "))
A = list()
while n != 1 :
    for i in range(2,100000000):
        if n % i == 0:
            A.append(i)
            n = n/i
            break
for i in A : print(f"{i}",end= ' ')