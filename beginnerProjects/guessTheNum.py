import random, time

print("Hi, welcome to Dice Roll...")
time.sleep(1)
min = 1
max = int(input("Enter the maximum value you'd like to generate: "))
value = random.randrange(min, max)

while(True):
    print(f"Guess the Number between {min} and {max}:", end = " ")
    guess = int(input())
    time.sleep(1)
    if value == guess: print("You made the right guess.")
    elif value > guess: print("Your guess is too low.")
    else: print("Your guess is too high.")
    time.sleep(1)
    ask = input("Would you like to guess again? ").upper()
    if ask == 'Y' or ask == 'YES': continue
    else: break
print("Thanks for playing!")