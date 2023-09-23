from time import sleep
import random


def red(text):
    print("\033[91m {}\033[00m" .format(text))


def cyan(text):
    print("\033[96m {}\033[00m" .format(text))
    return ''


def yellow(text):
    print("\033[93m {}\033[00m" .format(text))


def green(text):
    print("\033[92m {}\033[00m" .format(text))


def purple(text):
    print("\033[95m {}\033[00m" .format(text))


def invalid():
    red("Invalid input! Try again:")
    return


cyan('''Welcome to the "Guess a number" game!''')
stop_playing = False
while not stop_playing:
    guess_or_be_guessed = input(cyan
("Would you like to choose a number or should the computer choose one instead?([p]layer or [c]omputer)")).lower()
    if guess_or_be_guessed[0] != "p" and guess_or_be_guessed[0] != "c":
        invalid()
        continue
    elif guess_or_be_guessed[0] == "c":
        answer = False
        computer_guesses = 0
        while not answer:
            random_or_not = input(cyan("Would you like the computer to guess randomly or not?(r/n)")).lower()
            if random_or_not[0] == "n":
                high = 100
                low = 0
                cyan("Think of a number between 1 and 100: ")
                sleep(1)
                while not answer:
                    guess = (high - low) // 2 + low
                    computer_guesses += 1
                    cyan(f"Is your number {guess}?")
                    response = input(cyan
                        ("""Enter "h" if your number is higher, "l" if it's lower, or "c" if it's correct: """)).lower()
                    if response[0] == "h":
                        low = guess
                    elif response[0] == "l":
                        high = guess
                    elif response[0] == "c":
                        answer = True
                    else:
                        invalid()
                purple(f"Guesses needed: {computer_guesses}")
            if random_or_not[0] == "r":
                answer = False
                cyan("Think of a number between 1 and 100: ")
                sleep(1)
                low = 1  # trying to limit the "random" choices of the computer
                high = 100
                random_guess = random.randint(low, high)
                while not answer:
                    computer_guesses += 1
                    current_guess = random_guess
                    cyan(f'Is your number {random_guess}')
                    response = input(cyan
                        ("""Enter "h" if your number is higher, "l" if it's lower, or "c" if it's correct: """)).lower()
                    if response[0] == "h":
                        low = current_guess
                        random_guess = random.randint(low+1, high)
                    elif response[0] == "l":
                        high = current_guess
                        random_guess = random.randint(low, high-1)
                    elif response[0] == "c":
                        purple(f"Guesses needed: {computer_guesses}")
                        answer = True
                    else:
                        invalid()
                        computer_guesses -= 1
                        continue
            elif random_or_not[0] != "r" and random_or_not[0] != "n":
                invalid()
                continue
    elif guess_or_be_guessed[0] == "p":
        answer = False
        player_guesses = 0
        computer_number = random.randint(1, 100)
        while not answer:
            player_input = input(cyan("Guess the number (1-100): "))
            if not player_input.isdigit():
                invalid()
            else:
                player_guess = int(player_input)
                player_guesses += 1
                if player_guess > computer_number:
                    cyan("Your guess is too high!")
                elif player_guess < computer_number:
                    cyan("Your guess is too low!")
                elif player_guess == computer_number:
                    green("You guessed it!")
                    answer = True
        purple(f"Guesses needed: {player_guesses}")
    while True:
        play_again = input(cyan("Would you like to play again? (y/n): ")).lower()
        if play_again[0] == "y":
            break
        elif play_again[0] == "n":
            green("Thanks for playing!")
            stop_playing = True
            break
        else:
            invalid()
            continue
