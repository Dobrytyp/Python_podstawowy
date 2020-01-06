# # Zadanie 1   ZROBIONE
# var1 = input("Podaj skalę Celcjusz (c), fahrenheita (F)\n")
# var2 = int(input("podaj temperaturę\n"))
#
# if var1 == "f":
#     print("twoja temperatura w stopniach celcjusza to: ", (var2 - 32) / 1.8)
# elif var1 == "c":
#     print("twoja temperatura w stopniach fahrenheita to: ", var2 *1.8 +32)

# =============================================

# Zadanie 2
# userPasword = input('podaj hasło\n')
# password = []
#
# list ="abcdefghijklmnoprstuwyz"
# digits ="1234567890"
# specials = "@$#"
# list_lower = []
# list_upper = []
# list_digits = []
# list_specials = []
# test = []
#
# for i in list: # rozbijam na listę z małymi oraz dużymi literami
#     list_lower += i.lower()
#     list_upper += i.upper()
#
# for i in digits: # rozbijam na pojedyncze liczby
#     list_digits += i
#
# for i in specials: # rozbijam na pojedyncze znaki specjalne
#     list_specials += i
#
# for i in userPasword: #rozbijam haslo na pojedyńcze znaki
#     password += i
#
# for i in password:
#     if i in list_lower:
#         test += "l"
#     elif i in list_upper:
#         test += "u"
#     elif i in list_digits:
#         test += "d"
#     elif i in list_specials:
#         test += "s"
#
# if "d" in test and "l" in test and "u" in test and "s" in test:
#     print('hasło poprawne')
# else:
#     print('hasło błędne')



# ============================================

# # Zadanie 3  ZROBIONE
# var1 = input("wpisz liczbę\n")
# var2 = {1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"pięć", 6:"sześć", 7:"siedem", 8:"osiem", 9:"dziwieć", 0:"zero"}
# var3 = ""
#
# for i in var1: # rozbija var1 na pojedyńcze znaki
#     var3 += var2[int(i)] + " " # dodaje do zbioru var3 liczbę ze słownika
#
# print(var3)

#==============================================


# #  zadanie 4   ZROBIONE
# list1 = [2, 8, 122, 44, 87, 250, 1164]
# var = list1[0]
# position = 0
#
# for i in range(1, len(list1)):
#     if list1[i] < var:
#         var = list1[i]
#         position = i
# print(var, position)


#===================================

# Zadanie 5 Zrobione

# var1 = [1, 2, 4, 4, 5]
# cyfra = var1[0]
# for i in var1:
#     cyfra *= i
# print(cyfra)

# Ta wersja nie działa, spytaj o nią.
# var1 = input("Podaj jakąś liczbę\n")
# cyfra = var1[0] # tworzymy nową zmienną
# print(cyfra)
# for i in var1:
#     cyfra *= i
# print(cyfra)

#======================================================

# # zadanie 9 Niby ok ale set usuwa duplikaty z list
# list1 = [1, 2, 3, 4, 5, 5]
# list2 = [2, 3, 4]
# list3 = [5, 6, 7]
#
# list1.sort()
# print(list1)
#
# set1 = set(list1)
# set2 = set(list2)
# set3 = set(list3)
# print(set1)
#
#
# test1 = set1 & set2
# if test1 == set2:
#     print("Zbiór 2 zawiera się w zbiorze 1")
# else:
#     print("Zbiór 2 nie zawiera się w zbiorze 1")



# #  Zadanie 10 ZROBIONE
# var1  = input("Podaj swoje słowo\n")
# list1 = list(var1)
# set1 = set(var1) #zamienia na zbiór
# list2 = list(set1) # ponownie tworzymy listę
# if len(list1) == len(list2):
#     print("twoje słowo to izogram")
# else:
#     print("twoje słowo nie jest ideogramem")
#


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

# ========  Teraz jest ok bo zmienna dodaj_do_listy bedzie czyszczona

# def dodaj_do_listy(element, lista=None):
#     if lista == None:
#         lista = []
#     lista.append(element)
#     return lista
#
# print(dodaj_do_listy(5, [1, 2, 3]))
# print(dodaj_do_listy(5))
# print(dodaj_do_listy(8))

# ZADANIA 3

# Zadanie 1

