# zmienna1 = 3 # integer to liczby całkowite
# zmienna2 = 4.6655 # float to liczby zmiennoprzecinkowe
# zmienna3 = "lubie placki" # String to tekst
# zmienna4 = True # boolean to wartości logiczne True albo False
# zmienna5 = None # None to specjalny znak oznaczający brak wartości

# print(zmienna1, zmienna2, zmienna3,zmienna4, zmienna5)


# zmienna6 = "Napis z cytatem: \"Lubie Placki\"" #jeśli chcemy dac cytat
# print(zmienna6)


# Slicing (szatkowanie) Zmienna[początek:Koniec:krok]
# zmienna7 = "1234567890"
# print(zmienna7[0:5])#da nam pierwszych 5 znaków ostaniego nie wyświetla
# print(zmienna7[0:10])#jak chcesz cały napis to musisz dodac na końcu o jeden większy
# print(zmienna7[5:]) #da nam znaki od 6 wzwyż
# print(zmienna7[0:10:2]) #daje nam co dwa kroki
# print(zmienna7[::3]) #daje co trzy kroki z całości
# print(zmienna7[-6:]) #od -6 czyli 5 do końca
#
# print(type(zmienna7)) #podaje nam jakiego typu jest zmienna n.p. string


# 1.zadanie #napisz program, w którym utowrzysz trzy zmienne: 10, "b', 3,7 a potem podaj wartości i typy
# zmienna1 = 10
# zmienna2 = "b"
# zmienna3 = 3.7
# zmienna4 = True
# zmienna5 = None
# print(type(zmienna1))
# print(type(zmienna2))
# print(type(zmienna3))
# print(type(zmienna4))
# print(type(zmienna5))
# zmienna1 = 42
# zmienna2 = "\"Hacksaw Ridge\""
# print(zmienna2)

# zmienna6 = zmienna1 + zmienna3 #zadanie stórz nową zmienną która doda zmienną 1 oraz 3
# print(zmienna6)
#
# zmienna6 = zmienna6 + 10 #zwiększ zmienną o 10
# print(zmienna6)


# zmienna1 = "Maciej"
# print(zmienna1)

# Zadanie #oblicz pole powierzchni koła = pi* R kwadrat
# r = float(input("Podaj długość promienia koła\n"))
# pi = 3.14
# print(r*pi*pi)

# Zadanie wzór na pole trójkąta 1/2 a * h
# podstawa = float(input("Podaj długość podstawy trójkąta\n"))
# wysokość = float(input("Podaj wyskość trójkąta\n"))
# print(podstawa/2*wysokość)

# Zadanie wzór na pole trapezu (a+b)h/2
# a = float(input("Podaj długość podstawy trapezu\n"))
# b = float(input("Podaj długośc góry trapezu\n"))
# h = float(input("Podaj wysokość trapezu\n"))
# print((a+b)*h/2)

# zbiór = "1234567890"
# print(zbiór)
# print(zbiór[0:6])
# print(zbiór[-1])
# print(zbiór[6:10])


# float(x) zmienia argument na liczbę z przecinkiem
# int(x) zmienia argument na liczbę całkowitą
# str(x) zmienia argument na łąncuch znaków
# bool(X) zmienia argument na wartość logiczną
# x = 10
# print(float(x)) #zmienia liczbę na liczbę po przecinku
# y = 5.5
# print(int(y)) #zmienia liczbę po przecinku na liczbę całkowitą
# z = "50"
# print(str(z))

# Program
# year = int(input("Podaj rok urodzenia\n")) #int jest po to żeby trzeba było wpisać liczbę
# age = 2019 - year
# print(age)

# Program na pole trójkąta
# h = int(input("podaj wysokośc trójkąta\n"))
# a = int(input("podaj długośc podstawy trójkąta\n"))
# print(a * h * 0.5)


# name = "john"
# year = 2019
# age = 21
# print(name, year, age)
# print(name, year, age, sep="_") # dodaje wartość między zmiennymi
# print(name, year, age, end=",") # dodaje wartość na końcu
# print(name, year, age, sep="_", end=",") # można łączyć
# print(name, year, age, end="5")
# print(name, year, age, sep="bla")


# imie = input("Jak masz na imię?\n")
# print("Cześć", imie)
# rok = int(input("W którym roku się urodziłeś?\n"))
# wiek = 2019 - rok
# if wiek > 30:
#     print("Masz", wiek, "lata", imie, ", jesteś stary.")
# elif 30 > wiek > 17:
#     print("Masz", wiek, "lata", imie, ", jesteś młody.")
# else :
#     print("Masz", wiek, "lata", imie, ", ty gówniarzu.")


# Napisz program który spyta o imię i nazwisko i poda inicjały
# imie = input("Podaj swoje imie\n")
# nazwisko = input("podaj swoje naziwsko\n")
# print("Twoje inicjały to: ", imie[0], nazwisko[0], sep="")


# Napisz program który zapyta o imie, naziwsko i wiek. I wyświetl je w jednej lini oddzielone spacjami
# imie = input("Podaj swoje imie\n")
# nazwisko = input("Podaj swoje naziwsko\n")
# wiek = input("podaj swój wiek\n")
# print(imie, nazwisko, wiek)


# imie = "Rafał"
# spotkanie = "urodziny"
# czas = "15:00"
# text1 = "Witaj %s, zapraszamy na %s na godzinę %s" % (imie, spotkanie, czas) # na końcy zadnia musi być %
# text2 = "Witaj {}, zapraszamy na {} na godzinę {}".format(imie, spotkanie, czas) #musi być .format(coś tam)
# text3 = "Witaj {0}, zapraszamy na {1} na godzinę {2}".format(imie, spotkanie, czas)
# text4 = f"Witaj {imie}, zapraszamy na {spotkanie} na godzinę {czas}"
# print(text1, "do zobaczenia", imie)
# print(text2)
# print(text3)
# print(text4)

# imie, naziwsko wiek pensja stanowisko. Nastęnie zrób: Adam kowalski (wiek 35 lat) pracuje
# na stanoiwsku młodszy inżynier procesu (pensja 6000 brutto).

# imie = "Maciej"
# nazwisko = "Pińczewski"
# wiek = 34
# pensja = 6000
# stanowisko = "Junior Python Developer"
#
# print("Pan", imie, nazwisko, wiek, "lat, pracuje na stanowisu:", stanowisko, "pensja:", pensja, "brutto")


# print(2+2)
# print(8-3)
# print(2*5)
# print(6/3)
# print(13%4) #reszta z dzielenia
# print(5//2) # dzielenie całkwoite
# print(3**3) # potęgowanie


# dodaj 10 i 20 wynik podziel przez 2. Od wyniku odejmij 5, potem wynik pomnóz przez 5
# print((((10+20)/2)-5)*3)

# operatory porównania
# == równa się
# != nie jest równe
# > większe niż
# < mniejsze niż
# >= większe lub równe
# <= mniejsze lub równe


# print(2 == 2)
# print(10 == 3)
# print(10>3)
# print(8 != 5)
# print(7 <= 7)

# a = (20+20)
# b = (25+15)
# print(a == b)
#
# a = (3*3)
# b = (12-3)
# print(a == b)


# Operatory logiczne
# AND (koniukcja) - jeżeli oba warunki są prawdziwe
# OR (alterntywa) - jeden z warunków jest orawdziwy
# NOT - zaprzeczenie

# print(2 == 2 or 10 == 3)
# print(10 > 3 and 8 !=5)
# print(not 7 <= 7)


# a = "Dupa"
# b = "Cipa"
# print(a < b) #sprawdz alfabetyczność
# print("zenon" < "adrian")


# operacje na napisach
# print("python " + "is " + "cool") #dodawania (konkatencja)
# print("python " * 3) # powielanie


# znaki specjalne
# print("jestem wesoły romek\nmam na przedmieściu domek") # \n znak nowej linii
# print("jestem wesoły romek\t mam na przedmieściu domek") # \t tabulator przerwa
# print("\"jestem wesoły romek\" mam na przedmieściu domek") # \" cudzysłów
# print("\'jestem wesoły romek\' mam na przedmieściu domek") # \' apostrof

# program na trzykrotnośc jakijeś wartości tekstowej
# a = "jestem wesoły romek\nmam na przedmieściu domek\n"
# print(a * 3)


# imie nzwiako i wyświetl ze spacją
# a = "Maciej"
# b = "Pińczewski"
# print(a, b, sep=" ")


# hello world w dwóch liniach
# print("hello world\nhello world")


# Operacje na
from random import randint

napis = "phyton"


# print(napis.upper()) # uppnapis = input("Podaj słowo\n")er() zamienia na wielkie litery
# print(napis.lower()) # lowwe() zmienia na małe litery
# print(napis.swapcase()) # swapcase() zamienia litery duże na małe i odwrotnie
# print(napis.capitalize()) # capitalize() robi pierwszą literę wielką
# print(napis.title()) # title() zmienia pierwze litery na wielkie
# print(napis.strip()) # strip() usuwa wszystkie spacje tabuatory etc, na poczatku i końcu


# Instrukcja warunkowe

# liczba = int(input("podaj swoją liczbę\n"))
# if liczba > 0:
#     print("Twoja liczba jest dodatnia")
# elif liczba < 0:
#     print("Twoja liczba jest ujemna")
# else:
#     print("Twoja liczba to 0")

