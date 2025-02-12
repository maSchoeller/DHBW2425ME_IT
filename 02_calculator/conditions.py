dayOfWeek = input("Bitte geben Sie den Wochentag ein: ")
time = int(input("Bitte geben Sie die Uhrzeit ein (als ganze Zahl): "))

if dayOfWeek == "Montag":
    print("Heute ist Montag!")
    if time < 9:
        print("Guten Morgen!")
    elif time < 15:
        print("Frohes arbeiten!")
    elif time < 20:
        print("Guten Abend!")
    else:
        print("Feierabend!")        
else:
    print("Heute ist nicht Montag!")
