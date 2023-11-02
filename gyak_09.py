class Felhasznalo:
    pass

class Jelszo:
    jelszo = ""
    def __init__(self):
        #self.jelszo_generalasa()
        pass

    def jelszo_bekerese(self):
        pass
    def jelszo_ellenorzese(self):
        pass

    def jelszo_generalasa(self, hossz=10, kisbetu=True, nagybetu=True, szam=True):
        import string
        import random
        jelszo = ""
        karaktersor = ""
        if kisbetu:
            karaktersor = karaktersor + string.ascii_lowercase
        if nagybetu:
            karaktersor = karaktersor + string.ascii_uppercase
        if szam:
            karaktersor = karaktersor + string.digits
        for _ in range(hossz):
            jelszo = jelszo + karaktersor[random.randint(0, len(karaktersor) - 1)]
        self.jelszo = jelszo


if __name__ == "__main__":
    pw = Jelszo()

    pw.jelszo_generalasa()
    print(pw.jelszo)

