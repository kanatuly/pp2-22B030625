import random
name = ""
tries = 0
NUMBER = 0
def ask_name():
    global name
    name = input("Hello! What is your name?\n")


def start_game():
    global NUMBER
    NUMBER = random.randint(1, 20)
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    make_guess()


def make_guess():
    global tries
    tries += 1
    print("Take a guess.")
    check(int(input()))


def check(X):
    if X < NUMBER:
        print("Your guess is too low.")
        make_guess()
    elif X > NUMBER:
        print("Your guess is too high.")
        make_guess()
    else:
        print(f'Good job, {name}! You guessed my number in {tries} guesses!')
        exit(0)


ask_name()
start_game()