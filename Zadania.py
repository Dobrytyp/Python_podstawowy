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
# list1 = [50, 8, 122, 44, 87, 250, 1164]
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
# ZADANIE 6
# Napisz program, który pobierze 5 słów od użytkownika, a następnie
# wypisze najdłuższe z nich.

# lista = []
# for i in range(5):
#     var = input()
#     lista.append(var)
#
# wynik = ''
# for i in lista:
#     if len(wynik) < len(i):
#         wynik = i
#
# print(wynik)

#======================================================
# ZADANIE 7
# Napisz program, który obliczy liczbę małych i wielkich liter w ciągu.

# word = input("Podaj zdanie\n")
# small ="abcdefghijklmnoprstuwyz"
# capital = small.upper()
#
# counter_s = 0
# counter_c = 0
#
# for i in word:
#     if i in small:
#         counter_s += 1
#     elif i in capital:
#         counter_c += 1
#
# print(counter_s)
# print(counter_c)

# ZADANIE 8
# Pobierz od użytkownika wartość n, a następnie stwórz słownik, którego
# elementy dla i < n będą postaci: (i, i2)

# n = int(input())
# dupa = {}
#
# for i in range(1, n):
#     dupa[i] = [i*i]
#
# print(dupa)


# ZADANIE 9
# Napisz program, w którym zdefiniujesz dwie listy, a następnie sprawdzisz,
# czy pierwsza zawiera się w drugiej.

# list1 = [1, 3, 5, 7]
# list2 = [1, 3, 5, 9, 11]
# licznik = 0
#
# for i in list1:
#     if i in list2:
#         licznik += 1
#
# if len(list1) == licznik:
#     print("Zawiera się")
# else:
#     print("Nie zawiera się")



# #  Zadanie 10 ZROBIONE
# Napisz program, który poprosi użytkownika o podanie słowa i napisze,
# czy jest ono izogramem (słowo, w którym żadna litera się nie powtórzyła,
# np. „skrzynia”)

# word = input("podaj słowo\n")
# list1 = []
# for i in word:
#     list1.append(i)
#
# set1 = set(list1)
# if len(set1) == len(list1):
#     print("ideogram")
# else:
#     print("nie ideogram")


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

# def dodaj_do_listy2(element, lista=None):
#     if lista == None:
#         lista = []
#     lista.append(element)
#     return lista
#
# print(dodaj_do_listy2(5, [1, 2, 3]))
# print(dodaj_do_listy2(5))
# print(dodaj_do_listy2(8))

#======================================================
# ZADANIA II

# ZADANIE 1

# Napisz funkcję, która sprawdzi, czy podany jako argument napis jest
# palindromem (tj. czytany od przodu i wspak jest dokładnie taki sam, np.
# „kajak”, „Madam”, „nurses run”).

# word = input("Give a sentence\n")
# word = word.replace(" ", "")
# word = word.replace(",", "")
# word = word.replace(".", "")
# word = word.lower()
# reverse = word[::-1]
# if word == reverse:
#     print("sentence is Palindrom")
# else:
#     print("this is not a palindrom")

#-----------------------------------------------------------

# ZADANIE 2

# Napisz funkcję, która sprawdzi, czy podany jako argument napis jest
# pangramem (tj. zawiera każdą literę alfabetu co najmniej raz, np. „The
# quick brown fox jumps over the lazy dog”).

# word = input("Give a sentence\n")
# word = word.lower()
# word = word.replace(" ", "")
#
# lista_word = []
# lista = []
#
# alphabet = "abcdefghijklmnopqrstuvwxyz"
#
# for i in alphabet:
#     lista.append(i)
# lista = set(lista)
#
# for i in word:
#     lista_word.append(i)
# lista_word.sort()
# lista_word = set(lista_word)
#
# if lista == lista_word:
#     print("pangram")
# else:
#     print("nie pangram")

#----------------------------------------------

# ZADANIE 3.
#
# Napisz funkcję, która zamieni liczbę w zapisie rzymskim na dziesiętny.

        #NIE SKONCZONE#

#-----------------------------------------------

# ZADANIE 4

# Napisz funkcję, która sprawdzi, czy podana liczba jest doskonała (tj. jest
# sumą swoich dzielników właściwych, np. 6 = 1 + 2 + 3).

