# male = "abcdefghijklmnoprstuwyz"
# wielkie = male.upper()
# cyfry = "1234567890"
# specjalne = "!@#$%"
# checksum = []
#
# war = True
#
# while war:
#     password = input("podaj hasło\n")
#     for i in password:
#         if i in male:
#             checksum += "m"
#         elif i in wielkie:
#             checksum += "w"
#         elif i in cyfry:
#             checksum += "c"
#         elif i in specjalne:
#             checksum += "s"
#
#     if "m" in checksum and "w" in checksum and "c" in checksum and "s" in checksum and 5 < len(password) < 12:
#         war = False
#         print("Brawo")
#     else:
#         print("zjebałeś")

# Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr
# na formę tekstową, np.:
# 112 - > „jeden jeden dwa”

# liczba = input("podaj ciąg cyfr\n")
# cyfry = {1:"Jeden" , 2: "Dwa", 3: "Trzy", 4: "Cztery", 5 : "Pięć", 6: "sześć", 7: "siedem", 8: "osiem", 9: "dziwieć", 0: "zero" }
# wynik = ''
#
# for i in liczba:
#     wynik += cyfry[int(i)] + " "
#
#
# print(wynik)


# Stwórz listę zawierającą kilka liczb całkowitych, a następnie program,
# który wskaże indeks najmniejszego z nich, iterując po nich.

# list1 = [4, 7, 3, 9, 2, 15, 8]
# minimal = list1[0]
# counter = 0
# pozycja = 0
# for i in range(1, len(list1)):
#     if list1[i] < minimal:
#         minimal = list1[i]
#         counter = i
#
# print(counter)
# print(minimal)

# Napisz program, który policzy iloczyn elementów wybranej przez siebie
# listy, iterując po nich.

# lista = [1, 2, 3, 4, 5]
# wynik = 1
# for i in lista:
#     wynik = wynik * i
#
# print(wynik)

# Napisz program, który pobierze 5 słów od użytkownika, a następnie
# wypisze najdłuższe z nich.


# Pobierz od użytkownika wartość n, a następnie stwórz słownik, którego
# elementy dla i < n będą postaci: (i, i2)

# Napisz program, w którym zdefiniujesz dwie listy, a następnie sprawdzisz,
# czy pierwsza zawiera się w drugiej.

# Napisz program, który poprosi użytkownika o podanie słowa i napisze,
# czy jest ono izogramem (słowo, w którym żadna litera się nie powtórzyła,
# np. „skrzynia”)

# Napisz funkcję, która sprawdzi, czy podany jako argument napis jest
# palindromem (tj. czytany od przodu i wspak jest dokładnie taki sam, np.
# „kajak”, „Madam”, „nurses run”).

# word = input("Give a sentence\n")
# word = word.replace(" ", "")
# word = word.lower()
# reverse = word[::-1]
# if word == reverse:
#     print("sentence is Palindrom")
# else:
#     print("this is not a palindrom")

# Stwórz klasę reprezentującą koło o danym promieniu z metodami do obliczania jego pola powierzchni i obwodu.
# Odpowiednią stałą zaimportuj z zewnętrznego modułu.



# Zadanie 8.
# Napisz funkcję, która zwróci 5 najczęstszych słów z dzieła Mickiewicza
# https://pastebin.com/raw/aAHeW5Pt
# Ćwiczymy odczytywanie z pliku

f = open("mick.txt", "r")
print(f.read())