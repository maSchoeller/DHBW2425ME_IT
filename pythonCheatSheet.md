# 🐍 Python Cheat Sheet für Einsteiger (50 essentielle Befehle)

Dieses Cheat Sheet soll dir helfen, die Grundlagen der Python-Programmierung zu verstehen und direkt anzuwenden. Jede Kategorie enthält erklärende Sätze, Beispiele und potenzielle Fallstricke, damit du typische Fehler vermeiden kannst.

---

## 🔤 Variablen und Datentypen

Variablen speichern Informationen, die später verwendet werden können. Python erkennt den Datentyp automatisch anhand des Werts. Achte auf die Schreibweise von Strings (" oder ') und achte auf Typkonsistenz.

```python
x = 10              # Integer
name = "Alice"      # String
pi = 3.14           # Float
is_valid = True     # Boolean
```

**Fallstrick:** Keine Leerzeichen im Variablennamen und Case-Sensitivity beachten ("Name" ist nicht "name").

## 📆 Datentypen prüfen & Umwandlung

Manchmal musst du sicherstellen, dass eine Variable einen bestimmten Typ hat oder den Typ konvertieren. Python bietet einfache Methoden dafür.

```python
type(x)             # Gibt den Typ zurück
int("10")           # String zu Integer
str(123)            # Integer zu String
float("3.14")       # String zu Float
```

**Fallstrick:** Ungültige Konvertierung führt zu Fehlern (z. B. int("abc")).

## 🧱 Mathematische Operatoren

Diese Operatoren helfen dir, Rechnungen durchzuführen. Besonders wichtig in Schleifen, Bedingungen und Berechnungen.

```python
+  -  *  /          # Grundrechenarten
%                  # Modulo (Rest)
**                 # Potenz
//                 # Ganzzahldivision
```

**Fallstrick:** Die Division `/` liefert immer einen Float. Nutze `//` für Integer-Ergebnisse.

## 🗺 Bedingungen

Verwende Bedingungen, um Entscheidungen im Programmablauf zu treffen. Der Code innerhalb eines Blocks muss eingerückt sein (typisch: 4 Leerzeichen).

```python
if x > 5:
    print("Größer als 5")
elif x == 5:
    print("Gleich 5")
else:
    print("Kleiner als 5")
```

**Fallstrick:** Kein Doppelpunkt vergessen! Indentationsfehler sind häufig.

## 🔁 Schleifen

Schleifen wiederholen Codeblöcke. Nutze `while` für unbestimmte Wiederholungen und `for` für zählbare Durchläufe.

```python
while x > 0:
    print(x)
    x -= 1

for i in range(5):
    print(i)
```

**Fallstrick:** `while` kann in eine Endlosschleife geraten, wenn die Bedingung nie falsch wird.

## ❋ Schleifensteuerung

Manchmal willst du eine Schleife vorzeitig beenden oder zur nächsten Runde springen.

```python
break              # Beendet Schleife sofort
continue           # Springt zur nächsten Iteration
```

**Fallstrick:** Unbedachter Einsatz kann zu übersprungenem Code führen.

## 🛠️ Funktionen

Funktionen fassen wiederverwendbaren Code zusammen. Gute Funktionsnamen machen Programme lesbarer.

```python
def begruessung(name):
    return f"Hallo {name}!"

print(begruessung("Lena"))
```

**Fallstrick:** Ohne `return` gibt eine Funktion `None` zurück.

## 📆 Listen

Listen speichern mehrere Werte. Sie können verändert (mutiert) werden.

```python
zahlen = [1, 2, 3]
zahlen.append(4)
zahlen.remove(2)
print(zahlen[0])
```

**Fallstrick:** Zugriff auf einen Index, der nicht existiert, verursacht einen Fehler.

## 🔑 Dictionaries

Dictionaries speichern Werte unter Schlüsseln ("key-value pairs"). Nützlich für strukturierte Daten.

```python
person = {"name": "Tim", "alter": 25}
print(person["name"])
person["stadt"] = "Berlin"
```

**Fallstrick:** Zugriff auf nicht existierende Keys ohne vorherige Prüfung führt zu Fehlern.

## 📚 Sets & Tupel

Sets speichern einzigartige Werte, Tupel sind wie Listen, aber unveränderlich.

```python
farben = {"rot", "blau", "grün"}        # Set
koordinaten = (10, 20)                  # Tuple
```

**Fallstrick:** Sets sind ungeordnet, d.h. die Reihenfolge ist nicht garantiert.

## 📄 Dateien lesen/schreiben

Dateien speichern Informationen dauerhaft. Verwende `with`, um sie sicher zu öffnen und automatisch zu schließen.

```python
with open("text.txt", "w") as f:
    f.write("Hallo Welt")

with open("text.txt", "r") as f:
    inhalt = f.read()
```

**Fallstrick:** Im Schreibmodus (`w`) wird die Datei überschrieben.

## ❓ Eingabe & Ausgabe

Mit `input()` kannst du Benutzereingaben verarbeiten. `print()` zeigt Ausgaben im Terminal an.

```python
name = input("Wie heißt du?")
print("Hallo", name)
```

**Fallstrick:** `input()` liefert immer einen String – Typumwandlung nicht vergessen.

## 🔍 Fehlerbehandlung

Fehler können das Programm abbrechen. Mit `try/except` kannst du sie abfangen und behandeln.

```python
try:
    zahl = int(input("Zahl eingeben: "))
except ValueError:
    print("Ungültige Eingabe!")
```

**Fallstrick:** Fang nur spezifische Fehler ab – `except:` allein ist zu allgemein.

## 🎠 Module importieren

Python hat viele Standardmodule. Mit `import` greifst du auf sie zu.

```python
import math
print(math.sqrt(16))
```

**Fallstrick:** Modulnamen dürfen nicht gleich heißen wie eigene Dateien (z. B. `math.py`).

## 🔍 Listen-Komprehension

Eine elegante Methode, Listen zu erzeugen. Kurz, aber mächtig.

```python
quadrate = [x**2 for x in range(5)]
```

**Fallstrick:** Nicht zu komplex machen – sonst leidet die Lesbarkeit.

## ⚖️ Bedingungen in Listen

Mit Bedingungen kannst du direkt filtern, was in die Liste aufgenommen wird.

```python
gerade = [x for x in range(10) if x % 2 == 0]
```

**Fallstrick:** Klammern nicht vergessen; sonst SyntaxError.

## 🧱 Built-in Funktionen

Python bietet viele eingebaute Funktionen, die dir das Leben leichter machen.

```python
len([1, 2, 3])
sum([1, 2, 3])
max([4, 1, 7])
min([4, 1, 7])
```

**Fallstrick:** Gib Listen oder passende Datentypen weiter, sonst Fehler.

## 🔧 Klassen und Objekte

Objektorientierte Programmierung ermöglicht komplexe Strukturen. Eine Klasse ist wie ein Bauplan.

```python
class Auto:
    def __init__(self, marke):
        self.marke = marke

    def hupen(self):
        print("Hup Hup!")

audi = Auto("Audi")
audi.hupen()
```

**Fallstrick:** `self` muss immer als erstes Argument in Methoden stehen.

## ➕ Operatorenvergleich

Nutze Vergleichsoperatoren, um Werte miteinander zu vergleichen. Das Ergebnis ist immer ein Boolean.

```python
==  !=  >  <  >=  <=
```

**Fallstrick:** Nicht `=` mit `==` verwechseln! `=` weist zu, `==` vergleicht.

## 🔤 String-Methoden

Strings besitzen viele praktische Methoden zur Bearbeitung.

```python
name.lower()
name.upper()
name.startswith("A")
name.replace("a", "@")
```

**Fallstrick:** Strings sind unveränderlich – Methoden geben neue Strings zurück.

## 🪝 Formatierte Strings (f-Strings)

Formatierte Strings sind eine einfache Möglichkeit, Variablen in Texte einzubauen.

```python
name = "Lena"
print(f"Hallo {name}!")
```

**Fallstrick:** Nur ab Python 3.6 verfügbar.

## 🔄 Enumerate

`enumerate()` liefert Index und Wert gleichzeitig bei Iterationen über Listen.

```python
for i, wert in enumerate(["a", "b"]):
    print(i, wert)
```

**Fallstrick:** Nicht direkt mit Index starten? `enumerate(..., start=1)` verwenden.

## 💥 Assert

`assert` prüft Bedingungen während der Entwicklung – praktisch für Tests.

```python
assert x > 0, "x muss positiv sein"
```

**Fallstrick:** Wird in Produktionscode oft entfernt (nicht für Laufzeit-Fehlermeldungen gedacht).

## 🧪 Boolesche Logik

Verwende `and`, `or`, `not` für logische Verknüpfungen.

```python
x > 0 and x < 10
not x == 5
```

**Fallstrick:** Vermeide zu viele verschachtelte Bedingungen.

## ⛓️ Verkettung von Bedingungen

Bedingungen lassen sich elegant verbinden.

```python
if 0 < x < 10:
    print("x liegt zwischen 0 und 10")
```

**Fallstrick:** Keine logischen Operatoren wie `and` nötig bei dieser Schreibweise.

## 🔂 Zip-Funktion

`zip()` kombiniert zwei oder mehr Listen zu Tupeln.

```python
namen = ["Tom", "Sue"]
alter = [22, 23]
for n, a in zip(namen, alter):
    print(n, a)
```

**Fallstrick:** Stoppt bei der kürzesten Liste.

## 🧮 Any & All

`any()` prüft, ob mindestens ein Element True ist. `all()` ob alle True sind.

```python
any([False, True])   # True
all([True, True])    # True
```

**Fallstrick:** Leere Listen geben bei `all` True, bei `any` False zurück.

## 🧹 Listenelemente entfernen

Elemente kannst du mit verschiedenen Methoden aus Listen löschen.

```python
zahlen = [1, 2, 3]
zahlen.remove(2)
zahlen.pop(0)
```

**Fallstrick:** `remove()` löscht nach Wert, `pop()` nach Index.

## 🔁 For-Schleife über Dictionaries

Über Keys, Values oder beides iterieren.

```python
for key in d:
    print(key)
for val in d.values():
    print(val)
for key, val in d.items():
    print(key, val)
```

**Fallstrick:** Reihenfolge kann (bis Python 3.7) variieren.

## 🧾 Mit `*args` und `**kwargs`

Flexible Funktionen für beliebige Argumente.

```python
def foo(*args, **kwargs):
    print(args)
    print(kwargs)
```

**Fallstrick:** Reihenfolge muss `*args`, dann `**kwargs` sein.

## ⌛ Zeitfunktionen

Das `time`-Modul erlaubt Wartezeiten oder Zeitmessungen.

```python
import time
time.sleep(1)
start = time.time()
```

**Fallstrick:** Zeitangaben immer in Sekunden.

## 🔃 Rekursion

Eine Funktion ruft sich selbst – nützlich bei z.B. Fakultätsberechnung.

```python
def fakultaet(n):
    if n == 0:
        return 1
    return n * fakultaet(n - 1)
```

**Fallstrick:** Zu tiefe Rekursion führt zu Fehlern (RecursionError).

## ✅ Exit mit return

Mit `return` kannst du Funktionen gezielt verlassen.

```python
def test():
    return "Fertig"
```

**Fallstrick:** Danach wird kein Code mehr in der Funktion ausgeführt.

## 🔄 While-else

Ein `else` kann auch bei `while`-Schleifen stehen – wird ausgeführt, wenn `break` nicht auftritt.

```python
while x > 0:
    x -= 1
else:
    print("Fertig")
```

**Fallstrick:** `else` wird übersprungen, wenn `break` in der Schleife ausgelöst wird.

## 📚 Hilfe & Doku

`help()` zeigt Dokumentation direkt im Terminal.

```python
help(print)
```

**Fallstrick:** Funktioniert nur im interaktiven Modus oder Jupyter Notebook gut.

## 🔄 Multiple Zuweisung

Du kannst mehrere Variablen gleichzeitig zuweisen.

```python
a, b = 1, 2
```

**Fallstrick:** Anzahl Variablen muss zu Anzahl Werte passen.

## 🧼 Liste leeren

Listen lassen sich schnell leeren.

```python
liste.clear()
```

**Fallstrick:** Alte Referenzen bleiben erhalten, wenn sie vorher kopiert wurden.

## 🚨 Kommentare

Kommentare helfen, Code zu erklären. Werden vom Interpreter ignoriert.

```python
# Das ist ein Kommentar
```

**Fallstrick:** Kein mehrzeiliger Kommentar mit `/* ... */` wie in C oder Java.

## ✅ Pass-Anweisung

`pass` dient als Platzhalter, wo Code syntaktisch nötig, aber nicht gewollt ist.

```python
def zukunft():
    pass
```

**Fallstrick:** Wird oft vergessen zu entfernen und blockiert tatsächliche Logik.

## 🔍 Scope und Gültigkeit

Variablen haben Gültigkeitsbereiche – lokal oder global.

```python
def func():
    x = 5  # lokal
```

**Fallstrick:** `global` verwenden, wenn innerhalb von Funktionen globale Variablen verändert werden sollen.

## 🧊 Konstanten-Konvention

Konstanten schreibt man in Großbuchstaben – sind aber nicht wirklich konstant.

```python
PI = 3.1415
```

**Fallstrick:** Python erzwingt Konstanz nicht – reine Konvention.

## 🎉 Glückwunsch!

Du hast jetzt 50 wichtige Python-Konzepte kennengelernt. Nutze dieses Sheet als Referenz beim Coden!

