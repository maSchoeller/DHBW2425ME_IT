
## 🧩 Aufgabe: Gebäudeteil-Analyse mit Zonen und Fensterwerten

**Lernziel:**
- Verschachtelte Datenstrukturen (Listen & Dictionaries)
- Schleifen, Bedingungen
- Funktionsstruktur & Fehlerbehandlung

**Aufgabenstellung:**
Ein Gebäude besteht aus mehreren Zonen (z. B. „Nordtrakt“, „Südflügel“). Jede Zone enthält Räume. Jeder Raum besitzt:
- Anzahl Fenster
- Fensterfläche pro Fenster
- U-Wert (Wärmedurchgangskoeffizient)

Ziel:
- Berechne für jede Zone die **Gesamtfensterfläche** und den **gewichteten mittleren U-Wert**
- Markiere Zonen mit U-Wert > 1.6
- Benutzer kann mehrere Zonen mit beliebig vielen Räumen eingeben

<!-- ```python
def eingabe_raum():
    name = input("Raumname: ")
    try:
        anzahl = int(input("Anzahl Fenster: "))
        flaeche = float(input("Fläche pro Fenster (m²): "))
        uwert = float(input("U-Wert (W/m²K): "))
        return {"name": name, "anzahl": anzahl, "flaeche": flaeche, "uwert": uwert}
    except ValueError:
        print("Fehlerhafte Eingabe. Wiederhole.")
        return eingabe_raum()

def eingabe_zone():
    zone_name = input("Name der Zone: ")
    raeume = []
    while True:
        weiter = input("Raum hinzufügen (j/n)? ")
        if weiter.lower() != "j":
            break
        raeume.append(eingabe_raum())
    return {"zone": zone_name, "raeume": raeume}

def analyse_zone(zone):
    gesamtflaeche = 0
    gewichtete_uwert_summe = 0
    fenster_gesamt = 0
    for raum in zone["raeume"]:
        flaeche = raum["anzahl"] * raum["flaeche"]
        gesamtflaeche += flaeche
        gewichtete_uwert_summe += raum["uwert"] * flaeche
        fenster_gesamt += raum["anzahl"]
    u_mittel = gewichtete_uwert_summe / gesamtflaeche if gesamtflaeche > 0 else 0
    return gesamtflaeche, u_mittel, fenster_gesamt

def hauptprogramm():
    zonen = []
    while True:
        zonen.append(eingabe_zone())
        if input("Weitere Zone (j/n)? ").lower() != "j":
            break

    print("\nZONENANALYSE")
    for z in zonen:
        flaeche, u, anzahl = analyse_zone(z)
        kritisch = "!!" if u > 1.6 else ""
        print(f"{z['zone']}: Fensterfläche: {flaeche:.2f} m², mittlerer U-Wert: {u:.2f} W/m²K {kritisch}")

hauptprogramm()

``` -->

---

## 🧩 Aufgabe: Hydraulikverteiler – Rohrnetzverwaltung mit Druckverlustrechner

**Lernziel:**
- Arbeiten mit Listen von Dictionaries
- Menügesteuerte Eingabe
- Modularisierung & Validierung

**Aufgabenstellung:**
Ein Heizungsverteiler versorgt mehrere Heizkreise. Jeder Kreis hat:
- Name
- Rohrlänge (m)
- Rohrdurchmesser (mm)
- Volumenstrom (l/min)

Berechne Druckverlust je Kreis nach Formel:
> Δp = 0.02 * L * Q² / d⁵

Anforderungen:
- Benutzer kann Kreise hinzufügen, anzeigen, löschen
- Druckverluste pro Kreis anzeigen
- Kreise nachträglich veränderbar

<!-- ```python
def kreis_eingabe():
    try:
        name = input("Kreisname: ")
        l = float(input("Rohrlänge (m): "))
        d = float(input("Durchmesser (mm): "))
        q = float(input("Volumenstrom (l/min): "))
        return {"name": name, "laenge": l, "durchmesser": d, "strom": q}
    except ValueError:
        print("Ungültige Eingabe, versuche es erneut.")
        return kreis_eingabe()

def druckverlust(k):
    d_m = k["durchmesser"] / 1000  # mm -> m
    return 0.02 * k["laenge"] * (k["strom"] ** 2) / (d_m ** 5)

def kreise_anzeigen(kreise):
    for k in kreise:
        dp = druckverlust(k)
        print(f"{k['name']:10} | L={k['laenge']}m | d={k['durchmesser']}mm | Q={k['strom']}l/min | Δp={dp:.2f} Pa")

def hauptmenu():
    kreise = []
    while True:
        print("\n[1] Kreis hinzufügen\n[2] Kreise anzeigen\n[3] Löschen\n[0] Beenden")
        wahl = input("Option: ")
        if wahl == "1":
            kreise.append(kreis_eingabe())
        elif wahl == "2":
            kreise_anzeigen(kreise)
        elif wahl == "3":
            name = input("Kreisname zum Löschen: ")
            kreise = [k for k in kreise if k["name"] != name]
        elif wahl == "0":
            break
        else:
            print("Ungültige Auswahl.")

hauptmenu()
``` -->

---

## 🧩 Aufgabe: Lüftungszonen-Optimierung nach Zeitprofil

**Lernziel:**
- Zeitbasierte Analyse
- Komplexe Entscheidungsstrukturen
- Verarbeitung und Visualisierung von Zeitreihendaten

**Aufgabenstellung:**
Ein Gebäude hat drei Lüftungszonen. Für jede Zone liegt ein Zeitprofil über 24 h vor (CO₂-Konzentration in ppm).

Regeln:
- Aktivierung der Lüftung, wenn CO₂ > 1000 ppm
- Abschaltung, wenn CO₂ < 800 ppm

Ziel:
- Status „AN“ / „AUS“ pro Stunde berechnen
- Ergebnis strukturiert ausgeben
- Aktivstunden pro Zone anzeigen

<!-- ```python
import random

def erstelle_profil():
    return [random.randint(600, 1400) for _ in range(24)]

def generiere_zonen():
    zonen = {}
    for name in ["Zone A", "Zone B", "Zone C"]:
        zonen[name] = {"werte": erstelle_profil(), "status": []}
    return zonen

def berechne_status(zonen):
    for name, daten in zonen.items():
        aktiv = False
        for ppm in daten["werte"]:
            if not aktiv and ppm > 1000:
                aktiv = True
            elif aktiv and ppm < 800:
                aktiv = False
            daten["status"].append("AN" if aktiv else "AUS")

def ausgabe(zonen):
    for name, daten in zonen.items():
        print(f"\n{name}:")
        for stunde in range(24):
            print(f"{stunde:02d}h | CO₂: {daten['werte'][stunde]} ppm | Status: {daten['status'][stunde]}")
        aktiv_stunden = daten["status"].count("AN")
        print(f"Aktivstunden: {aktiv_stunden}")

def haupt():
    zonen = generiere_zonen()
    berechne_status(zonen)
    ausgabe(zonen)

haupt()
``` -->


---
