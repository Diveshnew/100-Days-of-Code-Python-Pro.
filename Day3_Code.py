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


# Leap Year 
year = int(input("which year do you want to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a leap Year.")
    else:
        print("Leap Year")
else:
    print("Not a leap Year")


# Multiple if
print("Welcome to the rollerCoaster!")
height = int(input("What is Your height in cm?"))

if height >=120:
    print("You can ride the roller coaster")
    age = int(input("What is Your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do You need photo? Y or N")
    if wants_photo == "Y":
        bill +=3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, You have to grow taller before")



# Day 3.4 Pizza Order Exercise
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L")
add_pepperoni = input("Do You want pepperoni? Y or N")
extra_cheese = input("Do You want extra cheese? Y or N")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
    
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")



# Logical Operators

# elif age >= 45 and age <= 55:
#     print("Everything is going to be oK!")



# Day 3.5 Love calculator
print("Welcome to the love calculator!")
name1 = input("What is Your name?\n")
name2 = input("What is their name?\n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r  = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if(love_score<10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos ")
elif(love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"You score is {love_score}")
