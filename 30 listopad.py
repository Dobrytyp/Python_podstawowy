# zadanie 2

# Można if i porównywać lower. Źle przeczytaliśmy instrukcje! mogąbyć same duże litery


# zadanie 9

# lista1 = [1, 3, 2, 4]
# # lista2 = {5, 4, 57, 45, 6, 3, 2, 55, 1}
# #
# # zawiera = 0
# # for elem in lista1:
# #     if elem in lista2:
# #         zwiera = False
# #
# # if zawiera:
# #     print("lista 1 zawiera się w liście ")


# zadanie 10

# słowo  = input("Podaj swoje słowo\n").lower() #żeby duże litery wywalić
# if len(słowo) == len(set(słowo)):
#     print("jest izogramem")
# else:
#     print("nie jest izogramem")


# Zadanie 1 liczby od 1 do 10 bez podzielnych przez 3


# var1 = []
# for i in range(0, 11): # moze być bez 0
#     if i % 3 != 0:
#         var1.append(i)
# print(var1)

# albo while

# lista = []
# idx = -1
# while idx <10:
#     idx += 1
#     if idx % 3 == 0:
#         continue
#     lista.append(idx)
# print(lista)

# albo inny while
#
# lista = []
# idx = 0
# while idx < 11:
#     if idx % 3 != 0:
#         lista.append(idx)
#     idx +=1
# print(lista)

# jeszcze jeden przykład z for

# lista = []
# for i in range(11):
#     if i % 3 == 0: # doadajemy każdy element z listy, oprócz tych podzielnych przez 3
#         continue
#     lista.append(i)
# print(lista)

# Moduły!

# import random
# print(random.randint(0, 10))


# import random
# print(dir(random)) # oglądamy zawartość modułu
# print(help(random.randint))

# zadanie 2 6 losowych niepowtarzających się cyfr od 1 do 50

from random import randint
lista = []
while len(lista) < 6: # ma przerwać kiedy będzie miał 6 elementów
    liczba = randint(1, 50)  # zakres liczb losowych
    if not liczba in lista: # żeby się nie powtarzały
        lista.append(liczba)
print(lista)

# Albo z Continue zamiast not


# from random import randint
#
#
# lista = []
# while len(lista) < 6: # ma przerwać kiedy będzie miał 6 elementów
#     liczba = randint(1, 50)  # zakres liczb losowych
#     if liczba in lista: # żeby się nie powtarzały
#         continue
#     lista.append(liczba)
# print(lista)


# losowa liczba 0, 10 masz odgadnac za 3 razem


# print("Mam na myśli pewną liczbę z zakresu od 0 do 10.\n"
# "Spróbuj ją odgadnąć, w jak najmniejszej liczbie prób.")
# import random
# my_number = random.randint(0, 10)
# print(my_number)
# var1 = int(input()) #tu użytkownik podaje swoją liczbę
# tries = 0
# while var1 != my_number: # pętla zaczyna się jeśli nie zgadłeś
#     tries += 1
#     print("dawaj jeszcze raz")
#     var1 = int(input())  # tu użytkownik podaje swoją liczbę
#     if tries == 2:
#         print("przegrałeś")
#         break
# if var1 == my_number:
#     print("Brawo zgadłeś")

# albo

# from random import randint
# wylosowana_liczba = randint(0,10)
# proba = 0
# while proba < 3
#     liczba = int(input("POdaj liczbę\n"))
#     if liczba == wylosowana_liczba:
#         print("zgadłeś")
#         break
#     if proba < 2:
#         print("dawaj jeszcze raz")
#     proba += 1
# if proba == 3:
#     print("Hasta la vista baby")

# Albo

# from random import randint
# wylosowana_liczba = randint(0,10)
# proba = 0
# while True:
#     liczba = int(input("POdaj liczbę\n"))
#     if liczba == wylosowana_liczba:
#         print("zgadłeś")
#         break
#     if proba == 2:
#         print("Hasta la vista baby")
#         break
#     else:
#         print("Spróbuj jeszcze raz")
#     proba += 1

# Albo

# from random import randint
#
# liczba = randint(0,10)
# for i in range(3):
#     wpis =  int(input("podaj liczbę\n"))
#     if wpis == liczba:
#         print("zgadłeś")
#     elif i < 2:
#         print("spróbuj jeszcze raz")
#     else:
#         print("hasta la vista babe")


# ############# FUNKCJE ######################


# def nazwa_funkcji():
#     print("coś")
#
# nazwa_funkcji()

# # Jak działa funkcja
# def nazwa_funkcji(a, b, c):
#     zmienna = a + b + c
#     return zmienna
#
# print(nazwa_funkcji(10 ,20 ,30))


# def nazwa_funkcji(a, b, c):
#     zmienna = a + b + c
#     if zmienna < 0:
#         zmienna = -zmienna
#     return zmienna
#
# print(nazwa_funkcji(10 ,20 ,30))


