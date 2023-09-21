# Jövedelemszámítás
print("Jövedelemszámítás")
brutto = int(input("Mennyi a bruttód:"))
kor = int(input("Hány éves vagy?"))
if kor > 25:
    gyerek = input("Van 3 gyereked és nő vagy (igen/nem)?")
    while gyerek not in ["igen", "Igen", "i", "I", "nem", "Nem", "n", "N"]:
        gyerek = input("Nem jó a válasz!!!!\nVan 3 gyereked és nő vagy (igen/nem)?")
if kor <= 25 or gyerek in ["igen", "Igen", "i", "I"]:
    if brutto > 500000:
        szja = (brutto - 500000) * 0.15
    else:
        szja = 0
else:
    szja = brutto * 0.15

print("Adók".center(40))
print("SZJA:".ljust(30, "_"), str(int(szja)).rjust(10, "_"), " Ft", sep="")
print("Nyugdíj:".ljust(30, "_"), str(int(brutto * 0.1)).rjust(10, "_"), " Ft", sep="")
print("TB:".ljust(30, "_"), str(int(brutto * 0.07)).rjust(10, "_"), " Ft", sep="")
print("Mkvállalói:".ljust(30, "_"), str(int(brutto * 0.015)).rjust(10, "_"), " Ft", sep="")
print("")
print("Nettó:".ljust(30, "_"), str(int(brutto - szja - brutto * 0.185)).rjust(10, "_"), " Ft", sep="")
