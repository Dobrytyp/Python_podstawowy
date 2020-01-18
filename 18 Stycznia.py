# Dekoratory

# from datetime import datetime
#
# def say_something():
#     print("Hello!")
#
# def disable_at_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour <22:
#             func()
#         else:
#             pass
#     return wrapper
#
# func = disable_at_night(say_something)
# func()

# -----------------------------------------------

# from datetime import datetime
#
# def disable_at_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#             pass
#     return wrapper
#
# @disable_at_night   #<---------
# def say_something():
#     print("hello!")
#
# say_something()     #<---------

# ----------------------------------------

# def funkcja():
#     print(f"Ala ma kota")
# #
# def start_stop(funkcja):
#     def wrapper():
#         print("START")
#         resault = funkcja()
#         if resault is not None:
#             print(resault)
#         print("STOP")
#     return wrapper
#
# @start_stop
# def funkcja():
#     print(f"Ala ma kota")
#
# funkcja()

# ------------------------------------------------
#
# @start_stop
# def zwroc():
#     return [i for i in range(1, 100) if i % 3]

# zwroc()

# -----------------------------------------------

# Zadanie
# Zastanów się, co należy zmienić, by możliwe było udekorowanie dowolnej
# funkcji, nawet takiej, która przyjmuje dowolną liczbę argumentów.

# def start_stop(funkcja):
#     def wrapper(*args, **kwargs):
#         print("START")
#         print(args, kwargs)
#         resault = funkcja(*args, ** kwargs)
#         if resault is not None:
#             print(resault)
#         print("STOP")
#     return wrapper
#
# @start_stop
# def funk(zwierze="kota"):
#     print(f"Ala ma {zwierze}")

# funk("psa")
# funk()
# funk(zwierze="Słonia")

# --------------------------------------


# Moje
# from datetime import datetime
#
# def funkcja():
#     return (f"Ala ma kota")
#
# def czas():
#     def wrapper():
#         print(datetime.now())
#         resault = funkcja()
#         print(datetime.now())
#
#
# @czas   #<---------
# def funkcja():
#     print("hello!")
#
# funkcja()     #<---------

# --------------------------------------------

# Zadanie
# Udekoruj dowolną funkcję zwracającą jakąś wartość, tak, by możliwe było
# zbadanie czasu jej wykonania.

# import time
# print(time.time)
#
# def time_decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         resault = func(*args, **kwargs)
#         print(f"{time.time() - start:.8f} seconds")
#         return resault
#     return wrapper
#
#
# def suma_cyfr_potega(liczba, n):
#     suma = 0
#     while liczba:
#         suma += (liczba % 10) ** n
#         liczba = liczba // 10
#     return suma
#
# @time_decorator
# def narcystyczna(liczba):
#     return suma_cyfr_potega(liczba, len(str(liczba))) == liczba
#
# print(narcystyczna(9474))
# print(narcystyczna(12))


# Zadanie
# Zoptymalizuj rekurencyjną funkcję zwracającą n-ty wyraz ciągu Fibonacciego.

# import time
#
# def fibonacci_recursive(n):   # sposób rekurencyjny
#     if n in [0, 1]:
#         return n
#     return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)
#
# start =time.time()
# resault = fibonacci_recursive(30)
# print(f"{time.time() - start:.8f} seconds")
# print(resault)

# -----------------------------------------------------

# Rozwiązanie

import time


# def optymalizuj(funkcja):
#     cache = {}                # Pusty Słownik
#     def wrapper(n):
#         if n in cache:
#             resault = cache[n]
#         else:
#             resault = funkcja(n)
#             cache[n] = resault
#         return resault
#     return wrapper
#
# @optymalizuj
# def fibonacci_recursive(n):   # sposób rekurencyjny
#     if n in [0, 1]:
#         return n
#     return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)
#
# start =time.time()
# resault = fibonacci_recursive(500)
# print(f"{time.time() - start:.8f} seconds")
# print(resault)

# ------------------------------------------------------------

# Zadanie
# Napisz dekorator, który spowoduje, że przy wywołaniu udekorowanej funkcji wypisze się na ekran informacja po raz który ta funkcja jest
# wywoływana, np.: "Funkcja <nazwa funkcji> została uruchomiona <n> raz"


