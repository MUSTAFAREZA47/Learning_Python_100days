num_char = len(input('What is your name?'))

new_num_char = str(num_char)

print(type(num_char))

a = float(123)
print(type(a))

# DATA TYPES
# STRING
# NUMBER
# FLOAT
# BOOLEAN

two_digit_number = input("Type two digit number?")
add_two_digit_number = int(two_digit_number[0]) + int(two_digit_number[1])

print(add_two_digit_number)

# BMI CALCULATOR
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = int(height) / float(weight)**2

BMI_result = print(round(BMI, 2))

# f-String
print(f"your BMI result is {BMI_result}")

# Your life in weeks
age = input("What is your current age?")

years = 90 - int(age)
months = 12*years
weeks = 4*months
days = 7*weeks

print(f"You have {days} days, {weeks} weeks, {months} years left")

# TIP CALCULATOR
print("Welcome to the tip calculator.")
total_bill = float(input("What is the total bill $?"))
percentage_of_tip = int(input("what percentage tip would you like to give? 10, 12, or 15?"))
bill_split = int(input("How many people to split the bill?"))

bill_with_percentage_of_tip = total_bill + total_bill * (percentage_of_tip/100)

bill_per_person = bill_with_percentage_of_tip / bill_split

final_bill = round(bill_per_person, 2)

print(f"Each per should pay ${final_bill}")
