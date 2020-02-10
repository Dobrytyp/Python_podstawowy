# def count_digits(lista):
#     count = {}
#     for elem in lista:
#         count[elem] = count.get(elem, 0) + 1 # gdy robimy get na słowniku to liczy
#     return count
#
# pierwsza_lista = [1, 2, 3, 4, 4]
# druga_lista = [1, 2, 3, 4, 4, 2, 9]
# pierwszysw_słownik = count_digits(pierwsza_lista)
# drugi_słownik = count_digits(druga_lista)
#
# czy_zawiera = True
# for key, value in pierwszysw_słownik.items():
#     if key not in drugi_słownik or value >drugi_słownik[key]:
#         czy_zawiera = False
#         break
# print(czy_zawiera)

## Albo

# def count_digits(lista):
#     count = {}
#     for elem in lista:
#         if elem in count:
#             count[elem] += 1
#         else:
#             count[elem] = 1
#         return count
#
# pierwsza_lista = [1, 2, 3, 4, 4]
# druga_lista = [1, 2, 3, 4, 4, 2, 9]
# pierwszysw_słownik = count_digits(pierwsza_lista)
# drugi_słownik = count_digits(druga_lista)
#
# czy_zawiera = True
# for key, value in pierwszysw_słownik.items():
#     if key not in drugi_słownik or value >drugi_słownik[key]:
#         czy_zawiera = False
#         break
# print(czy_zawiera)

# #albo
# pierwsza_lista = [1, 2, 3, 4, 4]
# druga_lista = [0, 3, 4, 5, 1, 2, 9]
#
# pierwsza_lista = sorted(pierwsza_lista)
# druga_lista.sort()
#
# idx = 0
# czy_zawiera = True
# for elem in pierwsza_lista:
#     if not elem in druga_lista[idx:]: #  idx: znaczy, że do końca listy
#         czy_zawoera = False
#         break
#     idx = druga_lista.index(elem) + 1
#
# print(czy_zawiera)

# Napisz Funkcję która sprawdz czy podana liczba jest pierwsza
#
#
# def nazwa_funkcji(a):
#     czy_pierwsza = True  # ustalamy warunek
#     for i in range(2, a): # dla każdego przypadku od 2 do ustalonej a
#         if a % i == 0: # jeżeli reszta z dzielenia
#             czy_pierwsza = False
#             break
#
#     return czy_pierwsza
#
# print(nazwa_funkcji(8))

#albo
#
# def czy_pierwsza(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# assert czy_pierwsza(7) # assert wykona się bez błędu jeżeli wartośc logiczna jest true
# assert czy_pierwsza(11)


# Funkcja o zmiennej licznie argumentów, zwracjaća średnią przezkazanych liczb
#
# def srednia(*liczby):
#     wynik = 0
#     for i in range(0, len(liczby)):
#         wynik += liczby[i]
#
#     return wynik/ len(liczby)
#
# print(srednia(10,5,20))

#albo
# def srednia(*args):
#     suma = 0
#     for elem in args:
#         suma += elem
#     return suma / len(args)
#
# print(srednia(3,4,5))

# Napisz funkcję która zwróci n jako !n
# wzór
# dla n = 0
# dla n*(n-1)!

# def silnia(n):
#     if n == 0:
#         return 1
#     else:
#         return n * silnia(n-1) # rekurencja!
#
# print(silnia(5))

#albo

# def silnia_iteracyjnie(n):
#     silnia = 1
#     for i in range(1, n+1):
#         silnia *= i
#     return silnia
#
# print(silnia_iteracyjnie(5))


# PYTANIE REKRUTACYJNE Sprawdź co się się dzieje

# def dodaj_do_listy(element, lista=[]):
#     lista.append(element)
#     return lista
#
# lista = [1, 2, 3]
# lista2 = dodaj_do_listy(5, lista)
# print(lista)
#
# lista2 = dodaj_do_listy(5)
# print(lista2)
# lista3 = dodaj_do_listy(8)
# print(lista3)

#========  Teraz jest ok bo zmienna dodaj_do_listy bedzie czyszczona

