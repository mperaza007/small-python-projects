import random
import string


def get_yes_no_input(question):
    while True:
        response = input(question + "(y/n):").lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("I didn't get that! Please enter 'y' or 'n'.")


def check_pass_strength(password):
    score = min(len(password) / 16, 1.0)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    variety = (has_lower + has_upper + has_digit + has_special) / 4.0

    final_score = (score * 0.6) + (variety * 0.4)
    if final_score >= 0.8:
        return "ULTRA STRONG"
    elif final_score >= 0.6:
        return "STRONG"
    elif final_score >= 0.4:
        return "DECENT"
    else:
        return "NEEDS IMPROVEMENT"


def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_special):
    chars = ""
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        print("Oops! No character types selected. Using lowercase letters by default.")
        chars = string.ascii_lowercase

    password = ""
    for _ in range(length):
        password += random.choice(chars)

    return password


def main():
    print("==== PASSWORD GENERATOR ====")
    print("Create super strong and secure passwords with ease!")

    while True:
        try:
            length = int(input("Enter password length (8-30): "))
            if 8 <= length <= 30:
                break
            print("Please choose a length between 8 and 30!")
        except ValueError:
            print("Oops! Please enter a number, like 12 or 34.")
    print("\nLet's customize your password!")

    use_lowercase = get_yes_no_input("Include lowercase letters? (a-z)? ")
    use_uppercase = get_yes_no_input("Include uppercase letters? (A-Z)? ")
    use_numbers = get_yes_no_input("Include numbers? (0-9)? ")
    use_special = get_yes_no_input("Include special characters? (!@#$%)? ")

    print("\n Generating your password...")

    password = generate_password(
        length, use_lowercase, use_uppercase, use_numbers, use_special)

    print("\n ====YOUR NEW PASSWORD====")
    print(f"{password}")

    strength = check_pass_strength(password)

    print(f"Strength: {strength}")
    print("====PASSWORD TIPS===="
          "\n Never use the same password for multiple accounts"
          "\n Consider using a password manager"
          "\n Change important passwords every few months"
          "\n Even strong passwords need to be kept secret!")

    if get_yes_no_input("\nWould you like to play again?"):
        main()
    else:
        print("Goodbye! Stay secure!")


main()
