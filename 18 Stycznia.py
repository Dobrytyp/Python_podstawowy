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

def napis():
    def wrapper():
        print("Siema")

    return wrapper


@napis
def ile_razy(n):
    var = napis * n
    return var


ile_razy()

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
