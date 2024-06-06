# input can be "rock", "paper" or "scissors"
# show warning if invalid input
# "rock" beats "scissors", "scissors" beats "paper", "paper" beats "rock"
# output: "You win", "You lose", "It's a draw"
# player plays vs computer
# when game over, show score and ask if player wants to play again

import random

def game():
    player_score = 0
    computer_score = 0
    while True:
        player = input("Enter 'rock', 'paper' or 'scissors': ")
        if player not in ["rock", "paper", "scissors"]:
            print("Invalid input")
            continue
        computer = random.choice(["rock", "paper", "scissors"])
        print(f"Computer: {computer}")
        if player == computer:
            print("It's a draw")
        elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
            print("You win")
            player_score += 1
        else:
            print("You lose")
            computer_score += 1
        print(f"Score: Player {player_score} - {computer_score} Computer")
        if input("Do you want to play again? (y/n): ") != "y":
            break

if __name__ == "__main__":
    game()
