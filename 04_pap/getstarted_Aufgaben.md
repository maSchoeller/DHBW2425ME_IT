# Arbeitsblatt: Programmablaufpläne zu Gesellschaftsspielen

---

## Aufgabe 1: "Mensch ärgere dich nicht" – Würfeln für einen Spielzug

Ein Spieler darf ziehen, wenn er eine **6** würfelt. Bei einer 6 darf er nochmals würfeln, insgesamt aber **maximal dreimal**. Dies entspricht dem klassischen Einstieg in das Spiel, wenn sich die Spielfigur noch auf dem Startfeld befindet.

**Aufgabe:** Entwickeln Sie einen PAP, der diesen Ablauf abbildet. Modellieren Sie die Schleifenstruktur für die drei Würfe und die Entscheidung, ob der Spieler ziehen darf oder nicht.

**Hinweise:**
- Maximal drei Versuche
- Bei Wurf == 6: Spieler darf ziehen
- Achten Sie auf eine sinnvolle Initialisierung von Zählvariablen

---

## Aufgabe 2: "UNO" – Karte ziehen

Ein Spieler hat keine passende Karte auf der Hand und muss nun so lange Karten vom Nachziehstapel aufnehmen, bis er eine passende Karte erhält oder der Stapel erschöpft ist. Die Funktion `passt()` entscheidet, ob eine gezogene Karte spielbar ist.

**Aufgabe:** Entwickeln Sie einen PAP, der diesen Zug beschreibt und den Spielverlauf bei leerem Stapel korrekt behandelt.

**Hinweise:**
- Funktion `passt()` prüft, ob Karte spielbar ist
- Der Nachziehstapel kann leer werden
- Denken Sie an die Wiederholung (Schleife), bis eine passende Karte gezogen wurde

---

## Aufgabe 3: "Monopoly" – Aus dem Gefängnis freikaufen

Ein Spieler befindet sich im Gefängnis. Ihm stehen zwei Optionen offen: Entweder er zahlt 50 Geldeinheiten und kommt sofort frei oder er versucht, durch Würfeln eines Paschs innerhalb von drei Versuchen freizukommen.

**Aufgabe:** Entwickeln Sie einen PAP, der diesen Entscheidungsprozess abbildet. Der Ablauf sollte alle Möglichkeiten des Spielers berücksichtigen, inklusive automatischer Freilassung nach dem dritten Fehlversuch gegen Zahlung.

**Hinweise:**
- Wenn nach 3 Versuchen kein Pasch: Zahlung erforderlich
- Entscheidung am Anfang: zahlen oder würfeln
- Zähle und verarbeite die Würfelversuche sinnvoll

---

## Aufgabe 4: "Leiterspiel" – Spielfortschritt mit Leitern und Schlangen

Der Spieler würfelt und zieht auf einem Spielbrett mit 100 nummerierten Feldern vorwärts. Auf manchen Feldern befinden sich Leitern, die ihn weiter nach oben bringen, oder Schlangen, die ihn zurückfallen lassen. Die Position des Spielers muss daher nach jedem Wurf auf Sonderfelder geprüft und ggf. angepasst werden.

**Aufgabe:** Entwerfen Sie einen PAP, der die Bewegung inklusive der Spezialfelder realistisch simuliert und das Spiel fortsetzt, bis das Zielfeld 100 erreicht ist.

**Hinweise:**
- Wiederhole Züge, bis Feld 100 erreicht ist
- Nutze Datenstruktur für Spezialfelder (z. B. Dictionary oder Array)
- Achten Sie auf Bedingungen, wenn die Zielposition über 100 hinausgeht

---

## Aufgabe 5: "Die Siedler von Catan" – Ressourcen tauschen

Ein Spieler möchte eine Straße bauen, was 1 Holz und 1 Lehm kostet. Falls er diese Ressourcen nicht besitzt, kann er mit einem 4:1-Tausch vier gleiche Rohstoffe gegen einen gewünschten tauschen. Nach dem Tausch soll erneut geprüft werden, ob der Bau nun möglich ist.

**Aufgabe:** Entwickeln Sie einen PAP, der den Ablauf von Prüfung, Tausch und Bau realistisch abbildet. Achten Sie auf die Wiederholung der Prüfung nach einem erfolgreichen Tausch.

**Hinweise:**
- Ressourcen prüfen und strukturiert speichern (z. B. als Variablen)
- Tauschoption nutzen, wenn Bau nicht sofort möglich ist
- Nach jedem Tausch erneut prüfen, ob gebaut werden kann
- Endbedingung: entweder Bau erfolgreich oder nicht möglich

---

## Aufgabe 6: "Cluedo" – Verdacht äußern durch Ausschluss

In "Cluedo" versucht ein Spieler durch Ausschluss zu einer möglichen Täterkombination zu gelangen. Er kennt bereits einige Karten, die sich sicher nicht in der Lösung befinden. Der Spieler soll nun aus den verbleibenden Optionen zufällig eine gültige Kombination aus Person, Raum und Waffe auswählen.

**Aufgabe:** Entwickeln Sie einen PAP, der diesen logischen Auswahlprozess abbildet. Dabei sollen bekannte Karten vorher ausgeschlossen und aus den verbleibenden Listen jeweils ein Element gewählt werden.

**Hinweise:**
- Bekannte Karten aus den drei Kategorien entfernen
- Zufällige Auswahl aus den verbleibenden Optionen
- Strukturieren Sie die Auswahl in drei getrennte Blöcke (Person, Raum, Waffe)

---

