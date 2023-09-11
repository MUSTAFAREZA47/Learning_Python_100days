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
 