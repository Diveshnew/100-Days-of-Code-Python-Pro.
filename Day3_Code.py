# Control flow - conditional statements
print("Welcome to the rollercoaster")
height = int(input("Enter Your Height in cm:"))

if height == 120:
    print("You can go for a ride in the rollercoaster")
else:
    print("Sorry! You have to grow tall in order to get a ride in the roller coaster")


# 3.1 - Odd and even exercise
number = int(input("Enter the number do You want to check?"))
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number.")


#Nested if/else
print("Welcome to the rollercoaster")
height = int(input("Enter Your Height in cm:"))

if height >= 120:
    print("You can go for a ride in the rollercoaster")
    age = int(input("What is Your age?"))
    if age<=18:
        print("Please Pay $7")
    else:
        print("Please Pay $12")
else:
    print("Sorry! You have to grow tall in order to get a ride in the roller coaster")


# if/elif/else
print("Welcome to the rollercoaster")
height = int(input("Enter Your Height in cm:"))

if height >= 120:
    print("You can go for a ride in the rollercoaster")
    age = int(input("What is Your age?"))
    if age < 12:
        print("Please Pay $5")
    elif age <= 18:
        print("Please Pay $7")
    else:
        print("Please Pay $12")
else:
    print("Sorry! You have to grow tall in order to get a ride in the roller coaster")


# Day 3.2 - Upgraded Bmi 2.0 Calculator
height = float(input("Enter Your height in m:"))
weight = float(input("Enter Your weight in kg:"))

bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, You have a normal weight.")
elif bmi < 30:
    print(f"You bmi is {bmi}, You are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, You are obese.")
else:
    print(f"You bmi is {bmi}, You are clinically Obese.")