# liczba = int(input("Podaj swoją liczbę\n")) # Drugi sposób
# if liczba > 0:
#     print("twoja liczba jest dodatnia")
# elif liczba == 0:
#     print("twoja liczba to 0")
# else:
#     print("twoja liczba jest ujemna")

# Czy liczba jest parzysta
# liczba = int(input("Podaj liczbę\n"))
# if liczba % 2 == 0:                    # musi być dwa razy znak równośći "%' daje resztę z dzielenia
#     print("twoja liczba jest parzysta")
# else:
#     print("twoja liczba jest nieparzysta")


# number=int(input("podaj liczbę\n"))   #inny sposób
# if number % 2:
#     print("Podana liczba jest nieparzysta")
# else:
#     print("Podana liczba jest parzysta")


# sprawdz czy wartośc mieści się w przedziale od 0 do 9
# liczba = int(input("podaj liczbę\n"))
# if 10 > liczba >-1:
#     print("twoja liczba mieści się w przedziale")
# else:
#     print("twoja liczba nie mieście się w przedziale")


# punkty = int(input("Podaj wynik\n"))
# if -1 < punkty < 21:
#     print("Masz ocenę niedostateczną")
# elif 20 < punkty < 41:
#     print("Masz ocenę dopuszczającą")
# elif 40 < punkty < 61:
#     print("Masz ocenę dostateczną")
# elif 60 < punkty < 81:
#     print("Masz ocenę dobrą")
# elif 80 < punkty <= 100:
#     print("Masz ocenę bardzo dobrą")
# else:
#     print("źle podałeś punkty")


# Program
# pyt1 = input("Czy lubisz podróżować?\n")
# if pyt1 == "nie":
#     print("Na pewno masz inne ciekawe hobby!")
# elif pyt1 == "tak":
#     pyt2 = input("Często podróżujesz?\n")
#     if pyt2 == "tak":
#         print("Ekstra!")
#     elif pyt2 == "nie":
#         print("Podróżuj więcej polecam!")


# sprawdź pełnoletniość
# rok = int(input("w którym roku się urodziłeś?\n"))
# if 2019 - rok > 17:
#     print("jesteś pełnoletni")
# else:
#     print("Nie jesteś pełnoletni")


# Program do liczenia dni miesiąca
# month = input("Wybierz jakiś miesiąc\n")
# if month == "styczeń" or month == "marzec" or month == "maj" or month == "lipiec" or month == "sierpień" or month == "październik" or month == "Grudzeiń":
#     print("twój miesiąc ma 31 dni")
# elif month == "kwiecień" or month == "czerwiec" or month == "wrzesień" or month == "listopad":
#     print("twój miesiąc ma 30 dni")
# elif month == "luty":
#     print("twój miesiąc ma 28 albo 29 dni")
# else:
#     print("nie podałeś nazwy miesiąca")


# wartość bezwzględna liczby
# liczba = int(input("Podaj liczbę\n"))
# # if liczba >= 0:
# #     print(liczba)
# # elif liczba <0:
# #     print(liczba*-1)


# drugi sposób
# number=int(input("wpisz liczbę\n"))
# if number >= 0:
#     print(number)
# else:
#     print(- number)


# liczba1 = int(input("Podaj pierwszą liczbę\n"))
# liczba2 = int(input("Podaj drugą licznę\n"))
# if liczba2 > liczba1:
#     print(liczba2)
# elif liczba1 > liczba2:
#     print(liczba1)
# else:
#     print("liczny są równe")


# list1 = ["Gruszka", "jabłko", "cytryna", "Whisky", "Cola", "woda", "gówno"]
# print(list1[1],list1[4:])

# var1 = [1,6,12,18,34] #dodaj dwie liczby do listy i usuń jedną
# print(var1)
# var1.append(24)
# var1.append(48)
# print(var1)
# var1.pop(2)
# print(var1)


# var1 = int(input("Podaj liczbę\n"))
# var2 = 30
# while not var1 == var2:  # wykonuje pętle tak długo aż zmienne nie są równe
#     if var2 > var1:
#         print("nie zgadłeś. Ta liczba jest mniejsza")
#     else:
#         print("nie zgadłeś. ta liczba jest większa")
#     var1 = int(input("spróbuj jescze raz\n"))
# print("zgadłeś")  # to jest poza pętlą

# var1 = int(input("Podaj liczbę\n"))
# var2 = 30
# licznik = 1 # licnzik zgadnięć
# while not var1 == var2:  # wykonuje pętle tak długo aż zmienne nie są równe
#     if var2 > var1:
#         print("nie zgadłeś. Ta liczba jest mniejsza")
#     else:
#         print("nie zgadłeś. ta liczba jest większa")
#     var1 = int(input("spróbuj jescze raz\n"))
#     licznik = licznik + 1 # dodaje wartośc do licznika
#
# print("zgadłeś za", licznik, "razem")  # to jest poza pętlą

#
# var1 = int(input("Podaj liczbę parzystą"))


# number=int(float(input("podaj liczbę\n")))
# if number %2 == 0:
#     print("Podana liczba jest parzysta")
# else:
#     print("Podana liczba jest nieparzysta")

# number=int(input("podaj liczbę\n"))
# if number % 2:
#     print("Podana liczba jest nieparzysta")
# else:
#     print("Podana liczba jest parzysta")


# number=int(input("podaj liczbę\n"))
# while not number %2 == 0:
#     print("podana liczba jest nieparzysta")
#     number = int(input("podaj liczbę\n"))
#
# print("Ta liczba jest parzysta")


# for
# var = "dupa"   #for wyświetla po kolei elementy
# var2 =""
# for i in var:
#     print(i)


# var = (1, 2, 3, 4)   #for wyświetla po kolei elementy nawet krotki
# for i in var:
#     print(i)


# var = "ABCD"
# var2 =""
# for i in var:
#     var2 += i
#     print(var2)


# list = [1,2,3,4,5,6,7] # tu mnoży kązdy element zniory przez 10
# list2 = []
# for i in list:
#     list2.append(i * 10)
# print(list2)


# list = [1,2,3,4,5,6,7] #bierze pierwszy element mnoży, powtarza i bierze kolejny
# list2 = []
# for i in list:
#     list2.append(i * 10)
#     print(list2) # to jest róznica we wcięciu


# var = [3,4,5,6,7,8,9]
# var2 = []
# for i in var:
#     var2.append(i * i)
# print(var2)


# zadanie 0
# var1 = input("Podaj skalę Celcjusz (c), kelwin (k)\n")
# var2 = int(input("podaj temperaturę\n"))
#
# if var1 == "c":
#     print(var2 + 273)
# elif var1 == "k":
#     print(var2 - 273)

# Zadanie 1
# var1 = input("Podaj skalę Celcjusz (c), fahrenheita (F)\n")
# var2 = int(input("podaj temperaturę\n"))
#
# if var1 == "f":
#     print("twoja temperatura w stopniach celcjusza to: ", (var2 - 32) / 1.8)
# elif var1 == "c":
#     print("twoja temperatura w stopniach fahrenheita to: ", var2 *1.8 +32)


# Lista - jest to uporządkowana kolekcja obiektów. n.p. karta dań w restauracji
# my_list = [1, "Ala", True]
# print(my_list)

# my_list.append("Ola") # .append() dodaje element listy
# print(my_list)

# my_list.append(2)
# print(my_list)

# my_list.pop(2) # .pop usuwą konkretny element listy (zaczynamy liczenie od 0
# print(my_list)
#
# print(my_list[2]) # można odwołać się do konkretnego elementu listy
#
# print(my_list[-1]) # można odwoływac się również od końca
#
# my_list[1] = "Ala ma kota" # można łatwo podmienić element listy
# print(my_list)


# Slicing - Szatkowanie
# list_1 = [1,2,3,4,5,6,7]
# print(list_1)

# print(list_1[2:6]) #to wyświeta listę od 3 elementu do 6
#
# list_2 = ["dupa", "noga,", "głowa", "ręka"]
# print(list_2)
# print(list_2[0:5:2]) # pierwszy element : ostatni element : liczba kroków
# print(list_1[::-1]) # tu zakres jest odwrócony

# list_3 = list_2 + list_1 # listy można dodawać
# print(list_3)

# list_1.extend(list_2) # komenda .extend dodaje inną listę jest to szybsza metoda
# print(list_1)

# del list_1[2] # del przed zmienną usuwa element

# del list_2[1]


# list_1 = [9] + list_1 # to dodaje coś na początku listy

# list_1 = list_1[:-1] + [8] + list_1[-1:] # tu dodajemy element do listy w konkretnym miejscu
# list_2 = list_2[:1] + ["stopa"] + list_2[1:]


# print(min(list_1)) # min() zwraca najmniejszą wartość z listy
# print(max(list_1)) # max() zwraca największą wartośc  listy
# print(sum(list_1)) # sum() sumuje wartość z listy
# print(len(list_1)) # len() zwraca długośc listy
# print(list(reversed(list_1))) # list(reversed() odwraca listę

# print(list(sorted(list_1))) # list(sorted() sortuje listę ale robi to w kopii listy
# list.sort(list_1) # list.sort() też sortuje podmienia listę
# # print(list_1)


# zip
# list_1 = ['jajko', 'marmolada', 'ser']
# list_2 = ['szynka', 'kiełbasa', 'salceson']
# quantities = [10, 1, 2]

# print(list(zip(list_1, quantities)))# list(zip()) zwraca sekwencje krotek, gdzie każdy element pochodzi z jednej z list
#
# print(list(zip(list_1, list_2))) # drugi przykład

