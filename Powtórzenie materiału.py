# =====================================================================
# =====================================================================

# DZIEN PIERWSZY

# # ZMIENNE
# Do zmiennej można podstawić wartość innej zmiennej
# Do zmiennej możemy również przypisać dowolne inne wyrażenie
#
# Podstawowe typy:
# Integer (liczby całkowite)
# Float (liczby zmiennoprzecinkowe)
# String (teksty - łańcuchy znaków)
# Boolean (wartości logiczne – True/False, prawda/fałsz)
# None (specjalny typ oznaczający brak wartości)
# zmienna = 12              # intiger
# zmienna = int(12)         # intiger
# zmienna = float(12)       # float
# zmienna = 12.0            # float
# zmienna = str("Cześć")    # string
# zmienna = "Cześć"         # string
# zmienna = False           # boolean
# zmienna = True            # boolean
# zmienna = None            # oznacza brak wartości

# ======================================================================

# ŁAŃCUCHY ZNAKÓW

# Z łanucha znaków można wydobyć intersujące nasz wartośći
# Nazywamy to slicing - Szatkowanie
# n.p. :

# var1 = "ABCDEFGHIJ"
# print(var1[2])      # wydobywamy konkretną pozycję  łancucha
# print(var1[2:5])    # wydobywamy znaki "od" : "do"
# print(var1[2:9:2])  # wydobywamy znaki "od" : "do" : "co ile"
# print(var1[::2])    # wydobywamy : : "co ile" Czyli z całośći
# print(var1[-4])     # wydobywamy któryś od tyłu
#
# var2 = var1[3:7:2]  # ty tworzymy nową zmienną z konkretnych elementów

# str1 = "Przykład"
# var2 = str1[:len(str1) // 2]    # Tym dzielmy zapis na pół i tworzymy zmienną z pierwszej połowy
# print(var2)

# ======================================================================

# ZADANIA NA ZMIENNYCH
# var1 = 10, 20, 30
# var2 = var1 * 10    # Tu poda nam pierwszą zmienną powtórzoną razy 10
# var3 = 10+20
# var4 = var3 * 5     # Tu pomnoży pierwsża zmienną razy 5

# =======================================================================

# KONWERSJA TYPÓW
# var1 = 10
# var2 = float(var1)  # zamieniamy liczbę, na liczbe po przecinku
# var3 = 15.3
# var4 = int(var3)    # Zamieniamy liczbę po przecinku na liczbę całkowitą
# var5 = str(var4)    # Zamieniamy zmienną liczbową na tekst
#
# print(var5[1])      # możemy poprosić o konkretny indeks

# =======================================================================

# OBRÓBKA TEKSTU
# var1 = "Python nie jest"
# var2 = "taki straszny"
# print(var1, var2, sep=' ')  # dzielimy teksty separatorem, jeśli chcemy by była spacja to dajemy ją między nawiasami

# ========================================================================

# OPEARTORY
# == równa się
# != nie równa się
# > większe niż
# < mniejsze niż
# >= mniejsze lub równe
# <= większe lub równe

# ========================================================================

# OPERATORY LOGICZNE
# AND (koniunkcja) – jeśli oba warunki są prawdziwa, wówczas True
# OR (alternatywa) – jeden z warunków musi być prawdziwy
# NOT – zaprzeczenie

# ========================================================================

# ZNAKI SPECJALNE
#  \n – znak nowej linii
#  \t – tabulator
#  \” - cudzysłów
#  \’ - apostrof

# ========================================================================

# OPERACJE NA NAPISACH

# var1 = "Pythonie uważaj. Nadchodzę!"
# print(var1.lower())         # Zmniejsza wszystkie znaki na małe
# print(var1.upper())         # Zmniejsza wszystkie znaki na wielkie
# print(var1.swapcase())      # Zmienia znaki na odwrotne
# print(var1.capitalize())    # Ustawia pierwsze litery jako wielkie
# print(var1.title())         # Ustawią wszystkie pierwsze litery na wielkie
# print(var1.strip())         # Usuwa wszystkie białe znaki na początku i na końcy. n.p. spacja na początku

# =========================================================================

