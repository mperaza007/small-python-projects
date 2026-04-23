print("REVERSE NAME GENERATOR")


while True:
    user_name = input("Enter a name: ")

    # if no input, break out of the loop
    if not user_name:
        break

    reversed_name = user_name[::-1]
    print(f"Your reversed name is {reversed_name}")
    print(f"In a parallel universe, they call you {reversed_name}")

    continueGame = input("Try another name?(y/n): ")
    if continueGame.lower() == 'y':
        continue
    elif continueGame.lower() == 'n':
        print("Goodbye!")
        break
    else:
        print("That option does not exist. Try next time")


"""
Another way to get out of the loop:

if continueGame != 'y':
break

"""
