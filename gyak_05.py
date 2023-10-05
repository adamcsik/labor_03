# Beléptetőrendszer
def regisztracio():
    felhasznalonev()
    jelszo_bekerese()
    jelszo_ellenorzese()
    ok_regisztracio = True
    return ok_regisztracio

def felhasznalonev():
    felhasznalo_email = input("Kérem az email címét: ")
    while " " in felhasznalo_email or "@" not in felhasznalo_email or "." not in felhasznalo_email:
        felhasznalo_email = input("Nem megfelelő az amail!!!\nKérem az email címét: ")

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
        if ok_jelszo:
            ok_jelszo = False
        else:
            felhasznalo_jelszo = input("Nem jó a jelszó!!!\nKérek egy jelszót (1,a,A, min 8 kar.): ")
            ok_jelszo = True
def jelszo_ellenorzese():
    pass

def beleptetes():
    pass


# Innen indul majd a program
felhasznalo_email = ""
felhasznalo_jelszo = ""
jelszo_bekerese()
if regisztracio():
    beleptetes()