# INSTRUKCJE WARUNKOWE

# number = float(input("podaj liczbę\n"))
# if number >= 0:
#     print("Twoja liczba jest dodatnia")
# elif number < 0:
#     print("Twoja liczba jest ujemna")

# =========================================================================
# =========================================================================
# DZIEN DRUGI

# KOLEKCJE

# Wyróżniamy dwa podstawowe kategorie typów:
# Proste: int, float, string, bool, None
# Złożone – składające się z wielu elementów.
#
# Dzielą się na:

# =========================================================================
# =========================================================================

# LISTY
# Lista jest uporządkowaną kolekcją obiektów.
# - Wyobraź sobie kartę dań w restauracji, gdzie każdemu daniu jest
#   przyporządkowana liczba porządkowa - to jest właśnie lista.
# - Kiedy składasz zamówienie podajesz po prostu numery dań.
# - Jeśli restauracja chce dodać nowe zamówienie do karty dań, najprościej
#   je dopisać do końca listy i nadać mu kolejną liczbę porządkową.
# - Sytuacja komplikuje się, kiedy restauracja chce dodać nowe danie na
#   początek lub gdzieś w środku listy, ponieważ trzeba wtedy zmienić
#   numerację pozostałych dań.
# - To samo następuje kiedy usuwamy - łatwo skreślić ostatni element ale
#   kiedy wykreślamy element ze środka to przydałoby się zmienić liczbę
#   porządkową innych dań.
# - Nie jest to oczywiście niemożliwe ale zajmie więcej czasu niż dodawanie /
#   usuwanie ostatniego elementu.

# list1 = ["Mała", "Ala", "ma", 10, "kotów"]
# list1.append("Bardzo dużych")       # funkcja .append() dodaje element do listy
# print(list1)
# list1.pop(0)                        # fukcja .pop() usuwa wybrany element z listy
# print(list1)
# print(list1[2])                     # podaje konkretną wartość z listy
# print(list1[1:4])                   # możemy poprosić o konkretne elementy listy. "od" : "do"
# print(list1[0:6:2])                 # możemy poprosić o konkretne elementy listy. "od" : "do" : "co ile"

# ---------------------------------------------------------------------------

# list2 = ["Pyton", "nie", "taki", "straszny, "]
# list3 = ["jak", "go", "malują"]
# list2.extend(list3)                 # .extend() dołącza listę do listy
# print(list2)
# del list2[4:]                       # del usuwa elementy z listy
# print(list2)

# ---------------------------------------------------------------------------

# list4 = [4, 7, 3, 9, 6, 5]
# print(min(list4))                   # min() wskazuje najmniejszą wartość z listy
# print(max(list4))                   # max() wskazuje najmniejszą wartość z listy
# print(sum(list4))                   # sum() zwraca sumę składników listy
# print(len(list4))                   # len() wskazuje długośc listy

# list5 = list(reversed(list4))       # reversed() odwraca listę
# print(list5)
# list4.sort()                        # .sort() sortuje listę
# print(list4)

# list6 = ["jaja", "ser", "bułki"]
# list7 = [10, 1, 6]
# list8 = list(zip(list6, list7))     # list(zip()) tworzy krotki w parach
# print(list8)

# print("asd" in [1, 2, "asd", 3, True, 4.5])     # sprawdzamy czy element jest na liście (True)
# print(-52.1 in [1, 2, "asd", 3, True, 4.5])     # sprawdzamy czy element jest na liście (False)
# print(-52.1 not in [1, 2, "asd", 3, True, 4.5]) # sprawdzamy czy element nie jest na liście (True)

# ===========================================================================
# ===========================================================================

# Krotki

# -Krotki zapisujemy w nawiasach okrągłych, oddzialając elementy
#  przecinkiem

# -Działają analogicznie do list, ale nie można edytować ich elementów
#  oraz dodawać ich (nie ma metody append)

# ===========================================================================
# ===========================================================================

# Zbiory

# -Kolejnym po liście złożonym typem danych w języku Python jest zbiór (set).
# -Zbiór można sobie wyobrażać jako worek. Kiedy wkładasz rękę do worka nigdy nie wiesz
#  co z niego wyciągniesz.

