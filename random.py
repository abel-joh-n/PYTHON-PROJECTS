import random
num=random.randint(1,100)
attempts=0
print("Welcome to the number guessing game!!!")
print("I am thinking of a number between 1 and 100.")
while True:
    try:
        g=int(input("Take a guess..."))
        attempts +=1
    except ValueError:
        print("Invalid input. Please enter a number...")
        continue
    if g < num:
        print("too low")
    elif g > num:
        print("too high")
    else:
        print("CONGRATULATIONS!!! You guessed the number in", attempts,"attempts.")
        break
