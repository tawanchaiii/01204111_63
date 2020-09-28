jum1 = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
jum2 = [0 for i in range(13)]

def add(s):
  for i in range(0,13) :
    if (s == jum1[i]) :
      jum2[i] += 1 

card = list(map(str,input("Cards: ").split()))

for i in card :
  add(i)

four = False
three = False 
two = 0 

for i in jum2:
  if (i == 4) :
    four = True
  if (i == 3) :
    three = True
  if (i == 2) :
    two += 1


if (four) :
  print('Mark got "Four of a kind"')
elif (three and two == 1) :
  print('Mark got "Full House"')
elif (three and two == 0) :
  print('Mark got "Three of a kind"')
else : 
  print('Mark got "High Card"')

