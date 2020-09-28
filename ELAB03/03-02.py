n = int(input("How many subject: "))
c = 0
sum = 0.0
sumC = 0.0
for i in range(0,n) :
  c = float(input(f"Subject {i+1} Credits: "))
  g = input(f"Subject {i+1} Grade: ")
  ww = 0
  sumC += c
  if g == 'A' :
    ww = 4
  elif g == 'B+' :
    ww = 3.5
  elif g == 'B' :
    ww = 3.0
  elif g == 'C+' :
    ww = 2.5
  elif g == 'C' :
    ww = 2.0
  elif g == 'D+' :
    ww = 1.5
  elif g == 'D' :
    ww = 1
  elif g == 'F' :
    ww = 0
  sum+= ww*c
print(f"Output: Total Credit = {sumC:.1f} ,GPA = {sum/sumC:.2f}")