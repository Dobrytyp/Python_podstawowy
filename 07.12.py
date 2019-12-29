# Zadanie 1

# def is_palindrom(napis):
#     napis = "".join(napis.lower().split()) # split dzieli wyrazy
#     return napis == napis[::-1]
#
# is_palindrom("ala ma kota")

# Zadanie 2
# Napisz funkcję, która sprawdzi, czy podany jako argument napis jest pangramem
# (tj. zawiera każdą literę alfabetu co najmniej raz, np. „The quick brown fox jumps over the lazy dog”).

# import string
#
# def is_pangram1(napis):
#     count_letters = {}
#     napis = "".join(napis.lower(). split())
#     for znak in napis:
#         count_letters[znak] = count_letters.get(znak, 6) +1
#
#     alphabet = set(string.ascii_lowercase)
#     return set(count_letters.keys()) == alphabet
#
# print(is_pangram1("the quick brown fox jumps over the lazy dog"))

# Albo

# from collections import Counter
#
# def is_pangram2(napis):
#     napis = "".join(napis.lower().split())
#     return len(Counter(napis).keys()) == 26
#
# print(is_pangram2("the quick brown fox jumps over the lazy dog"))

# Albo
# import string
#
# def is_pangram3(napis):
#     napis = "".join(napis.lower().split())
#     alphabet = set(string.ascii_lowercase)
#     for znak in alphabet:
#         if znak not in napis:
#             return False
#     return True
#
# print(is_pangram3("the quick brown fox jumps over the lazy dog"))



# Zadanie 3
# Napisz funkcję, która zamieni liczbę w zapisie rzymskim na dziesiętny.

# roman_numbers = {    # Ten słownik jest do wszystkich przykłądów tego zadania
#     "I":1,
#     "V":5,
#     "X":10,
#     "L":50,
#     "C":100,
#     "D":500,
#     "M":1000
# }

# def roman_to_int_rec(roman_number): # nie działa
#     if not roman_number:
#         return 0
#     if len(roman_number) == 1:
#         return roman_numbers[roman_number]
#     first = roman_numbers[roman_number[0]]
#     second = roman_numbers[roman_number[1]]
#     if first < second:
#         return second - first + roman_to_int_rec(roman_number[2:0])
#     else:
#         return first + roman_to_int_rec(roman_number[1:0])
#
# roman_to_int = roman_to_int_rec
# print(roman_to_int("XL"))
# print(roman_to_int("LXXX"))

# Albo

# def roman_to_int_iter(roman_number):
#     suma = 0
#     idx = 0
#     while idx < len(roman_number):
#         first = roman_numbers[roman_number[idx]]
#         if idx + 1 <len(roman_number):
#             second = roman_numbers[roman_number[idx+1]]
#             if first < second:
#                 suma += second - first
#                 idx += 2
#             else:
#                 suma+= first
#                 idx +=1
#         else:
#             suma += first
#             idx += 1
#     return suma
#
# roman_to_int = roman_to_int_iter
# print(roman_to_int("XL"))
# print(roman_to_int("LXXX"))

#Albo

# def roman_to_int_iter2(roman):
#     suma = 0
#     for i in range(0, len(roman)):
#         if i == len(roman) - 1:
#             suma += roman_numbers.get(roman[i])
#             return suma
#         elif roman_numbers.get(roman[i]) < roman_numbers.get(roman[i+1]):
#             suma += roman_numbers.get(roman[i])
#         else:
#             suma += roman_numbers.get(roman[i])
#
# roman_to_int = roman_to_int_iter2
# print(roman_to_int("XL"))
# print(roman_to_int("LXXX"))


# Zadanie 4
# Napisz funkcję, która sprawdzi, czy podana liczba jest doskonała
# (tj. jest sumą swoich dzielników właściwych, np. 6 = 1 + 2 + 3).

# def is_perfect(liczba):
#     suma = 0
#     for x in range(1, liczba):
#         if liczba % x == 0:
#             suma += x
#     return suma == liczba
#
# print(is_perfect(6))
# print(is_perfect(9))


# zadanie 5
# Napisz funkcję, która obliczy wartość zadanego elementu ciągu Fibonacciego rekurencyjnie i iteracyjnie.

# def fibonacci_recursive(n):   # sposób rekurencyjny
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)
#
# print(fibonacci_recursive(5))
# print(fibonacci_recursive(19))

