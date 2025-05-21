from temperatur import celsius_to_fahrenheit, celsius_to_kelvin

celsius = float(input("Gib die aktuelle Temperatur ein:"))

fahrenheit = celsius_to_fahrenheit(celsius)
kelvin = celsius_to_kelvin(celsius)

print(f"Fahrenheit: {fahrenheit}, Kelvin: {kelvin}")