# number = int(input("podaj liczbę\n"))
# dzielniki = []
# for i in range(1, number):
#     if number % i == 0:
#         dzielniki.append(i)
#
# if sum(dzielniki) == number:
#     print("liczba jest doskonała")
# else:
#     print("liczba nie jest doskonała")

#------------------------------------------------

# ZADANIE 5

# Napisz funkcję, która obliczy wartość zadanego elementu ciągu
# Fibonacciego rekurencyjnie i iteracyjnie
# # Fn = F(n - 1)+F(n-2)

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
#
# # albo
#
# def fibonacci_iterative(n):
#     fibonacci = [0, 1]
#     for i in range(2, n+1):
#         fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
#     return fibonacci[n]
#
# print(fibonacci_iterative(5))
# print(fibonacci_iterative(19))



#---------------------------------------------------

# ZADANIE 6

# Napisz funkcję, która sprawdzi, czy rok podany jako argument jest
# przestępny.

# rok = int(input())
#
# if rok % 4 == 0 and rok % 100 != 0:
#     print("Rok przestępny")
# elif rok % 400 == 0:
#     print("Rok przestępny")
# else:
#     print("Rok zwykły")

#---------------------------------------------------

# ZADANIE 7

# Wyobraź sobie, że obsługujesz sklep. Wszystkie produkty, które posiadasz w magazynie, wraz z ich cenami oraz dostępną
# liczbą przechowujesz w słowniku (hint: zagnieżdżonym słowniku :D).
# Pozwól użytkownikowi podać nazwę produktu, który chce nabyć oraz liczbę sztuk, następnie sprawdź,
# czy posiadasz taki produkt w tej ilości na stanie, a na koniec zwróć informację o cenie do zapłaty.

    #NIE SKONCZONE

#---------------------------------------------------

# ZADANIE 8

# Napisz funkcję, która zwróci 5 najczęstszych słów z dzieła Mickiewicza
# https://pastebin.com/raw/aAHeW5Pt
# Ćwiczymy odczytywanie z pliku

#---------------------------------------------------

# ZADANIE 9

# Stwórz klasę reprezentującą koło o danym promieniu z metodami do obliczania jego pola powierzchni i obwodu.
# Odpowiednią stałą zaimportuj z zewnętrznego modułu.

# from math import pi
#
# class Kolo:
#     def __init__(self,r):
#         self.r = r
#
#     def pole(self):
#         return f"Pole twojego koła wynosi: {pi * self.r * self.r} "
#
#     def obwod(self):
#         return f"Pole twojego koła wynosi: {2 * pi * self.r} "
#
# kolo1 = Kolo(10)
#
# print(kolo1.pole())
# print(kolo1.obwod())

#----------------------------------------------------

# ZADANIE 10

# Zamodeluj działanie koszyka w Allegro (nie, nie zapłacili mi za reklamę :<). Potrzebujemy klasę Produkt,
# która będzie posiadała argumenty takie jak: nazwa oraz cena oraz umożliwiała wypisanie produktu na ekran.
# Dodatkowo, chcemy posiadać klasę Koszyk, która będzie przechowywała dodawane przez użytkownika produkty
# wraz z ich licznością w słowniku oraz umożliwiała usunięcie wszystkiego z koszyka, pokazania jego zawartości,
# obliczenie łącznej wartości dotychczasowych produktów z koszyka, dodanie nowego produktu do niego
# (czyli dodanie lub zwiększenie ilości)oraz usunięcie.

        # NIE ZROBIONE#

#=====================================================================================

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


# def sum_digits(n):              # Spytaj o to
#     suma = 0
#     while n:
#         suma += n % 10     # reszta z dziel. przez 10, chodzi o to żeby brał pojedyńczą cyfrę, a ta jest mniejsza od 10
#         n //= 10        # // ozancza dzielenie całkowite bez reszty
#     return suma
#
# print(sum_digits(1234))


# Rekurencyjnie

# def suma_rek(liczba):
#     if liczba < 10:
#         return liczba
#     else:
#         return suma_rek(liczba // 10) + liczba % 10
#
# print(suma_rek(1234))


# Zadanie  ZROBIONE