# def dodaj_do_listy(element, lista=None):
#     if lista == None:
#         lista = []
#     lista.append(element)
#     return lista
#
# print(dodaj_do_listy(5, [1, 2, 3]))
# print(dodaj_do_listy(5))
# print(dodaj_do_listy(8))

#zapisywanie do pliku

#Jak otwierać pliki

# f = open("plik tekstowy.txt, 'r")
# print(f.read)

# f = open("C:\\Users\eliza\Documents\python.txt", "r")
# print(f.read())
#
# f = open("C:\\Users\eliza\Documents\python.txt", "r")
# print(f.readlines())

# Zapisywanie
# f = open("\\Users\eliza\Documents\python3.txt", "w")
# f.write("python is cool\n"
#         "python is cool\n"
#         "Python is cool")


# f = open("\\Users\eliza\Documents\python3.txt", "w")
# f.write("Jeśli będziez starał się i pracował wystarczająco ciężko. To uda ci się zastąpić pustkę w swoim życiu, zmęczeniem")

# f = open("c:\\Users\eliza\Documents\python3.txt", "a")  # dopisywanie na końcu
# f.write("\nSiema")

# with open("c:\\Users\eliza\Documents\python3.txt", "r") as f: # dopisywanie na końcu
#     print(f.read())


#Stwórz plik tekstowy w notatniku, gdzie będzie kilka linii tekstu. Następnie odczytaj go w kodzie pythonowym,
# zamień każde słowo na wielkie litery, a następnie zapisz w innym pliku

# f = open("C:\\Users\eliza\Documents\\nova.txt", "w")
# f.write("python is cool\n"
#         "python is cool\n"
#         "python is cool\n")
#
# f = open("C:\\Users\eliza\Documents\\nova.txt", 'r') as zmienna:
# lista = zmienna.readlines()
# print(lista)
#
# nowa_lista = []
# for elem in lista:
#     nowa_lista.append(elem.upper())
#
# with open("plik tesktowy2.txt", "w") as zmienna2:
#     zmienna2/writelines(nowa_lista)

#albo
#
# with open("plik tekstowy.txt", "r") as f1:
#     new_list = []
#     for line in f1:
#         new_list.append(line.upper())
#
# with open("plik tekstowy2.txt", "w") as f2:
#     for x in new_list:
#         f2.write(x)

# with open("plik tkest3.txt", 'w') as plik:
#     lista = ["Ala", "ma", "kota"]
#     for elem in lista:
#         plik.write(elem + "\n")
#
# f = open("C:\\Users\eliza\Documents\\nova.txt", 'r') as zmienna:
# lista = zmienna.readlines()
# print(lista)
#
# nowa_lista = []
# for elem in lista:
#     nowa_lista.append(elem.upper())
#
# with open("plik tesktowy2.txt", "w") as zmienna2:
#     zmienna2/writelines(nowa_lista)

# import os   # sprawdzamy czy istnieje taki plik a jeśli nie, to tworzymy pana tadeusza
# if os.path.isfile("pan_tadeusz.txt") is False:
#     f = open("pan_tadeusz.txt", "w")
#     f.write("Litwo ojczyzno moja\n"
#             "Ty jesteś jak zdrowie\n")
#     f.close()
# f = open("pan_tadeusz.txt", "r")
# print(f.read())
#
#
# import os
# filename = "pan tadeusz2.txt"
# if os.path.isfile(filename):
#     with open(filename, "r") as plik:
#         print(plik.read())
# else:
#     with open(filename, "w") as plik:
#         plik.write("Litwo ojczyzna moja/\n"
#                    "Ty jesteś jak zdrowie")
#         print(plik.read())

# import os #
# filename = "pan tadeusz4.txt"
# if os.path.isfile(filename):
#     with open(filename, "r") as plik:
#         print(plik.read())
# else:
#     with open(filename, "w+") as plik:
#         plik.write("Litwo ojczyzna moja/\n"
#                    "Ty jesteś jak zdrowie")
#         plik.seek(0) # tu możemy kazac czytać plik od początlu, domyśłnie jest na końcu ostatneij operacji
#         print(plik.read())

