def gcd(a,b):
    if (b != 0) : return gcd(b, a % b)
    else : return a
a = int(input("a : "))
b = int(input("b : "))
print(f"GCD : {int(gcd(a,b))}")
print(f"LCM : {int(a*b/gcd(a,b))}")