# oryginał

# stan_p = float(input("podaj stan poczatkwy konta\n"))
# procent = float(input("podaj oprocentowanie\n"))
# okres = int(input("ile lat będziez trzymał środki\n"))
# pytanie = input("Co jaki okres występuje kapitalizacja?\n Dziennie (d), miesiąc (m), rok (r)\n")
# pytanie = pytanie.lower()
#
# miesiąc = okres*12
# procent_m = procent/12
#
# dzień = okres*365
# procent_d = procent/365
#
# if pytanie == "m":
#     wynik = stan_p * ((1 + (procent_m / 100)) ** miesiąc)
#     print("Twój kapitał po wskaznym okresie, wyniesie:",wynik)
#
# elif pytanie == "r":
#     wynik = stan_p * ((1 + (procent / 100)) ** okres)
#     print("Twój kapitał po wskaznym okresie, wyniesie:",wynik)
#
# elif pytanie == "d":
#     wynik = stan_p * ((1 + (procent_d / 100)) ** dzień)
#     print("Twój kapitał po wskaznym okresie, wyniesie:",wynik)

#
# stan_p = float(input("podaj stan poczatkwy konta\n"))
# procent = float(input("podaj oprocentowanie\n"))
# okres = float(input("ile lat będziez trzymał środki\n"))
# pytanie = input("Co jaki okres występuje kapitalizacja?\n Dziennie (d), miesiąc (m), rok (r)\n")
# pytanie = pytanie.lower()
# while not pytanie in ["m", "d", "r"]:
#     print("Wybierz zdefiniowaną odpowedź: d - dzień, m - miesiąc, r - rok")
#     pytanie = input("Co jaki okres występuje kapitalizacja?\n Dziennie (d), miesiąc (m), rok (r)\n")
#
#
# miesiąc = okres*12
# procent_m = procent/12
#
# dzień = okres*365
# procent_d = procent/365
#
# if pytanie == "m":
#     wynik = stan_p * ((1 + (procent_m / 100)) ** miesiąc)
#     print("Twój kapitał po wskaznym okresie, wyniesie:",wynik)
#
# elif pytanie == "r":
#     wynik = stan_p * ((1 + (procent / 100)) ** okres)
#     print("Twój kapitał po wskaznym okresie, wyniesie:",wynik)
#
# elif pytanie == "d":
#     wynik = stan_p * ((1 + (procent_d / 100)) ** dzień)
#     print("Twój kapitał po wskaznym okresie, wyniesie:",wynik)






# Brutto - netto
# import sys
#
# podaj = ''
# while podaj != "b" or podaj != "n" or podaj != "e":
#     podaj = input("Co chcesz obliczyć? Brutto (b) czy netto (n)?\nZakończ program (e)\n ")
#     if podaj == "b":
#         kwota = float(input("Podaj wysokść wynagrrodzenia netto\n"))
#         wynagrodzenie = kwota * 140.26 / 100
#         print("twoja kwota brutto to:", wynagrodzenie)
#     elif podaj == "n":
#         kwota = float(input("Podaj wysokść wynagrrodzenia brutto\n"))
#         wynagrodzenie = kwota * 71.3 / 100
#         print("twoja kwota netto to:", wynagrodzenie)
#     elif podaj == "e":
#         print("Dziękujemy za skorzystanie z naszego systemu bankowości\n")
#         sys.exit(0)

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
#     ask1 = input("czy chcesz się teraz zalogowaćC? \n tak(t), nie 👎?\n")
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
#             podaj = input("Co chcesz obliczyć? Brutto (b) czy netto 👎?\nPowrót do menu (r)\nZakończ program (e)\n ")
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