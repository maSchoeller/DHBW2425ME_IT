# 01_Addition.py

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Fehler: Bitte eine gültige Zahl eingeben.")

def main():
    print("Bitte geben Sie die Zahl A ein:")
    a = get_number("A: ")
    
    print("Bitte geben Sie die Zahl B ein:")
    b = get_number("B: ")
    
    result = a + b
    print(f"Das Ergebnis der Addition von {a} und {b} ist: {result}")

if __name__ == "__main__":
    main()