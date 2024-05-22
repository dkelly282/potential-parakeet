print ("Welcome to the distance converter!\n")

def imperial():
    miles = float(input ("What is the distance in miles? "))
    conversion = 0.62137119
    km = round (miles / conversion, 2)
    print(f"{miles} miles = {km} km")
    another_go()
    
def metric():
    km = float(input ("Ok then, what is the distance in km? "))
    conversion = 1.609344
    miles = round (km / conversion, 2)
    print(f"{km} km = {miles} miles")
    another_go()
    
def another_go():
    print("Do you want another go? (y/n)")
    answer = input(">")
    if "y" in answer:
        start()
    else:
        print("Goodbye!")
        exit()
        
def start():                
    print ("Do you want to convert miles to kilometres? (enter: 1)\nor kilometres to miles?                     (enter: 2)")    
    

    while True:
        try:
            answer = float(input(">"))
        except ValueError:
            
            print("Sorry I don't recognise that input as a number. Please try again.\n")
            start()
            continue 
    
        if answer == 1:
            imperial()
    
        else:
            answer == 2
            metric()
        
start()

 