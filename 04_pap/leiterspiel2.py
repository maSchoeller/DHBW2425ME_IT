import random

leiterspiel_dict = {
    3: 10,
    5: -3,
    8: 22,
    10: -5,
    20: 15,
    24: -10,
    40: 20,
    45: 15,
    70: 13,
    98: -20
}

anzahl_wuerfe = 0
position  = 0

while position < 100 :
    anzahl_wuerfe += 1
    wurf = random.randint(1,6)
    print(f"Der Wurf war eine: {wurf}")
    position = position + wurf + leiterspiel_dict[position + wurf]
    print(f"Du bist auf der aktuellen Position: {position}")

print(f"Spiel nach {anzahl_wuerfe} zuende")