x = int(input("x: "))
s = input("Operator: ")
y = int(input("y: "))
if s=="+":
  print(f"{x+y}")
elif s=="-":
  print(f"{x-y}")
elif s=="*":
  print(f"{x*y}")
elif s=="/":
  rr = float(x/y)
  print("%.2f"%rr)
elif s=="%":
  print(f"{x%y}")
else :
  print(f"Unknown Operator")