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
