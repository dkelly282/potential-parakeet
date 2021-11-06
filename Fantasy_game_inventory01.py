import random
global name
print("Welcome brave adventurer\n\nWhat is your name?")
name = input(":")

def start():
    print(f"\n\nHello {name}")  
    commands = input ("Do you want to know the actions available to you, Y or N? :")
    if commands == "y":
        available_commands()
    else:
        carry_on()
        
def available_commands():
    print("\n\ni = inventory\nu = use item\nq = quit")
    action_loop()
    
def check_inventory():
    
    inventory = {"ropes": 1,"torches": 6, "gold coins": 42,
                     "arrows": 12, "hunting bow": 0,"dagger": 1}
    for key, value in inventory.items():
        print(key, ":", value)
    action_loop()

def get_dagger():
    print("\n\nYou are now holding your dagger in your hand")
    dagger = 1
    action_loop()

def get_rope():
    print("\n\nYou uncoil the rope and hold it in both hands")
    rope = 1
    action_loop()
    
def get_torch():
    print("\n\nYou take a torch from your bag and light it")
    torch = 1
    action_loop()
    
def carry_on():
    print("Suit yourself!")
    action_loop()

def use_item():
    item = input("""\n\nWhich item do you want to use?\n\nR = Rope
T = Torch\nD = Dagger\n:""")
    if item == "d":
        get_dagger()
    elif item == "r":
        get_rope()
    elif item == "t":
        get_torch()
    else:
        action_loop()
    
def action_loop():
    response = random.randint(1,3)
    if response == 3:
        move = input("\nOk, what next? :")
    elif response == 2:
        move = input("What do you want to do now? :")
    else:
        move = input("Tell me your next move :")
    
    if move == "i":
        check_inventory()
    elif move == "u":
        use_item()
    elif move == "q":
        print("See you next time")
        exit()
    else:
        action_loop()
start()




    




    



                                