# -Tak samo jest ze zbiorami - w przeciwieństwie do list kolejność elementów w zbiorze
#  nie jest ustalona (ani istotna

# -Kolejną różnicą jest to, że elementy zbioru nigdy się nie powtarzają -
#  wszystkie elementy są unikalne.

# -Zbiór tworzymy podając jego elementy rozdzielone przecinkami w nawiasach klamrowych.

# -Można też przekształcić listę w zbiór i ponownie zbiór na listę. Jest to najprostszy sposób na
#  usunięcie duplikatów z listy

# ===========================================================================

# W szkole poznaliśmy podstawowe operacje na zbiorach:

# - suma (unia)
# - iloczyn (przecięcie, część wspólna)
# - różnica (również różnica symetryczna)

# set1 = {1, 2 ,3, 4, 5}
# set2 = {4, 5 ,6 ,7, 8}
#
# set3 = set1 | set2      # znak | to suma lub unia, dodaje zbiory (i oczwywiście usuwa duplikaty
# set4 = set1 & set2      # znak & to iloczyn lub przecięcie, czyli część wspólna zbiorów
# set5 = set1 - set2      # zmak - to róznica, lub róznica symetryczna, odejmuje wartości jednego set od drugiego.

# print(set3)
# print(set4)
# print(set5)

# ==========================================================================

# - add dodaje element do zbioru
# - update dodaje elementy innego zbioru
# - remove usuwa element ze zbioru
# - clear usuwa elementy ze zbioru

# set6 = {1, 2}
# set7 = {3, 4}
# set8 = {5, 6}
# set9 = {8}
#
# set6.add(7)
# set7.update(set8)
# set8.remove(6)
# set9.clear()
#
# print(set6)
# print(set7)
# print(set8)
# print(set9)

# ===========================================================================


# - Podobnie jak w przypadku listy operator in służy do
#   sprawdzenia czy element należy do zbioru.

# set1 = {1, 2, 3}
# print(4 in set1)


# - Ponieważ zbiór nie jest uporządkowany i nie można
#   odnosić się do jego elementów po indeksie nie ma
#   metody index


# - Metoda issubset sprawdza czy zbiór, na którym
#   wywoływana jest metoda, jest podzbiorem zbioru
#   podanego jako argument.

# set1 = {1, 2, 3}
# print(set1.issubset({1, 2, 3, 4}))


# - Metoda issuperset sprawdza czy zbiór, na którym
#   wywoływana jest metoda, jest nadzbiorem zbioru
#   podanego jako argument.

# set1 = {1, 2, 3}
# print(set1.issuperset({1, 2}))


# ===============================================================
# ===============================================================

# Słowniki

# - Ta struktura danych jest podobna do książki
#   telefonicznej lub encyklopedii.
# - Zaglądamy pod pewien klucz (nazwisko
#   abonenta, hasło encyklopedyczne) a w zamian
#   dostajemy pewną użyteczną wartość (numer
#   telefonu, definicję pojęcia)
# - Słownik przypomina zbiór w tym sensie, że
#   jego klucze muszą być unikalne.

# Słownik tworzymy wypisując pary klucz:wartość,
# oddzielając dwukropkiem klucz od wartości. Pary
# oddzielamy od siebie przecinkami, całość jest ujęta
# w nawiasy klamrowe.

# dict = {"Ala": 1, "Dupa": 2, "Głowa": 3, "Ręka": 4}

# =========================================================

# - Do wartości ze słownika możemy odnieść się
#   poprzez korespondujący z nim klucz używając
#   operatora [ ].

# - Tego samego operatora można użyć aby zmienić
#   wartość spod danego klucza.

# - Aby usunąć klucz (i jego wartość) ze słownika
#   należy użyć poznanego już słowa kluczowego del.


# - Jeśli użyjemy operatora [ ] w celu dostania się pod
#   klucz, który nie istnieje w słowniku to dostaniemy
#   błąd.
# - Aby ustrzec się przed błędem w takiej sytuacji
#   należy użyć metody get, która zwróci None jeśli
#   klucza nie ma lub wartość domyślną jeśli ją
#   podamy.

