# IF, ELIF AND ELSE CONDITIONS & NESTED IF ELSE CONDITIONS
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height == 112:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age > 18:
        print("Please pay $12.")
    elif 12 < age < 18:
        print("Please pay $7.")
    else:
        print("Please pay $5.")
else:
    print("Sorry, You have to grow taller before you can ride.")

# ODD AND EVEN PROJECT
number = int(input("Which number do you want to choose?"))

if number % 2 == 0:
    print(f"The number {number} you choosed is even!!!")
else:
    print(f"The number {number} you choosed is odd!!!")


# UPGRADED VERSION OF BMI VERSION 2.O
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = int(height) / float(weight)**2

BMI_result = print(round(BMI))

if BMI_result < 18.5:
    print(f"Your BMI is {BMI_result}, and you are underweight.")
elif 18.5 < BMI_result < 25:
    print(f"Your BMI is {BMI_result}, and you are normal weight.") 
elif 25 < BMI_result < 30:
    print(f"Your BMI is {BMI_result}, and you are overweight.")
elif 30 < BMI_result < 35:
    print(f"Your BMI is {BMI_result}, and you are obese.")
else:
    print(f"Your BMI is {BMI_result}, and you are clinically obese.")

# LEAP YEAR PROJECT
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if  year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year.")
    else:
        print("Leap year")
else:
    print("Not a leap year.")

# Enhance version of rollercoster ride
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height == 112:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age > 18:
        bill = 12
        print("Please pay $12.")
    elif 12 < age < 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 5
        print("Please pay $5.")
    wants_photo = input("Do you want to take photo? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        print(f"your total bill is {bill}")

else:
    print("Sorry, You have to grow taller before you can ride.")

# PIZZA ORDER PRACTICE
print("Welcome to Python Pizza Deliveries.")

size = input("What size pizza do you want? S, M or L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N.")

pizza_bill = 0

if size == "S":
    pizza_bill += 15
elif size == "M":
    pizza_bill += 20
else:
    pizza_bill += 25

if add_pepperoni == "Y":
    if size == "S":
        pizza_bill += 2
    elif size == "M" or size == "L":
        pizza_bill += 3

if extra_cheese == "Y":
    pizza_bill += 1
    print(f"Your final bill is ${pizza_bill}")
else:
    print(f"Your final bill is ${pizza_bill}")

# LOVE CALCULATOR
print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n").lower()
name2 = input("What is your partner name? \n").lower()
combine_name = name1 + name2

T = combine_name.count('t')
R = combine_name.count('r')
U = combine_name.count('u') 
E = combine_name.count('e')

true = T + R + U + E

L = combine_name.count("l")
O = combine_name.count("o")
V = combine_name.count("v")
E = combine_name.count("e")

love = L + O + V + E

result = int(str(true) + str(love))

if result < 10 or result > 90:
    print(f"Your love score is {result}, you go to like metos")
else:
    print(f"Your love score is {result}, you both are perfect.")

# TRESURE GAME
print("Welcome to Treasure island. Your mission is to find the tresure.")

step1 = input("left or right?")

if step1 == "left":
    step2 = input("swim or wait")
    if step2 == "swim":
        step3 = input("Which dooor? Red, Blue or Yellow.")
        if step3 == "Yellow":
            print("You win.")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")