prime = list()
for i in range(0,10000000):
  prime.append(True)
for i in range(2,1000):
  for j in range(2,1000):
    prime[i*j] = False


n = int(input("N: "))

while True:
  if(prime[n]and prime[n+2] ):
    print(f"({n}, {n+2})")
    break
  n=n+1
