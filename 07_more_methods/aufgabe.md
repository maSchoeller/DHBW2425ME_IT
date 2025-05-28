
# 🔌 Energieeffizienz-Analyse von Haushaltsgeräten (Python-Projekt)

**Fachbereich:** Gebäude- und Energietechnik  
**Zielgruppe:** Programmieranfänger  
**Dauer:** ca. 2 Stunden  
**Thema:** Vergleich des Stromverbrauchs von Haushaltsgeräten anhand einer CSV-Datei

---

## 🧠 Lernsituation

In modernen Haushalten sind viele elektrische Geräte im Dauereinsatz. Als angehende Techniker*innen im Bereich Gebäude- und Energietechnik ist es wichtig, den Stromverbrauch dieser Geräte bewerten zu können. In dieser Aufgabe programmierst du ein Werkzeug zur Analyse von Verbrauchsdaten.

---

## 📁 Vorbereitung: Beispiel-CSV-Datei

Lege eine Datei `geraete.csv` mit folgendem Inhalt an:

```csv
Name,Leistung (W),Nutzungsdauer (h)
Kühlschrank,100,24
Fernseher,80,4
Waschmaschine,2000,1
Ladegerät,5,3
Luftreiniger,60,12
```

---

## 🧩 Teil 1: CSV-Datei einlesen und anzeigen

### ✅ Ziel
- Lese Gerätedaten aus einer CSV-Datei
- Gib die Namen, Leistungen und Nutzungszeiten aus

### 💡 Hinweise
- Verwende das Modul `csv`
- Wandle Zahlen in `float` um

<!-- ### 🧪 Beispielcode
```python
import csv

def lade_geraete_datei(dateiname):
    geraete = []
    with open(dateiname, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            geraet = {
                "name": row["Name"],
                "leistung": float(row["Leistung (W)"]),
                "dauer": float(row["Nutzungsdauer (h)"])
            }
            geraete.append(geraet)
    return geraete

geraete = lade_geraete_datei("geraete.csv")

print("\n--- Geräte aus CSV-Datei ---")
for g in geraete:
    print(f"{g['name']} – {g['leistung']} W – {g['dauer']} h")
``` -->

---

## 🔍 Teil 2: Verbrauch berechnen

### ✅ Ziel
- Berechne den Tagesverbrauch jedes Geräts in kWh
- Ergänze das Dictionary um den Verbrauch

### 📐 Formel
```
Verbrauch = (Leistung * Dauer) / 1000
```

<!-- ### 🧪 Beispielcode
```python
for g in geraete:
    g["verbrauch"] = (g["leistung"] * g["dauer"]) / 1000

print("\n--- Geräte mit Verbrauch ---")
for g in geraete:
    print(f"{g['name']}: {g['verbrauch']:.2f} kWh/Tag")
``` -->

---

## 📊 Teil 3: Sortierung & Analyse

### ✅ Ziel
- Sortiere Geräte nach Verbrauch (aufsteigend)
- Markiere sparsamstes und stromhungrigstes Gerät

<!-- ### 🧪 Beispielcode
```python
geraete.sort(key=lambda x: x["verbrauch"])

print("\n--- Sortierter Verbrauch ---")
for i, g in enumerate(geraete):
    status = ""
    if i == 0:
        status = " (effizientestes)"
    elif i == len(geraete) - 1:
        status = " (höchster Verbrauch)"
    print(f"{g['name']}: {g['verbrauch']:.2f} kWh/Tag{status}")
``` -->

---

## 📤 Teil 4: Export als neue CSV-Datei

### ✅ Ziel
- Speichere analysierte Daten in einer neuen Datei `verbrauchsauswertung.csv`

<!-- ### 🧪 Beispielcode
```python
def speichere_geraete_csv(geraete, dateiname):
    with open(dateiname, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Leistung (W)", "Nutzungsdauer (h)", "Verbrauch (kWh)"])
        for g in geraete:
            writer.writerow([g["name"], g["leistung"], g["dauer"], f"{g['verbrauch']:.2f}"])

speichere_geraete_csv(geraete, "verbrauchsauswertung.csv")
print("\nAnalyse wurde in 'verbrauchsauswertung.csv' gespeichert.")
``` -->

---

## 💡 Bonus: Nur Geräte mit hohem Verbrauch anzeigen

<!-- ### 🧪 Beispielcode
```python
schwelle = 1.5
print(f"\n--- Geräte mit Verbrauch über {schwelle} kWh ---")
for g in geraete:
    if g["verbrauch"] > schwelle:
        print(f"{g['name']}: {g['verbrauch']:.2f} kWh")
``` -->

---
<!-- 
# 🧩 Gesamtlösung

```python
import csv

def lade_geraete_datei(dateiname):
    geraete = []
    with open(dateiname, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            geraet = {
                "name": row["Name"],
                "leistung": float(row["Leistung (W)"]),
                "dauer": float(row["Nutzungsdauer (h)"])
            }
            geraete.append(geraet)
    return geraete

def berechne_verbrauch(geraete):
    for g in geraete:
        g["verbrauch"] = (g["leistung"] * g["dauer"]) / 1000

def sortiere_geraete(geraete):
    geraete.sort(key=lambda x: x["verbrauch"])

def ausgabe_geraete(geraete):
    print("\n--- Sortierter Verbrauch ---")
    for i, g in enumerate(geraete):
        status = ""
        if i == 0:
            status = " (effizientestes)"
        elif i == len(geraete) - 1:
            status = " (höchster Verbrauch)"
        print(f"{g['name']}: {g['verbrauch']:.2f} kWh/Tag{status}")

def speichere_geraete_csv(geraete, dateiname):
    with open(dateiname, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Leistung (W)", "Nutzungsdauer (h)", "Verbrauch (kWh)"])
        for g in geraete:
            writer.writerow([g["name"], g["leistung"], g["dauer"], f"{g['verbrauch']:.2f}"])

# Hauptprogramm
geraete = lade_geraete_datei("geraete.csv")
berechne_verbrauch(geraete)
sortiere_geraete(geraete)
ausgabe_geraete(geraete)
speichere_geraete_csv(geraete, "verbrauchsauswertung.csv")
``` -->

---

## 🏁 Zusammenfassung

✅ Du hast ein komplettes Analyseprogramm erstellt  
✅ Du kannst CSV-Dateien einlesen, berechnen, analysieren und exportieren  
✅ Du hast mit Python-Datenstrukturen, Schleifen, Funktionen und dem CSV-Modul gearbeitet

---

> 🎓 Wenn du möchtest, erweitere das Programm um eine grafische Darstellung (z. B. mit `matplotlib`) oder eine Verbrauchsprognose über ein Jahr!
