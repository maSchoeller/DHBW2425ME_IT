from math import sqrt
def is_prime(number : int):
    ## Ermitteln ob es eine primzahl ist
    sq_num = int(sqrt(number))
    zaehler = 2
    while sq_num >= zaehler:
        rest = number % zaehler
        if rest == 0:
            return False
        zaehler += 1   
    return number != 1

border = 100
for i in range(border):
    checkPime = is_prime(i)
    if checkPime:
        print(f"Die Zahl {i} ist eine Primzahl")