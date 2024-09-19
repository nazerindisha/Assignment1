import random


print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 100.")

attemp = 0
random_number = random.randint(1, 100)

while True:

    try:
        user_input = int(input("Enter Your Guess: "))
        attemp = attemp + 1

        if user_input < 1 or user_input > 100:
            print("Enter Number Between 1 to 100")

        elif user_input > random_number:
            print("Too high")

        elif user_input < random_number:
            print("Too low")

        else:
            print(
                "Congratulations! You've guessed the number in ", attemp, " attempts."
            )
            break

    except ValueError as e:
        print("Error: ", e)