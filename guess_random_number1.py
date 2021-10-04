
import random
number = random.randint(1, 99)
guess = int(input("Enter a whole number from 1 to 99: "))
loop=1
while number != "guess":
    print
    if guess < number:
        print("Your guess is too low")
        guess =int(input("Take another go: "))
        loop = loop + 1
    elif guess > number:
        print("Your guess is too high")
        guess = int(input("Take another go: "))
        loop = loop + 1
    else:
        print ("You guessed it right!")
        print(f"You took {loop} guesses")
        break
    
        

    