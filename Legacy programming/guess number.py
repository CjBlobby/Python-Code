Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random

def is_valid_num(s):
    if s.isdigit() and 1 <= int(s) <= 100:
        return True
    else:
        return False

    def main():
        number = randon.randint(1,100)
        guessed_number = False
        guess = input("Guess a number between 1 and 100: ")
        num_gueses = 0
        while not guessed_number:
            if not is_valid_num(guess):
                guess = input("I won't count that one. A number between 1 and 100 please: ")
                continue
            else:
                num_guesses +=1
                guess = int(guess)

            if guess < number:
                guess = input("Too low. Guess again: ")
            elif guess > number:
                guess = input("Too high. Guess again: ")
            else:
                print("You got it in", num_guesses,"guesses!")
                guessed_number = True

        print("Thanks for playing.")

    main()
