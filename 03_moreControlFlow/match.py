dayOfWeek = input("wochentag: ")

match dayOfWeek :
    case "Montag":
        print("Montag")
    case "Dienstag":
        print("Dienstag")
    case "Samstag" | "Sonntag":
        print(f"Es ist Wochenende, der Tag: {dayOfWeek} ist die nächsten 24 Stunden.")
    case _:
        print(f"Unbekannter Wochentag: {dayOfWeek}")