# nowa = list(zip(list_1, list_2)) # przykład tworzenia zmiennej
# print(nowa)


# zadanie Utwórz listę siedmiu artykułów spoż. Wyświetl trzy pierwsze i trzy ostatnie

# list_3 = list_1 + list_2 + ['marmolada'] # wykorzystałem już istniejące listy i dodałem jeden artykuł
# print(list_3)
# print(list_3[0:3],list_3[4:7])


# list_1 = [5,2,3,1,4] # dodaj dwa elementy do listy i usuń 3 element
# # print(list_1)
# list_1.append(6)
# list_1.append(7)
# del(list_1[2])
#
# print(list_1)
#
# list.sort(list_1) # mam posortowac listę
# print(list_1)


# Operator in oraz metoda index
# print([1,2,3] == [1,2,4])
# print([1,2,3] == [1,2,3])
# print([1,2,3] > [1,2,0])
# print([1,2,3] > [1,"a", 0]) # tak się nie da tam jest string


# print("asd" in [1,2, "asd", 3, True, 4.5]) # sprawdzamy czy w "asd" znajduje się na liście
# print(-52.1 in [1,2,"asd", 3, True, 4.5])
# print(-52.1 not in [1,2,"asd", 3, True, 4.5]) # sprawdzamy czy nie ma tam elementu -52.1


# Krotki zapisujemy a nawiasach okrągłych. działają jak listy ale nie można edytowac elementów

# krotka_1 = (1,2,3)
# print(krotka_1)
#
# krotka_1 = krotka_1 +(5,) # krotki można tylko konkatenować
# print(krotka_1)


# zbiory (set) jest jak worek. Kiedy wkładasz rękę do worka nie wiesz co wyciągniesz
# w przeciwieśntwie do list kolejność elementów nie ma znaczenia, ale się nie powatarzają

# set_1 = {1,2,3,4,5,6,7,}
# print(set_1)

# list_1 = [1,2,3,4,5,5,6,6,6,7]
# print(list_1)
# # set_1 = set(list_1) # przekształcamy listę w zbiór, żeby pozbyc się duplikatów
# # print(set_1)
# # list_2 = list(set_1) # i zamieniamy spowrotem zbiór na listę
# # print(list_2)
#
# #albo
#
# list_2 = list(set(list_1)) # tu też pozbędziemy się duplikatów
# print(list_2)

# # Operacje na zbiorach
# set_1 = {1,2,3,4,5}
# set_2 = {4,5,6,7,8}
#
# print(set_1 | set_2 # znak | sumuje zbiory (unia)
# print(set_1 & set_2 # znak & daje iloczyn (przecięcie, część wspólna)
# print(set_1 - set_2) # różnica
# print(set_2 - set_1) # inny przykład
# print(set_1 ^ set_2) # znak ^ pokazuje częsci zbiorów które się nie pokrywają

# set_1.add(6) # funkcja .add() dodaje element do zbioru
# set_1.update({7,8,9}) # funkcja .update({}) dodaje elementy do zbioru
# set_1.remove(4) # .remove() usuwa element zbioru

# print(set_1.clear()) # .clear() czyści zbiór
# print(set_1)

# print(len(set_1)) # len() daje wielkośc zbioru
# print(min(set_1)) # min() podaje najmniejszą wartość
# print(max(set_1)) # max() podaje największą wartośc
# print(sum(set_1)) # sum() podaje sumę elementów zbioru

# print(8 in set_1 # in sprawdza czy w zbiorze jest taka wartość


# Słownik - dict Podobny do ksiązki tlefonicznej lub encyklopedii
# zaglądamy pod pewien klucz (n.p. nazwisko, hasło encyklopedii i dostajemy jakąś wartość
# w Słowniku jak w zbiorze jego klucze musza być unikalne
# Słownik tworzymy wpisując pary: klucz:wartość

# dict_1 = {"Eliza":30, "Maciej":34, "Tomasz":23, "Iwona":58}
#
# print(dict_1["Eliza"]) # sprawdzam wiek elizy
# dict_1['Tata'] = "nie pamiętam" # tak dodaejmy element do słownika
# print(dict_1)
# del dict_1["Tata"] # usuwa klucz ze słownika
# print(dict_1)
#
# print(dict_1["Kupa"]) # jeżeli wywołamy klucz którego nie ma wywali nam błąd, zamiast tego używamy get
# print(dict_1.get("Brat")) # funkcja .get() sprawdza czy dany klucz istnieje, bez wywalania błedu

# dict_2 = {} # {} tworzy nam pusty słownik
#
#
# # zadanie spytaj o miesiąc i zwróc info ile ma dni
# var1 = input("Podaj swój miesiąc\n")
# var2 = var1.lower() #zmieniamy litery na małe
# if var2 == "styczeń" or var2 == "marzec" or var2 == "maj" or var2 == "lipiec" or var2 == "sierpień" or var2 == "październik" or var2 == "Grudzeiń":
#     print("Twój miesiąc ma 31 dni")
# elif var2 == "kwiecień" or var2 == "czerwiec" or var2 == "wrzesień" or var2 == "listopad":
#     print("Twója miesiąc ma 30 dni")
# elif var2 == "luty":
#     print("Twój miesiąc ma 28 lub 29 dni")
# else:
#     print("musisz podac miesiąc")


# for
# list_1 = [1,2,3,4,5,6,7]
# list_2 = [] # tworzymy nową zmienną
# for element in list_1: # dodajemy nową zmienną < element >
#     list_2.append(element-5) # dodajemy < append() żeby wykonac równania
# print(list_2)


# list_1 = [1,2,3,4,5,6,7]
# list_2 = [8,9,0]
# list_4 = list_1 + list_2
# print(list_4)
# list_3 = []
# for element in list_4:
#     list_3.append(element*10)
# print(list_3)


# var1 = "Siema!, "
# print(var1*3)


# Funkcja Range określa zakres
# print(list(range(10))) # Funkcja range() daje sekwencje liczb całkowitych
# print(list(range(1, 11))) # podaje zakres liczb
# print(list(range(10, 100 ,10)) # od, do, co ile
# print(list(range(0, -10, -1)))

# Funkcja enumerate numeruje każdy argument z listy

# var1 = list(range(0, 50, 5))
# print(var1)
#
# print(list(enumerate(var1)))

# n.p.
# list1 = [32, 43, 5, 6, 87, 13, 9 ,64]
# for idx, value in enumerate(list1): # idx to argument dla for, mógłby być inny
#     print(idx, value)


# pętla while działa tak długo aż zostanie spełniony warunek
# number = int(input("podaj liczbę\n"))
# while number >= 0:
#     print(number)
#     number -=1 #odlicza do 0

# kwadraty liczb od 3 do 9


# list_1 = []
# for liczby in range(3, 10):
#     list_1.append(liczby ** 2)
# print(list_1)

#
# new_list = []
# _list)for l in range(3, 10):
#     new_list.append(l ** 2)
# print(new

# list1 = []
# for liczby in range(1, 10):
#     list1.append(liczby -2)
# print(list1)

#
# list1 = [] #liczby naturalne do 99, parzyste
# for l in range(0, 99, 2):
#     list1.append(l)
# print(list1)


# s = "125" #można zamieniać stringi na intigery
# print(2*int(s))


#
# numbers = input("Podaj cyfry\n")
# dict = {1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"pięć", 6:"sześć", 7:"siedem", 8:"osiem", 9:"dziwięć", 0:"zero"}
#
# for i in numbers:
#     print(dict(i))

#
# var1 = input("podaj 1 słowo\n")
# var2 = input("podaj 2 słowo\n")
# var3 = input("podaj 3 słowo\n")
# var4 = input("podaj 4 słowo\n")
# var5 = input("podaj 5 słowo\n")
#
# var6 = len(var1)
# var7 = len(var2)
# var8 = len(var3)
# var9 = len(var4)
# var10 = len(var5)
#
# dict = {var1:var6, var2:var7, var3:var8, var4:var9, var5:var10}
# print(dict.values())


# var1 = input("podaj 1 słowo\n")
# var2 = input("podaj 2 słowo\n")
# var3 = input("podaj 3 słowo\n")
# var4 = input("podaj 4 słowo\n")
# var5 = input("podaj 5 słowo\n")
#
#
# my_list = (var1, var2, var3, var4, var5)
# max_count = 0 # zmienna o wartości 0
# the_word = ""
#
# for i in range(5): # tu musi być 5 żeby kazac 5 tazy liczyć
#     len(my_list[i]) # i działa jak pierwszy obrót pętli czyli podstawia najpier var1
#     if len(my_list[i]) > max_count: # to jest ta zamienna o wartości 0
#         the_word = "" # przy kolejnej pętli jesli słowo bylo krótsze ot zamieniamy je w puste
#         the_word += my_list[i] + " " # jeżeli to słowo które jest sprawdzane jest większe od 0 to do pustej zmiennej wkleja to słowo
#         max_count = len(my_list[i]) # podaje długośc najdłuższego słowa przy kolejnych pętlach
#
# print(the_word)

#

# Stwórz listę zawierającą kilka liczb całkowitych, a następnie program,
# który wskaże indeks najmniejszego z nich, iterując po nich.

# lista = [5, 3, 8, 1, 9]
# najmniejsza = lista[0]
# indeks = 0
# for elem in range(1, len(lista)):
#     if lista[elem] < najmniejsza:
#         najmniejsza = lista[elem]
#         indeks = elem
#
# print(najmniejsza, indeks)


