#adventure game
print(" Welcome adventurer\n What is your name?")
global name
name = input(">")

def play_again():
    print(f"\n Ok, do you want to play again? (y or n)")
  
    answer = input(">").lower()

    if "y" in answer:
        start()
    else:
        exit()
        
def wrong_input():
    print(f"Come on {name} please follow the instructons!\n Let's start again....")
    start()

def wrong_number():
    print("You only have two choices - 1 or 2")
    monster_room()
    
def wrong_number2():
    print("You only have two choices - 1 or 2")
    diamond_room()

def wrong_number3():
    print("You only have two choices - 1 or 2")
    bear_room()

def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
  
    play_again()

def diamond_room():
    print(f"\n{name} you cannot believe your luck, as you now find yourself in a  small room that is filled with a large mound of diamonds reaching up almost to the ceiling")
    print("Ahead of you is a flight of steps leading to a trapdoor that appears to lead to the surface!")
    print("What would you do? (1 or 2)")
    print("1). Take some diamonds and go through the trapdoor.")
    print("2). Just go through the trapdoor.")
  
    answer = input(">")
  
    if answer == "1":
    
        game_over(f" Bad luck {name}. The moment you moved the diamonds, you triggered a hidden lever and set off a massive tremor that made the tunnel collapse. Your lifeless corpse will lie there for eternity")
    elif answer == "2":
    
        print("\nWow!, you proved yourself to be an honest person. Congratulations! you have saved your life and win the game! You can now return home to your miserable hovel and eke out the rest of your pathetic sad existence wondering what would have happened if you had taken one of the diamonds.")
    
        play_again()
    else:
    
        wrong_number2()

def monster_room():
  
    print("\nNow you have entered the room of a large fearsome looking ogre! He is also very ugly and extremely smelly.")
    print("However, luck is on your side and the ogre is asleep, and snoring very loudly.\nBehind the ogre, there is another door. What shall you do? (1 or 2)")
    print("1). Creep through the door as quietly as you can.")
    print("2). Sneak up and stab the ogre whilst it sleeps.")
    answer = input(">")
    if answer == "1":
        diamond_room()
    elif answer == "2":
    
        game_over("Your puny penknife merely tickles the ogre and makes him swing his arm round to scratch the itch. His huge clublike hand crushes your skull and the ogre carries on snoring unaware that a tasty little snack now lies next to him.")
    else:
        wrong_number()
        
def bear_room():
  
    print("\nYou push open the door to find a giant bear standing there  You have startled him and only have a few seconds to choose your next move before the bear reacts to your presence.")
    print("You can see that behind the bear there is another door.")
    print("The bear has a large honeycomb lying at his feet.")
    print("What do you do? (1 or 2)")
    print("1). Take the honeycomb.")
    print("2). Taunt the bear.")
    answer = input(">")
  
    if answer == "1":
        game_over("Are you really that stupid? The bear loves his honey and with one sweep of his giant paw kills you.")
    elif answer == "2":
        print("\nGood choice! The bear is particularly sensitive about his weight and your cruel taunts made him run away and hide in the far corner of the room. You can now go through the door behind him!")
        diamond_room()
    else:
        wrong_number3()

def start():
    
    print(f"\n Well {name} after many hours of searching and stumbling through a dank, water-filled cave you find yourself standing in a dark alcove.")
    print("Within the alcove there is a door to your left and right, which one do you take? (l or r)")
    answer = input(">").lower()
    if "l" in answer:
        bear_room()
    elif "r" in answer:
        monster_room()
    else:
        wrong_input()
start()    