# dict = {"Ala": 1, "Dupa": 2, "Głowa": 3, "Ręka": 4}
# print(dict["Dupa"])     # znajdujemy wartośc w słowniku po haśle
#
# dict["oko"] = 5         # tak dodajemy hasło do słownika
# print(dict)
#
# del dict["oko"]         # del kasuje wpis ze słownika
# print(dict)
#
# print(dict.get("Ala"))  # ten klucz istnieje w słowniku
# print(dict.get("Nos"))  # a tego klucza nie ma słowniku, zwraca nam "None"


# dict1 = {}                # tym poleceniem tworzym pusty słownik
# print(type(dict1))

# ================================================================================

# - Słownik udostępnia trzy ważne metody:
# - keys - zwraca zbiór wszystkich kluczy
# - values - zwraca zbiór wszystkich wartości
# - items - zwraca zbiór wszystkich par (klucz, wartość).


# list1 = dict.keys()                                     # Keys zwraca zbiór kluczy
# print(list1)

# list2 = dict.values()                                   # values zwraca zbiór wartości
# print(list2)

# list3 = dict.items()                                    # items zwraca pary: klucz, wartość
# print(list3)


# Operator in umożliwia sprawdzenie czy dany klucz (ale nie wartość) jest w słowniku.

# dict = {"Ala": 1, "Dupa": 2, "Głowa": 3, "Ręka": 4}
# print("oko" in dict)                                    # in sprawdza czy dany klucz jest w słowniku


# ==============================================================================================
# ==============================================================================================

# PĘTLA FOR

# - Pętla for służy między innymi do wykonania jakiejś operacji na każdym elemencie listy.

# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = []
# for i in list:
#     list2.append(i * 10)
#
# print(list2)


# - Pętla for może również służyć do powtórzenia jakiejś czynności określoną liczbę razy.

# def Stonoga(haslo):
#     for i in range(3):
#         print(f'Was się powinno {haslo}!')
#
# print(Stonoga("ruchać"))


# =============================================================================================
# =============================================================================================

# FUNKCJA RANGE

# - Jedną z ważnych dla nas funkcji jest range
# - range zwraca sekwencję liczb całkowitych.
# - range(n) zwraca sekwencjęliczb od 0 do n-1.
# - range(a, b) zwraca sekwencję liczb od a do b-1.
# - range(a, b, c) zwraca sekwencję liczb [a, a+c, a+c+c, …] aż do b-1.
# - Używając funkcji range można szybko tworzyć listy.

# list1 = list(range(10))
# print(list1)
#
# list2 = list(range(2, 90))
# print(list2)
#
# list3 = list(range(1, 100, 2))
# print(list3)


# ===============================================================================================
# ===============================================================================================

# FUNKCJA ENUMERATE

# -Przydatną funkcją jest również enumerate, która każdemu elementowi z przekazanej jako argument listy
#  przypisuje liczbę całkowitą, zaczynając numerowanie od zera
#
# list1 = [0, 5, 10, 15, 20]
# list2 = list(enumerate(list1))
# print(list2)
#
# list3 = [0, 5, 10, 15, 20]              # Przykład użycia
# for i , value in enumerate(list3):
#     print(i, value)


# ===============================================================================================
# ===============================================================================================

# PĘTLA WHILE

# - Pętla while działa tak długo jak długo spełniony jest logiczny warunek podany w jej definicji.

# - Zaimplementujmy odliczanie oparte na pętli while.
#   Odliczamy w dół od zadanej liczby aż do zera

# number = int(input("Podaj liczbę.\n"))
# while number >= 1:
#     number -= 1
#     print(number)


# - Dwa słowa kluczowe w istotny sposób wpływają na zachowanie pętli.
# - Słowo kluczowe break przerywa wykonanie pętli, nawet jeśli warunek pętli jest spełniony.
# - Słowo kluczowe continue przerywa bieżącą iterację i przechodzi do następnego obiegu pętli.

# def przedwczesne(cyfra):
#     while(cyfra):
#         print(cyfra)
#         cyfra -= 1
#         if cyfra == 5:
#             break
#     print("Przerwać odliczanie")
#
# print(przedwczesne(12))