# def nazwa_funkcji(a, b, c):
#     suma = a + b + c
#     if suma < 0:
#         suma = -suma
#     return suma, suma **2 # return konczy funkcję
#
# a, b = nazwa_funkcji(10 ,20 ,30)
# print(a)
# print(b)

#
# def funkcja(a, b, c=12):
#     print(a, b, c)
#     return
#
# funkcja(2, "ala ma kota", 14)
# funkcja(2, "ala ma kota")


# def func(a, b, c=10, d): # jak c ma jakąś wartośc to kolejne po nim też musza mieć wartość inaczej wyzwya
#     print(a, b, c)
#
# func(2, "ala ma kota", 14, 31)


# def wypisz_wszystko(*argumenty):
# #     for element in argumenty:
# #         print(element)
# #
# # wypisz_wszystko(1, 2, 3, 4, "Ala ma kota")


# funkcja na pole powierchni trójkąta
#
# def nazwa_funkcji(a, h):
#     zmienna = a * h * 0.5
#     return zmienna
#
# a = int(input("Podaj podstawe trójkąta\n"))
# h = int(input("Podaj wysokość trójkąta\n"))
# print("pole powierzchni trójkąta to:", nazwa_funkcji(a,h))


# def nazwa_funkcji(a, h):
#     zmienna = a * h * 0.5
#     return zmienna
#
# print("pole powierzchni trójkąta to:", nazwa_funkcji(5,4))

# Albo

# def nazwa_funkcji(a, h):
#     return a * h * 0.5
#
# print("pole powierzchni trójkąta to:", nazwa_funkcji(5,4))

# albo

# def pole(a, h):
#     return a* h /2
# a = float(input(" podaj długość podstawy\n"))
# h = float(input(" podaj wysokość boku\n"))
# print(pole(a, h))


# Zadanie Napisz funkcję która przymujuje paramter n i zwraca n liczb parzystych od 1.


# def liczby_parzyste(n):
#     lista = []
#     i = 1
#     while len(lista) < n:
#         if i % 2 == 0:
#             lista.append(i)
#         i += 1
#     return lista
# print(liczby_parzyste(8))


# Zadanie z psem

# from math import log
#
# def wiek_psa(n):
#     return log(n)*16 + 31
#
# print(wiek_psa(4))


# zadanie is_ten Napisz funkcję is_ten(), która przyjmuje dwa argumenty, a na wyjściu
# zwraca True, jeśli którykolwiek z nich jest równy 10. To samo w
# przypadku, gdy ich suma jest równa 10.


# def is_ten(a, b):
#     var1 = ''
#     if a + b == 10 or a == 10 or b == 10:
#         return True
#     else:
#         return False
#
# print(is_ten(5,6))

# albo

# def is_ten(a, b):
#     var1 = ''
#     if a + b == 10 or a == 10 or b == 10:
#         return True
#
# print(is_ten(5,6))

# albo
#
# def is_ten(a, b):
#     var1 = ''
#     return a + b == 10 or a == 10 or b == 10
#
# print(is_ten(4,6))


# is_vowel - Czy znak to samogłoska Napisz funkcję, która dla podanego napisu zwróci informację, która litera
# ile razy w nim wystąpiła (duże i małe litery traktujemy tak samo).

# def is_vowel(n):
#     samogloski = ["a", "e", "i", "o", "u", "y"]
#     return n.lower() in samogloski
#
# print(is_vowel("f"))


# Zadanie która litera ile razy wystąpiła

# def count_letters(napis):
#     count = {} # tworzymy pusty słownik można zrobić dict()
#     for znak in napis.lower():
#         if znak not in count:
#             count[znak] = 1
#         else:
#             count[znak] += 1
#             return count
#
# print(count_letters("Python is cool"))

# albo

# def count_letters(napis):
#     count = {} # tworzymy pusty słownik można zrobić dict()
#     for znak in napis.lower():
#         count[znak] = count.get(znak, 0) +1
#     return count
#
# print(count_letters("Python is cool"))


# zadanie Napisz funkcję, która jako argumenty będzie przyjmowała listę i parametr
# n z domyślną wartością równą 5. Funkcja ma zwrócić sumę wszystkich
# elementów listy większych od n.

# def funkcja(lista, n=5):
#     suma = 0 # zmienna pomocnicza
#     for i in lista: # dla kazdego elementu
#         if i > n: #sprawdzamy czy wartośc jest większa od zmiennej on n
#             suma += i
#     return suma
#
# print(funkcja([5, 6,7]))

#

# def funkcja(lista, n=5):
#     suma = 0  # zmienna pomocnicza
#     i = 0
#     while i < len(lista):
#         if lista[i] > n:
#             suma += lista[i]
#         i += 1
#     return suma
#
#
# print(funkcja([5, 6, 7]))

# print(funkcja(var1, n))


#
# def czy_pierwsza(n):
#     while i in range(1, lent(n)):
#
#
#

# print(czy_pierwsza(5))
