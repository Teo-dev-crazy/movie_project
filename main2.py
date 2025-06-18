import os

def hernoem_en_nummer_bestanden(mappad):
    if not os.path.isdir(mappad):
        print(f"De map '{mappad}' bestaat niet.")
        return

    bestanden = sorted([
        bestand for bestand in os.listdir(mappad)
        if os.path.isfile(os.path.join(mappad, bestand))
    ])

    originele_namen = []

    for index, origineel in enumerate(bestanden, start=1):
        _, extensie = os.path.splitext(origineel)
        nieuwenaam = f"movie_poster_{index:02d}{extensie}"
        oudpad = os.path.join(mappad, origineel)
        nieuwpad = os.path.join(mappad, nieuwenaam)
        os.rename(oudpad, nieuwpad)
        originele_namen.append(origineel)
        print(f"Hernoemd: {origineel} → {nieuwenaam}")

    met_open = os.path.join(mappad, "originele_bestandsnamen.txt")
    with open(met_open, "w", encoding="utf-8") as f:
        for naam in originele_namen:
            f.write(naam + "\n")

    print(f"Originele bestandsnamen opgeslagen in '{met_open}'.")

def herstel_naar_originele_namen(mappad):
    bestandspad = os.path.join(mappad, "originele_bestandsnamen.txt")
    if not os.path.exists(bestandspad):
        print("Geen bestand met originele namen gevonden.")
        return

    with open(bestandspad, "r", encoding="utf-8") as f:
        originele_namen = [regel.strip() for regel in f.readlines()]

    huidige_bestanden = sorted([
        bestand for bestand in os.listdir(mappad)
        if os.path.isfile(os.path.join(mappad, bestand)) and bestand.startswith("movie_poster_")
    ])

    if len(huidige_bestanden) != len(originele_namen):
        print("Aantal huidige bestanden komt niet overeen met het aantal originele namen.")
        return

    for huidig, origineel in zip(huidige_bestanden, originele_namen):
        oudpad = os.path.join(mappad, huidig)
        nieuwpad = os.path.join(mappad, origineel)
        os.rename(oudpad, nieuwpad)
        print(f"Hersteld: {huidig} → {origineel}")

    print("Alle bestanden zijn teruggezet naar hun originele namen.")

def main():
    print("1. Hernoem en nummer bestanden")
    print("2. Hernoem bestanden naar originele naam")
    keuze = input("Keuze ? ")

    if keuze == "1":
        mappad = input("Geef de naam van de map met afbeeldingen: ")
        hernoem_en_nummer_bestanden(mappad)
    elif keuze == "2":
        mappad = input("Geef de naam van de map met afbeeldingen: ")
        herstel_naar_originele_namen(mappad)
    else:
        print("Ongeldige keuze.")

if __name__ == "__main__":
    main()
