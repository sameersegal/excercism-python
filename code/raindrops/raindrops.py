def convert(number):
    
    s = ""
    factorable = False

    if number % 3 == 0:
        s += "Pling"
        factorable = True

    if number % 5 == 0:
        s += "Plang"
        factorable = True

    if number % 7 == 0:
        s += "Plong"
        factorable = True

    if not factorable:
        s = str(number)    

    return s
