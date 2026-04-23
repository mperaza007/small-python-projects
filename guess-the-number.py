import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. You have 10 attempts to guess it.")

playing = True
while playing:
    secret_num = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    game_over = False
    while attempts < max_attempts and not game_over:
        try:
            guess = int(
                input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: "))

        except ValueError:
            print("Please enter a valid number")
            continue
        attempts += 1
        if guess < secret_num:
            print("Too low! Please try a higher number")
        elif guess > secret_num:
            print("Too high! Please try a lower number")
        else:
            print(
                f"Congratulations! You guessed the number {secret_num} in {attempts} attempts.")
            game_over = True

        if attempts < max_attempts and not game_over:
            print(f"You have {max_attempts-attempts} attempts left!")
    if not game_over:
        print(f"Game over! The number was {secret_num}")
    again = input("Would you like to play again? (y/n): ")
    if again.startswith("y"):
        print("New game starting...")
    else:
        print("Goodbye!")
        playing = False
