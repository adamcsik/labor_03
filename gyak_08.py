from tkinter import *
from tkinter import messagebox
import gyak_09
from gyak_11 import *

def belepes_ablak():
    def reg_gomb_kezelse():
        belepes.destroy()

    def ok_gomb_kezelese():
        if fhsz.get() == "" or fjsz.get() == "":
            messagebox.showerror("Hiba", "Nem lehet üres egyik mező sem!")
        else:
            if ab_jelszokeres(fhsz.get()) == "":
                messagebox.showerror("Hiba", "Nincs regisztrálva vagy nm jó a jelszó!")
            else:
                messagebox.showinfo("Belépés", "Üdv a fedélzeten!")
                belepes.destroy()

    belepes = Tk()
    belepes.title("Belépés")

    felh_nev_cimke = Label(belepes, text="Felhasználó neve (email):")
    felh_jelszo_cimke = Label(belepes, text="Jelszó:")

    fhsz = StringVar()
    fhsz.set("")
    felh_nev = Entry(belepes, textvariable=fhsz, width=30)
    fjsz = StringVar()
    fjsz.set("")
    felh_jelszo = Entry(belepes, textvariable=fjsz, width=20)

    gomb_ok = Button(belepes, text="OK", command=ok_gomb_kezelese, width=10)
    gomb_reg = Button(belepes, text="Regisztráció", command=reg_gomb_kezelse)

    felh_nev_cimke.grid(row=0, column=0, pady=20, padx=10, sticky=E)
    felh_jelszo_cimke.grid(row=1, column=0, sticky=E, padx=10)
    felh_nev.grid(row=0, column=1, padx=10, sticky=W)
    felh_jelszo.grid(row=1, column=1, sticky=W, padx=10)
    gomb_ok.grid(row=2, column=0, pady=20)
    gomb_reg.grid(row=2, column=1)

    belepes.mainloop()

def reg_ablak():
    def ok_gomb_kezelese():
        if jsz.get() != jsz2.get():
            messagebox.showerror("Hiba", "Nem egyforma a két beírt jelszó!")
        elif jsz.get() == "" or jsz2.get() == "" or  fhnev.get() == "":
            messagebox.showerror("Hiba", "Nem lehet üres mező az ablakban")
        else:
            ab_rogzites(fhnev.get(), jsz.get())
            regisztracio.destroy()
    def jelszo_gomb_kezelese():
        pw.jelszo_generalasa()
        jsz.set(pw.jelszo)
        jsz2.set(pw.jelszo)


    regisztracio = Tk()
    regisztracio.title("Regisztráció")

    pw = gyak_09.Jelszo()

    felh_nev_cimke = Label(regisztracio, text="Felhasználó neve (email):")
    felh_jelszo_cimke =Label(regisztracio, text="Jelszó:")
    felh_jelszo2_cimke = Label(regisztracio, text="A jelszó ismét:")

    fhnev = StringVar()
    fhnev.set("")
    felh_nev = Entry(regisztracio, textvariable=fhnev, width=30)
    jsz = StringVar()
    jsz.set("")
    felh_jelszo = Entry(regisztracio, textvariable=jsz, width=20)
    jsz2 = StringVar()
    jsz2.set("")
    felh_jelszo2 = Entry(regisztracio, textvariable=jsz2, width=20)

    gomb_ok = Button(regisztracio, text="OK", command=ok_gomb_kezelese, width=15)
    gomb_jelszo = Button(regisztracio, text="Jelszó generálása!", command=jelszo_gomb_kezelese)

    felh_nev_cimke.grid(row=0, column=0)
    felh_jelszo_cimke.grid(row=1, column=0)
    felh_jelszo2_cimke.grid(row=2, column=0)
    felh_nev.grid(row=0, column=1)
    felh_jelszo.grid(row=1, column=1)
    felh_jelszo2.grid(row=2, column=1)
    gomb_ok.grid(row=3, column=0, columnspan=3, pady=10)
    gomb_jelszo.grid(row=1, column=2)

    regisztracio.mainloop()

ab_lerehoz()
#reg_ablak()
belepes_ablak()
ab_lezar()