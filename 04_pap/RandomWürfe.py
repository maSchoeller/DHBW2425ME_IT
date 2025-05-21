Würfel = [1,2,3,4,5,6]
import random

Anz_Wurf = 0

while Anz_Wurf < 3 or Wurf == 6:
    Anz_Wurf = Anz_Wurf + 1
    Wurf = random.choice(Würfel)
    print("Wurf:", Wurf)

    if Wurf == 6:
        Anz_Wurf = 3
    elif Anz_Wurf == 3:
        print("Keine Würfe mehr übrig")
        break