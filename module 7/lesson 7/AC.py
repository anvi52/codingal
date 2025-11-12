import random

numbers = list(range(1, 51))
secret_number = random.choice(numbers)
print("try to guess the secret number between 1 and 50")

while True:
    guess = int(input("enter your guess:"))
    if guess == secret_number:
        print("you  guesssed it right!")

    elif guess > secret_number:
        print("too high! try again")
    else:
        print("too low! try again")    