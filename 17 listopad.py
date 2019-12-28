# zmienna = input("Dobrze się czujesz?\n")
# if zmienna == "tak":
#     print("to zajebiście")
# elif zmienna == "nie":
#     print("to słabo")


# zmienna2 = float(input("jaka jest długośc boku kwadratu?\n"))
# print(zmienna2 * zmienna2)


# waga = float(input("Podaj masę w Kilogramach\n"))
# wzrost = float(input("Podaj wzrost w metrach, do dwóch meiejscach po przecinku\n"))
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


# waga = float(input("Podaj masę w Kilogramach\n"))
# wzrost = float(input("Podaj wzrost w metrach, do dwóch meiejscach po przecinku\n"))
# bmi = waga / (wzrost*wzrost)
#
# if bmi < 18.5:
#     print("masz niedowagę")
# elif bmi < 25:
#     print("Ważysz prawdiłowo")
# elif bmi < 30:
#     print("Masz nadwagę")
# else:
#     print("Jesteś otyły")


# my_list - [1,"kot", True]

# list_1 = [1, 2, 3, 4, 5, 6, 7]
# print(list_1[0])
# del list_1[3]
# print(list_1)
#
# print(len(list_1))

# warzywa = ["jabłko", "gruszka", "banan", "kiwi", "ser", "kurczak", "ziemniaki"]
# print(warzywa [4:])
# print(warzywa [0])
# print(warzywa [:4:])


# liczby = [1, 2, 3 ,4 ,5]
# liczby.append(6)
# liczby.append(7)
# del(liczby [2])
# print(liczby)


# lista2 = [23, 66, 88, 28, 67]
# lista2.extend([85, 166])
# lista2 = lista2 + [87, 33]
# print(lista2)
# print(list(sorted(lista2)))
# list.sort(lista2)
# print(lista2)
# lista2.sort(reverse=True)
# print(lista2)
#

# a = [1, 2 ,3]
# b = [1, 2, 4]
# c = [1, 2, 0]
# d = [1, 'a', 0]
#
# print(a == b)
# print()

# print("asd" in [1, 2, "asd", 3, True, 4.5])
# print(-52 in [1, 2, "asd", 3, True, 4.5])
# print(-52 not in [1, 2, 'asd', 3, True, 4.5])

# lista = ["groszek", "cyborg", "python", "stal", "puch"]
# pytanie =(input("Podaj słowo\n"))
#
# if pytanie in lista:
#     print("brawo zgadłeś")
# else:
#     print("przykro mi")


# lst = [45, 55, 7, 56, 32]
# print(7 in lst)
# print(lst.index(7))
# print(lst[lst.index(7)])


# krotka = (1, 2, 3)
# krotka1 = (5, 1, "mój napis")
# krotka = krotka + (5, )
#
# print(krotka)



# set = {1, 4, 5, 5, 3, 1}
# print(set)

# kalendarz = {"styczeń": 31, "luty": 28, "marzec": 31, "kwiecień": 30, "maj": 31, "czerwiec": 30,
#              "lipiec": 31, "sierpień": 31, "wrzesień": 30, "pażdziernik": 31, "listopad": 30, "grudzień": 31}
# miesiąc = input("wpisz nazwe miesiąca\n")
# print(kalendarz.get(miesiąc))


# słownik = {
#     "chleb": 2.5,
#     "bułka": 0.3,
#     "sok": 1,
#     34: "klucz",
#     (1, 2, 3): 999
# }
#
# print(słownik)
# print(słownik.get("chleb"))
# print(słownik.get(34))
# print(słownik.get((1, 2, 3)))
# del słownik["sok"]
# print(słownik)
# print(list(słownik.keys()))
# print("chleb" in słownik)
# print("głowa" in słownik)

# słownik.update({"ciastko": 45})
# print(słownik)


# zbiór = {1, 66, 72, 88, 112, 33, 33, 112}
# print(zbiór)
#
# zbiór.add(555)
# print(zbiór)
# zbiór.remove(66)
# print(zbiór)
# zbiór.update({51, 98, 99})
# print(zbiór)
#
# zbiór2 = {2, 98, 99}
#
# print(zbiór.intersection(zbiór2))
# print(zbiór | zbiór2)
# print(zbiór - zbiór2)
# print(zbiór2 - zbiór)
# print(zbiór.difference(zbiór2))
# print(sum(zbiór))
# print(len(zbiór))


# a = [3, 5, 1, 34, 34, 66]
# print(a)
# print(set(a))
# print(list(set(a)))


# a_list = [1, 2, 3, 4, 5, 6, 7]
# new_list = []
# for element in a_list:
#     new_list.append(element * 10)
# print(new_list)


# lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
# nowa_lista = []
# for element in lst1:
#     nowa_lista.append(element * 10)
# print(nowa_lista)


# number = int(input("Podaj liczbę\n"))  #pętla WHILE
# while number >= 0:
#     print(number)
#     number -= 1


# new_list = []
# for l in range(3, 10):
#     new_list.append(l ** 2)
# print(new_list)
#
#
nowa_lista = []
liczba = 3
while liczba < 10:
    nowa_lista.append(liczba ** 2)
    liczba += 1
print(nowa_lista)


# lista = []
# liczba = 3
# while True:
#     lista.append(liczba ** 2)
#     liczba +=1
#     if liczba == 10:
#         break
# print(lista)


# new_list = []
# for l in range(1, 99):
#     if l % 2 == 0:
#         new_list.append(l)
#
# print(new_list)
#
# new_list2 = []
# for el in range(2, 99, 2):
#     new_list2.append(el)
# print(new_list2)
#
# new_list3 = []
# number = 1
# while number < 99:
#     if number % 2 == 0:
#         new_list3.append(number)
#     number +=1
# print(new_list3)

#
# lista = [2, 8, 55, 44, 95,]
# cyfra = 0
# for el in lista:
#     cyfra += el
# print(cyfra)

#
# lst = [2, 8, 55, 44, 95]
# suma = 0
#
# for elem in lst:
#     suma += elem
# print(suma)
#
# suma = 0
# liczba = 0
# while liczba < len(lst):
#     suma += lst[liczba]
#     liczba += 1
# print(suma)


# lista = [2, 8, 55, 44, 95,]
# cyfra = 0
# for el in lista:
#     cyfra += el
#
# print(cyfra/len(lista))

# lst = [2, 8, 55, 44, 87, 9, 64]           #znajdź indeks elementu największego na liśćie
# najw = lst[0]
# for l in range(1, len(lst)):
#     if lst[l] > najw:
#         najw = lst[l]
#         najw_id = l
# print(najw, najw_id)


# lst = []                         #wszystkie liczy od 1 do 20 na wzrór liczba kwadrat+1
# for l in range(0,21):
#     lst.append(l ** 2 +1)
# print(lst)





