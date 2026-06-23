import random
import string

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        print("\nSelect character types:")
        upper = input("Include Uppercase? (y/n): ").lower() == 'y'
        lower = input("Include Lowercase? (y/n): ").lower() == 'y'
        numbers = input("Include Numbers? (y/n): ").lower() == 'y'
        symbols = input("Include Symbols? (y/n): ").lower() == 'y'

        selected_types = sum([upper, lower, numbers, symbols])

        if selected_types < 2:
            print("Select at least 2 character types.")
            continue

        characters = ""

        if upper:
            characters += string.ascii_uppercase
        if lower:
            characters += string.ascii_lowercase
        if numbers:
            characters += string.digits
        if symbols:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))

        print("\nGenerated Password:")
        print(password)

        again = input("\nGenerate another password? (y/n): ").lower()
        if again != 'y':
            break

    except ValueError:
        print("Please enter a valid number.")