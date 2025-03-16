import random

num_to_guess=random.randint(1, 100)
while True:
    try:
        guess=int(input("Guess the number between 1 and 100:"))
        if guess < num_to_guess:
            print("Too Low")
        elif guess >num_to_guess:
            print("Too High")
        else:
            print("Well Done")
            break
    except ValueError:
        print("Please enter a valid number")