# def co_dwa(liczba):
#     while(liczba):
#         liczba -= 1
#         if liczba % 2:
#             continue
#         print(liczba)
#
# print(co_dwa(14))

# ==========================================================================
# ==========================================================================

# DZIEŃ TRZECI

# MODUŁY

# Czym są moduły?
# Pliki z rozszerzeniem .py, w których zawarto pewien zestaw funkcji
# Korzystać z funkcji, które znajdują się w module możemy na trzy sposoby:

# import random
# print(random.randint(0,10))
#
# from random import *
# print(randint(1, 10))
#
# from random import randint
# print(randint(1, 10))

# ====================================================================================================

# Czym są moduły?
# Aby podejrzeć zawartość modułu używamy funkcji dir(), a gdy chcemy dowiedzieć się szczegółów
# na temat konkretnej metody modułu korzystamy z help()

# import random
# print(dir(random))
# print(help(random.randint))

# =====================================================================================================
# =====================================================================================================

# FUNKCJE

# - Dotąd korzystaliśmy z wbudowanych funkcji Pythona, nie wymagających implementacji – wystarczyło je jedynie wywołać i poprawnie zastosować,
# - Funkcja to blok kodu, który może być wielokrotnie wywołan.
# = Definicja funkcji musi zawierać:
#   Słowo kluczowe def
#   Nazwę, która pozwoli ją zidentyfikować.
#   Ciało funkcji, zawierające instrukcje, które zostaną wykonane w momencie jej wywołania
#   Jeśli ma zwracać wartość, musi zawierać instrukcję return

# - Parametry do funkcji możemy przekazywać albo podając ich wartości w kolejności podanej w nagłówku jej definicji
#   albo w dowolnej kolejności, wykorzystując ich nazwy.
# - Funkcja może przyjmować wiele argumentów i zwracać wiele rezultatów
# - Wywołanie funkcji wymaga podania wartości dla wszystkich parametrów – jeśli tego nie zrobimy, wystąpi błąd
# - Możemy tego uniknąć, podając domyślne wartości argumentów

# def nazwa_funkci(wartośc_fukncji):
#     działanie = wartośc_fukncji * 10
#     return działanie
#
# print(nazwa_funkci(4))

# ==========================================================================================

# Jeżeli w momencie definiowania funkcji nie jesteśmy w stanie określić liczby argumentów,
# które będą do niej przekazywane, poprzedzamy nazwę parametru formalnego
# oznaczającego wszystkie pozostałe argumenty funkcji gwiazdką.

# def fukncja(*argumenty):
#     for element in argumenty:
#         print(element)
#
# fukncja(1, 2, 3, 4, "ala ma kota")


# ==========================================================================================
# ==========================================================================================

# ZAPISYWANIE PLIKÓW

# Python posiada wbudowaną funkcję open, służącą do otwierania plików z dysku.
# open zwraca obiekt pliku posiadający metody i atrybuty,
# dzięki którym możemy dostać się do pliku i wykonywać na nim pewne operacje.

# W metodzie open należy podać ścieżkę do pliku oraz tryb. Drugi parametr jest opcjonalny,
# domyślnie plik zostanie otwarty do odczytu w trybie tekstowym.

# =========================================================================================

# Aby odczytać jego zawartość używamy metod read lub readlines

# f = open("plik.txt", "r")
# print(f.read())

# Parametry to: r - odczyt, r+ - odczyt i zapis, w - zapis, a - dopisywanie

# =========================================================================================

# Do zapisu do pliku służy metoda write lub writelines.

# f = open("plik2.txt", "w")
# f.write("Python is cool")

# TU DOKOŃCZ


# =========================================================================================
# =========================================================================================

# PROGRAMOWAIE OBIEKTOWE

