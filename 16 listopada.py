# var = 'python is cool'
# print(var[2])
# print(var[5:12:3])
# print(var[2:8])
# print(var[5:])
# print(var[5:12:3])
# print(var[::2])
# print(var[-6:])

# print("hello world")

zmienna1 = 10
zmienna2 = "b"
zmienna3 = 3.7

# print(zmienna1)
# print(zmienna2)
# print(zmienna3)

# print(type(zmienna1))
# print(type(zmienna2))
# print(type(zmienna3))

zmienna1 = 42
zmienna2 = "platoon"

# print(zmienna1)
# print(zmienna2)

zmienna4 = (zmienna1 + zmienna3)
# print(zmienna4)

zmienna4 = zmienna4 + 10

# print(zmienna4)

# zmienna5 = 'Maciek'
# print(zmienna5)

pi = 3.14
r = 6
# print(pi * r * r)

# name = input("whats your name")
# print(name)

# year = input("whats your birth year\n")
# age = 2019 - int(year)
# print(age)


# a = float(input("Jaka jest długość podstaywy trojkąta?\n"))
# h = float(input("Jaka jest wysokość trojkąta?\n"))
# print(0.5 * a * h)

# pi = 3.14
# r = float(input("jaka jest długośc promienia koła?\n"))
# print(pi * r * r)

# name = "john"
# year = 2018
# age = 21

# print(name, year, age)
# print(name, year, age, sep="_")
# print(name, year, age, end=", ")
# print(name, year, age, sep="_", end=",")


# imie = input("Jakie Jest twoje imie?\n")
# nazwisko = input("Jakie jest twoje naziwsko?\n")
# print(imie[0],nazwisko[0], sep="")

# imie = input("Jakie Jest twoje imie?\n")
# nazwisko = input("Jakie jest twoje naziwsko?\n")
# wiek = input("Ile masz lat\n")
# print(imie, nazwisko, wiek)

# name = "Rafał"
# party_type = "pogrzeb"
# time = "15:00"
# text1 = "Witaj %s, zapraszamy na %s, na godzinę %s, do zoabczenia %s" % (name, party_type, time, name)
# text2 = "Witaj {}. zapraszam na {} na godzinie {}, do zobaczenia {}" .format(name, party_type, time, name)
# text3 = 'Witaj {0}, zapraszamy na {1} na godzinę {2}, do zobaczenia {0}' .format(name, party_type, time, name)
# text4 = f"Witaj {name}, zapraszamy na {party_type} na godzinę {time}, do zobaczenia {name}"
#
# print(text1)
# print(text2)
# print(text3)
# print(text4)

# imie = "Marian"
# nazwisko = "Kowalski"
# wiek = "37"
# pensja = "2300"
# stanowisko = "Dozorca"
#
# text1 = f"Pan {imie} {nazwisko} (wiek {wiek} lat), pracuje na stanoiwsku: {stanowisko} (pensja: {pensja} brutto)."
# print(text1)

# print(2+3)
# print(8-3)
# print(2*5)
# print(6/3)
# print(9%2)
# print(5//2)
# print(3**2)


# print((((10 + 20)/2)-5)*3)

# print(2==2)
# print(10==3)
# print(10>3)
# print(8!=5)
# print(7<=7)

# print(2==2 or 10==3)
# print(10>3 and 8!=5)
# print(not 7 <= 7)

# print("głowa" < "noga")
# print("zenon" < "adrian")
# to sprawdza alfabetycznośc

# print("ą"< "b")

# zmienna5 = "Obiad\n"
# print(zmienna5*3)
#
# zmienna5 = "Obiad"
# print((zmienna5+"\n")*3)
# print(f"zmienna5\n"*3)
#

# imie = "Maciej"
# nazwisko = "Pińczewski"
# print(imie + " " + nazwisko)
#
# print("Hello\nWorld")

# print("Hello\n")
# print("World")

# zmienna6 = input("Wpidz dowolne słowo\n")
#
# print(zmienna6.upper())
#

# number=float(input("podaj liczbę\n"))
# if number > 0:
#     print("podana liczba jest dodatnia")
# else:
#     print("Podana liczba jest ujemna")
#

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
#

# number=int(input("wpisz liczbę\n"))
# if number >= 0 and number <= 9:
#     print("To cyfra mój drogi")
# else:
#     print("To jest liczba większa od 9 lub mniejsza od 0")

# number=int(input("wpisz wynik\n"))
# if number >= 0 and number <= 20:
#     print("Masz Pałę")
# elif number > 20 and number <= 40:
#     print("Przeczołgałeś się")
# elif number > 40 and number <= 60:
#     print("Masz trójkę")
# elif number > 60 and number <= 80:
#     print("Czwórka, gratki")
# elif number > 80 and number <= 100:
#     print("Lubisz błyszczeć co?")
# elif number > 100:
#     print("Oszukujesz")

var = input("Czy lubisz podróżować?\n")
if var == "nie":
    print("Na pewno masz inne ciekawe hobby")
elif var == "tak":
    var2 = input("Czy czesto podróżujesz?\n")
    if var2 == "tak":
        print("Ekstra!")
    elif var2 == "nie":
        print("Podróżuj więcej, polecam!")


