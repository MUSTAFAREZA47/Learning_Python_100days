fruits = ["apple", "banana", "peer"]

for fruit in fruits:
    print(fruit)
    print(fruit + " " + "pie")
    print(fruits)

# print(len(fruits))

scores = [78, 65, 89, 86]

high_score = 0
for score in scores:
    if score > high_score:
        high_score = score
# print(high_score)

# Project -------> Average Height of Students
# Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(f"total height = {total_height}")
#
# number_of_students = 0
# for students in student_heights:
#     number_of_students += 1
# print(f"number of students = {number_of_students}")
#
# average_height = round(total_height / number_of_students)
#
# print(f"average height = {average_height}")
#
# # Project ---------> High Score
# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
#
# # Write your code below this row 👇
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(highest_score)

# For Loop with Range
# for number in range(1, 11):
#     print(number)
#
# target = int(input()) # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️
#
# # Write your code here 👇
# total_sum = 0
# for number in range(0, target + 1):
#   if number % 2 == 0:
#     total_sum += number
# print(total_sum)


# Write your code here 👇
for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
import random

# my_list = 1234
# random.shuffle(my_list)
# print(my_list)

my_string = "Hello"

# Breaking the string into a list of individual characters
char_list = list(my_string)
random.shuffle(char_list)
print(char_list)

# Password Generator Project

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
# 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
# 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] symbols = [
# '!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ''
# for char in range(0, nr_letters):
#   password_char = random.choice(letters)
#   password += password_char
# for sym in range(0, nr_symbols):
#   password_sym = random.choice(symbols)
#   password += password_sym
# for num in range(0, nr_numbers):
#   password_num = random.choice(numbers)
#   password += password_num
# print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password_list = []
# for char in range(0, nr_letters):
#     password_char = random.choice(letters)
#     password_list.append(password_char)
# for sym in range(0, nr_symbols):
#     password_sym = random.choice(symbols)
#     password_list.append(password_sym)
# for num in range(0, nr_numbers):
#     password_num = random.choice(numbers)
#     password_list.append(password_num)
#
# random.shuffle(password_list)
# random_password = ''.join(password_list)
# print(random_password)