# - Python jest językiem zorientowanym obiektowo i aby w pełni korzystać z
#   jego możliwości należy poznać programowanie obiektowe.
# - Zasadniczą koncepcją w podejściu obiektowym do programowania jest połączenie w całość danych oraz algorytmów,
#   które na tych danych operują.
# - Obiekt posiada pewne własności, czyli dane oraz pewne metody, czyli algorytmy do przetwarzania tych danych.
# - Zbiór obiektów o tych samych własnościach i metodach nazywamy klasą.
# - Programowanie obiektowe to podejście do modelowania konkretnych rzeczy w świecie rzeczywistym,
#   takich jak samochody, a także relacji między firmami i pracownikami, uczniami i nauczycielami itp.

# - Każdy obiekt ma atrybuty (które opisują jego cechy) oraz metody (które opisują zachowania)
#  Na przykład:
#                imię, wiek, kolor to atrybuty
#                śpiew, taniec, szczekanie to metody, czyli zachowania, które może wykonać dany obiekt

# - Koncepcja programowania obiektowego opiera się na tworzeniu reużywalnego kodu (DRY – don’t repeat yourself).
#       Podstawowe cechy tej koncepcji:
#           - Abstrakcja - ograniczenie cech obiektu ze świata rzeczywistego do cech istotnych,
#             kluczowych z punktu widzenia programisty
#           - Hermetyzacja – ukrywanie dostępu do prywatnych detali obiektu
#           - Polimorfizm – możliwość stosowania tego samego kodu dla obiektów różnych typów
#           -  Dziedziczenie – rozszerzanie klas

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# azor = Dog("Azor", 6)
# burek = Dog("Burek", 4)
#
# print("{} is {} and {} is {}.".format(azor.name, azor.age, burek.name, burek.age))

# ======================================================================================

# METODY

# class Dog:
#     def __init__(self, name, age):          # Tu mamy informacje jakie parametry definiują psa
#         self.name = name
#         self.age = age
#
#     def descritpion(self):                  # określamy metodę
#         return f"{self.name}, {self.age}"
#
#     def make_sound(self, number):           # tu kolejna metoda
#         return "Hau! " *number
#
# azor = Dog("Azor", 6)
# burek = Dog("Burek", 4)
#
# print(azor.descritpion())
# print(burek.make_sound(4))

# -------------------------------------------------------------

# # METODA specjalna __str__
# Wywoływana przez wbudowaną funkcję str() oraz instrukcję print celem wygenerowania napisu zawierającego "informacyjną" reprezentację obiektu
#
# class Dog:
#     def __init__(self, name, age):          # Tu mamy informacje jakie parametry definiują psa
#         self.name = name
#         self.age = age
#
#     def descritpion(self):                  # określamy metodę
#         return f"{self.name}, {self.age}"
#
#     def make_sound(self, number):           # tu kolejna metoda
#         return "Hau! " *number
#
#     def __str__(self):                      # tu określamy co ma zostac zwrócone
#         return f"{self.name}, ma {self.age} lat."
#
# azor = Dog("Azor", 6)
# burek = Dog("Burek", 4)
#
# print(azor)
# print(burek)

# ====================================================================================

# DZIEDZICZENIE

# - mimo że na pewnym poziomie abstrakcji obiekty zachowują się tak samo, to mogą się też różnić na innym poziomie,
#   np. każdy pies ma swoje imię i wiek, ale każda rasa ma swoje specyficzne własności
# - aby móc to zamodelować możemy wykorzystać dziedziczenie, rozwijając klasę bazową

# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):              # To po to, żeby zwracało info po wpisaniu psa linia 681 i 683
#         return f"{self.name} is a dog, {self.age} year old."
#
# class Labrador(Dog):                # Tworzymy podklasę
#     def make_sound(self):
#         return "WHOOF!"
#
# class York(Dog):                    # Druga podklasa
#     def make_sound(self):
#         return "Hau!"
#
# lucky_dog = Labrador("Lucky", 6)
# coco_dog = York("Coco", 4)
# print(lucky_dog)
# print(lucky_dog.make_sound())
# print(coco_dog)
# print(coco_dog.make_sound())

# =========================================================================

