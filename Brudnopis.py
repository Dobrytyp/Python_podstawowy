class Człowiek:
    def __init__(self, imię, nazwisko, wzrost, waga, stawka, godziny):
        self.imię = imię
        self.nazwisko = nazwisko
        self.wzrost = wzrost
        self.waga = waga
        self.stawka = stawka
        self.godziny = godziny

    def bmi(self):                  # określamy metodę
        bmi = self.waga / (self.wzrost/100) ** 2
        if bmi < 18.5:
            return "niedowaga"
        elif bmi <25:
            return "Optimum"
        elif bmi < 30:
            return "nadwaga"
        else:
            return "otyłość"

    def __str__(self):          # tu definiujemy co ma zostac zwróconę
        return f"{self.imię} {self.nazwisko}, ma wskaźnik BMI na poziomie: {self.bmi()}, zarabia {self.stawka} złotych. Przeprcował/a {self.godziny} godzin w tym miesiącu. Zarobił/a  {self.stawka * self.godziny} złotych brutto"    # musi być ()

marek = Człowiek("Marek", "Klepczarek", 187, 82, 18, 182)
janina = Człowiek("Janina", "Kowalska", 164, 72, 40, 170)
grzegorz = Człowiek("Grzegorz", "Wolski", 178, 89, 60, 168)
halina = Człowiek("Halina", "Białek", 168, 62, 25, 160)

print(marek)
print(janina)
print(grzegorz)
print(halina)