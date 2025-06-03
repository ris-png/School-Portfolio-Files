woord = input("Voer een woord in: ")

def tel_klinker(woord):
    aantal = 0
    for letter in woord:
        if letter.lower() == "e":
            aantal += 1
    return aantal

letter_e = tel_klinker(woord)
print(f"Het aantal 'e' in het woord '{woord}' is: {letter_e}")