# FUNKCJA SUPER()

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} is a dog. {self.age} years old."
#
# class Labrador(Dog):
#     def __init__(self, name, age):
#         super().__init__(name, age)                 # Umożliwia zaciągnięcie z klasy nadrzędnej Dog
#         self.size = "big"
#
#     def make_sound(self):
#         return "WOOOOOF!"
#
# class York(Dog):
#     def __init__(self, name, age, size="small"):
#         super().__init__(name, age)
#         self.size = size
#
#     def make_sound(self):
#         return "hau"
#
# dog1 = York("baron", 12, "small")

# =====================================================================================

# Tworzymy klasę Prostokąt, której atrybutami będą wysokość i szerokość. Zaimplementujemy metody do mierzenia obwodu i pola.

# class Prostokąt:
#     def __init__(self, wyskość, szerokość):
#         self.wysokość = wyskość                         # tu zawsze jest self.
#         self.szerokość = szerokość
#
#     def pole(self):                                     # tu jest metoda na pole
#         pole = self.wysokość * self.szerokość
#         return pole
#
#     def obwod(self):                                    # tu jest metoda na obwód
#         obwod = self.wysokość * 2 + self.szerokość * 2
#         return obwod
#
#
# ob1 = Prostokąt(4, 6)                                   # przykładowy obiekt
#
# print(ob1.pole(), ob1.obwod())

# Teraz dodajemy podklasę kwadrat

# class Prostokąt:
#     def __init__(self, wyskość, szerokość):
#         self.wysokość = wyskość
#         self.szerokość = szerokość
#
#     def pole(self):
#         return self.wysokość * self.szerokość
#
#     def obwod(self):
#         return self.wysokość * 2 + self.szerokość * 2
#
#
# ob1 = Prostokąt(4, 6)  # przykładowy prostokąt
#
# print(ob1.pole())
# print(ob1.obwod())
#
#
# class Kwadrat(Prostokąt):
#     def __init__(self, bok):
#         super().__init__(bok, bok)  # Przkazujemy klasie prostokąt wartości z klasy kwadrat, czyli "w" i "s" jako bok i bok
#
#
# ob2 = Kwadrat(6)    # przykładowy kwadrat
#
# print(ob2.pole())
# print(ob2.obwod())

#=========================================================================

# Hermetyzacja (enkapsulacja)

# - Polega na tym, że szczegóły implementacji są ukryte. Dzięki temu obiekt nie może zmieniać stanu wewnętrznego
#   innych obiektów w nieoczekiwany sposób. Tylko wewnętrzne metody danego obiektu są uprawnione do zmiany jego stanu.
#   Każdy typ obiektów ma swój interfejs, który określa dopuszczalne metody współpracy.

# - Jesteśmy jakimś obiektem A. Widzimy drugi obiekt, B. Obiekt B wie o sobie wszystko, my wiemy o nim tylko tyle,
#   ile on nam udostępnia. W szczególności nie mamy dostępu do wielu zmiennych tego obiektu,
#   możemy natomiast go "poprosić" żeby coś zrobił z tymi zmiennymi, lub podał nam ich wartość,
#   wywołując metodę, jaką obiekt nam udostępnia.

# - Przykład - Idziemy do apteki, chcemy kupić jakiś lek — nie bierzemy go z półki sami,
#   tylko wywołujemy określoną metodę obiektu Apteka, prosząc Panią Sprzedawczynię, aby ten lek nam podała.
#   Nie interesuje nas w jaki sposób ona to zrealizuje — tzn. czy będzie np. musiała poszukać go w magazynie,
#   czy też wejść na stołek bo lek stoi na górnej półce. My tego sami robić nie musimy, to już nie nasz problem,
#   a drugiego obiektu.

#==========================================================================

# Przekazywanie argumentów przez referencję

# Zadanie - policz sumę obiektów listy

# Można zrobić to iteracyjnie:

# def list_iter(lst):
#     suma = 0                            # tworzymy pustą listę
#     for elem in lst:                    # dla każdego elementu:
#         suma += elem                    # dodajemy go do pustej listy
#     return suma                         # zwracamy sumę
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(list_iter(lista))                 # dostajemy listę wplecioną w funkcję

# Ale można też rekurencyjnie

# def list_rek(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         elem = lst.pop()               # .pop() usuwa wybrany element z listy
#         return elem + list_rek(lst)
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(list_rek(lista))


