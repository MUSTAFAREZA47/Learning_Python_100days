######### Debugging ##############

# Describe Problems

def my_function():
    # for i in range(1, 20):
    for i in range(1, 21):
        if i == 20:
            print("You got it.")


# my_function()


# Reproduce the bug

from random import randint

dice_imgs = ["a", "b", "c", "d", "e", "f"]
dice_nums = randint(1, 6)


# print(dice_imgs[dice_nums])

# Play_Computer
# year = int(input("What is your year of birth? "))
# if 1980 < year < 1994:
#     print("YOu are a mallenial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# Use Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    # b_list.append(new_item)
        b_list.append(new_item)
    print(b_list)


# mutate([2, 5, 8, 7, 6])

