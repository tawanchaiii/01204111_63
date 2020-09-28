h = int(input("h: "))
ch = input("Character: ")
con = input("Is the tree invert?(y/n): ")
if con == 'n' :
  for i in range(h) :  ####
    s = ''
    for j in range(1,(h-i)) :
      s+=" "
    for j in range(1,(i+1)*2) :
      s+=ch
    print(s)
  for i in range(h//2) : ###button
    s = ''
    for j in range(1,h) :
      s+=" "
    s+=ch
    print(s)
else : 
  for i in range(h//2) : 
    s = ''
    for j in range(1,h) :
      s+=" "
    s+=ch
    print(s)
  for i in range(h) : 
    s = ''
    for j in range(i) :
      s+=" "
    for j in range(0,2*(h-i)-1) :
      s+=ch
   
    print(s)

 