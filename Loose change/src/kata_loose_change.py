from socket import if_nametoindex
import math

def loose_change(cents):
    
    
    coins = { "Pennies" : 1, "Nickels": 5, "Dimes": 10, "Quarters": 25 }
    change = { "Pennies" : 0, "Nickels": 0, "Dimes": 0, "Quarters": 0 }

    if cents <= 0:
        return change
    

    for i in range(math.ceil(cents)):

        if cents >= 25:
            cents = cents - coins["Quarters"]
            change["Quarters"] +=1        
        elif cents >= 10:
                cents = cents - coins["Dimes"]
                change["Dimes"] +=1
        elif cents >= 5:
                cents = cents - coins["Nickels"]
                change["Nickels"] +=1
        elif cents >= 1:
            cents = cents - coins["Pennies"]
            change["Pennies"] +=1
        else:
            return change