one = input("What's the result of Manchester city's match? ")
two = input("What's the result of Liverpool's match? ")
if one != two:
	if(one == "won"):
		print("Manchester city is the champion of Premier League.")
	else:
		print("Liverpool is the champion of Premier League.")

else:
	x = input("What is the margin that Manchester city won by? ")
	y = input("What is the margin that Liverpool won by? ")
	if(x>y):
		print("Manchester city is the champion of Premier League. ")
	elif(x<y):
		print("Liverpool is the champion of Premier League.")
	else:
		t = input("Which team won the play-off match?(Manchester city/Liverpool) ")
		if(t == "Manchester city"):
			print("Manchester city is the champion of Premier League.")
		else:
			print("Liverpool is the champion of Premier League.")