# Napisz funkcję która sprawdzi, czy dana liczba jest liczbą narcystyczną
# (n-cyfrowa liczba naturalna która jest sumą swoich cyfr podniesionych do
# potęgi n)
# np.
# 153 = 1^3 + 5^3 + 3^3
# 9474 = 9^4 + 4^4 + 7^4 + 4^4

# print(1*1*1 + 5*5*5 + 3*3*3)

# def narcistic(a):
#     result = 0
#     list1 = list(map(int, str(a)))  # zamieniam int na listę
#     len_list1 = len(list1)          # wyciągam długość listy
#
#     for i in list1:
#         result += i ** len_list1
#     return result == a
#
# print(narcistic(9474))

#Albo





# Zadanie
# Napisz funkcję pow(a, b), która będzie podnosiła a do b-tej potęgi. (Nie
# używając poznanego operatora ** i zewnętrznych bibliotek).
# Rekurencyjnie i teracyjnie.

# (2, 3) -> 2*2*2 = 8

# Iteracyjnie

# def pow(a,b):
#     result = 1                  # Żeby później mnożenie nie było przez 0 dajemy cyfrę 1
#     list1 = []                  # Pusta lista
#     for i in range(b):          # Dla elementów w zasięgu b
#         list1.append(a)         # do pustej listy dodajemy a
#     for i in list1:
#         result = i * result     # Daltego daliśmy 1 w result
#     return result
# print(pow(2,8))
#
# def pow(a,b):
#     result = 1
#     for i in range(b):
#         result *= a
#     return result

#Ablo

# Rekurencyjnie
# def pow(a,b):
#     if b == 0:
#         return 1
#
#     return a * pow(a, b-1)
#
#
# print(pow(4,3))

# Zadanie               częsciowo zrobione
# Stwórz funkcję do znajdowania największego wspólnego dzielnika dwóch liczb.
# (algorytm Euklidesa)


# def nwd(a,b):
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     return a
#
# print(nwd(120,22))

# Rekurencja

# def nwd_rek(a, b):
#     if a == b:
#         return a
#     elif a > b:
#         return nwd_rek(a-b, b)
#     else:
#         return nwd_rek(b-a, a)
#
# print(nwd_rek(120,22))

# Albo

# def nwd_rek2(a, b):
#     x = a % b
#     if x == 0:
#         return b
#     return nwd_rek2(b, x)
#
# print(nwd_rek2(25, 5))


# Napisz program (rekurencyjnie i iteracyjnie), który wyświetli n kolejnych
# wyrazów ciągu zdefiniowego następująco:
#         2, dla n=1
# an =    an-1 * 2 dla n nieparzystego
#         an-1 + 2 dla n parzystego

# def wyrazy_ciagu(a, n):
#     ciag = []
#     if n == 1:
#         ciag = a
#         return ciag
#     elif n % 2 != 0:
#         for i in range(1, n):
#             ciag.append(a * (n-1) * 2)
#             n -= 1
#         ciag.append(a)
#         ciag.sort()
#         return ciag
#     elif n % 2 == 0:
#         for i in range(1, n):
#             ciag.append(a * (n-1) + 2)
#             n -= 1
#         ciag.append(a)
#         ciag.sort()
#         return ciag
#
# print(wyrazy_ciagu(2,4))

# def ciag_iter(n):
#     lista = []
#     for i in range(1, n+1):
#         if i  == 1:
#             lista.append(2)
#         elif i % 2 == 0:
#             lista.append((lista[-1]+ 2))
#         else:
#             lista.append((lista[-1] +2 ))
#     return lista
#
# print(ciag_iter(5))



# Zadanie       Zrobione
# Napisz funkcję, która przyjmuje dwa stringi i sprawdza, czy są swoimi anagramami.Np.
# „army” i „Mary”,
# „dzielenia” i „niedziela”,
# „Quid est veritas?” i „Vir est qui adest”,
# „Jim Morrison” i „Mr Mojo Risin”
# „Tom Marvolo Riddle” i „I am Lord Voldemort”
#
# def anagram(a, b):
#     a = a.lower()
#     b = b.lower()
#     a_list = []
#     b_list = []
#     for i in a :
#         if i != " " and i != "!" and i != "?" and i != ":" and i != ";":
#             a_list += i
#     for i in b :
#         if i != " " and i != "!" and i != "?" and i != ":" and i != ";":
#             b_list += i
#     a_list.sort()
#     b_list.sort()
#     return a_list == b_list
#
# print(anagram("Tom Marvolo Riddle", "I am Lord Voldemort!"))

