# Tak jest z błędem
from inspect import v
from random import randint

# for i in range(10):
#     a = randint(0, 10)
#     b = randint(0, 2)
#     wynik = a / b
#     print(i, a ,b, wynik)


# Fix it

# from random import randint
# for i in range(10):
#     a = randint(0, 10)
#     b = randint(0, 2)
#     try:
#         wynik = a / b
#     except ZeroDivisionError:
#         wynik = 0
#     print(i, a ,b, wynik)



# def funkcja(lista):
#     ind = 0
#     while ind < len(lista):
#         try:
#             print(10 / lista[ind])
#         except ZeroDivisionError:
#             break
#         finally:
#             ind +=1
#     print(f"indeks: {ind}")
#
# funkcja([2,3,5,0,4])


# Zadanie
# Napisz program, który zapyta użytkownika o rok jego urodzenia, a
# następnie zwróci informację o tym, czy jest pełnoletni. Program powinien
# być idiotoodporny.

# try:
#     rok = int(input("Podaj rok swojego urodzenia\n"))
#     if 2020 - rok < 18:
#         print("nie jesteś pełnoletni")
#     else:
#         print("Jesteś pełnoletni")
# except ValueError:
#     print("Debil")


# Zadanie
# Napisz program, który zapyta użytkownika o nazwę miesiąca, a następnie
# zwróci informację, ile dany miesiąc ma dni. Program powinien być
# idiotoodporny.


# month = {
#     "styczeń" : 31,
#     "luty" : 29,
#     "marzec" : 31,
#     "kweicień" : 30,
#     "maj" : 31,
#     "czerwiec" : 30,
#     "lipiec" : 31,
#     "sierpień" : 31,
#     "wrzesień" : 30,
#     "pażdziernik" : 31,
#     "listopad" : 30,
#     "grudzień" : 31
# }
#
#
# miesiac = input("Podaj miesiąc\n")
# miesiac = miesiac.lower()
# try:
#     print(f"Miesiaąc {miesiac} ma {month[miesiac]} dni.")
#
# except KeyError:
#     print("Nie ma takiego miesiąca")


# Zadanie
# Napisz program, który wypisze na ekran zawartość pliku, którego nazwę podaje użytkownik.

# nazwa_pliku = input("podaj nazwę pliku\n")
# try:
#     with open(nazwa_pliku) as plik:
#         print(plik.read())
# except FileNotFoundError:
#     print("nie ma takiego pliku")


# Zadanie
# Napisz program, który zwróci wartość bezwzględną liczby pobranej od
# użytkownika. Program powinien pytać o tę liczbę tak długo, aż nie
# zostanie ona poprawnie podana.

# while True:
#     try:
#         liczba = int(input("Podaj liczbę\n"))
#         print(abs(liczba))
#         break
#     except ValueError:
#         print("Nie podałeś poprawnej liczby")

# Mamy również możliwość rzucania wyjątków w kodzie, gdy chcemy go zasygnalizowąć
# Służy do tego słowo kluczowe raise

# from random import randint
#
# for i in range(10):
#     a = randint(0, 10)
#     b = randint(0, 2)
#     if b == 0:
#         raise ValueError("dzielnik nie może być równy zeru")
#     wynik = a/b
#     print(i, a ,b ,wynik)

# Zadanie
# Napisz program, który obliczy pole trójkąta na podstawie podanych przez
# użytkownika długości podstawy oraz wysokości, pod warunkiem, że obie
# te liczby są dodatnie.


class MojWlasnyWyjatek(Exception):
    pass

def pole_trojkata(a, h):
    if a < 0 or h < 0:
        raise MojWlasnyWyjatek("Długość i wysokość Trójkąta muszą mieć wartość dodatnią")
    return 0.5 * a * h

x = float(input("podaj długość podstawy \n"))
y = float(input("podaj długość podstawy \n"))

print(pole_trojkata(x, y))

#===========================================================


# class MojWlasnyWyjatek(Exception):
#     def __init__(self):
#         message = "Długość i wysokość Trójkąta muszą mieć wartość dodatnią"
#         super().__init__(message)
#
#
# def pole_trojkata(a, h):
#     if a < 0 or h < 0:
#         raise MojWlasnyWyjatek()
#     return 0.5 * a * h
#
# x = float(input("podaj długość podstawy \n"))
# y = float(input("podaj długość podstawy \n"))
#
# print(pole_trojkata(x, y))

#======================================================

# class MojWlasnyWyjatek(Exception):
#     def __init__(self):
#         message = "Długość i wysokość Trójkąta muszą mieć wartość dodatnią"
#         super().__init__(message)
#
#
# def pole_trojkata(a, h):
#     if a < 0 or h < 0:
#         raise MojWlasnyWyjatek()
#     return 0.5 * a * h
# try:
#     x = float(input("podaj długość podstawy \n"))
#     y = float(input("podaj długość podstawy \n"))
# except ValueError:
#     print("musisz podać liczbę")
#
# print(pole_trojkata(x, y))

#==========================================================
# Zadanie
# Stwórz program, który pobiera od użytkownika liczbę z zakresu od 1 do
# 100 i losuje drugą, z zakresu od -5 do 5, a następnie dzieli pierwszą przez
# drugą. Pamiętaj o odpowiedniej obsłudze niepożądanych działań.

# from random import randint
#
# class RangeException(Exception):
#     def __init__(self):
#         super().__init__("Liczba musi byż z zakresu od 1 do 100\n")
#
# try:
#     liczba1 = int(input("Podaj liczbę od 1 do 100\n"))
#     if liczba1 < 1 or liczba1 > 100:
#         raise RangeException()
#     liczba2 = randint(-5, 5)
#     print(liczba2/liczba1)
# except ValueError:
#     print("Nie podałeś liczby")
# except ZeroDivisionError:
#     print("nie można dzielić przez 0")

