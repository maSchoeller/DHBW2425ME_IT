# Python-Übungen

## Aufgabe 1: Heizleistung berechnen (Einsteiger)

**Lernziel:** Einführung in Benutzereingaben, einfache Berechnungen, `if`-Abfragen.

**Aufgabenstellung:**
Ein Raum soll beheizt werden. Die benötigte Heizleistung berechnet sich näherungsweise nach folgender Formel:

> `P = V * dT * 0.024`

Dabei ist:

* `P`: Heizleistung in kW
* `V`: Raumvolumen in m³ (Breite \* Länge \* Höhe)
* `dT`: Temperaturdifferenz innen-außen in Grad Celsius

**Aufgabe:**

* Lese die Raummaße (Breite, Länge, Höhe) und Temperaturen innen/außen über `input()` ein.
* Berechne die Heizleistung.
* Wenn die Temperaturdifferenz kleiner als 0 ist, gib eine Warnung aus.

<!-- ### Musterlösung Aufgabe 1

```python
breite = float(input("Breite des Raumes (m): "))
laenge = float(input("Länge des Raumes (m): "))
hoehe = float(input("Höhe des Raumes (m): "))
t_innen = float(input("Innentemperatur (Grad Celsius): "))
t_aussen = float(input("Außentemperatur (Grad Celsius): "))

volumen = breite * laenge * hoehe
dt = t_innen - t_aussen

if dt < 0:
    print("Warnung: Innentemperatur ist kälter als außen!")

leistung = volumen * dt * 0.024
print(f"Benötigte Heizleistung: {leistung:.2f} kW")
```

--- -->

## Aufgabe 2: Raumdaten verarbeiten mit Funktionen

**Lernziel:** Einführung in Funktionen.

**Aufgabenstellung:**
Erweitere die Heizleistungsberechnung durch eine Funktion `berechne_heizleistung(volumen, dt)`.

**Aufgabe:**

* Implementiere die Funktion.
* Verwende sie, um die Heizleistung zu berechnen.
* Gliedere die Eingabe ebenfalls in eine Funktion `eingabe()`.

<!-- ### Musterlösung Aufgabe 2

```python
def eingabe():
    breite = float(input("Breite (m): "))
    laenge = float(input("Länge (m): "))
    hoehe = float(input("Höhe (m): "))
    t_innen = float(input("Innentemperatur: "))
    t_aussen = float(input("Außentemperatur: "))
    return breite * laenge * hoehe, t_innen - t_aussen

def berechne_heizleistung(volumen, dt):
    return volumen * dt * 0.024

volumen, dt = eingabe()
leistung = berechne_heizleistung(volumen, dt)
print(f"Benötigte Heizleistung: {leistung:.2f} kW")
``` -->

---

## Aufgabe 3: Temperaturumrechnung mit Modulimport

**Lernziel:** Nutzung eigener Module und Imports.

**Aufgabenstellung:**
Implementiere ein Modul `temperatur.py`, das Funktionen zur Umrechnung zwischen Celsius, Kelvin und Fahrenheit enthält.

**Aufgabe:**

* Erstelle das Modul `temperatur.py` mit den Funktionen:

  * `celsius_to_kelvin(c)`
  * `celsius_to_fahrenheit(c)`
* Importiere das Modul in einem Hauptskript und verarbeite die Eingaben.

<!-- ### Musterlösung `temperatur.py`

```python
def celsius_to_kelvin(c):
    return c + 273.15

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32
```

### Hauptprogramm `main.py`

```python
import temperatur

c = float(input("Temperatur in Celsius: "))
print(f"In Kelvin: {temperatur.celsius_to_kelvin(c):.2f} K")
print(f"In Fahrenheit: {temperatur.celsius_to_fahrenheit(c):.2f} °F")
```-->

--- 

## Aufgabe 4: Solaranlage – Fehlerbehandlung bei Eingaben

**Lernziel:** Exception Handling mit `try`/`except`, saubere Benutzereingaben, Anwendung von Funktionen.

**Aufgabenstellung:**
Ein Benutzer gibt die Einstrahlung (in kWh/m²) und Fläche (m²) einer Solaranlage ein. Berechne die Energiemenge. Es sollen ungültige Eingaben (z. B. Text) abgefangen werden.

**Aufgabe:**

* Nutze `try`/`except` zur Fehlerbehandlung
* Verwende Funktionen für Eingabe und Berechnung

<!-- ### Musterlösung Aufgabe 4

```python
def eingabe_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ungültige Eingabe, bitte Zahl eingeben.")

def berechne_energie(einstrahlung, flaeche):
    return einstrahlung * flaeche

print("Berechnung der Solarenergie")
e = eingabe_float("Einstrahlung (kWh/m²): ")
f = eingabe_float("Fläche der Anlage (m²): ")
energie = berechne_energie(e, f)
print(f"Erzeugte Energie: {energie:.2f} kWh")
``` -->

---

## Aufgabe 5: Heizkostenabschätzung mit Verbrauchsprofilen

**Lernziel:** Kombination von Funktionen, Fehlerbehandlung, Import eigener Module, Mehrfachauswahl.

**Aufgabenstellung:**
Basierend auf den Daten zur Heizleistung und Heizdauer soll die Heizkostenabschätzung berechnet werden.
Dabei stehen verschiedene Energieträger zur Auswahl:

* Erdgas: 0.09 €/kWh
* Heizöl: 0.11 €/kWh
* Strom: 0.30 €/kWh

**Aufgabe:**

