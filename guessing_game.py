
import random

start_game = (input("Would you like to play my number guessing game? "))
print()
if start_game.lower() != "yes":
    quit()
else: 
    print("Ok, cool!")
print()
num_range = input("I'll let you pick the upper range of the numbers. Pick a number above 25: ")

if num_range.isdigit():
    num_range = int(num_range)
else:
    print("You didn't pick a number")
    quit()

if num_range < 25:
    print("Number not over 25")
    quit()
print()

random_number = random.randint(0, num_range)

print(f"Ok, I generated a number between 0 and {num_range}.")
print()

guesses = 0

while True:
    guesses += 1

    player_guess = input("Take a guess! ")
    if player_guess.isdigit():
        player_guess = int(player_guess)
    else:
        print("Type a number next time!")
        continue
    if player_guess == random_number:
        print("Nailed It!")
        break
    elif player_guess < random_number:
        print("Higher Please!")
    else:
        print("Lower Please!")

print(f"You got it in {guesses} guesses")