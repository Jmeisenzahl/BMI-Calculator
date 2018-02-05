height = input("What is your height in inches?:")
weight = input("What is your weight in pounds?:")
BMI = 703*(int(weight)/(int(height)**2))
print("Your body mass index is " + str(BMI))
if(BMI<=18):
	print("you are underweight")
elif(BMI>18) and (BMI<26):
	print("you are normal Weight")
else:
	print("you are overweight")
