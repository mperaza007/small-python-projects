import random
import time
import os


def clear_screen():
    # Clear the terminal screen
    os.system("cls" if os.name == "nt" else "clear")


print("===MEMORY SEQUENCE GAME===")
print("Remember the sequence and type it back!")
print("Rules:"
      "\n- Watch as numbers appear one by one"
      "\n- After the sequence is shown, type it back in order"
      "\n- Each round adds one more number to remember"
      "\n- How far can you go?")

input("Press Enter to start...")

sequence = []
current_round = 1
game_over = False

while not game_over:
    sequence.append(random.randint(1, 9))
    clear_screen()
    print(f"\n===Round i{current_round} ===")
    print(f"Remember this sequence of {len(sequence)} numbers: ")

    for num in sequence:
        time.sleep(1)
        print(f"{num}")
        time.sleep(1)
        clear_screen()

    print("\nNow repeat the sequence by typing each number, separated by spaces:")
    player_answer = input("> ")

    # Convert the string of numbers into a list and then into an integer list
    try:
        player_sequence = [int(num) for num in player_answer.split()]
    except ValueError:
        print("Please enter numbers only!")
        game_over = True
        continue
    if player_sequence == sequence:
        print(f"Congrats! You remembered all {len(sequence)} numbers!")
        current_round += 1
        time.sleep(2)
    else:
        print(f"Game over! You remember all {current_round - 1} numbers!")
        print(
            f"The correct sequence was {" ".join(str(num) for num in sequence)}")
        game_over = True

    if game_over:
        play_again = input("Play again? (y/n): ")
        if play_again.startswith("y"):
            sequence = []
            current_round = 1
            game_over = False
        else:
            print("Thanks for playing :)")


