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

#Zadanie #oblicz pole powierzchni koła = pi* R kwadrat
# r = float(input("Podaj długość promienia koła\n"))
# pi = 3.14
# print(r*pi*pi)

#Zadanie wzór na pole trójkąta 1/2 a * h
# podstawa = float(input("Podaj długość podstawy trójkąta\n"))
# wysokość = float(input("Podaj wyskość trójkąta\n"))
# print(podstawa/2*wysokość)

#Zadanie wzór na pole trapezu (a+b)h/2
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


#dodaj 10 i 20 wynik podziel przez 2. Od wyniku odejmij 5, potem wynik pomnóz przez 5
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


#znaki specjalne
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
# napis = "phyton"
# # print(napis.upper()) # uppnapis = input("Podaj słowo\n")er() zamienia na wielkie litery
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


#drugi sposób
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


#for
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


#zadanie 0
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


#Slicing - Szatkowanie
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


#zadanie Utwórz listę siedmiu artykułów spoż. Wyświetl trzy pierwsze i trzy ostatnie

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

dict_1 = {"Eliza":30, "Maciej":34, "Tomasz":23, "Iwona":58}
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

#n.p.
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
# for i in range(5):
#     print(len(my_list[i])) # i działa jak pierwszy obrót pętli czyli podstawia najpier var1
#     if len(my_list[i]) > max_count: # to jest ta zamienna o wartości 0
#         the_word = "" # przy kolejnej pętli jesli słowo bylo krótsze ot zamieniamy je w puste
#         the_word += my_list[i] + " " # jeżeli to słowo które jest sprawdzane jest większe od 0 to do pustej zmiennej wkleja to słowo
#         max_count = len(my_list[i]) # podaje długośc najdłuższego słowa przy kolejnych pętlach
#
# print(the_word)

#################################

# Zadanie
# Napisz program, który wyświetli listę cyfr od 0 do 10 z pominięciem tych
# podzielnych przez 3.

# list1 = []
# list2 = []
# for i in range(1, 11):
#     if i % 3 != 0:
#         list1.append(i)
# print(list1)


# z while

# list1 = []
# idx = -1
# while idx < 10:
#     idx += 1
#     if idx % 3 == 0:
#         continue
#     list1.append(idx)
# print(list1)

# od 20 do 40 podzielne przez 2


# napisz program, który będzie robić kwadrat jakiejś liczby aż dojdzie do 1000
#
# liczba = 3
# potęga = []
# lista = []
# while True:
#     lista.append(liczba ** 2)
#     lista = liczba ** 2
#     for i in lista:
#
#         break
# print(lista)




# lista = []
# liczba = 3
# while True:
#     lista.append(liczba ** 2)
#     liczba +=1
#     if liczba == 10:
#         break
# print(lista)














# lista = []
# idx = -1
# while idx <10:
#     idx += 1
#     if idx % 3 == 0:
#         continue
#     lista.append(idx)
# print(lista)





#albo dla 20

# var1 = []
# for i in range(1,21):
#     if i % 3 != 0:
#         var1.append(i)
# print(var1)

# liczby od  20 do 40 których suma nie przekorczy 50

# list1 = []
# for i in range(20, 41):
#     if i + i < 50:
#         list1.append(i)
# print(list1)


# Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr
# na formę tekstową, np.:
# 112 - > „jeden jeden dwa”

# dict1 = {1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"pięć", 6:"sześć", 7:"siedem", 8:"osiem", 9:"dziwieć", 0:"zero"}
# list1 = int(input("wpisz jakąś iczbę"))
# var1 = " "
# for i in list1: # rozbijamy listę na elementy
#     var1 += dict1(int[i])
# print = var1

# zakres liczb 0 do 200 w których reszta z dzielenie przez 3 daje 2
#
# liczby = []
# liczby_poprawnie =[]
# for i in range(3, 200):
#     if i % 3 == 2:
#         liczby_poprawnie.append(i)
# print(liczby_poprawnie)

from 07.12.  import wieksze5
print(wieksze5([2, 5, 7, 9]))