# Napisz program, który policzy iloczyn elementów wybranej przez siebie
# listy, iterując po nich.

# lista = [1, 2, 3, 4, 5]
# iloczyn = lista[0]
# for elem in lista:
#     iloczyn *= elem
# print(iloczyn)
#
# var1 = [1, 2, 4, 4, 5]
# cyfra = var1[0]
# for i in var1:
#     cyfra *= i
# print(cyfra)
#

# list1 = [1, 2, 3, 4, 5]
# newlist = list1[0]
#
# for elem in list1:
#     newlist  *= elem
# print(newlist)

# DOdajmy razy 2

# list1 = [1, 2, 3, 4, 5]
# wynik = list1[0]
#
# for elem in list1:
#     wynik *= elem*2
#     print(wynik)

# BMI

# wzrost = float(input("podaj wzrost w metrach\n"))
# waga = int(input("Podaj wagę w kg\n"))
# bmi = waga/(wzrost*wzrost)
# if bmi < 18.5:
#     print("masz niedowagę")
# elif 18.5 <= bmi <= 24.9:
#     print("prawidłowa waga")
# elif 25 <= bmi < 29.9:
#     print("masz nadwagę")
# elif bmi >= 30:
#     print("jesteś otyły")

# peron do hogwartu

# imie = input("Jak się nazywasz czarodzieju?\n")
# nazwisko = input("jak masz na anzwisko?\n")
# peron = float(input("z jakiego peronu chcesz jechać?\n"))
# if peron == 9.75:
#     print("Carodzieju", imie, nazwisko, "Zapraszamy do hogwartu")
# else:
#     print("Mugolu", imie, nazwisko, "wracaj do domu")


# lista1 = [4, 8, 3, 1, 10]
# najmniejsza = lista1[0]
# indeks = 0
#
# for elem in range(1, len(lista1)):
#     if lista1[elem] < najmniejsza:
#         najmniejsza = lista1[elem]
#         indeks = elem
# print(najmniejsza, indeks)
#

#
# list1 = [4, 3, 9, 1, 10]
# naj = list1[0]
# indeks = 0
# for elem in range(1, len(list1)):
#     if list1[elem] < naj:
#         naj = list1[elem]
#         indeks = elem
#
# print(naj, indeks)
#
# list1 = [100, 8, 122, 12, 87, 250, 1164]
# var = list1[0]
# position = 0
#
# for i in range(1, len(list1)):
#     if list1[i] < var:
#         var = list1[i]
#         position = i
# print(var, position)

# quote='''To jest wielolinijkowy tekst
# zawierający cytat
# "Always code as if the guy who ends up maintaining your code will be a
# violent psychopath who knows where you live"
# -John Wood'''
# print(quote)

# !!!!!!!!!!!!!!!!!
# print("{} ma {}".format("Ala", "kota"))
# print("{1} ma {0}".format("Ala", "kota"))

# Napisz skrypt, który, który obliczy stan konta za kilka lat. Program pyta użytkownika o:
#
# stan początkowy konta,
# stopę oprocentowania rocznego (zwróć uwagę, że odsetki podlegają miesięcznej kapitalizacji)
# liczbę lat na lokacie.
# Wynik wyświetl jako zdanie używając dowolnego sposobu formatowania tekstu. Wypisz np. takie zdanie:
# Twoje *stan_początkowy* zł przez *czas* lata na lokacie *oprocentowanie* % urośnie do *wynik*.
#
# stan_p = float(input("podaj stan poczatkwy konta\n"))
# procent = float(input("podaj oprocentowanie\n"))
# okres = int(input("ile lat będziez trzymał środki\n"))
# pytanie = input("Co jaki okres występuje kapitalizacja?\n")
#
# miesiąc = okres*12
# procent_m = procent/12
#
# dzień = okres*365
# procent_d = procent/365
#
# if pytanie == "miesiąc" or pytanie == "miesięcznie":
#     wynik = stan_p * ((1 + (procent_m / 100)) ** miesiąc)
#     print(wynik)
# elif pytanie == "rok" or pytanie == "rocznie":
#     wynik = stan_p * ((1 + (procent / 100)) ** okres)
#     print(wynik)
# elif pytanie == "dzień" or pytanie =="dziennie":
#     wynik = stan_p * ((1 + (procent_d / 100)) ** dzień)
#     print(wynik)


# stan_p = float(input("podaj stan poczatkwy konta\n"))
# procent = float(input("podaj oprocentowanie\n"))
# okres = int(input("ile lat będziez trzymał środki\n"))
# pytanie = input("Co jaki okres występuje kapitalizacja?\n")
#
# if pytanie = "dzień":
#
# miesiąc = okres * 12
# procent_m = procent / 12
#
# wynik = stan_p * ((1 + (procent_m / 100)) ** miesiąc)
# print(wynik)

# licznik = 0


# Zadanie program który wyświetli 6 losowych niepotwrzających się liczb od 1 do 50


# from random import randint
# lista = []
# while len(lista) < 6:
#     liczba = randint(1, 50)
#     if liczba in lista:
#         continue
#     lista.append(liczba)
# print(lista)


# from random import randint
# lista = []
# while len(lista) < 6: # ma przerwać kiedy będzie miał 6 elementów
#     liczba = randint(1, 50)  # zakres liczb losowych
#     if liczba in lista: # żeby się nie powtarzały
#         continue
#     lista.append(liczba)
# print(lista)

# from random import randint
# zbiór = []
# while len(zbiór) < 6:
#     liczba = randint(1, 50)
#     if liczba in zbiór:
#         continue
#     zbiór.append(liczba)
# print(zbiór)


# from random import randint
# list1 = []
# while len(list1) < 10:
#     number = randint(1, 50)
#     if number in list1:
#         continue
#     list1.append(number)
#
# print(list1)


# Zadanie
# Napisz program, który generuje losową liczbę z zakresu [0; 10] i każe ci ją
# odgadnąć. Masz trzy próby. Inaczej „Hasta la vista, baby”, sorry.

# import random
#
# number = random.randint(1, 10)
# print(number)
#
# licznik = 0
# while licznik < 3:
#     user_number = int(input("podaj liczbę od 1 do 10\n"))
#     if number == user_number:
#         licznik += 1
#         print("Brawo zgadłeś za", licznik, "razem!")
#         break
#     if licznik < 2:
#         print("spróbuj jeszcze raz")
#     licznik += 1
# if licznik == 3:
#     print("hasta la vista Baby!")


# from random import randint
# wylosowana_liczba = randint(0,10)
# proba = 0
# while proba < 3:
#     liczba = int(input("POdaj liczbę\n"))
#     if liczba == wylosowana_liczba:
#         print("zgadłeś")
#         break
#     if proba < 2:
#         print("dawaj jeszcze raz")
#     proba += 1
# if proba == 3:
#     print("Hasta la vista baby")

#
# var1 = input("wpisz liczbę\n")
# var2 = {1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"pięć", 6:"sześć", 7:"siedem", 8:"osiem", 9:"dziwieć", 0:"zero"}
# var3 = ""
#
# for i in var1: # rozbija var1 na pojedyńcze znaki
#     var3 += var2[int(i)] + " " # dodaje do zbioru var3 liczbę ze słownika
#
# print(var3)


# dict = var2 = {1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"pięć", 6:"sześć", 7:"siedem", 8:"osiem", 9:"dziewieć", 0:"zero"}
# var1 = input("wpisz liczbę")
# var2 = ""
#
# for i in var1:
#     var2 += dict[int(i)]
#
# print(var2)

# var1 = input("Podaj jakąś liczbę\n")
# cyfra = var1[0] # tworzymy nową zmienną
# print(cyfra)
# for i in var1:
#     cyfra *= i
# print(cyfra)


# var0 = input("podaj liczbę\n")
# var1 = 1
# for elem in var0:
#     var1 = var1 * int(elem)
# print(var1)


# var0 = input("podaj liczbę\n")
# var1 = 1
# for i in var0:
#     var1 = var1 * int(i) # tu zmieniamy "i" na intiger
# print(var1)

#
# var1 = input("podaj 1 słowo\n")
# var2 = input("podaj 2 słowo\n")
# var3 = input("podaj 3 słowo\n")
# var4 = input("podaj 4 słowo\n")
# var5 = input("podaj 5 słowo\n")
#
# var6 = (var1, var2, var3, var4, var5)
# print(var6)
# licznik = 0
# slowo = ""
#
# for i in range[5]:
#     len(var6[i])
#     if len(var6[i]) > licznik:


# a = "Dupa"
# b = 45
# c = 3.14
# d = True
# e = 1, 3 ,5
# f = (1, 2, "dupa")
# g = [1, 5, 6, "dupa"]
# h = {"ja":1, "ty":2, "my": 3}
# i = (1, 2, "dupa")
#
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))
# print(type(i))


# Zadanie
# Napisz program, który wczyta od użytkownika liczbę całkowitą i wyświetli
# informację czy jest parzysta, czy też nie.

# var1 = input("Podaj cyfrę\n")
#
# # letters = [a,ą,b,c,ć,d,e,ę,f,g,h,i,j,k,l,ł,m,n,ń,q,o,p,r,s,t,u,w,x,y,z,ź,ż]
#
# if int(var1) % 2 == 0:
#     print("Twoja liczba jest parzysta")
# else:
#     print("twoja liczba jest nieparzysta")


# Zadanie
# Napisz program, który sprawdzi, czy podana przez użytkownika wartość
# mieści się w przedziale od 0 do 9 (włącznie)

