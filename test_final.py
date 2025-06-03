def ber_verbruik(vermogen, uren, dagen):
    kwh = (vermogen / 1000) * uren * dagen
    return kwh

def ber_kosten(verbruik, prijs):
    kosten = verbruik * prijs
    return kosten

totaal_verbruik = 0
totaal_kosten = 0

while True:
    vermogen = float(input("Voer vermogen in (w): "))
    uren = float(input("Voer aantal uren per dag in: "))
    dagen = float(input("Voer aantal dagen in: "))
    prijs = float(input("Voer prijs in: "))

    verbruik = round(ber_verbruik(vermogen, uren, dagen))
    kosten = round(ber_kosten(verbruik, prijs))

    print(f"Verbruik: {verbruik} kWh")
    print(f"Kosten: SRD {kosten}")

    totaal_verbruik += verbruik
    totaal_kosten += kosten

    antwoord = input("Wil je nog een apparaat invoeren? (ja/nee): ")
    if antwoord.lower() != "ja":
        print("Programma stopt.")
        break

print(f"Totaal verbruik: {totaal_verbruik} kWh")
print(f"Totaal kosten: SRD {totaal_kosten}")
