w=input("Enter your weight:")
h=input("Enter your height in meters:")
bmi=int(w)/float(h)**2
print(bmi)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal Weight")
else:
    print("Overweight")
