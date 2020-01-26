# Stwórz klaśe pies z atrybitami wiek, a nstępnir napisz program, który posortuje listę psów rosnąco wedłóg wieku, liczby znaków w m=imieniu oraz samym imieniu

# class Pies:
#     def __init__ (self, imie, wiek):
#         self.imie = imie
#         self.wiek = wiek
#
#     def __str__(self):
#         return f"Pies({self.imie}, {self.wiek}"
#
#     def __repr__(self):
#         return f"Pies({self.imie}, {self.wiek}"
#
#
# if __name__ == "__main__":
#     psy = [Pies("Burek", 4), Pies("Pik", 8), Pies("Conan", 5)]
#     print(psy)
#     sorted_psy = sorted(psy, key=lambda x: (x.wiek, len(x.imie), x.imie))
#     print(sorted_psy)

# ALBO

# class Pies:
#     def __init__ (self, imie, wiek):
#         self.imie = imie
#         self.wiek = wiek
#
#     def __str__(self):
#         return f"Pies({self.imie}, {self.wiek}"
#
#     def __repr__(self):
#         return f"Pies({self.imie}, {self.wiek}"
#
#     def __gt__(self, other):                        # o tu nowe rozwiązanie
#         return (self.wiek, len(self.imie),self.imie) > (other.wiek, len(other.imie), other.imie)
#
#
# if __name__ == "__main__":
#     psy = [Pies("Burek", 4), Pies("Pik", 8), Pies("Conan", 5)]
#     print(psy)
#     sorted_psy = sorted(psy)
#     print(sorted_psy)



# Zadanie 1
#
# lista = []
# for i in range(2000, 3200):
#     if i % 7 == 0 and i % 5 != 0:
#         lista.append(i)
#
#     for i in lista:
#         print(i, end= "; ")

 # Generator

# def zad1():
#
#     for i in range(2000, 3201):
#         if i % 7 == 0 and i % 5 != 0:
#             yield i
#
# liczby = zad1()
# for i in liczby:
#     print(i, end=": ")

# Albo list comprenhesion

# def sposob2(pocz, kon):
#     return [x for x in range(pocz, kon+1) if not x % 7 and x % 5]


# class SposobIterator:
#     def __init__(self, pocz, kon):
#         self.pocz = pocz - 1
#         self.kon = kon
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.pocz >= self.kon:
#             raise StopIteration
#
#         self.pocz +=1
#         if not self.pocz % 7 and self.pocz % 5:
#             return self.pocz
#         return self.__next__()
#
# liczby = SposobIterator(2000, 3200)
# for i in liczby:
#     print(i, end=": ")

# LAMBDA

# def sposob_lambda(pocz, kon):
#     return list(filter(lambda x: not x % 7 and x % 5, range(pocz, kon+1)))
#
# liczby = sposob_lambda(2000, 3200)
# for i in liczby:
#     print(i, end=": ")


# zadanie 3

# slowa = "głowa, noga, ropa, zaraza, anomalia"
# lista = slowa.split("'")
# string = str(sorted(lista))
# string = str(lista)
#
# string = string.replace("[", "")
# string = string.replace("]", "")
# string = string.replace("'", "")
#
# print(string)


# napis = "głowa, noga, ropa, zaraza, anomalia"
# slowa = [item.strip() for item in napis.split(",")]
# sorted_slowa = sorted(slowa, key=lambda x: x.lower())
# print(", ".join(sorted_slowa))


# zadanie 2

# def dwie_liczby(x, y):                  # Ale to jest żle, bo nie to to chodziło
#     for i in range(0, x):
#         for j in range(0, y):
#             print(i*j, end = "\t")
#
#         print()
#     return
#
# print(dwie_liczby(12, 7))


# def tabliczka(x, y):                  # Ale to jest żle, bo nie to to chodziło
#     lst = []
#     for i in range(x):
#         row = []
#         for j in range(y):
#             row.append(i * j)
#         lst.append(row)
#
#     return lst
#
# tablica = tabliczka (10, 20)
# for row in tablica:
#     print("\t".join([str(item) for item in row]))

# Albo

# def tabliczka(x, y):
#     lst = []
#     for i in range(x):
#         lst.append([i * j for j in range(y)])
#
#     return lst
#
# tablica = tabliczka (20, 20)
# for row in tablica:
#     print("\t".join([str(item) for item in row]))


# Zadanie 4


# from collections import defaultdict
#
# napis = "Ala, ma, kota, nie,Ma, plastik, plasTIK"
# lista_slow = [item.strip() for item in napis.split(",")]
# dict_forms = defaultdict(list)
#
# for slowo in lista_slow:
#     dict_forms[slowo.lower()].append(slowo)
#
# unikalne = [value[0] for key, value in dict_forms.items() if len(value) == 1]
# print(unikalne)


# Zadanie 5

# def cyfry_parzyste(number):
#     while number > 0:
#         if (number % 10) % 2 % 2:
#             return  False
#         number = number // 10
#     return True


# print(cyfry_parzyste())

# Albo


# import re
#
# def cyfry_parzyste2(number):
#     pattern = r"^-?[2468]?[02468]+$"
#     return bool(re.match(pattern, str(number)))
#
# def zwroc_liczby(pocz, kon):
#     return [x for x in range(pocz, kon+1) if cyfry_parzyste(x)]
#
# print(cyfry_parzyste2(2468))


# Zadanie 8

 # Generator

# def generator8(n):
#     for i in range(1, n + 1):
#         if i % 7:
#             yield i
#
# for i in generator8(14):
#     print(i, end=", ")


# class iterator8:
#     def __init__(self, n):
#         self.n = n
#         self.number = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.number == self.n:
#             raise StopIteration
#
#         self.number += 1
#         if self.number % 7:
#             return self.number
#         return self.__next__()
#
# liczby = iterator8(20)
# for i in liczby:
#     print(i, end=", ")

#----------------------------------------------------

# Utwórz klasę Osoba przyjmującą parametr name i balance. Niezbędna również będzie metoda reprezentacji obiektu oraz metoda
# borrow() przyjmującą jakiś obiekt i kwotę jako parametr, aby w razie potrzeby pożyczyć od innej Osoby pieniądze.
# Pożyczać pieniądze możesz tylko w przerwie w kursie czyli 11:00 - 11:20 oraz 13:00 - 13:30. Należy to obslużyć dekoratorem.
# Uwzględnij, że jeden obiekt może nie mieć pieniędzy aby pożyczyć drugiemu. Przetestuj dzialanie programu tj utwórz
# minimum 2 instancje klasy, pożycz pieniadze o ile umozliwia to obecna godzina.

class Osoba:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


    @borrow_time_limited
    def borrow(selfself, obiekt, kwota):
        if



    def __str__(self):
        return f'Osoba o imieniu {self.name} ma {self.balance}'

    def __repr__(self):
        return f'Osoba o imieniu {self.name} ma {self.balance}'

    def borrow(self, borrow):
        self.balance += borrow


osoba1 = Osoba("Marek Klepczarek", 1000)

osoba2 = Osoba("Grzgorz Puś", 2000)

print(osoba1)