# var1 = int(input("wpidz jakąś liczbę\n"))
#
# if   0 >= var1 < 10:
#     print("ta liczba jest jednocyfrowa")
# else:
#     print("ta liczba nie jest jednocyfrowa")


# Zadanie
# Napisz program, który zwróci wartość bezwzględną danej liczby

# var1 = int(input("podaj liczbę"))
# if var1 < 0:
#     print(var1*-1)
# else:
#     print(var1)


# Zadanie
# Utwórz listę zawierającą siedem artykułów spożywczych. Wyświetl na
# ekranie pierwszy i trzy ostatnie elementy listy

# list = ["oko", "ucho", "nos", "dupa", "głowa", "kolano", "stopa"]
# print(list[0], list[-3:])


# Zadanie
# Utwórz listę pięciu liczb naturalnych. Następnie dodaj dwie nowe na jej
# koniec. Usuń trzeci element.
# Na końcu posortuj listę

# list = [7, 5, 11, 12, 3]
# list.append(17)
# list.append(13)
# print(list)
# list.pop(2)
# print(list)
# list.sort()
# print(list)


# Zadanie 7.                 DZIAłA!
# Napisz program, który obliczy liczbę małych i wielkich liter w ciągu.
# np : 'The quick Brown Fox'
# oczekiwany wynik :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

# var1 = "The quick Brown Fox"
# upper = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,Q,P,R,S,T,U,W,X,Y,Z"
# lower = upper.lower()
# lowcount = []
# uppercount = []
#
# for elem in var1:
#     if elem in upper:
#         uppercount += elem
#     if elem in lower:
#         lowcount += elem
#
# print(len(lowcount))
# print(len(uppercount))


# Zadanie 2.                        DZIAłA
# Napisz funkcję, która sprawdzi, czy podany jako argument napis jest
# pangramem (tj. zawiera każdą literę alfabetu co najmniej raz, np. „The
# quick brown fox jumps over the lazy dog”).

# lower = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,q,p,r,s,t,u,w,x,y,z"
# var1 = str(input("Podaj zdanie\n"))
# var2 = {1}
# var2.clear()
#
# for i in var1:
#     if i in lower:
#         var2.add(i)
# lower = set(lower)
# if var2 >= lower:
#     print("twoje zdanie to pangram")
# else:
#     print("twoje zdanie nie jest pangramem")


# Zadanie 6.
# Napisz funkcję, która sprawdzi, czy rok podany jako argument jest
# przestępny.


# def rok_przestępny(a):      #DZIAłA
#     rok = a
#     if rok % 4 == 0 and rok % 100 != 0:
#         return print("twoj rok jest przestępny")
#     elif rok % 400 == 0:
#         return print("twoj rok jest przestępny")
#     else:
#         return print("twoj rok nie jest przestępny")
#
# rok_przestępny(2020)


# Zadanie
# Napisz program, który wyświetli 6 losowych i niepowtarzających się liczb
# całkowitych od 1 do 50.

# from random import randint
# var1 = []
# while len(var1) < 6: # ma przerwać kiedy będzie miał 6 elementów
#     liczba = randint(1, 50)  # zakres liczb losowych
#     if not liczba in var1: # żeby się nie powtarzały
#         var1.append(liczba)
# print(var1)


# from random import randint
# var1 = []
# while len(var1) < 6:
#     var2 = randint(1, 50)
#     if var2 not in var1:
#         var1.append(var2)
#
# print(var1)


# Zadanie
# Napisz program, który generuje losową liczbę z zakresu [0; 10] i każe ci ją
# odgadnąć. Masz trzy próby. Inaczej „Hasta la vista, baby”, sorry.

# from random import randint
#
# var2 = randint(1, 10)
# counter = 0
# print(var2)
#
# while counter < 3:
#     var1 = int(input("Podaj liczbę od 0 do 10\n"))
#     counter += 1
#     if var1 == var2:
#         print("brawo zgadłeś za", counter,"razem")
#         break
#     if counter < 3:
#         counter += 1
#         var1 = int(input("spróbuj jeszcze raz\n"))
# if counter == 3:
#     print("hasta la vista baby")


# from random import randint
#
# var2 = randint(1, 10)
# counter = 0
# print(var2)
# var1 = int(input("Podaj liczbę od 0 do 10\n"))
# while True:
#
#     if var1 == var2:
#         counter += 1
#         print("brawo zgadleś za", counter, "razem")
#         break
#     if counter == 2:
#         print("hasta la vista baby!")
#         break
#     else:
#         counter +=1
#         var1 = int(input("Spróbuj jeszcze raz\n"))


# import math
#
# def pole_koła(r):
#     var1 = math.pi * r**2
#     return var1
#
# print(pole_koła(33))

# def palindrom(pal):
#     if pal == reversed(pal):
#         return print("twój wyraz jest palindromem")
#     else:
#         return print("twója wyraz nie jest palindromem")
#
# print(palindrom("abcdcba"))

# def palindrom(var1):
#     pal = list(var1.lstrip())
#     pal2 = list(reversed(pal))
#
#     if pal == pal2 :
#         return print("twój wyraz to palindrom")
#     else:
#         return print("twój wyraz nie jest palindromem")
#
# palindrom(var1 = "kobyłamamałybok")


# Zadanie Napisz funkcję która przymujuje paramter n i zwraca n liczb parzystych od 1


# def parzyste(n):
#     var1 = []
#     i = 1
#     while len(var1) < n:
#         if i % 2 == 0:
#             var1.append(i)
#         i += 1
#     return var1
#
#
# print(parzyste(10))


# lower = "aąbcćdeęfghijklłmnńopqrstóuwxyzźż"
# upper = lower.upper()
# digits = "01234567890"
# specials = "!@$%^&*"
# totatlcounter = set()
#
# password = input("Wpisz swoje hasło\n")
#
# for i in password:
#     if i in lower:
#         totatlcounter.add("l")
#     if i in upper:
#         totatlcounter.add("u")
#     if i in digits:
#         totatlcounter.add("d")
#     if i in specials:
#         totatlcounter.add("s")
# print(totatlcounter)
# while len(password) > 12 or len(password) < 6 and "l" not in totatlcounter or "u" not in totatlcounter or "d" not in totatlcounter or "s" not in totatlcounter:
#     print("Twoje hasło powinno mieć od 6 do 12 znaków, oraz zawierać Jedną wielką literę, jedną małą, cyfrę i jeden znak specjalny\n")
#     totatlcounter.clear()
#     password = input("Wpisz swoje hasło\n")
#     for i in password:
#         if i in lower:
#             totatlcounter.add("l")
#         if i in upper:
#             totatlcounter.add("u")
#         if i in digits:
#             totatlcounter.add("d")
#         if i in specials:
#             totatlcounter.add("s")
# print(totatlcounter)
#
#         if "l" in totatlcounter or "u" in totatlcounter or "d" in totatlcounter or "s" in totatlcounter and 6 >= len(password) < 13:
#             break
# print("Hasło zostało zmienione")


# def haslo(password):
#     lower = "aąbcćdeęfghijklłmnńopqrstóuwxyzźż"
#     upper = lower.upper()
#     digits = "01234567890"
#     specials = "!@$%^&*"
#     totatlcounter = set()
#
#     while len(password) > 12 or len(password) < 6:
#         return print("Twoje hasło powinno mieć od 6 do 12 znaków\n")
#
#     for i in password:
#         if i in lower:
#             totatlcounter.add("l")
#         elif i in upper:
#             totatlcounter.add("u")
#         elif i in digits:
#             totatlcounter.add("d")
#         elif i in specials:
#             totatlcounter.add("s")
#
#     while "l" not in totatlcounter or "u" not in totatlcounter or "d" not in totatlcounter or "s" not in totatlcounter:
#         return print("Twoje hasło nie spełnia wymagań\n")
#
#     if "l" in totatlcounter or "u" in totatlcounter or "d" in totatlcounter or "s" in totatlcounter:
#         return print("Hasło zostało zmienione")
#
# haslo1 = input("podaj hasło\n")
#
# haslo(haslo1)


# Zadanie 5.
# Napisz program, który policzy iloczyn elementów wybranej przez siebie
# listy, iterując po nich.


# var1 = [1, 2, 3, 4, 5]
# var2 = var1[0]
#
# for i in var1:
#     var2 *= i
# print(var2)


