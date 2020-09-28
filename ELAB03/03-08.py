arr = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
n = 1
while True:
  dec = int(input("Input Decimal: "))
  if dec == -1 :
    print("Good bye.")
    break
  else :
    octal = ''
    while dec > 0:
      octal = arr[dec%16] + octal
      dec = dec // 16
    print(f"Hex: {octal}")