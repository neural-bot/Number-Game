from random import randint
print("Welcome to Number Guessing Game")

secret_number = randint(1, 10)

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("You guessed low. Try agian! ")
    elif guess > secret_number:
        print("You Guessed high. Try agian!")
    else:
        print("Congrats, You guessed the right number")
        break

print("Game Over")