# def howmany(func):
#     cache = {}
#     def wrapper(*args, **kwargs):
#         cache[func.__name__] = cache.get(func.__name__, 0) + 1
#         print(f"Funkcja {func.__name__} została wywołana już {cache[func.__name__]} razy")
#         return func(*args, **kwargs)
#     return wrapper
#
# @howmany
# def func():
#     print("Ala ma Kota")
#
# @howmany
# def dodaj(a, b):
#     return a + b
#
# @howmany
# def halko():   # sposób rekurencyjny
#     pass
#
#
# func()
# print(dodaj(3, 5))
# print(dodaj(2, 1))
# print(dodaj(8, 11))
# halko()

# --------------------------------------

# Dekorator może rónież przekzywać argumenty

# from datetime import datetime
#
# def run_only_between(_from=7, _to=22):      # Patrz niżej!
#     def real_decorator(func):
#         def wrapper():
#             if _from <= datetime.now().hour < _to:
#                 func()
#             else:
#                 pass
#         return wrapper
#     return real_decorator
#
# @run_only_between(7,21)                     # Tu zmieniamy warunki ktre były wyżej
# def say_something():
#     print("Hello!")

# say_something()

# ------------------------------------
# Stwórz funkcję wyświetlającą na ekranie dowolny napis, a następnie
# dekorator, który będzie wykonywał tę funkcję n razy (gdzie n jest
# parametrem przekazywanym do dekoratora).


# def n_times(n=1):
#     def dec(funkcja):
#         def wrapper():
#             for x in range(n):
#                 funkcja()
#         return wrapper
#     return dec
#
# def napis():
#     def wrapper():
#         return "Siema"
#
#     return wrapper
#
#
# @n_times(5)
# def func():
#     print("ala Ma kota")
#
# func()

#------------------------------------

# Zadanie
# Napisz dekorator, który będzie wymagał podania hasła przed właściwym
# wywołaniem funkcji. Jeśli zostanie podane błędne hasło to niech będzie
# wypisany komunikat o braku dostępu


# To jest nie zrobione

# def validate(password):
#     def dec(funkcja):
#         def wrapper():
#             if password == "poziomka":
#                 print("nie masz dostępu")
#         return wrapper
#     return dec
#
#
# @validate("poziomka")
# def func():
#     print("ala ma kota")
#
# func("poziomka")


#--------------------------------------------

# Pliki CSV

# Zadanie
# Stwórz plik CSV, w którym zapiszesz informacje o tym, kto pracuje w
# Twojej firmie i ile miesięcznie zarabia. Następnie odczytaj ten plik w
# kodzie pythonowym (nazwa pliku niech będzie przekazywana przez
# input), przyznaj każdemu 10% podwyżki i zapisz nową pensję jako
# kolejną kolumnę w nowym pliku CSV

import csv

# nazwa_pliku = input("podaj nwazę pliku:\n")
#
# with open(nazwa_pliku) as in_file:
#     reader = csv.reader(in_file)
#     for row in reader:
#         print(row)

# with open("plik2.csv", 'w') as out_file:
#     writer = csv.writer(out_file)
#     writer.writerow(["Anna kowalska", 2500])

# with open('plik.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=";")
#     your_list = list(reader)
#
# print(your_list)

# nazwa_pliku = input("Podaj nazwe pliku CSV\n")
# with open(nazwa_pliku) as in_file, open("pracownicy2.csv", 'w') as out_file:
#     reader = csv.reader(in_file, delimiter=";")
#     writer = csv.writer(out_file)
#     for idx, row in enumerate(reader):
#         if idx == 0:
#             row.append("pensja po podwyżce")
#         else:
#             row.append(int(row[-1]) * 1.1)
#         print(row)

#---------------------------------------------------

# Zadanie
# Stwórz plik JSON, w którym zapiszesz informacje o tym, kto pracuje w
# Twojej firmie i ile miesięcznie zarabia. Następnie odczytaj ten plik w
# kodzie pythonowym (nazwa pliku niech będzie przekazywana przez
# input), przyznaj każdemu 10% podwyżki i zapisz nową pensję jako
# kolejną wartość w nowym pliku JSON.

import json

nazwa_pliku = input("Podaj nazwe pliku JSON\n")
with open(nazwa_pliku) as in_file:
    data = json.load(in_file)

for pracownik in data:
    pracownik["nowa_pensja"] = pracownik['pensja'] * 1.1

with open("json2.json", 'w') as out_file:
    json.dump(data, out_file, indent=2)



