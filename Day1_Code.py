# '\n' -> this is used for next line 
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print)")


#input() will get user input in console
#Then print() will print the word "Hello" and the user input
print("Hello " + input("What is Your name: "))


#This code prints the number of characters in a user's name
print(len(input("What is Your name: ")))

#Use of a Variable
name = input("What is Your Name: ")
length = len(name)
print(length)


#swifting challenge
a=input("a: ")
b=input("b: ")

c=a
a=b
b=c

print("a =" + a)
print("b =" + b)