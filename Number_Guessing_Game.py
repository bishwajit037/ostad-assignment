import random
secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))

        attempts = attempts + 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("Error: Please Input an Integer.")
