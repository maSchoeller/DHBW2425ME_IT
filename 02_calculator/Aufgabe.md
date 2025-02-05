# Taschenrechner

1. Erstelle ein Python Skript mit dem Namen '01_Addition.py' das folgende Bedingungen erfüllt:
    - Der Anwender wird auf der Konsole darauf hingewiesen, das er die Zahl A eingeben soll.
    - Die Zahl A wird vom Python Skript eingelesen.
    - Der Anwender wird auf der Konsole darauf hingewiesen, das er die Zahl B eingeben soll.
    - Die Zahl B wird vom Python Skript eingelesen.
    - Das Python Skript addiert A und B und gibt das Ergebnis aus.
    - Das Skript beendet sich.
    - Sollte der Anwender bei den Eingaben für A und B keine Zahlen eingeben gib im eine Fehlermeldung aus und beende vorzeitig das Skript.

2. Kopiere das Python Skript aus Aufgabe 1 und passe den Dateinamen folgendermaßen an '02_Division.py'. Das Skript soll folgende Bedingungen Erfüllen:
    - Das Skript soll dem Bediener wie bisher auf die Eingabe von Zahl A und B hinweisen.
    - Sollte dieses eine der beiden Eingaben Fehlerhaft sein, das Skript nicht abbrechen sondern erneut um die Eingabe bitte.
      Solange bis der Anwender eine richtige Zahl eingibt.
    - Außerdem sol überprüft werden ob die Zahl B den Wert '0' hat, in diesem Fall soll die Eingabe auch wiederholt werden.
    - A und B sollen jetzt geteilt werden und ausgeben werden.
    - Zur Ausgabe gehört eine Fließkommazahldivision, eine Ganzzahldivision und eine Restdivision(Modulooperation).

3. Kopiere das Python Skript aus Aufgabe 2 und passe den Dateinamen folgendermaßen an '03_Calculator.py'. Das Skript soll folgende Bedingungen erfüllen:
    - Das Skript soll ab jetzt alle Rechnenoperationen beherrschen (Addition, Subtraktion, Multiplikation, Division).
    - Die Operation wird am Anfang des Skripts abgefragt und kann vom Bediener durch eine Eingabe festgelegt werden.
        - Add
        - Sub
        - Mul
        - Div
    - Danach soll wie gehabt die Eingabe der beiden Zahlen A und B abgefragt werden. Auch mit der Überprüfung ob die Eingabe Valide ist.
    - Außerdem soll sich das Skript nach erfolgreicher Berechnung nicht beenden sondern von Vorne beginnen solange bis der Bediener bei den Rechnenoperationen 'exit' eingibt. Sobald diese Zeichenkette eingegeben wurde soll das Skript sich sofort beenden.