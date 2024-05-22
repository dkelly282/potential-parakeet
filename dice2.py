import random
min_value = 1
max_value = 6
die1 = 0
die2 = 0
loop = "yes"
while loop == "yes" or loop =="y":
    print( " I am rolling two dice....")
    die1 = random.randint(min_value, max_value)
    die2 = random.randint(min_value, max_value)
    print (f"Die 1 is a {die1}")
    print (f"Die 2 is a {die2}")
    print (f"That is {die1+die2} in total")
    loop = input("Do you want to roll the die again?")
