print("BMI         |     WIEGHTSTATUS")
print("==========================")
print("below 18.5  |underweight")
print("18.5 - 24.9 |normalweight")
print("25 - 29.9   |overweight")
print("30 and above|obese")


weight = input("enter your weight in pounds ")
height1 = input("enter your height in feet ")
height2 = input("enter your height in inches ")
convweight = int(weight) * 0.45
convheight = (int(height1) * 12 + int(height2)) * 0.025
num = convheight * convheight
bmi = convweight/num
print(f"your BMI is roughly {bmi}!")
if bmi < 18.5:
    print("you are under weight!")
elif  18.5 < bmi < 24.9:
    print("you are normal weight!")
elif  25 < bmi < 29.9:
    print("you are over weight!")
elif bmi > 30:
    print("you are obese!")