# albo

# def fibonacci_iterative(n):
#     fibonacci = [0, 1]
#     for i in range(2, n+1):
#         fibonacci.append(fibonacci[i-2]) + fibonacci[i-1])
#     return fibonacci[n]
#
# print(fibonacci_iterative(5))
# print(fibonacci_iterative(19))
#

# zadanie 6

# def is_lap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 4 == 0 and year % 100 != 0:
#         return True
#     else:
#         return False
#
# print(is_lap_year(2020))


# Zadanie 7
# Wyobraź sobie, że obsługujesz sklep. Wszystkie produkty, które posiadasz w magazynie,
# wraz z ich cenami oraz dostępną liczbą przechowujesz w słowniku (hint: zagnieżdżonym słowniku :D).
# Pozwól użytkownikowi podać nazwę produktu, który chce nabyć oraz liczbę sztuk, następnie sprawdź,
# czy posiadasz taki produkt w tej ilości na stanie, a na koniec zwróć informację o cenie do zapłaty.

# sklep = {
# #     "bułka": {
# #         "cena" : 1.5,
# #         "ilość" : 300
# #     }
# #     "chleb" : {
# #         "cena" : 3,
# #         "ilość" : 200
# #     }
# #     "rogalik": {
# #         "cena" : 10,
# #         "ilość" : 3
# #     }
# # }
# #
# # produkt = input("czego chcesz?\n")
# # ]if -rodukt in sklep:
# #     ilość = int(input)

# Zadanie 8
# Napisz funkcję, która zwróci 5 najczęstszych słów z dzieła Mickiewicza https://pastebin.com/raw/aAHeW5Pt
# Ćwiczymy odczytywanie z pliku

# def most_common():
#     words_freq = {}
#     with open("to powinien być plik") as f:
#         for line in f:
#             words = line.lower().split()
#             for word in words:
#                 words_freq[word] = words_freq.get(word, 0) +1
#
#     print(sorted(words_freq.items(), key=lambda x: x[1], reverse=True)[:5])
#
# most_common()

# # Zadanie 9
# #
# # class Kolo:
# #     def __init__(selfself, promien):
# #         self.r = promien
# #
# #     def obwod(self):
# #
# #     def pole(self):
# #         return 2 * math.pi * self.r ** 2
# #
# # a = Kolo(4)
# # print(o)


# Zadanie 10
#
# class Produkt:
#     def __init__(self, nazwa, cena):
#         self.nazwa = nazwa
#         self.cena = cena
#
#     def __str__(self):
#         return f"produkt {self.nazwa}, o cenie {self.cena}"
#
#
# class Koszyk:
#     def __init__(self):
#         self.produkty = {}
#
#     def usun_wszystko(self):
#         self.produkty = {}
#
#     def pokaz(self):
#         for produkt, ilosc, in self.produkty.items():
#
#         print(self.produkty)
#
#     def oblicz_wartosc(self):
#         suma = 0
#         for produkt in self.produkty.items():
#             suma+= produkt.cena * ilość
#             print(suma)
#
#     def dodaj(self, produkt):
#         if produkt in self.produkty:
#             self.produkty[produkt] += 1
#         else:
#             self.produkty[produkt] = 1
#
#
# produkt1 = Produkt("komputer", 3000)
# produkt2 = Produkt("zegarek", 500)
# produkt3 = Produkt("chleb", 3000)
#
# koszyk = Koszyk()
# koszyk.dodaj


# Klasy

# class Prostokąt:
#     def __init__ (self, bok_a, bok_b):
#         self.bok_a = bok_a
#         self.bok_b = bok_b
#
#     def pole(self):
#         return self.bok_a * self.bok_b
#
#     def obwod(self):
#         return 2 * (self.bok_a + self.bok_b)
#
# p1 = Prostokąt(5, 7)
# p2 = Prostokąt(4, 5)
#
# # print(p1.obwod())
# # # print(p1.pole())
#
# class Kwadrat(Prostokąt):  # dodajemy nową klasę
#     def __init__(self, bok):
#         super().__init__(bok, bok) # Przkazujemy klasie prostokąt wartości z klasy kwadrat
#
#
# k1 = Kwadrat(6)
#
# print(k1.pole())
# print(k1.obwod())


# Dodatki

