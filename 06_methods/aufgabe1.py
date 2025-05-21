def eingabe_der_werte():
    breite = float(input("Breite des Raumes (m): "))
    laenge = float(input("Länge des Raumes (m): "))
    hoehe = float(input("Höhe des Raumes (m): "))
    t_innen = float(input("Innentemperatur (Grad Celsius): "))
    t_aussen = float(input("Außentemperatur (Grad Celsius): "))

    volumen = breite * laenge * hoehe
    dt = t_innen - t_aussen
    return volumen, dt

def berechne_heizleistung(l_volumen, l_dt):
    return l_volumen * l_dt * 0.024

volumen, dt= eingabe_der_werte()

if dt < 0:
    print(f"Achtung die Temperaturdifferenz ist kleiner als {dt} < 0")

heizleistung = berechne_heizleistung(volumen, dt)
print(f"benötigte Heizleistung beträgt: {heizleistung}kw")