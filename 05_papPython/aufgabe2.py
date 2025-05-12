kartenStapel = ["gr7", "gl2","+4", "bl3"]
while len(kartenStapel) != 0:
    print(kartenStapel)
    akutelleKarte = kartenStapel.pop(0)

    if akutelleKarte == "+4" :
        print("+4 kann gespielt werden.")
        break

if len(kartenStapel) == 0:
    print("Stapel ist leer")
else:
    print("Stapel ist nicht leer")

# variante 2
# if len(kartenStapel) != 0:
#     akutelleKarte = kartenStapel.pop(0)
#     while akutelleKarte != "+4" and len(kartenStapel) != 0:
#         print(kartenStapel)
#         akutelleKarte = kartenStapel.pop(0)
        
#     print("karte gefunden")
# if len(kartenStapel) == 0:
#     print("Stapel ist leer")


