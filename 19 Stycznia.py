"Nie wydajna metoda"

# from datetime import datetime
# from math import sqrt
#
# def is_prime(n):
#     for i in range(2, int(sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True
#
#
# def get_n_primes(n):
#     primes = []
#     i = 2
#     while len(primes) != n:
#         if is_prime(i):
#             primes.append(i)
#         i += 1
#     return primes
# var1 = datetime.now()
# lst = get_n_primes(5000)
# for i in lst:
#     print(i)
#     print(lst)  # sprawdż czym jest lst
# var2 = datetime.now()
# print(var2 - var1)



# -----------------------------------------------------------

" Usprawnienie          ITERATOR"

# from datetime import datetime
# from math import sqrt
#
# def is_prime(n):
#     for i in range(2, int(sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True
#
# class PrimeIterator:
#     def __init__(self, n):
#         self.n = n
#         self.generated_numbers = 0
#         self.number = 2
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.number +=1
#         if self.generated_numbers >= self.n:
#             raise StopIteration
#         elif is_prime(self.number):
#             self.generated_numbers += 1
#             return self.number
#         return self.__next__()
#
# var1 = datetime.now()
# lst = PrimeIterator(5000)
# for i in lst:
#     print(i)
#     print(lst)
# var2 = datetime.now()
# print(var2 - var1)


# ----------------------------------------
"Da się  jeszcze łatwiej ! GENERATOR"

# from math import sqrt
# from datetime import datetime
#
# def is_prime(n):
#     for i in range(2, int(sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True
#
# def prime_generator(n):
#     number = 2
#     generated_numbers = 0
#     while generated_numbers != n:
#         if is_prime(number):
#             yield number
#             generated_numbers += 1
#         number += 1
#
# var1 = datetime.now()
# lst = prime_generator(5000)
# for i in lst:
#     print(i)
#     print(lst)
# var2 = datetime.now()
# print(var2 - var1)
# ----------------------------------

# Zadanie
# Napisz iterator i generator zwracające sumę składaną, tj. sumę liczb od 1
# do n, gdzie n podawane jest jako wartość końcowa jako parametr.
# gdy n = 10: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

# Iterator

# class SumIterator:
#     def __init__(self, n):
#         self.n = n
#         self.current_sum = 0
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n == self.i:
#             raise StopIteration
#         self.i +=1
#         self.current_sum += self.i
#         return self.current_sum
#
# for i in SumIterator(10):
#     print(i)

# --------------------------------

# Generator

# def sum_generator(n):
#     suma = 0
#     for i in range(1, n + 1):
#         suma += i
#         yield suma
#
# for i in sum_generator(10):
#     print(i)

# ----------------------------------
# Albo z peetlą While

# def sum_generator2(n):
# #     suma = 0
# #     i = 1
# #     while i != n + 1:
# #         suma += i
# #         i += 1
# #         yield suma
# # for i in sum_generator2(10):
# #     print(i)

# ---------------------------------------

# Zadanie
# Napisz iterator i generator zwracające kwadrat danej liczby
#  gdy n = 10: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# ITERATOR

# class PowerIterator:
#     def __init__(self, n):
#         self.n = n
#         self.number = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.number >= self.n:
#             raise StopIteration
#         self.number += 1
#         return self.number ** 2
#
# for i in PowerIterator(10):
#     print(i)

# --------------------------------------------

# Generator

# def kwadrat_generator(n):
#     suma = 0
#     for i in range(1, n + 1):
#         suma = i*i
#         yield suma
#
# for i in kwadrat_generator(10):
#     print(i)

# -------------------------------------------------

# Teraz while'm

# def Kwadrat_Generator2(n):
#     x = 1
#     while x <= n:
#         yield x ** 2
#         x+= 1
#
# for i in Kwadrat_Generator2(10):
#     print(i)

# -------------------------------------------------

# Zadanie
# Napisz generator i iterator zwracjacy n-ty wyraz ciagu Fibonacciego


# Iterator

# class FibonnaciIterator:
#     def __init__(self, n):
#         self.n = n
#         self.i = 0          #zmienna która będzie przechowywać który to wyraz ciągu
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i == self.n:
#             raise StopIteration
#
#         self.i += 1
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
#
# for i in FibonnaciIterator(10):
#     print(i)

# ------------------------------------------

# Generator