# lower = "aąbcćdeęfghijklłmnńopqrstóuwxyzźż"
# upper = lower.upper()
# digits = "01234567890"
# specials = "!@$%^&*"
# totatlcounter = set()
#
# password = input("Wpisz swoje hasło\n")
#
# for i in password:
#     if i in lower:
#         totatlcounter.add("l")
#     if i in upper:
#         totatlcounter.add("u")
#     if i in digits:
#         totatlcounter.add("d")
#     if i in specials:
#         totatlcounter.add("s")
#
# while "l" not in totatlcounter or "u" not in totatlcounter or "d" not in totatlcounter or "s" not in totatlcounter or len(password) > 12 or len(password) < 6:
#     totatlcounter = set()
#     print("Twoje hasło nie spełnia wymagań\n")
#     password = input("Wpisz jeszcze raz hasło\n")
#     for i in password:
#         if i in lower:
#             totatlcounter.add("l")
#         if i in upper:
#             totatlcounter.add("u")
#         if i in digits:
#             totatlcounter.add("d")
#         if i in specials:
#             totatlcounter.add("s")
#
# print("Hasło zostało zmienione")
#
#
# lower = "aąbcćdeęfghijklłmnńopqrstóuwxyzźż"
# upper = lower.upper()
# digits = "01234567890"
# specials = "!@$%^&*"
# totatlcounter = set()
#
# def petla(password):
#
#     for i in password:
#         if i in lower:
#             totatlcounter.add("l")
#         elif i in upper:
#             totatlcounter.add("u")
#         elif i in digits:
#             totatlcounter.add("d")
#         elif i in specials:
#             totatlcounter.add("s")
#
#     return totatlcounter
#
# password = input("Wpisz jeszcze raz hasło\n")
# petla(password)
# print(totatlcounter)
# while "l" not in totatlcounter or "u" not in totatlcounter or "d" not in totatlcounter or "s" not in totatlcounter or len(password) > 12 or len(password) < 6:
#     totatlcounter.clear()
#     print("Twoje hasło nie spełnia wymagań\n")
#     password = input("Wpisz jeszcze raz hasło\n")
#     petla(password)
#
#
# print("Hasło zostało zmienione")
#
#
#
# lower = "aąbcćdeęfghijklłmnńopqrstóuwxyzźż"
# upper = lower.upper()
# digits = "01234567890"
# specials = "!@$%^&*"
# totatlcounter = ""
#
# def petla(password):
#     totatlcounter = ""
#     for i in password:
#         if i in lower:
#             totatlcounter += "l"
#         elif i in upper:
#             totatlcounter += "u"
#         elif i in digits:
#             totatlcounter += "d"
#         elif i in specials:
#             totatlcounter += "s"
#     return totatlcounter
#
# password = input("Witamy w systemie bankowości elektronicznej.\n \nWpisz nowe hasło. Hasło musi mieć od 6 do 12 "
#                  "znaków. \nHasło musi zawierać przynajmniej jedną wielką, jedną mała litere, cyfrę i znak "
#                  "specjalny\n")
# petla(password)
# totatlcounter = petla(password)
#
# while "l" not in totatlcounter or "u" not in totatlcounter or "d" not in totatlcounter or "s" not in totatlcounter or len(password) > 12 or len(password) < 6:
#     totatlcounter = ""
#     print("Twoje hasło nie spełnia wymagań\n")
#     password = input("Wpisz jeszcze raz hasło\n")
#     petla(password)
#     totatlcounter = petla(password)
#
#
# print("Hasło zostało zmienione\n")
#
# #
#
# import sys
# ask1 = ''
#
# while ask1 != "t" or ask1 != "n":
#     ask1 = input("czy chcesz się teraz zalogowaćC? \n tak(t), nie (n)?\n")
#     if ask1 == "t" or ask1 == "n":
#         break
# if ask1 == "n":
#     print("Dziękujemy za skorzystanie z naszego systemu logowania\n")
#     sys.exit(0)
# elif ask1 == "t":
#     ownerpassword = input("podaj swoje hasło\n")
#
# if ownerpassword != password:
#     print("Podałeś błedne hasło")
# else:
#     print("Witamy w systemie bankowosci elektronicznej")
#
# #
#
# program = ''
# while program != "k" or program != "e" or program != "b":
#     program = input("Z jakiej funkcji chcesz skorzystać?\nKalkulator oprocentowania: (k)\nKalkulator Brutto - Netto ("
#                     "b)\nWyjście z systemu bankowości: (e)\n")
#     if program == "k":
#         stan_p = float(input("podaj stan poczatkwy konta\n"))
#         procent = float(input("podaj oprocentowanie\n"))
#         okres = float(input("ile lat będziez trzymał środki\n"))
#         pytanie = input("Co jaki okres występuje kapitalizacja?\n Dziennie (d), miesiąc (m), rok (r)\n")
#         pytanie = pytanie.lower()
#         while not pytanie in ["m", "d", "r"]:
#             print("Wybierz zdefiniowaną odpowedź: d - dzień, m - miesiąc, r - rok")
#             pytanie = input("Co jaki okres występuje kapitalizacja?\n Dziennie (d), miesiąc (m), rok (r)\n")
#
#         miesiąc = okres * 12
#         procent_m = procent / 12
#
#         dzień = okres * 365
#         procent_d = procent / 365
#
#         if pytanie == "m":
#             wynik = stan_p * ((1 + (procent_m / 100)) ** miesiąc)
#             print("Twój kapitał po wskaznym okresie, wyniesie:", wynik, "\n")
#
#         elif pytanie == "r":
#             wynik = stan_p * ((1 + (procent / 100)) ** okres)
#             print("Twój kapitał po wskaznym okresie, wyniesie:", wynik, "\n")
#
#         elif pytanie == "d":
#             wynik = stan_p * ((1 + (procent_d / 100)) ** dzień)
#             print("Twój kapitał po wskaznym okresie, wyniesie:", wynik, "\n")
#     elif program == "b":
#         podaj = ''
#         while podaj != "b" or podaj != "n" or podaj != "e" or podaj != "r":
#             podaj = input("Co chcesz obliczyć? Brutto (b) czy netto (n)?\nPowrót do menu (r)\nZakończ program (e)\n ")
#             if podaj == "b":
#                 kwota = float(input("Podaj wysokść wynagrrodzenia netto\n"))
#                 wynagrodzenie = kwota * 140.26 / 100
#                 print("twoja kwota brutto to:", wynagrodzenie)
#             elif podaj == "n":
#                 kwota = float(input("Podaj wysokść wynagrrodzenia brutto\n"))
#                 wynagrodzenie = kwota * 71.3 / 100
#                 print("twoja kwota netto to:", wynagrodzenie)
#             elif podaj == "e":
#                 print("Dziękujemy za skorzystanie z naszego systemu bankowości\n")
#                 sys.exit(0)
#             elif podaj == "r":
#                 break
#
#
#     elif program == "e":
#         print("Dziękujemy za skorzystanie z naszego systemu bankowości\n")
#         sys.exit(0)


# Zaimplementujmy odliczanie oparte na pętli while.
#  Odliczamy w dół od zadanej liczby aż do
# zera

# Zadanie
# Wyświetl kwadraty liczb od 3 do 9

# list1 = []
# # list2 = []
# # for i in range(3, 10):
# #     list1.append(i)
# #
# # for i in list1:
# #     list2.append(i * i)
# #
# # print(list2)


# Stwórz listę zawierającą parzyste liczby naturalne mniejsze od 99.

# list1 = []
# for i in range(0, 100):
#     if i % 2 == 0:
#         list1.append(i)
#
# print(list1)


# Stwórz listę zawierającą kilka liczb całkowitych, a następnie program, który policzy sumę jej elementów, iterując po nich.

# list1 = [4, 7, 11, 45, 67]
# sum = 0
# for i in list1:
#     sum += i
# print(sum)


# Zmodyfikuj program, aby policzyć średnią po wszystkich elementach

# list1 = [4, 7, 11, 45, 67]
# sum = 0
# aver = 0
# for i in list1:
#     sum += i
#     aver = sum / len(list1)
# print(sum)
# print(aver)

# Znajdź indeks elementu największego na liście.

# list1 = [4, 7, 11, 45, 67]
# index = list1[0]
#
# for i in range(1, len(list1)):
#     if list1[i] > index:
#         index = list1[i]
#         index_id = i
# print(index, index_id)

# Jeszcze raz

# lst = [3, 133, 25, 822, 77, 699]
# najw = lst[0]
#
# for i in range(1, len(lst)):
#     if lst[i] > najw:
#         najw = lst[i]
#         index = i
#
# print(najw, index)


# Dla n = 0, 1, …, 20 wypisz wartości określone wzorem:
# x(n) =n2+1

# lst = []
# lst2 = []
# for i in range(1, 21):
#     lst.append(i)
# for i in lst:
#     lst2.append(i*i + 1)
#
# print(lst2)


# Napisz program, który wyświetli listę cyfr od 0 do 10 z pominięciem tych
# podzielnych przez 3.

# lst = []
# for i in range(1, 11):
#     if i % 3 != 0:
#         lst.append(i)
#
# print(lst)

# Zadanie
# Napisz program, który wyświetli 6 losowych i niepowtarzających się liczb
# całkowitych od 1 do 50.

# from random import randint
# var1 = []
# var1 = set(var1)
# while len(var1) < 6:
#     var1.add(randint(1, 50))
# var1 = list(var1)
# print(var1)

# Albo z continue

# from random import randint
#
# var1 = []
# while len(var1) < 6:
#     var2 = randint(1, 50)
#     if var2 in var1:
#         continue
#     var1.append(var2)
#
# print(var1)


# Napisz program, który generuje losową liczbę z zakresu [0; 10] i każe ci ją
# odgadnąć. Masz trzy próby. Inaczej „Hasta la vista, baby”, sorry.

# from random import randint
# rand = randint(1,10)
# print(rand)
# counter = 0
# anticounter = 3
#
#
# while anticounter > 0:
#     print("Masz", anticounter, "podejścia.")
#     num = int(input("Zgadnij liczbe z zakresu od 1 d0 10\n"))
#     if counter != 3:
#         if num == rand:
#             anticounter -= 1
#             counter += 1
#             print("Brawo zgadłes za", counter, "razem.")
#             break
#         else:
#             anticounter -= 1
#             counter += 1
#             if counter < 3:
#                 print("nie zgadłeś spróbuj jeszcze raz")
#             else:
#                 print("Hasta la vista Baby!")