* Erstelle ein Modul `energiekosten.py` mit der Funktion `berechne_kosten(energie_kwh, tarif)`
* Ermögliche dem Benutzer, die Heizleistung (kW), Heizdauer (h) und den Energieträger auszuwählen
* Rechne die Energiekosten aus und gib sie aus

<!-- ### Musterlösung `energiekosten.py`

```python
def berechne_kosten(energie_kwh, tarif):
    return energie_kwh * tarif
```

### Hauptprogramm

```python
import energiekosten

tarife = {
    "gas": 0.09,
    "oel": 0.11,
    "strom": 0.30
}

try:
    leistung = float(input("Heizleistung (kW): "))
    dauer = float(input("Heizdauer (h): "))
    traeger = input("Energieträger (gas/oel/strom): ").lower()
    if traeger not in tarife:
        raise ValueError("Unbekannter Energieträger")

    energie = leistung * dauer
    kosten = energiekosten.berechne_kosten(energie, tarife[traeger])
    print(f"Gesamtkosten: {kosten:.2f} €")

except ValueError as e:
    print(f"Fehler: {e}")
``` -->

---

## Aufgabe 6: Lüftungsverluste in einem Gebäude

**Lernziel:** Mehrstufige Berechnungen mit mehreren Eingaben, komplexere Verzweigungen, modulare Struktur.

**Aufgabenstellung:**
Lüftungsverluste entstehen durch den Austausch warmer Innenluft mit kalter Außenluft. Die Verlustleistung $P$ kann mit folgender Formel berechnet werden:

> `P = V * n * dT * 0.34`

Dabei:

* `V`: Raumvolumen (m³)
* `n`: Luftwechselrate (1/h)
* `dT`: Temperaturdifferenz innen-außen (°C)

**Aufgabe:**

* Erfasse Volumen, Temperaturdifferenz und Luftwechselrate über die Konsole
* Berechne und gib die Lüftungsverluste aus
* Baue die Berechnung in eine Funktion
* Nutze `try`/`except` zur Absicherung

<!-- ### Musterlösung

```python
def berechne_lueftungsverlust(volumen, luftwechsel, dt):
    return volumen * luftwechsel * dt * 0.34

try:
    v = float(input("Raumvolumen in m³: "))
    n = float(input("Luftwechselrate (1/h): "))
    dt = float(input("Temperaturdifferenz (°C): "))
    verlust = berechne_lueftungsverlust(v, n, dt)
    print(f"Lüftungsverlust: {verlust:.2f} W")
except ValueError:
    print("Ungültige Eingabe")
``` -->

---

## Aufgabe 7: Hydraulischer Abgleich – Heizkreisoptimierung

**Lernziel:** Komplexe Eingabeverarbeitung, Schleifen, Funktionen mit Listen, strukturierte Ausgabe.

**Aufgabenstellung:**
Ein Gebäude besitzt mehrere Heizkreise. Jeder Heizkreis hat eine Länge (in m) und einen Volumenstrom (in l/min). Berechne für jeden Kreis den Druckverlust:

> `dp = 0.015 * länge * (volumenstrom / 10)^2`

**Aufgabe:**

* Erfasse n Heizkreise über die Konsole (Anzahl wählbar)
* Speichere die Werte in Listen
* Berechne den Druckverlust für jeden Heizkreis
* Gib eine Tabelle mit allen Werten aus

<!-- ### Musterlösung

```python
def druckverlust(l, q):
    return 0.015 * l * (q / 10) ** 2

anzahl = int(input("Anzahl Heizkreise: "))
laengen = []
stroeme = []
druckverluste = []

for i in range(anzahl):
    l = float(input(f"Länge Kreis {i+1} (m): "))
    q = float(input(f"Volumenstrom Kreis {i+1} (l/min): "))
    laengen.append(l)
    stroeme.append(q)
    druckverluste.append(druckverlust(l, q))

print("\nHeizkreis | Länge (m) | Strom (l/min) | Druckverlust (Pa)")
for i in range(anzahl):
    print(f"{i+1:^9} | {laengen[i]:^9} | {stroeme[i]:^14} | {druckverluste[i]:^17.2f}")
``` -->

---

## Aufgabe 8: Energiebilanz für ein Gebäude (Tagesprofil)

**Lernziel:** Kombinierte Anwendung aller vorherigen Konzepte: Modularisierung, Listenverarbeitung, Fehlerbehandlung, Strukturierung.

**Aufgabenstellung:**
Ein Tag wird in 24 Stunden unterteilt. Für jede Stunde soll der Heizbedarf (in kW) angegeben und die insgesamt benötigte Energie berechnet werden.

**Aufgabe:**

* Lese für jede Stunde den Heizbedarf (z. B. per Schleife)
* Berechne die Gesamtsumme
* Ermögliche alternativ die Eingabe einer Standardkurve (z. B. Nachtabsenkung)
* Nutze Funktionen zur Strukturierung

<!-- ### Musterlösung

```python
def eingabe_profil():
    werte = []
    print("Heizbedarf für jede Stunde eingeben:")
    for h in range(24):
        while True:
            try:
                wert = float(input(f"{h:02d} Uhr: "))
                werte.append(wert)
                break
            except ValueError:
                print("Bitte gültige Zahl eingeben.")
    return werte

def berechne_energie(profil):
    return sum(profil)

profil = eingabe_profil()
total = berechne_energie(profil)
print(f"Gesamter Energiebedarf: {total:.2f} kWh")
``` -->

---