# def fibonacci_generator(n):
#     i = 0
#     first, second = 1, 1
#     while i != n:
#         yield first
#         first, second = second, first + second
#         i += 1
#
#
#
# for i in fibonacci_generator(10):
#     print(i)

# ---------------------------------

# Albo "for'em"

# def fibonacci_generator2(n):
#     first, second = 0, 1
#     for i in range(n):
#         first, second = second, first + second
#         yield first
#
# for i in fibonacci_generator2(10):
#     print(i)

# =========================================================

# WYRAŻENIA REGULARNE

# Zadanie
# Stwórz wyrażenie regularne, które pozwoli wyszukać w dowolnym tekście
# wszystkie zawarte w nim adresy e-mail.
# Np. „Kamil kamil@google.com, Tomek tomek@o2.pl"


# import re
#
# text = "Kamil kamil@google.com, Tomek tomek@o2.pl, zofia.oracz@google.com.pl"
#
# print(re.findall(r'\w+@\w+\.\w+', text))
#
# print(re.findall(r"[\w\.-]+@[\w\.]+\.\w+", text))

# Zadanie
# Przy wykorzystaniu funkcji re.search dokonaj usunięcia z poniższego
# adresu e-mail stwierdzenia 'remove_this': jan@onremove_thiset.pl.
# Efektem końcowym powinien być adres: jan@onet.pl

# import re
#
# text = "jan@onremove_thiset.pl"
#
# start, stop = re.search(f"remove_this", text).span()
# new_text = text[:start]+text[stop:]
# print(new_text)

# Przy wykorzystaniu funkcji re.sub w dowolnie napisanym przez Ciebie
# zdaniu zacenzuruj jego część na '*'

# import re
# text = "Dzień dobry, moi mili"
#
# pattern = r"moi"
# print(re.sub(pattern, "*"*len(pattern), text))

# albo

# import re
# text = "Dzień dobry, moi mili"
#
# pattern = r"moi"
# match = re.search(pattern, text)
# if match:
#     start, stop = match.span()
#     print(re.sub(pattern, "*"* (stop - start), text))

# Zadanie
# Wypisz wszystkie wyrazy długości mniejszej niż 6 ze zdania „Nie lubię w
# poniedziałki wcześnie wstawać”

# import re
#
# text = 'Nie lubię w poniedziałki wcześnie wstawać'
#
# pattern = "wstawać"
#
# print(re.findall(r'\b\w{1,6}\b', text))

#Albo

# import re
#
# text = 'Nie lubię w poniedziałki wcześnie wstawać'
# pattern = r"\b\w{1,6}\b"
# print(re.findall(pattern, text))

#---------------------------------------------

# Zadanie
# Załóżmy, że poprawny numer telefonu składa się z 9 cyfr i zaczyna od 7,
# 8 lub 9. Napisz funkcję, która sprawdzi, czy numer telefonu przekazany
# przez użytkownika jest poprawny.

# import re
#
# def is_phone_number_correct(number):
#     match = re.match(r"^[7-9][0-9]{8}$", number)
#     return bool(match)
#
# number = input("Podaj numer telefonu\n")
# print(is_phone_number_correct(number))

#-------------------------------

# Wypisz wszystkie wyrazy rozpoczynające się na ‘a’ lub ‘e’ z dowolnego
# # napisu.

# import re
#
# text = 'Nie lubię w poniedziałki wcześnie wstawać z avokado i enzymem aronia EB '
#
# pattern = r'\b[ae]\w*\b'
# print(re.findall(pattern, text, re.I))


# Wypisz wszystkie ciągi więcej niż dwóch samogłosek z tekstu.
# Na przykład dla napisu: „rabcdeefgyYhFjkIoomnpOeorteeeeet”
# poprawna odpowiedź to:
# [„ee”, „yY”, „Ioo”, „Oeo”, „eeeee”]


# import re
# text = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
#
# pattern = r'[aeiouy]{2,}'
# print(re.findall(pattern, text, re.I))

#---------------------------------------------

# Zadanie
# Z daty w postaci YYYY-MM-DD wyekstrahuj do osobnych zmiennych
# dzień, miesiąc i rok.


# import re
#
# data = "2019-01-19"
#
# pattern = r'(\d{4})-(\d{2})-(\d{2})'
# year, month, day = re.search(pattern, data).groups()
# print(day, month, year)