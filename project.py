import random

number = random.randint(1, 100)
guess = 0
win = 0
name = str(input("Hello, What is your name?" ))

print('okay! '+ name +". Guess a number between 1 and 100:")

for i in range(0,5):
    player = int(input())
    guess = guess + 1
    if player > number:
        print("Your guess is too high")
    elif player < number:
        print("Your guess is too low")
    else:
        print('You guessed the number in',guess,'tries!')
        win = win + 1
        break

if win == 0:
    print('You did not guess the number. The number was',number)
