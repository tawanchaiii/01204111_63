while True:
    str = input("Enter message: ")
    if str == '' :
        break
    num = list()
    for i in range(5):
        num.append(0)

    sra = ['a','e','i','o','u']
    Sra = ['A','E','I','O','U']
    for i in str:
        for j in range(5):
            if i == sra[j]:
                num[j]+=1
            if i == Sra[j]:
                num[j]+=1

    for i in range(5):
        if num[i] != 0 :
            print(f"{sra[i]}: {num[i]}")

print("Exiting the program.")