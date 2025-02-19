operation = input("Welche Operation wollen Sie durchführen? ")
while operation != "Exit":
    print("Wenn Sie zwei Zahlen addieren wollen, schreiben Sie 'Add'.")
    print("Wenn Sie zwei Zahlen voneinander subtrahieren wollen, schreiben Sie 'Sub'.")
    print("Wenn Sie zwei Zahlen multiplizieren wollen, schreiben Sie 'Mul'.")
    print("Wenn Sie zwei Zahlen dividieren wollen, schreiben Sie 'Div'.")
    print("Wenn Sie das Programm beenden wollen, schreiben Sie 'Exit")

    try:
        A = int(input("Bitte geben Sie eine Zahl A ein: "))
        B = int(input("Bitte geben Sie eine Zahl B ein: "))
    except ValueError:
        print("Bitte geben Sie nur Zahlen ein!")
        continue

    if operation == "Add":
            print("A + B = " + str(A + B))
    elif operation == "Sub":
            print("A - B = " + str(A - B))
    elif operation == "Mul":
            print("A * B = " + str(A * B))
    elif operation == "Div":    
        try:
            while B == 0:
                B = int(input("Bitte geben Sie eine Zahl B ungleich 0 ein: "))
            print("A/B = " + str(A/B))
            print("A/B ganzzahlig: " + str(A//B))
            print("Rest: " + str(A % B))
        except ValueError:
            print("Bitte geben Sie nur Zahlen ein!")
    else:
        print("Bitte geben Sie eine gültige Operation ein!")
    operation = input("Welche Operation wollen Sie durchführen? ")
