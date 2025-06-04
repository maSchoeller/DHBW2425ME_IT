# Eine Zahl die ich nur durch 1 und sich selber teilen kann.
from math import sqrt
# Überprüfe jede Zahl bis zur Quadratwurzel ob die Modulooperation ein Ganzzahlergebnis gibt
def evaluate_prime_candidate(potential_prime):
    is_prime_number = True
    sqrt_limit = sqrt(potential_prime)
    multiply_check = 2
    while multiply_check < sqrt_limit:
        rest = potential_prime % multiply_check
        if rest == 0:
            is_prime_number = False
        multiply_check+=1

    # for multiply_check in range(1,int(sqrt_limit+1)):#
    # if multiply_check == 1:
        #     continue
        # rest = potential_prime % multiply_check
        # if rest == 0:
        #     is_prime_number = False
    return is_prime_number

def find_prime_numbers(ziel_zahl : int):
    for potential_prime in range(2,ziel_zahl+1):

        is_prime_number = evaluate_prime_candidate(potential_prime)
    
        if is_prime_number:
            print(f"Die Zahl: {potential_prime} is eine Primzahl")

find_prime_numbers(100)