# Zadanie
# Napisz funkcję, która policzy i zwróci wartość pola powierzchni trójkąta

# def pole_tr(a, h):
#     pole = a * h * 0.5
#     return pole
#
# print(pole_tr(5, 2))

# Napisz funkcję, która przyjmuje parametr n i zwraca n liczb parzystych od 1.

# def parametr(n):
#     lista = []
#     i = 1
#     while len(lista) < n:
#         if i % 2 == 0:
#             lista.append(i)
#         i += 1
#     return lista
#
# print(parametr(10))

# Napisz funkcję, która przyjmuje jako argument liczbę lat Twojego psa, a
# zwraca jego wiek w odniesieniu do wieku człowieka mnożąc logarytm
# naturalny wieku psa przez 16, a następnie dodając 31.

# from math import log
#
# def wiek_psa(dage):
#     return log(dage)*16 + 31
#
# print(wiek_psa(18))

# Zadanie
# Napisz funkcję is_ten(), która przyjmuje dwa argumenty, a na wyjściu
# zwraca True, jeśli którykolwiek z nich jest równy 10. To samo w
# przypadku, gdy ich suma jest równa 10.

# def is_ten(a, b):
#     if a == 10 or b == 10 or a + b == 10:
#         return True
#     else:
#         return False
#
#
# print(is_ten(10, 2))

# Zadanie
# Napisz funkcję is_vowel(), która sprawdza, czy litera podana jako
# argument jest samogłoską.


# def is_vowel(x):
#     vow = ["a", "ą", "e", "ę", "i", "o", "u"]
#     if x in vow:
#         return True
#     else:
#         return False
#
# print(is_vowel("e"))

# Zadanie
# Napisz funkcję, która dla podanego napisu zwróci informację, która litera
# ile razy w nim wystąpiła (duże i małe litery traktujemy tak samo).

# def ile_razy(word):
#     dict1 = {}
#     for i in word.lower():
#         if i not in dict1:
#             dict1[i] = 1
#         else:
#             dict1[i] += 1
#             return dict1
# print(ile_razy("Dupaa"))


# Zadanie
# Napisz funkcję, która jako argumenty będzie przyjmowała listę i parametr
# n z domyślną wartością równą 5. Funkcja ma zwrócić sumę wszystkich
# elementów listy większych od n

# def funkcja(lista, n = 5):
#     suma = 0
#     for i in lista:
#         if i > n:
#             suma += i
#     return suma
#
# print(funkcja([4, 6, 8, 9]))


# Zadanie
# Napisz funkcję, która sprawdzi, czy podana liczba jest pierwsza.

# def pierwsza(n):
#
#     for i in range(2, n):
#         if n % i != 0:
#             return True
#         else:
#             return False
#
# print(pierwsza(6))

# Albo

# def pierwsza(n):
#     czy = True
#     for i in range(2, n):
#         if n % i == 0:
#             czy = False
#     return czy
#
# print(pierwsza(6))

# Zadanie
# Napisz funkcję o zmiennej liczbie parametrów zwracającą średnią
# przekazanych liczb.

# def zlp(*liczby):
#     suma = 0
#     for i in liczby:
#         suma += i
#     return suma / len(liczby)
#
# print(zlp(6,9,12))

# albo

# def zlp(*liczby):
#     suma = 0
#     for i in range(0, len(liczby)):
#         suma += liczby[i]
#     return suma / len(liczby)
#
#
# print(zlp(6,9,12))

# Zadanie
# Napisz funkcję, która dla danego argumentu n policzy wartość n!
# wzór
# dla n = 0
# dla n*(n-1)!

# def silnia_rek(n):
#     if n == 0:
#         return 1
#     else:
#         return n * silnia_rek(n-1)
# print(silnia_rek(4))

# def silnia_iteracyjnie(n):
#     silnia = 1
#     for i in range(1, n+1):
#         silnia *= i
#     return silnia
#
# print(silnia_iteracyjnie(5))

# Stwórz klasę człowiek
#
# class Człowiek:
#     def __init__(self, imię, nazwisko, wzrost, waga):
#         self.imię = imię
#         self.nazwisko = nazwisko
#         self.wzrost = wzrost
#         self.waga = waga
#
# marek = Człowiek("Marek", "Klepczarek", 187, 82)
# janina = Człowiek("Janina", "Kowalska", 164, 72)
# grzegorz = Człowiek("Grzegorz", "Wolski", 178, 89)
#
# print(marek.imię, marek.wzrost)


# Dodaj BMI

# class Człowiek:
#     def __init__(self, imię, nazwisko, wzrost, waga):
#         self.imię = imię
#         self.nazwisko = nazwisko
#         self.wzrost = wzrost
#         self.waga = waga
#
#     def bmi(self):                  # określamy metodę
#         bmi = self.waga / self.wzrost ** 2
#         if bmi < 18.5:
#             return "niedowaga"
#         elif bmi <25:
#             return "Optimum"
#         elif bmi < 30:
#             return "nadwaga"
#         else:
#             return "otyłość"
#
#     def __str__(self):          # tu definiujemy co ma zostac zwróconę
#         return f"{self.imię} {self.nazwisko}, ma wskaźnik BMI na poziomie: {self.bmi()}"    # musi być ()
#
# marek = Człowiek("Marek", "Klepczarek", 1.87, 82)
# janina = Człowiek("Janina", "Kowalska", 1.64, 72)
# grzegorz = Człowiek("Grzegorz", "Wolski", 1.78, 89)
#
# print(marek)
# print(janina)
# print(grzegorz)

# Stwórz klasę Pracownik, która będzie dziedziczyła po klasie Osoba. Jej
# unikalne pola to: stawka godzinowa oraz liczba godzin przepracowanych
# w miesiącu. Pamiętaj, że chcemy mieć możliwość informowania
# pracownika o jego kondycji na podstawie BMI.

# class Człowiek:
#     def __init__(self, imię, nazwisko, wzrost, waga):
#         self.imię = imię
#         self.nazwisko = nazwisko
#         self.wzrost = wzrost
#         self.waga = waga
#
#     def bmi(self):                  # określamy metodę
#         bmi = self.waga / (self.wzrost/100) ** 2
#         if bmi < 18.5:
#             return "niedowaga"
#         elif bmi <25:
#             return "Optimum"
#         elif bmi < 30:
#             return "nadwaga"
#         else:
#             return "otyłość"
#
#     def __str__(self):          # tu definiujemy co ma zostac zwróconę
#         return f"{self.imię} {self.nazwisko}, ma wskaźnik BMI na poziomie: {self.bmi()}"    # musi być ()
#
# class Pracownik(Człowiek):
#     def __init__(self, imię, nazwisko, wzrost, waga, stawka, godziny):
#         super().__init__(imię, nazwisko, wzrost, waga)
#         self.stawka = stawka
#         self.godziny = godziny
#     def __str__(self):          # tu definiujemy co ma zostac zwróconę
#         return f"{self.imię} {self.nazwisko}, ma wskaźnik BMI na poziomie: {self.bmi()}, zarabia {self.stawka} złotych. Przeprcował/a {self.godziny} godzin w tym miesiącu. Zarobiła więc {self.stawka * self.godziny}"    # musi być ()
#
#
# marek = Człowiek("Marek", "Klepczarek", 187, 82)
# janina = Człowiek("Janina", "Kowalska", 164, 72)
# grzegorz = Człowiek("Grzegorz", "Wolski", 178, 89)
#
# halina = Pracownik("Halina", "Białek", 168, 62, 25, 160)
#
# print(marek)
# print(janina)
# print(grzegorz)
#
# print(halina)

# Zadanie
# Stwórz klasę Prostokąt, której atrybutami będą wysokość i szerokość
# figury. Zaimplementuj metody do mierzenia obwodu i pola prostokąta.

# class Prostokąt:
#     def __init__(self, wyskość, szerokość):
#         self.wysokość = wyskość
#         self.szerokość = szerokość
#
#     def pole(self):
#         pole = self.wysokość * self.szerokość
#         return pole
#
#     def obwod(self):
#         obwod = self.wysokość * 2 + self.szerokość * 2
#         return obwod
#
#
#
# ob1 = Prostokąt(4, 6)
#
# print(ob1.pole(), ob1.obwod())


# Zadanie 2.
# Napisz program sprawdzający, czy podane przez użytkownika hasło jest
# poprawne. Poprawne hasło definiuje się w tym przypadku w ten sposób:
# posiada rzynajmniej jedną dużą literę,
# posiada przynajmniej jedną cyfrę,
# ● Posiada przynajmniej jeden znak specjalny [@, $, #],
# ● Jest minimalnie długości 6 znaków, a maksymalnie 15.

# password = input("podja hasło\n")
#
# lower ="abcdefghijklmnoprstuwyz"
# upper = lower.upper()
# digits ="1234567890"
# specials = "!@$#"
#
# check = []
#
# for i in password:
#     if i in lower:
#         check.append("l")
#     elif i in upper:
#         check.append("u")
#     elif i in digits:
#         check.append("d")
#     elif i in specials:
#         check.append("s")
#
# print(check)
#
# if "l" in check and "u" in check and "s" in check and "d" in check and 5 < len(check) < 16:
#     print("brawo zjebie")
# else:
#     print("zjebałeś")

# Zadanie 3.
# Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr
# na formę tekstową, np.:
# 112 - > „jeden jeden dwa”

