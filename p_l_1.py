#! /usr/python
import math
"""fPython Simple Lab 
#=====================
#Question 1
# a = [10, 20, 30, 20, 40, 50]
#   [0,  1,  2,  3,   4,  5]
#Remove the first occurance of 20

# Answer
# a.remove(20)
# print(a)

#==============================================================================================
#Question 2
# Remove element at index 1 and return its value in val
# val = a.pop(1);
# print(val)

#==============================================================================================
# Question 3
a = [10, 20, 30, 40, 50, 60, 70]
del a[1:4]  

print(a)
# Removes elements from index 1 to index 3 (which are 20, 30, 40)

#==============================================================================================
Question 4
a = [10, 20, 30, 40, 50, 60, 70]
del a[::]
print(a)

# Remove all elements


#==============================================================================================
# Write a program that prints the number of times the substring 'iti' occurs in a string
#iti in string
text = "iti is an iti institute called information technology institute And iti i go to is in The New Administrative Capital "
count = text.count("iti")

# i in iit 
text = "iti"
count = text.count("i")
print(f"{count=}")


#==============================================================================================
# application to take a number in binary form from the user, and print it as a decimal
user_input_binary = input("Enter a binary number: ")
input_to_number  = int(user_input_binary, 2)
print(input_to_number)

#==============================================================================================
# write a code take a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is divisible by both return "FizzBuzz"

def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n  

num = int(input("Enter a number: "))
print(fizz_buzz(num))

#==============================================================================================
# Ask the user to enter the radius of a circle print its calculated area and circumference


radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area: {area=}")
print(f"Circumference: {circumference=}")


#=============================================================================================="""
#Ask the user for his name then confirm that he has entered his name (not an empty string/integers).then proceed to ask him for his email and print all this data
def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name and not name.isdigit():
            return name
        print("Invalid name. Please enter a valid name.")

def get_valid_email():
    while True:
        email = input("Enter your email: ").strip()
        if "@" in email and "." in email:
            return email
        print("Invalid email. Please enter a valid email address.")

name = get_valid_name()
email = get_valid_email()

print("User Details:")
print(f"Name: {name}")
print(f"Email: {email}")

#==============================================================================================
#"""
