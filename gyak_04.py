# számológép
def adatkeres(tipus):
    valasz = 0
    if tipus == "sz":
        valasz = input("Kérek egy számot: ")
        while not valasz.isnumeric():
            print("Hibás szám!!!!")
            valasz = input("Kérek egy számot: ")
        valasz = int(valasz)
    elif tipus == "m":
        valasz = input("Milyen művelete legyen (+,-,*,/): ")
        while valasz not in ["+", "-", "*", "/"]:
            print("Nem jó a műveleti kód!!!")
            valasz = input("Milyen művelete legyen (+,-,*,/): ")
    return valasz


def szamitas():
    eredmeny = 0
    if muvelet == "+":
        eredmeny = szam1 + szam2
    elif muvelet == "-":
        eredmeny = szam1 - szam2
    elif muvelet == "*":
        eredmeny = szam1 * szam2
    elif muvelet == "/":
        eredmeny = szam1 / szam2
    return eredmeny


# A program indítási pontja
print("Számológép")
szam1 = adatkeres("sz")
muvelet = adatkeres("m")
szam2 = adatkeres("sz")
vegeredmeny = szamitas()

print(str(szam1).rjust(50))
print(muvelet, end="")
print(str(szam2).rjust(49))
print("".rjust(50, "-"))
print(str(vegeredmeny).rjust(50))
