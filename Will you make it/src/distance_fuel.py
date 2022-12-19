def zero_fuel(distance_to_pump, mpg, fuel_left):
    #25 kilometros por cada galón y tengo 2 galones
    
    if mpg*fuel_left == 50:
        return True
    elif mpg * fuel_left <= distance_to_pump:
        return True
    else:
        return False