# zmodyfiuj by usuwał plik był usuwany jak istnieje
#
# import os #
# filename = "pan tadeusz4.txt"
# if os.path.isfile(filename):
#     os.remove(filename)
# else:
#     with open(filename, "w+") as plik:
#         plik.write("Litwo ojczyzna moja/\n"
#                    "Ty jesteś jak zdrowie")
#         plik.seek(0) # tu możemy kazac czytać plik od początlu, domyśłnie jest na końcu ostatneij operacji
#         print(plik.read())

# Programowanie obiektpwe

# class Dog:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
#
#     def desription(self):
#         return f"{self.name}, {self.age}"
#
#     def make_sound(selfself, number):
#         return "Hau! " * number
#
# philo = Dog("Philo", 5)
# mikey = Dog("mikey", 6)
#
# print(philo.desription())
# print(mikey.make_sound(5))

#
# #
# class Osoba:
#     def __init__ (self, imie, nazwisko, wzrost, waga):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.wzrost = wzrost
#         self.waga = waga
#
#     def imie_i_nazwisko(self):
#         return f"{self.imie}, {self.nazwisko}"
#
#     def make_sound(self, number):
#         return "Dzień dobry " * number
#
#     def bmi(self):
#         bmi = self.waga / self.wzrost** 2
#         if bmi < 18.5:
#             return "niedowaga"
#         elif bmi <25:
#             return "Optimum"
#         elif bmi < 30:
#             return "nadwaga"
#         else:
#             return "otyłość"
#
#     def __str__(self): # __str__ zwraca informacje n.p. Patrz niżej
#         return f"{self.imie} {self.nazwisko} waży {self.waga} kilogramów. ma {self.bmi()}" # tu muszą być ()
#
#
#
# osoba1 = Osoba("Marian", "Paździoch", 1.65, 92)
# osoba2 = Osoba("Grzegorz", "Brzęczyszczykiwiecz", 1.82, 88)
#
# print(osoba1.imie_i_nazwisko())
# print(osoba2.make_sound(2))
# print(osoba1)
#
#
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is a dog. {self.age} years old."

class Labrador(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.size = "big"

    def make_sound(self):
        return "WOOOOOF!"

class York(Dog):
    def __init__(self, name, age, size="small"):
        super().__init__(name, age)
        self.size = size

    def make_sound(self):
        return "hau"

dog1 = York("baron", 12, "small")
#

# Zadanie stwórz klase osoba

# class Osoba:
#     def __init__ (self, imie, nazwisko, wzrost, waga):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.wzrost = wzrost
#         self.waga = waga
#
#     def imie_i_nazwisko(self):
#         return f"{self.imie}, {self.nazwisko}"
#
#     def make_sound(self, number):
#         return "Dzień dobry " * number
#
#     def bmi(self):
#         bmi = self.waga / self.wzrost** 2
#         if bmi < 18.5:
#             return "niedowaga"
#         elif bmi <25:
#             return "Optimum"
#         elif bmi < 30:
#             return "nadwaga"
#         else:
#             return "otyłość"
#
#     def __str__(self): # __str__ zwraca informacje n.p. Patrz niżej
#         return f"{self.imie} {self.nazwisko} waży {self.waga} kilogramów. ma {self.bmi()}" # tu muszą być ()
# #
# # osoba1 = Osoba("Marian", "Paździoch", 1.65, 92)
# # osoba2 = Osoba("Grzegorz", "Brzęczyszczykiwiecz", 1.82, 88)
#
# # print(osoba1.imie_i_nazwisko())
# # print(osoba2.make_sound(2))
#
# class Pracownik(Osoba):  # dodajemy nową klasę
#     def __init__(self, imie, nazwisko, wzrost, waga, stawka, godziny):
#         super().__init__(imie, nazwisko, wzrost, waga)
#         self.stawka = stawka
#         self.godziny = godziny
#
#
#
# prac1 = Pracownik("Arek", "klepczarek", 1.72, 67, 40, 170)
#
#
# print(prac1.stawka)
# print(prac1.godziny)





