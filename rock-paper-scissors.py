"""
import random
import time
print("===ROCK PAPER SCISSORS===")
print("Rules:"
      "\n- Rock crushes Scissors"
      "\n- Scissors cuts Paper"
      "\n- Paper covers Rock"
      "\n- First to win 3 rounds is the champion!")
print("-------------------------------------------")

game_over = False
current_round = 1
player_score = 0
computer_score = 0
game_values = {
    "1": "Rock",
    "2": "Paper",
    "3": "Scissors"
}
while not game_over:
    print(f"===Round {current_round}===")
    print(f"Score: You {player_score} - {computer_score} Computer")
    user_choice = int(input("Make your choice: "
                             "\n1. Rock"
                             "\n2. Paper"
                             "\n3. Scissors"
                             "\n"))
    if user_choice not in [1, 2, 3, 4]:
        print("That choice is not correct.")
        game_over = True
    else:
        continue
    print(f"You chose: {game_values[str(user_choice)]}")

    print("Computer is choosing...")
    time.sleep(1)
    computer_choice = random.randint(1, 3)
    print(f"Computer chose: {game_values[str(computer_choice)]}")

    if user_choice == computer_choice:
        print(
            f"It's a tie! You both selected {game_values[str(computer_choice)]} so there is no winner of the round.")
    elif user_choice == 1 and computer_choice == 3:
        print("Rock crushes Scissors! You win this round against Computer!")
        current_round += 1
        player_score += 1
    elif user_choice == 1 and computer_choice == 2:
        print("Paper covers Rock! You lose this round against Computer!")
        current_round += 1
        computer_score += 1
    elif user_choice == 2 and computer_choice == 1:
        print("Paper covers Rock! You win this round against Computer!")
        current_round += 1
        player_score += 1
    elif user_choice == 2 and computer_choice == 3:
        print("Scissors cuts Paper! You lost this round against Computer!")
        current_round += 1
        computer_score += 1
    elif user_choice == 3 and computer_choice == 1:
        print("Rock crushes Scissors! You lose this round against Computer!")
        current_round += 1
        computer_score += 1
    elif user_choice == 3 and computer_choice == 2:
        print("Scissors cuts Paper! You win this round against Computer!")
        current_round += 1
        player_score += 1
    else:
        print("Wrong choice. Try again")

    if player_score == 3 or computer_score == 3:
        print(
            f"Game is over! Final score: YOU {player_score} - {computer_score} COMPUTER")
        if computer_score > player_score:
            print("You lost!")
        else:
            print("You won!")
        game_over = True
    if game_over:
        play_again = input("Do you want to play again? (y\n): ")
        if play_again.startswith("y"):
            current_round = 1
            player_score = 0
            computer_score = 0
            game_over = False
        else:
            print("Thanks for playing :)")
"""
import random
import time


def get_computer_choice():
    return random.randint(1, 3)


def get_user_choice():
    while True:
        print("\nMake your choice:")
        print("\n1. Rock"
              "\n2. Paper"
              "\n3. Scissors")
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter a number between 1 and 3")
        except ValueError:
            print("Please enter a valid number.")


def display_welcome():
    print("===ROCK PAPER SCISSORS===")
    print("Rules:"
          "\n- Rock crushes Scissors"
          "\n- Scissors cuts Paper"
          "\n- Paper covers Rock"
          "\n- First to win 3 rounds is the champion!")
    print("\n-------------------------------------------")


def convert_choice_to_text(choice):
    options = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
    }
    return options[choice]


def determine_winner(user_choice, computer_choice):
    # tie
    if user_choice == computer_choice:
        return "tie"
    # user win cases
    elif ((user_choice == 1 and computer_choice == 3) or
          (user_choice == 3 and computer_choice == 2) or
          (user_choice == 2 and computer_choice == 1)):
        return "user"
    else:
        return "computer"


def display_round_result(user_choice, computer_choice, result):
    user_text = convert_choice_to_text(user_choice)
    computer_text = convert_choice_to_text(computer_choice)
    print(f"You chose: {user_text}")
    print("Computer is choosing", end="")

    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(f"Computer chose: {computer_text}")
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")


def play_game():
    # main game function
    display_welcome()

    user_score = 0
    computer_score = 0
    target_score = 3
    round_num = 1

    while user_score < target_score and computer_score < target_score:
        print(f"\n===Round {round_num}")
        print(f"Score: You {user_score}-{computer_score} Computer")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = determine_winner(user_choice, computer_choice)
        display_round_result(user_choice, computer_choice, result)
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        round_num += 1

    print("\n====GAME OVER====")
    print(f"Final Score: YOU {user_score} {computer_score} COMPUTER")
    if user_score > computer_score:
        print("Congrats! You are the champion!")
    else:
        print("You lost against Computer! Better luck next time!")
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.startswith('y'):
        play_game
    else:
        print("Goodbye!")


play_game()
