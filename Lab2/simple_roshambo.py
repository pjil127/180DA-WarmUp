# https://realpython.com/python-rock-paper-scissors/

import random

scores = [0, 0] # AI, Human

print("This is a game of Roshambo (Rock Papers Scissors).")
num_games = int(input("Number of times to play: "))

for i in range(num_games):
    user_action = input("Enter move (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"Your move: {user_action}, AI move: {computer_action}.")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            scores[1] += 1
        else:
            print("Paper covers rock! You lose.")
            scores[0] += 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            scores[1] += 1
        else:
            print("Scissors cuts paper! You lose.")
            scores[0] += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            scores[1] += 1
        else:
            print("Rock smashes scissors! You lose.")
            scores[0] += 1
    
    print("\n")

if scores[0] == scores[1]:
    print("Game over! It's a tie!")
elif scores[0] > scores[1]:
    print("Game over! AI won!")
else:
    print("Game over! You won!")