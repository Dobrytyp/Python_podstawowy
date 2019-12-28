# Zadanie 1
#
# var1 = input("czesć jak Masz na imie?\n")
# var2 = int(input("ile masz lat?\n"))
# var3 = int(input("Ile kilogramów ważysz?\n"))
#
# var4 = var2*365*24*3600
# var5 = var3/6.05
# var6 = var3*27.93
#
# print("Jeśli poeta E.E. cummings wysłałby do ciebie wiadoość e-mail, zswróciłby się do ciebie", var1.lower(),"\n"
# "Ale jeśli byłby wściekły, napisałby:", var1.upper(),"\n", "\n"
# "Jeżeli małe dziecko spróbowałoby zwrócić twoją uwagę,\n",
# "Twoje imie przybrałoby formę:\n",
# var1.capitalize(),var1.capitalize(),var1.capitalize(),"!" "\n", "\n"
# "Żyjesz już ponad", var4, "sekund.\n","\n"
# "Czy wiesz, że na księżycu Twoja waga wynosiłaby", var5, "kg?\n",
# "Na Słońcu twoja waga to", var6, "kg (ale niestety niedługo).")


# print("ucze się\n"
#       "dzielic tekst\n"
#       "na wiersze\n")


# print("tak też")
# print("działa, ale po co?...")


# print("siema ludzie pa...\t", "...ństwo izrael dokonuje eksterminacji palestyńczyków") # \t oddziela tekst tabulatorem


# print("Możesz dokonać kontanacji dwóch łańcuchów" + "za pomocą operatora '+'\n","\n")


# print("ciężarna hipopotamica, ważąca 1500kg rodzi 45 kg młode,\nale potem zjada 25 kg paszy. Ile wynosi jej nowa waga?\n")
# input("Dowiedz się wciskając Enter.") # sam input to oczekiwanie na enter
# var1 = 1500-45+25
# print("jej nowa waga to:",var1)


# print(" znak / to zwykłe dzielenie")
# print("znak // to dzielenie całkowite")

# # Zmiana rozmiau tekstu
# var1 = "Myślę, że istnieje światowy ryek dla może pięciu komputerów"
# print(var1)
# print(var1.lower())
# print(var1.upper())
# print(var1.title())



# #Program napiwek
# var1 = int(input("podaj kwotę, którą zapłaciłeś za posiłek\n"))
# print("Powinieneś zaroponować", var1/100*15, "napiwku, lub", var1/100*20, "jeżeli byłeś naprawde zadowolony.")



# # Pętla While      POKAŻ ELIZIE
# response = ""
# while response != "dlatego": #jeżeli odpowiedż jest inna niż "dlatego", pętla powraca do zmiennej response
#     response = input("dlaczego?\n")
# print("Aha już wiem.") # Jeśli odpowiedż to "dlatego" pętla się przerywa

#
# # Przykład na while
# print("witamy w naszej resturacji\n"
# "Niestety mamy prawie komplet gości")
# var1 = int(input("Ie pieniędzy wsuniesz do kieszeni kelnera?\n"))
# while var1 <= 0:
#     print("oczekiwanie na stolik może torche potrwać")
#     var1 = int(input("Ie pieniędzy wsuniesz do kieszeni kelnera?\n"))
#     print("Zapraszma do stolika")


# Wybredny licznik co pomija 5, demonstruje break i continue
# count = 0 # zaczynamy od 0
# while True: # kiedy prawdziwe
#     count += 1 # podajemy liczbę o 1 większą
#     if count > 10: # jeżeli wartość bedzie większa od 10
#         break # przerwij pętle
#     if count == 5: # Jeśli wartość w pętli wyniesie 5
#         continue # kontynuuj (bez niej)
#     print(count)


# # mój program liczy od 1 do 10 ale bez 4 i mnoży razy 2
# var1 = 0
# while True:
#     var1 += 1
#     if var1 > 10:
#         break
#     if var1 == 4:
#         continue
#     var2 = var1*2
#     print(var2)



# # Eksluzywna sieć demonstrouje opratory logiczne i warunki złożone
# print("\tEkskluzywna Sieć komputerowa")
# print("\t  Tylko dla członków!\n")

# user_name = "" # Zostawiamy puste żeby w następnym kroku pusta wartośc miała wartość "False" (while not)
# while not user_name: # to jest po to żeby ktoś nie zostawił pustego miejsca
#     user_name = input("Użytkownik: \n")
#     user_name = user_name.lower() #zmniejszma sobie litery na wypadek capslocka czy coś
#
# passwword = "" # tak samo puste, żeby w następnym kroku wymuszła jakąś wartość
# while not passwword: # ponownie po to żeby wpisac jakieś hasło
#     passwword = input("Hasło: \n")
#
# if user_name == "maciej pińczewski" and passwword == "Maciek123": # and dodaje warunek że i użytkownik i hasło musza być ok
#     print("Witaj Maciek\n")
# elif user_name == "szymon pisarski" and passwword == "Szymon123":
#     print("witaj Szymon")
# elif user_name == "tomasz muchalski" and passwword == "Tomasz123":
#     print("Witaj Tomasz")
# elif user_name == "gość" or passwword == "gość": # dodajemy or żeby zarówno haśo jak i login logowały jako gościa
#     print("Witaj Gościu")
# else:
#     print("Nieudana próba logowania")



# #Program jaka to liczba
# print("Mam na myśli pewną liczbę z zakresu od 1 do 100.\n"
# "Spróbuj ją odgadnąć, w jak najmniejszej liczbie prób.")
# import random
# my_number = random.randint(1, 100)
# print("Jaka to liczba?")
# var1 = int(input()) #tu użytkownik podaje sowją liczbę
# tries = 1 # zmienna będzie liczyć liczbę prób
#
# while var1 != my_number: # pętla zaczyna się jeśli nie zgadłeś
#     if var1 > my_number: # jeżeli liczba jest za duża
#        print("ta liczba jest za duża")
#     else:                # jażeli jest za mała
#         print("ta liczba jest za mała")
#     var1 = int(input("Taliczba to: \n"))
#     tries += 1           # dodaje próbę do licznika
# print(" Brawo zgadłeś za", tries, "razem")



# Program ciastko z wróżbą ma wyświetlić losowo jedną z 5 przepowiedni
# import random
# my_number = random.randint(1, 5) # zakres liczb losowych
# if my_number == 1:
#     print("Złapie cię kanar")
# elif my_number == 2:
#     print("Odpadnie ci kutas")
# elif my_number == 3:
#     print("Bedzie cię bolał brzuch")
# elif my_number == 4:
#     print("będziesz miał katar")
# elif my_number == 5:
#     print("Zesrasz się w pracy")


# # program który 100 razu rzuca monetą i podaje ile było reszet i orłów
# import random
# count1 = 0
# count2 = 0
# my_number = random.randint(1, 2)
# print(my_number) # do usunięcia
#
#
#
#
# if my_number == 1:
#     count1 += 1
# elif my_number == 2:
#     count2 += 1
#
#
#     print(count1)
#     print(count2)
#
#
# new_list = []
# for l in range(3, 10):
#     new_list.append(l ** 2)
# print(new_list)