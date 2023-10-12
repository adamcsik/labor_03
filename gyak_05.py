# Beléptetőrendszer
def regisztracio():
    felhasznalo_email = felhasznalonev()
    felhasznalo_jelszo = jelszo_bekerese()
    if jelszo_ellenorzese(felhasznalo_jelszo, 3):
        ok_regisztracio = True
        with open("felhasznalok.csv", "a", encoding="utf-8") as fajl:
            fajl.write(felhasznalo_email + ";" + felhasznalo_jelszo + "\n")
    else:
        ok_regisztracio = False
    return ok_regisztracio

def felhasznalonev():
    felhasznalo_email = input("Kérem az email címét: ")
    while " " in felhasznalo_email or "@" not in felhasznalo_email or "." not in felhasznalo_email:
        felhasznalo_email = input("Nem megfelelő az amail!!!\nKérem az email címét: ")
    return felhasznalo_email

def jelszo_bekerese():
    ok_jelszo = True
    felhasznalo_jelszo = input("Kérek egy jelszót (1,a,A, min 8 kar.): ")
    while ok_jelszo:
        if len(felhasznalo_jelszo) < 8:
            ok_jelszo = False

        van = 0
        for i in range(len(felhasznalo_jelszo)):
            if felhasznalo_jelszo[i].isnumeric():
                van += 1
        if van == 0:
            ok_jelszo = False

        van = 0
        for i in range(len(felhasznalo_jelszo)):
            if felhasznalo_jelszo[i].isupper():
                van += 1
        if van == 0:
            ok_jelszo = False

        van = 0
        for i in range(len(felhasznalo_jelszo)):
            if felhasznalo_jelszo[i].islower():
                van += 1
        if van == 0:
            ok_jelszo = False

        if ok_jelszo:
            ok_jelszo = False
        else:
            felhasznalo_jelszo = input("Nem jó a jelszó!!!\nKérek egy jelszót (1,a,A, min 8 kar.): ")
            ok_jelszo = True
    return felhasznalo_jelszo

def jelszo_ellenorzese(felhasznalo_jelszo, probalkozas):
    jelszo2 = input("Kérem ismét írja be a jelszót: ")
    i = 1
    while jelszo2 != felhasznalo_jelszo and i < probalkozas:
        jelszo2 = input("Nem megfelelő a jelszó!\nKérem ismét írja be a jelszót: ")
        i += 1
    if jelszo2 == felhasznalo_jelszo:
        egyezes = True
    else:
        egyezes = False
    return egyezes

def beleptetes():
    pass


# Innen indul majd a program
if regisztracio():
    print("Sikeres volt a regisztráció!\nElindítjuk az első beléptetést!")
    beleptetes()
else:
    print("Nem sikerült a regisztráció! Próbálja meg újra!")
