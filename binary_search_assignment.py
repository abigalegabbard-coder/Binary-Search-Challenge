import random
#min = input("Enter the minimum for the range").strip()
#max = input("Enter the maximum for the range").strip()
display_player_guesses = []
display_comp_guesses = []
target = random.randint(min, max)

def get_user_input():
    min = int(input("Enter the minimum for the range: "))
    max = int(input("Enter the maximum for the range: "))
    while True:
        user_input = int(input(f"Enter a number between {min} and {max}: "))
        display_player_guesses.append(user_input)
        target = random.randint(min, max)
        if user_input > target:
            print("Number too high")
        elif user_input < target:
            print("Number too low")
        else:
            print("You got it!")
            break
get_user_input()
def get_comp_guesses():
    while True:
        comp_guess = (min + max)//2
        comp_guess.append(display_comp_guesses)
        if comp_guess > target:
            comp_guess + 1 = min
        elif comp_guess < target:
            comp_guess - 1 = max
        else:
            break
def print_outcome():
    while True:
        play_again = input("Enter (I) to play again, any other character to stop").strip()
        if play_again == "i" or play_again == "I":
            target = random.randint(min, max)
            get_user_input
            get_comp_guesses
            print_outcome
        else:
            print("Have a good day")
            break