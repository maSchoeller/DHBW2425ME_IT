
ganzzahl = 0  # Ganzzahl
kommazahl = 0.1 # kommazahl
zeichenkette = "test" #zeichenkette
boolean = True  # Wahr oder falsch
float = 0.3 - (0.1 * 3)
if float <= 0.0000001 and float >= -0.000001:
    print("zahlen sind gleich")
else:
    print("zahlen sind nicht gleich: " + str(float))

zeichenkette = "neu Test" # Neuer Wert

liste = [(10,15)]
liste.append(0)
liste.append("marvin")
liste.append(zeichenkette)

zeichenkette = "altes Test" # Neuer Wert nach listenzuweisung
liste.pop()
liste.append(zeichenkette)

print(liste)
xypos = (10,15) # Tuple 
(x,y) = xypos

list = [1,2,3,4]
dict = {"deutsch" : 2 , "mathe": 5, "pyhsik" :6, "BK": 1}

note_mathe = dict["mathe"]
dict["mathe"] = 1

print(note_mathe)    # 5
print(dict["mathe"]) # 1
