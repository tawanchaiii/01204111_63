sum = 0.0
c = 0
while True:
    x = input("Student's weight (or Enter to stop): ")
    if x == '':
        break
    f = float(x)
    sum+=f
    if sum > 200:
        c+= sum // 200
        sum = sum % 200
        if sum !=0 :
            c+=1
        sum = 0.0
    
if sum > 0:
    c+=1
ic = int(c)
print(f"Elevator works {ic} time(s).")