# def swap(a,b):
#     a = a + b
#     b = a - b
#     a = a - b
#     return a, b
#
# print(swap(3,5))

# Zadanie 2

# import random
#
# print("zagrajmy w grę: Papier, nożyce, kamień")
# game = True
# while game is True:
#     var1 = ''
#     while "p" not in var1 or "n" not in var1 or "k" not in var1:
#         var1 = input("Co wybierasz?\n Papier - p, Nożyczki - n, Kamień - k\n")
#         if "p" in var1 or "n" in var1 or "k" in var1:
#             break
#
#     var2 = random.randint(1, 3)
#
#     var3 = ''
#     if var2 == 1:
#         var3 += "p"
#     elif var2 == 2:
#         var3 += "n"
#     elif var2 == 3:
#         var3 += "k"
#
#     humwin = 0
#     compwin = 0
#     draw = 0
#
#     if var1 == "p" and var3 == "n":
#         compwin = 1
#     elif var1 == "n" and var3 == "k":
#         compwin = 1
#     elif var1 == "k" and var3 == "p":
#         compwin = 1
#     elif var1 == "p" and var3 == "k":
#         humwin = 1
#     elif var1 == "n" and var3 == "p":
#         humwin = 1
#     elif var1 == "k" and var3 == "n":
#         humwin = 1
#     else:
#         draw = 1
#
#     if humwin == 1:
#         print("wygrałeś!")
#     elif compwin == 1:
#         print("przegrałeś!")
#     elif draw == 1:
#         print("remis!")
#
#     repeat = input("Czy chcesz zgrac jeszcze raz?\n Nie - n, Tak - Enter\n")
#     if repeat == "n":
#         print("Dziękujemy za wspólną grę.")
#         break

# Zadanie 3

# Napisz funkcję która policzy sumę cyfr liczby, nie zamieniając jej na
# stringa, ani listę. Rekurencyjnie oraz iteracyjnie.
# np. 123 → 1+2+3 = 6


def sum_digits(n):              # Spytaj o to
    s = 0
    while n:
        s += n % 10     # reszta z dzielenia przez 10, chodzi o to żeby brał pojedyńczą cyfrę, a ta jest mniejsza od 10
        n //= 10        # // ozancza dzielenie całkowite bez reszty
    return s

print(sum_digits(1230))


# Rekurencyjnie nie umiem

# def suma_rek(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         elem = lst.pop()
#         return elem + suma_rek(lst)


# Zadanie  ZROBIONE
# Napisz funkcję która sprawdzi, czy dana liczba jest liczbą narcystyczną
# (n-cyfrowa liczba naturalna która jest sumą swoich cyfr podniesionych do
# potęgi n)
# np.
# 153 = 1^3 + 5^3 + 3^3
# 9474 = 9^4 + 4^4 + 7^4 + 4^4

# print(1*1*1 + 5*5*5 + 3*3*3)

# def narcistic(a):
#     resault = 0
#     list1 = list(map(int, str(a)))  # zamieniam int na listę
#     len_list1 = len(list1)          # wyciągam długość listy
#
#     for i in list1:
#         resault += i ** len_list1
#     return resault == a
#
# print(narcistic(9474))


# Zadanie
# Napisz funkcję pow(a, b), która będzie podnosiła a do b-tej potęgi. (Nie
# używając poznanego operatora ** i zewnętrznych bibliotek).
# Rekurencyjnie i teracyjnie.

# (2, 3) -> 2*2*2 = 8

# Iteracyjnie

# def pow(a,b):
#     result = 1                  # Żeby później mnożenie nie było przez 0 dajemy cyfrę 1
#     list1 = []
#     for i in range(b):
#         list1.append(a)
#     for i in list1:
#         result = i * result     # Daltego daliśmy 1 w result
#     return result
# print(pow(2,8))

# Rekurencyjnie NIE ZROBIONE

# def pow_rek(a,b):

# Zadanie               NIEZROBIONE
# Stwórz funkcję do znajdowania największego wspólnego dzielnika dwóch liczb.
# (algorytm Euklidesa)

# def nwd(a,b):
#     if a % b == 0:
#         return b
#     else:
#         a = b
#         b =

#jeżeli reszta ?0, to przypisujemy liczbie a wartość liczby b, liczbie b wartość otrzymanej reszty, a następnie wykonujemy ponownie punkt 1.