arr = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def anytoten(any,n):
    x = 0
    l = len(any)
    for i in range(l):
        ee = 0 
        for j in range(len(arr)):
            if arr[j] == any[l-1-i] :
                ee = j
                break
        x += ee*(n**(i))
    return x 
def tentoany(ten,m) :
    dec = ten
    octal = ''
    while(dec > 0):
        octal = arr[dec%m] + octal
        dec = dec // m
    return octal

n = int(input())
m = int(input())
any = input()
ten = anytoten(any,n)
p = tentoany(ten,m)
print(p)