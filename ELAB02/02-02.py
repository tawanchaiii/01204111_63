w = int(input("Weight: "))
h = int(input("Height: "))
bmi = w/((h/100)*(h/100))
if bmi < 18.6 :
	print(f"Your BMI is {bmi:.1f} You're in the underweight range.")
elif bmi < 25:
	print(f"Your BMI is {bmi:.1f} You're in the healthy weight range.")
elif bmi < 30:
	print(f"Your BMI is {bmi:.1f} You're in the overweight range.")
else :
	print(f"Your BMI is {bmi:.1f} You're in the obese range.")