# cyfry = input("podaj liczbę\n")
# dict = {1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"pięć", 6:"sześć", 7:"siedem", 8:"osiem", 9:"dziewieć", 0:"zero"}
# var2 = ''
# for i in cyfry:
#     var2 += dict[int(i)] + " "
#
# print(var2)

# Zadanie 4.
# Stwórz listę zawierającą kilka liczb całkowitych, a następnie program,
# który wskaże indeks najmniejszego z nich, iterując po nich.

# lista = [1, 3, 5, 8,]
# naj = lista[0]
# position = 1
#
# for i in range(1, len(lista)):
#     if lista[i] > naj:
#         naj = lista[i]
#         position = i
# print(naj, position)


# Napisz funkcję, która pobiera uporządkowaną listę liczb (listę, w której elementy są uporządkowane od najmniejszej do największej) i inną liczbę.
# Funkcja decyduje, czy podana liczba znajduje się na liście, i zwraca (a następnie drukuje) odpowiednią wartość logiczną.

# def czy_liczba(lista, a):
#     lista.sort()
#     if a in lista:
#         return True, print(lista)
#     else:
#         return False, #print(lista)
#
# print(czy_liczba([2,6,9,2], 6))


# Ćwiczenie 1 (i rozwiązanie)
# Utwórz program, który prosi użytkownika o podanie imienia i nazwiska oraz wieku. Wydrukuj zaadresowaną do nich wiadomość, która mówi im, kiedy skończą 100 lat.

# name = input("podaj imie\n")
# surname = input("podaj naziwsko\n")
# age = int(input("podaj swój wiek\n"))
#
# count = 2019 - age + 100
#
# print(name, surname, "Skończysz 100 lat w roku:", count)


# Ćwiczenie 2 (i rozwiązanie)
# Poproś użytkownika o numer. W zależności od tego, czy numer jest parzysty czy nieparzysty, wydrukuj odpowiednią wiadomość dla użytkownika.
# Jeśli liczba jest wielokrotnością liczby 4, wydrukuj inną wiadomość.

# number = int(input("podaj jakś liczbę"))
#
#
# if number % 4 == 0:
#     print("twoja liczba jest wielokrotnością cyfry 4")
# elif number % 2 == 0:
#     print("twoja liczba jest parzysta")
# else:
#     print("twoja liczba jest nieparzysta")

# Take a list, say for example this one:

  # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


# c = int(input("podjal iczbę\n"))
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# for i in a:
#     if i < c:
#         b.append(i)
# print(b)


# Exercise 4 (and Solution)
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# Discussion
# The topics that you need for this exercise combine lists, conditionals, and user input. There is a new concept of creating lists.

# There is an easy way to programmatically create lists of numbers in Python.

# number = int(input("podjal iczbę\n"))
# list1 = []
# list1.append(number)
#
# for i in range(1, max(list1)):
#     list1.append(i)
# list1.sort()
#
# dzielniki = []
# for i in list1:
#     if number % i == 0:
#         dzielniki.append(i)
#
# print(dzielniki)


# Weź dwie listy, powiedz na przykład te dwie:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# i napisz program, który zwraca listę zawierającą tylko elementy wspólne dla list (bez duplikatów). Upewnij się, że twój program działa na dwóch listach o różnych rozmiarach.

# Dodatki:

# Stwórz listę z elementami wspólnymi obu list
# Wygeneruj losowo dwie listy, aby to przetestować
# Napisz to w jednym wierszu Pythona (nie martw się, jeśli nie możesz tego rozgryźć w tym momencie - wkrótce to zrobimy)

# import random
#
# a = []
# b = []
# c = []
#
# while len(a) < 10:
#     number = random.randint(1, 20)
#     if number not in a:
#         a.append(number)
#
# while len(b) < 10:
#     number = random.randint(1, 20)
#     if number not in b:
#         b.append(number)
#
# for elem in a:
#     if elem in b:
#         c.append(elem)
#
# print(c)


# Poproś użytkownika o ciąg i wydrukuj, czy ten ciąg jest palindromem, czy nie. (Palindrom to ciąg znaków, który czyta to samo do przodu i do tyłu.)

# var1 = input("Podah sentencje\n")
# var1 = var1.lower()
# var1 = var1.replace(" ", "")
# list1 = []
# for elem in var1:
#     list1.append(elem)
#
# list2 = list(reversed(list1))
#
# if list1 == list2:
#     print("twója sentencja do palindrom")
# else:
#     print("twója sentencja nie jest palindromem")



# Powiedzmy, że podaję listę zapisaną w zmiennej: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Napisz jedną linię Pythona,
# która pobiera tę listę a i tworzy nową listę, która zawiera tylko parzyste elementy tej listy.

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = []
#
# for elem in a:
#     if elem % 2 == 0:
#         b.append(elem)
#
# print(b)

# Stwórz grę Rock Paper Scissors dla dwóch graczy. (Wskazówka: Poproś o grę gracza (za pomocą danych wejściowych), porównaj je,
# wydrukuj wiadomość z gratulacjami dla zwycięzcy i zapytaj, czy gracze chcą rozpocząć nową grę)

# import sys
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
#     import random
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
#         sys.exit()

# Wygeneruj losową liczbę między 1 a 9 (w tym 1 i 9). Poproś użytkownika o odgadnięcie numeru, a następnie powiedz mu,
# czy zgadł za nisko, za wysoko lub dokładnie dokładnie. (Wskazówka: pamiętaj, aby korzystać z lekcji wprowadzania od pierwszego ćwiczenia)
#
#
# Kontynuuj grę, dopóki użytkownik nie wpisze „exit”
# Śledź, ile domysłów podjął użytkownik, a kiedy gra się skończy, wydrukuj to.

# import sys
# import random
#
# count = 0
# newgame = 0
#
# while newgame == 0:
#     rnum = random.randint(1, 9)
#     print(rnum)
#     while newgame == 0:
#         unum = int(input("podja liczbę od 1 do 9\n"))
#         if unum == rnum:
#             count += 1
#             print("brawo!, zgadłeś za", count, "razem.")
#             quitgame = input("Czy chcesz zagrac jeszcze raz?\n Tak - t, Nie - n\n")
#             if quitgame == "n":
#                 print("dziękujemy za wspólną grę.")
#                 sys.exit()
#             elif quitgame != "n":
#                 newgame = 0
#                 count = 0
#                 rnum = random.randint(1, 9)
#         elif unum > rnum:
#             count += 1
#             print("Twoja liczba jest za duża")
#         elif unum < rnum:
#             count += 1
#             print("twoja cyfra jest za mała")


# W tym tygodniu ćwiczenie powróci do starego ćwiczenia (patrz Ćwiczenie 5), z tym wyjątkiem, że wymaga rozwiązania w inny sposób.
# i napisz program, który zwraca listę zawierającą tylko elementy wspólne dla list (bez duplikatów). Upewnij się,
# że twój program działa na dwóch listach o różnych rozmiarach. Napisz to w jednym wierszu Pythona,
# używając co najmniej jednego zrozumienia listy. (Wskazówka: Zapamiętaj listę ze zrozumieniem z ćwiczenia 7).

# import random
#
# a = []
# b = []
# c = set()
#
# for i in range (0, 10):
#     a.append(random.randint(1, 50))
#
# for i in range (0, 12):
#     b.append(random.randint(1, 50))
#
# for elem in a:
#     if elem  in b:
#         c.add(elem)
# c = list(c)
# print(c)

# Poproś użytkownika o numer i ustal, czy jest on liczbą pierwszą, czy nie. (Dla tych, którzy zapomnieli, liczba pierwsza jest liczbą,
# która nie ma dzielników). Możesz (i powinieneś!) Skorzystać z odpowiedzi do ćwiczenia 4, aby ci pomóc. Skorzystaj z okazji,
# aby poćwiczyć korzystanie z funkcji opisanych poniżej.

# DO ZROBIENIA

# number = int(input("podaj jakąś liczbę\n"))
# for i in range(1, number-1):
#     if number == 0 or number == 1:
#         print("jedynka i zero są nieokreślone")
#     elif number % i == 0:
#         print("nie jest pierwszą")
#     else:
#         print("jest pierwszą")



# Napisz program, który pobiera listę liczb (na przykład a = [5, 10, 15, 20, 25]) i tworzy nową listę
# tylko z pierwszego i ostatniego elementu danej listy. Aby ćwiczyć, napisz ten kod w funkcji.

import random
# a = []
# b = []
# for i in range(1, 6):
#     a.append(random.randint(1, 50))
#
# print(a)
# b.append(a[0])
# b.append(a[-1])
# print(b)

# i to samo z funkcją

# import random
# a = []
# b = []
# for i in range(1, 6):
#     a.append(random.randint(1, 50))
#
# def list_ends(a_list):
#     return [a_list[0], a_list[len(a_list)-1]]
#
# print(list_ends(a))

# apisz program, który zapyta użytkownika, ile liczb Fibonnaci ma wygenerować, a następnie je wygeneruje. Skorzystaj z okazji,
# aby pomyśleć o tym, jak korzystać z funkcji. Pamiętaj, aby poprosić użytkownika o podanie liczby liczb w sekwencji,
# która ma zostać wygenerowana. (Wskazówka: Sekwencja Fibonnaci jest sekwencją liczb, w której następny numer w sekwencji
# jest sumą dwóch poprzednich liczb w sekwencji. Sekwencja wygląda następująco: 1, 1, 2, 3, 5, 8, 13,…)

var1 = int(input("ile liczb fibonacciego mam wygenerować?\n"))

for i in range