# def suma_iter(lst):
#     suma = 0
#     for elem in lst:
#         suma += elem
#     return suma
#
# lista = [2, 2, 2, 5, 3, 6, 3]
# print(lista)
# print(suma_iter(lista))
# print(lista)

#Albo

# def suma_rek(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         elem = lst.pop()
#         return  elem + suma_rek(lst)
#
# lista = [2, 2, 2, 5, 3, 6, 3]
# print(lista)
# print(suma_rek(lista))
# print(lista)

# inny przykład
# a = [1, 2, 3]
# b = a
# a = "hello"
# print(a, b)

# ale....

# a = [1, 2, 3]
# b = a
# b.append(5)
# print(a, b)

# rowiązanie:

# a = [1, 2, 3]
# b = a.copy()
# b.append(5)
# print(a, b)

#albo

# a = [1, 2, 3]
# b = list(a)
# b.append(5)
# print(a, b)

# Rozwiązanie problemu

# def suma_rek(lst):
#     lst2 = list(lst)
#     if len(lst2) == 1:
#         return lst2[0]
#     else:
#         elem = lst2.pop()
#         return  elem + suma_rek(lst2)
#
# lista = [2, 2, 2, 5, 3, 6, 3]
# print(lista)
# print(suma_rek(lista))
# print(lista)


# import os
#
# a = os.system("dir")
# print(a)
# print(type(a))



#!!!!!!!!!!!!!!!

# from subprocess import Popen, PIPE # Co to kurwa jest?
#
# a = Popen(["dir"], stdout=PIPE, stderr=PIPE).communicate()
# print(a)


# Funcja, którą przyjmuje listę, a zwraca liste kwadratów listy wyjściowej

# def kwadraty(lista):
#     nowa_lista = []
#     for elem in lista:
#         nowa_lista.append(elem ** 2)
#     return nowa_lista
#
# def kwadraty2(lista):
#     return [elem ** 2 for elem in lista] # Nawaisy kwadratowe tak naprawde tworzy listę - ! List comprehension !
#
#
# print(kwadraty([2, 3, 4, 5])) # [4, 9, 16, 25]
# print(kwadraty2([2, 3, 4, 5])) # [4, 9, 16, 25]


# od 1 do 100

# def parzyste():
#     lista = []
#     for i in range(0, 101):
#         if i % 2 == 0:
#             lista.append(i)
#     return lista
#
# print(parzyste())

# ale

# def parzyste2():
#     return [i for i in range(1, 101) if i %2 ==0]
#
# print(parzyste2())


# lista zwraca większe od 5

# def wieksze5(lista):
#     return [elem for elem in lista if elem > 5]
#
# print(wieksze5([2, 5, 7, 9]))



# Pobierz wartośc n a nastepnie stwórz słownik którego elementy dla i < n, będą postaci: (i, i2)

#
# def zwroc_slownik(n):
#     return {i: i**2 for i in range(0,n)}
#
# print(zwroc_slownik(10))

# albo krotki
# def zwroc_slownik(n):
#     return [(i, i**2, i ** 3) for i in range(0,n)]
#
# print(zwroc_slownik(10))

# Parzyste, nieparzyste

# def parzyste_nieparzyste_oraz_zero():
#     return ["parzyste" if i % 2 == 0 else "Nieparzyste" for i in range(0, 101)]
#
# print(parzyste_nieparzyste_oraz_zero())

#albo

# def parzyste_nieparzyste_oraz_zero():
#     return ["zero" if i == 0 else"parzyste" if i % 2 == 0 else "Nieparzyste" for i in range(0, 101)]
#
# print(parzyste_nieparzyste_oraz_zero())

# Funkcja która przyjmuje liste stringów a zwraca słwonik, gdzie kluczem jest string a wartością jego gługość

# def FKPLSAZS(napisy):
#     return [{i: len(i) for i in napisy}]
#
# print(FKPLSAZS(["głowa,", "noga", "oko"]))

# funkcja, która przyjmuję listę słów oraz listę słów zakazanyach a zwraca odfitrowaną pierwsza wejściową listę

# def filter_words(slowa, zakazane_slowa):
#     return [i for i in slowa if i not in zakazane_slowa]
#
# banned_words = ["i", "psa"]
# print(filter_words(["ala", "ma", "kota", "i", "psa"],banned_words))

# ile ma tysięcy ta liczba? (6)
liczba = 56475
print((liczba // 1000) %10)
