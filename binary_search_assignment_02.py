import random
min = int(input("Enter the minimum num: "))
max = int(input("Enter the maximum num: "))
target = random.randint(min, max)
display_player_guesses = []
display_comp_guesses = []

def get_valid_int():
    "<h1> This makes sure the users input is correct </h1>"
    while True:
        user_input = int(input(f"Enter a number between {min} and {max}: "))
        display_player_guesses.append(user_input)
        if user_input > target:
            print("Number too high")
        elif user_input < target:
            print("Number too low")
        else:
            print("You got it!")
            break
get_valid_int()

def get_valid_comp_input():
    "<h1> This calculates the computer's results </h1>"
    print(" ")
    print("My turn using binary search logic!")
    comp_min = min
    comp_max = max
    while True:
        comp_input = (comp_min + comp_max) // 2
        print(f"minimum: {comp_min} maximum: {comp_max}")
        print(f"({comp_min} + {comp_max}) // 2 = {comp_input}")
        print(f"Computer guesses: {comp_input}")
        display_comp_guesses.append(comp_input)
        if comp_input > target:
            print("Too high")
            comp_max = comp_input - 1
        elif comp_input < target:
            print("Too low")
            comp_min = comp_input + 1
        else:
            print("Correct!")
            break
get_valid_comp_input()

def print_the_outcome():
    "<h1> This prints the results of the player and the computer </h1>"
    while True:
        print("---------- FINAL RESULTS ----------")
        print(f"Target Number: {target}")
        print(" ")
        print(f"Player guesses:")
        print(display_player_guesses)
        print(f"Player guess count: {len(display_player_guesses)}")
        print(f"Computer guesses:")
        print(display_comp_guesses)
        print(f"Computer guess count: {len(display_comp_guesses)}")
        print(" ")
        if len(display_player_guesses) > len(display_comp_guesses):
            print("WINNER: COMPUTER")
            break
        elif len(display_comp_guesses) > len(display_player_guesses):
            print("WINNER: PLAYER")
            break
        elif len(display_player_guesses) == len(display_comp_guesses):
            print("IT'S A TIE")
            break
print_the_outcome()

def play_again():
    "<h1> This makes the user decide if they want to run the program again </h1>"
    while True:
        decision = input("Enter the character 'p' to play again, any other character to quit: ").strip()
        if decision == "p" or decision == "P":
            min = int(input("Enter the minimum num: "))
            max = int(input("Enter the maximum num: "))
            target = random.randint(min, max)
            get_valid_int()
            get_valid_comp_input()
            print_the_outcome()
            play_again()
        else:
            break
play_again()