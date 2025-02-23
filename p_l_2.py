#! /usr/bin/python3
import re

# Question 1 :
# Write a simple calculator program using match to perform addition, subtraction, multiplication, and division.
# operation = "add"
# a, b = 10, 5
def calculator(operation, a, b):
    match operation:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            return a / b if b != 0 else "Error: Division by zero"
        case _:
            return "Error: Invalid operation"

operation = "add"
a, b = 10, 5
result = calculator(operation, a, b)
print(f"{result=}")
# # Expected Output: 15
# =====================================================================================
# Question 2 :
# Write a program to filter out even numbers from a list and count how many are left.

def filter(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]  # Filter out even numbers
    count = len(odd_numbers)  # Count the remaining numbers
    return odd_numbers, count

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers, remaining_count = filter(numbers)

print(f"Filtered List (Odds Only): {filtered_numbers}")
print(f"Count of Remaining Numbers: {remaining_count}")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Expected Output: [1, 3, 5, 7, 9], Count = 5
# =====================================================================================
# Question 3 :
# Write a program to check if a password meets the following criteria:
# - At least 8 characters long.
# - Contains at least one uppercase letter.
# - Contains at least one digit.

def is_valid_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"\d", password):
        return "Password must contain at least one digit."
    return "Password is valid."

# Example usage
password = input("Enter a password: ")
result = is_valid_password(password)
print(result)

# password = "Pass1234"
# # Expected Output: "Valid Password"
# =====================================================================================
# Question 4: 
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {**dic1, **dic2, **dic3}
print(merged_dict)


# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# ======================================================================================
# Question 5: 
# takes a string and prints the longest
# alphabetical ordered substring occured.
# For example, if the string is 'abdulrahman' then the output is:
def longest_alphabetical_substring(s):
    longest = current = s[0]

    for i in range(1, len(s)):
        if s[i] >= s[i - 1]:  # Alphabetically increasing
            current += s[i]
            if len(current) > len(longest):
                longest = current
        else:
            current = s[i]

    return longest

s = "abdulrahman"
print("Longest substring in alphabetical order is:", longest_alphabetical_substring(s))


# Longest substring in alphabetical order is: abdu
# ======================================================================================
# Question 6:
# Write a program to check if a Email meets the following criteria:
# - Ensures the email follows a standard format (e.g., local@domain.com).
# - Does not check if the email actually exists or is deliverable.
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return "Valid Email" if re.match(pattern, email) else "Invalid Email"

email = "test@example.com"
print(is_valid_email(email))

# ======================================================================================
