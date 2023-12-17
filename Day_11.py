########## Scope ###############
enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(enemies)
#
#
# # print(increase_enemies())
#
# # Local Scope
# portion_strength = 8


def drink_portion():
    portion_strength = 4
    print(portion_strength)


# drink_portion()

# Global Scope
player_health = 10


def game():
    def drink_portion():
        portion_strength = 2
        print(player_health, portion_strength)

    drink_portion()


# drink_portion()
# print(player_health)
# game()

# How to modify Global Variable
enemies = 1


def increase_enemies():
    global enemies
    enemies += 2
    print(enemies)


# increase_enemies()

# Random Number Guessing Game

import random

logo = """   
   _____                     
  / ____|                    
 | |  __ _   _  ___  ___ ___ 
 | | |_ | | | |/ _ \/ __/ __|
 | |__| | |_| |  __/\__ \__ \
  \_____|\__,_|\___||_hard  __/___/
   """
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = int(random.choice(range(1, 101)))
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
    attempts = 10
    print("You have 10 attempts remaining to guess the number.")
else:
    attempts = 5
    print("You have 5 attempts remaining to guess the number.")

game_continue = False
while not game_continue:
    guessed_number = int(input("Make a Guess: "))
    if guessed_number == random_number:
        print(f"You won, guessed number was {guessed_number}")
        game_continue = True
    else:
        if guessed_number > random_number:
            print("Too high.")
        else:
            print("Too low.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")

        if attempts == 0:
            print(f"Sorry, You lose, guessed number was {random_number}. Try again!")
            game_continue = True

# play_again = input("Do you want to play again: Type 'y' or 'n': ")
#
# if play_again == "y":
#     continue_game()
# else:
#     print("Thank You for playing!")
