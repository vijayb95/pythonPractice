import random, time

print("Hi, welcome to Dice Roll...")
time.sleep(1)
min = 1
max = int(input("Enter the maximum value your Dice can roll: "))

while(True):
    value = random.randrange(min, max)
    print(f"Your number is {value}")
    time.sleep(1)
    ask = input("Would you like to roll again? ").upper()
    if ask == 'Y' or ask == 'YES': continue
    else: break
print("Thanks for playing!")