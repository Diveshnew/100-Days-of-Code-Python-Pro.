# Here i used indexing to print the 'l' of the Hello and the indexing starts from [0]
# Here the index of 'Hello' : [H][0],[e][1],[l][2],[l][3],[o][4]
print("Hello"[3])


# Here the '123' and '345' is a string that's why they are printing as it is!!
print("123"+"345")


#Integer: here the numbers are in integer form that's why are added!
print(123 + 345)

# for long integer we use commas(,) in real life but in python if you are using long integers you can use (_) underscore to indicate a comma and the python will understand it!
print(345_456_789)

#Float
3.455367

#Boolean
True
False



num_char = len(input("Enter Your name: "))
# The Below line will give and error because the type of the 'num_char' is integer but concatination is only possible in strings
# print("Your name is :" + num_char + "Characters long")
print(type(num_char))

#Type Conversion in python
new_num_char = str(num_char)

a=str(123)
b=float(333)
print(type(a))
print(type(b))

print(str(70) + str(70))
print(70 + float("100.5"))


#Small challenge to add two numbers by converting them from string to int 

first_value = input("Enter the two digit number: ")

number_one = first_value[0]
second_two = first_value[1]

result = int(number_one) + int(second_two)
print(result)


# -> PEMDAS
# 1) Parentheses
# 2) Exponents
# 3) Multiplication
# 4) Division
# 5) Addition
# 6) Subtraction


print(3 * 3 + 3 / 3 -3 )
print( 3 * (3 + 3) / 3 - 3 )


# Rounding the value of a number
print(round(8/3,2))

#the code below will give us an integer without the need of conversion
print( 8 // 3 )
print( type(8 // 3) )

#this will be a floating point number
print( type(8 / 3) )


#The concept of f-string
score = 0
height = 1.8
isWinning = True
print(f"Your Score is {score}, Your height is {height}, Your winning is {isWinning}")


#Code Challenge - Your life in weeks
age = input("What is Your age?")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months "
print(message)