# Spróbuj sam

# a = int(input("Podaj liczbę od 1 do 100\n"))
# while a > 100 or a < 1:
#     a = int(input("Podaj liczbę od 1 do 100\n"))
#     if 1 < a < 100:
#         break
# b = randint(-5, 5)

#===========================================================
        #WYRAŻENIA LAMBDA

# def funkcja(x):         # To jest zwykła funkcja
#     return x.lower()
#
# print(funkcja("Kołek"))
#
# funkcja_lambda = lambda x: x.lower()        # A to funkcja lambda
#
# print(funkcja_lambda("Kołek"))
#
# #---------------------------------
#
# kwadrat_lambda = lambda x: x**2
#
# print(kwadrat_lambda(6))

#-----------------------------------

# Zadanie
# Przy pomocy funkcji reduce znajdź w liście element największy.

# from functools import reduce
#
# print(reduce(lambda x, y: max(x,y), [1, 34, 12, 54, 6, 9]))
#
# print(reduce(lambda x, y: x if x > y else y, [1, 34, 12, 54, 6, 9]))

# #-------------------------------------
# list2 = [5, 9, 2, 4]
#
#
# def lista_szesciany_tradycyjna(list1):
#     new_list = []
#     for i in list1:
#         new_list.append(i ** 3)
#     return new_list
#
# print(lista_szesciany_tradycyjna(list2))
#
# #---------------------------------
#
# def lista_szesciany(lst):
#     return [elem ** 3 for elem in list2]
#
# print(lista_szesciany(list2))
#
# #---------------------------------
#
# lista_szesciany_lambda = list(map(lambda x: x ** 3, list2))
# print(lista_szesciany_lambda)
#
# #==========================================

# Zadanie
# Napisz funkcję, która zwraca listę wszystkich niepodzielnych przez 3 liczb z zakresu [1, 20]. Trzema sposobami.

# def dzielniki_tradycyjnie(list1):               # Program robi 58 kroków
#     list1 = []
#     for i in range(1, 20):
#         if i % 3 != 0:
#             list1.append(i)
#     return list1
#
# print(dzielniki_tradycyjnie([]))
# #-----------------------------------
#
# def dzielniki_compr():                          # Program robi 28 kroków
#     return [x for x in range(1, 20) if x % 3]
#
# print(dzielniki_compr())
#
# #-----------------------------------
#
# dzielniki_lambda = list(filter(lambda x: x % 3, range(1, 20)))  # Program robi 59 kroków
#
# print(dzielniki_lambda)

#===============================================================================

# Zadanie
# Napisz funkcję, która przyjmuje dwa parametry: jednym jest lista, a drugim liczba całkowita z domyślną wartością równą 5.
# Powinna zwracać listę tych elementów, które nie przekroczyły wartości tego parametru. Trzema sposobami.

# lst = [12, 4, 8, 88, 2]
#
# def czy5_tradycyjny(lista, x = 5):
#     lista1 = []
#     for i in lista:
#         if i <= x:
#             lista1.append(i)
#     return lista1
#
# print(czy5_tradycyjny(lst))
#
# def czy5_compr(lista, x = 5):
#     return [i for i in lista if i <= x]
#
# print(czy5_compr(lst))
#
# def czy5_lambda(lista, a = 5):
#     return list(filter(lambda x: x <= a, lista))

# print(czy5_lambda(lst))

# Zadanie
# Napisz funkcję, która przyjmuje listę i zwraca ją w zmienionej formie: tam, gdzie liczba była parzysta teraz mamy napis „Parzysta”,
# a tam, gdzie nieparzysta – (niespodzianka) „Nieparzysta”. Trzema sposobami.

# lst = [1, 2, 4, 5]
#
# def reverse(list):
#     list1 = []
#     for i in list:
#         if i % 2 == 0:
#             list1.append("parzysta")
#         else:
#             list1.append("nieparzysta")
#     return list1
#
# print(reverse(lst))
#
# def reverse_comp(lista):
#     return ["parzysta" if i % 2 == 0 else "nieparzysta" for i in lista]
#
# print(reverse_comp(lst))
#
#
# def reverse_lambda(lista):
#     return list(map(lambda x: "nieparzysta" if x % 2 else "parzysta", lista))
#
# print(reverse_lambda(lst))


# Zadanie
# Napisz funkcję, która przyjmuje listę i zwraca sumę kwadratów parzystych elementów.

# from functools import reduce
#
# lst = [ 2, 3, 4, 5, 6]
#
# def suma_kwadratow(lista):
#     suma = 0
#     for i in lista:
#         if i % 2 == 0:
#             suma += i ** 2
#     return suma
#
# print(suma_kwadratow(lst))
#
# def suma_comp(lista):
#     return sum([i ** 2 for i in lista if i % 2 == 0])
#
# print(suma_comp(lst))
# def suma_lambda(lista):
#     nowa_lista = filter(lambda i: 1 % 2 == 0, lista)
#     nowa_lista = map(lambda i: i ** 2, nowa_lista)
#     return reduce(lambda x, y: x + y, nowa_lista)
#
# print(suma_lambda(lst))


# Zadanie
# Stwórz listę z 10 losowymi wartościami z przedziału [-10; 10], a następnie
# posortuj ją rosnąco pod względem kwadratów elementów

# from random import randint
#
# lista = [randint(-10, 10) for i in range(10)]
# print(lista)
# print(sorted(lista, key=lambda x: x ** 2))
