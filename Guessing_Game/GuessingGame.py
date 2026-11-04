import random

attempts = 5
number = random.randint(1, 100)


def display_rules():
    print("Welcome to the Number Guessing Game!\n")
    print("I have selected a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it")

def start_game(number, attempt):
    if attempt > attempts:
        print("\nGame over, Womp Womp")
        print("The correct number was:", number)
        return

    guess = input(f"Attempt {attempt}/7 - Enter your guess:")

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number\n")
        return start_game(number, attempt)

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100 \n")
        return start_game(number, attempt)

    check_guess = lambda x, y: "correct" if x == y else(
        "low" if x < y else "high"
    )

    result = check_guess(guess, number)

    if result == "correct":
        print("\nCongraduations! You guessed the correct number!")
        print("You guessed it in", attempt, "attempt(s).")
        return

    if result == "low":
        print("Too Low!")
    else:
        print("Too High!")

    start_game(number, attempt + 1)

display_rules()
start_game(number, 1)