# Albo

# def anagram(napis1, napis2):
#     napis1 = napis1.lower().replace(" ", '')
#     napis2 = napis2.lower().replace(" ", '')
#     return sorted(napis1) == sorted(napis2)
#
# print(anagram("Tom Marvolo Riddle", "I am Lord Voldemort!"))

# Zadanie
# Korzystając z paradygmatu obiektowego zamodeluj swoje konto bankowe: chcemy móc otworzyć rachunek, zamknąć go, dowiedzieć się,
# ile pieniędzy mamy na koncie oraz wpłacić i wypłacić jakąś kwotę.
# (podpowiedź, klasa będzie miała dwa atrybuty, jeden przechowujący stan konta (otwarte, zamknięte), a drugi zdeponowaną kwotę)

# class Konto:
#     def __init__(self):
#         self.status = False
#         self.stan = 0
#
#     def otworz_konto(self):\
#         self.status = True
#
#     def zwroc_saldo(self):
#         if
#
#     def outcome(self):
#         out = ''
#         return self.amount - out
#
#
# karol_maj = Konto(True, 1000)
# maria_walewska = Konto(True, 2000)

# Zadanie 10

import math

# class Punkt:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"Współrzędne to: ({self.x}, {self.y}"


# Zadanie 1
# Stwórz program, który będzie pobierał od użytkownika liczby całkowite tak
# długo, aż ten nie wciśnie control+D – wówczas ma się pojawić informacja
# o tym, ile liczb całkowitych użytkownik podał, jaka jest ich suma oraz
# średnia



# print("Witamy w bezesnowym programie który nauczy nas wielu rzczy")
# lista = []
# loop = True
# while end_loop:
#     num = int(input("podaj liczbę"))
#     lista.append(num)
#     if:
#         loop = False
#
# print("Podałeś:", len(lista)," liczb" )
# print("Ich suma to:", sum(lista))
# print("Ich średnia to: ", (sum(lista)/len(lista)))


# Albo

# suma = 0
# counter = 0
#
# while True:
#     try:
#         liczba = int(input("Podaj liczbę\n"))
#         suma += liczba
#         counter +=1
#     except EOFError:                        # Ctrl+D kończy skrypt
#         print(f"Count: {counter}")
#         print(f"Suma: {suma}")
#         print(f"średnia: {suma/counter}")
#         break


# Zadanie 2             # Zrobione
# Stwórz znany już sobie kalkulator BMI, a następnie wczuj się w złośliwego
# testera i zabezpiecz przed wszelkimi błędami, które użytkownik może
# celowo wprowadzić.

# correct_waga = True
# while correct_waga:
#     try:
#         waga = float(input("Podaj masę w Kilogramach\n"))
#         if waga > 0:
#             correct_waga = False
#     except ValueError:
#         None
#
# correct_wzrost = True
# while correct_wzrost:
#     try:
#         wzrost = float(input("Podaj wzrost w centrymetrach\n"))
#         wzrost = wzrost/100
#         if wzrost > 0:
#             correct_wzrost = False
#     except ValueError:
#         None
#
# bmi = waga / (wzrost*wzrost)
#
# if bmi < 18.5:
#     print("masz niedowagę")
# elif 18.5 <= bmi < 25:
#     print("Ważysz prawdiłowo")
# elif 25 <= bmi < 30:
#     print("Masz nadwagę")
# else:
#     print("Jesteś otyły")

# Albo

# class NegativeValueError(Exception):
#     pass
#
# class ValueTooHighError(Exception):
#     pass
#
# correct_wzrost = True
# while correct_wzrost:
#     try:
#         masa = float(input("podaj masę\n"))
#         wzrost = float(input("podaj wzrost\n"))
#         if masa < 0 or wzrost < 0:
#             raise NegativeValueError()
#         if masa > 300 or wzrost > 2.51:
#             raise  ValueTooHighError()
#         correct_wzrost = False
#     except ValueError:
#         print("masa w kilogramach wzrost w metrach")
#     except NegativeValueError:
#         print("ma być nieujemna")
#     except ValueTooHighError:
#         print("wartości są zbyt duże")
#
# bmi = masa / wzrost **2
# if bmi < 18.5:
#     print("masz niedowagę")
# elif 18.5 <= bmi < 25:
#     print("Ważysz prawdiłowo")
# elif 25 <= bmi < 30:
#     print("Masz nadwagę")
# else:
#     print("Jesteś otyły")


# Zadanie 3

# Stwórz klasę Pies z atrybutami imię oraz wiek. Następnie stwórz listę, w której przechowasz kilka instancji tej klasy.
# Następnie, przy pomocy funkcji map przekształć listę tych psów w listę ich ludzkich lat

# from math import log
#
# class Pies:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

    # def __str__(self):
    #     return f"Pies {self.name} o wieku {self.age}"
#
# dog1 = Pies("Burek", 3)
# dog2 = Pies("Puś", 12)
# dog3 = Pies("Albar", 6)
#
# lst = [dog1, dog2, dog3]
# print(lst)
#
# human_age = list(map(lambda x:  16 * log(x.age) + 31, lst))
# print(human_age)


# Albo

# from math import log
#
# class Pies:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def konwertuj_wiek(self):
#         return 16 * log(self.age) + 31
#
#     def __repr__(self):
#         return f"Pies {self.name} o wieku {self.age}"
#
#
# dog1 = Pies("Burek", 3)
# dog2 = Pies("Puś", 12)
# dog3 = Pies("Albar", 6)
#
# lst = [dog1, dog2, dog3]
# print(lst)
#
# human_age = list(map(lambda x:  16 * log(x.age) + 31, lst))
# print(human_age)


# Zadanie 4
# Stwórz 3 różne funkcje, które przyjmują jako argument listę, a zwracają
# iloczyn wszystkich jej dodatnich elementów.

# lista = [-2, 1, 2, 3, 4, 5]

from functools import reduce

# def iloczyn(lista):         #done
#     suma = 1
#     for i in lista:
#         if i > 0:
#             suma *= i
#     return suma
#
# print(iloczyn(lista))

# def iloczyniloczyn_compr(lst):
#     return prod[i for i in lista if i > 0]

# def iloczyn_lambda(lista):
#     lista = filter(lambda x: x > 0, lista)
#     return reduce(lambda x, y: x * y, lista)




# dalej nie ma

# Zadanie 5                 #done
# Stwórz funkcję, która przyjmuje listę napisów i zwraca ją w postaci
# posortowanej, od najkrótszego do najdłuższego.

# lista_nap = ['droga boli', 'moja', 'mnie głowa']


# def sort_by_length(lista_nap):
#     lista_nap.sort(key=len)
#     return lista_nap
#
# print(sort_by_length(lista_nap))

# Albo

# lista_nap = ['droga boli', 'moja', 'mnie głowa']
#
# def sort_by_length(lista_nap):
#     return sorted(lista_nap, key=lambda x: len(x))

# def dlugosc(napis):
#     counter = 0
#     for i in napis:
#         counter += 1
#     return counter
#
# def sort_by_length(lista_nap):
#     return sorted(lista_nap, key=dlugosc)

# Zadania na 25.01

# Zadanie 3


# def generator(n, m):
#     lista = []
#     for i in range(n*m):
#         if i % m != 0:
#             lista.append(i)
#         elif len(lista) == n:
#             break
#
#     yield lista           # yield jest zamiast return
#
# for i in generator(10, 3):
#     print(i)



# def tradycyjnie(n, m):
#     lista = []
#     for i in range(n*m):
#         if i % m != 0:
#             lista.append(i)
#         elif len(lista) == n:
#             break
#
#     return lista
#
# print(tradycyjnie(10, 3))

# Nie umiem




# class Iterator:
#     def __init__(self, n, m):
#         self.n = n
#         self.m = m
#         self.o = 1
#         self.list = []
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n == len(self.list):
#             raise StopIteration
#         else:
#             if self.o % self.m != 0:
#                 self.list.append(self.o)
#                 self.o += 1
#             elif self.o % self.m == 0:
#                 self.o += 1
#
#         return self.list
#
#
# test = Iterator(10, 3)
# for i in test:
#     print(i)