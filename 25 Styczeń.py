"ZADANIA"

# Zadanie 1

# Stwórz dekorator o nazwie debug, który podczas wywoływania funkcji
# będzie wyświetlał informacje o jej nazwie, przekazanych parametrach
# oraz zwracanym wyniku.

# def debug(func):
#     def wrapper(*args, **kwargs):
#         resault = func(*args, **kwargs)
#         argumenty_pozycyjne = ", ".join(str(arg) for arg in args)
#         argumenty_nazwane = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
#         print(f"Funkcja {func.__name__} ({argumenty_pozycyjne}, {argumenty_nazwane}) zwróciła {resault}")
#         return resault
#     return wrapper
#
# @debug
# def func(a, b, c):
#     return a + b * c
#
# print(func(3, b=2, c=4))


# Zadanie 2  NIe działa

# Stwórz dekorator o nazwie multiply, który
# przyjmuje argument n i zwiększa n-krotnie
# rezultat wykonania udekorowanej funkcji

# def mulitply(n):
#    def function(func):
#        def wrapper(*args, **kwargs):
#            return n *func(*args,**kwargs)
#        return wrapper
#     return function
#        )
#
#
# @mulitply(3)
# def func1():
#     return "ala ma kota\n"


# Zadanie 3
# Stwórz iterator i generator, które będą zwracały n liczb niepodzielnych
# przez m.
# np. dla n=10, m=3: [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]

# class IndivisableIterator:
#     def __init__(self, n, m):
#         self.n = n
#         self.m = m
#         self.i = 0
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.counter == self.n:
#             raise StopIteration
#         if self.i % self.m != 0:
#             self.counter += 1
#             return self.i
#         return self.__next__()
#
# for i in IndivisableIterator(10,3):
#     print(i, end=", ")
#
# # Generator
#
# def indevisible_generator(n, m):
#     number = 0
#     count = 0
#     while count < n:
#         if number %  m != 0:
#             yield number
#             count +=1
#         number += 1
#
# for i in indevisible_generator(10,3):
#     print(i, end=", ")

# Zadanie 4

# Pobierz jsona ze strony: https://jsonplaceholder.typicode.com/todos
# Następnie załaduj go w skrypcie pythonowym, odfiltruj zadania
# nieukończone (każdy rekord ma odpowiednią flagę), a następnie zapisz w
# pliku CSV, pamiętając, by w pierwszym wierszu umieścić nazwy kolumn.
# Podziel kod na sensowne funkcje.

# import json
# import csv
# from collections import defaultdict
#
# def load_data(filename):
#     with open(filename) as in_file:
#         return json.load(in_file)

# def filter_json(data):  # drugi czytelny sposób
#     completed_tasks = []
#     for item in data:
#         if item["completed"]:
#             completed_tasks.append(item)
#     return completed_tasks

# def filter_json(data):
#     return [task for task in data if task ['completed']]
#
# def save_to_csv(data, output_filename):
#     header = [key for key in data[0].keys()]
#     with open(output_filename, 'w') as out_file:
#         writer = csv.writer(out_file, delimiter=",")
#         writer.writerow(header)
#         for row in data:
#             writer.writerow(row.values())
#
# def group_by_users(data):
#
#     users = {}
#     for task in data:
#         name = "user_"+ str(task.pop("userId"))
#         users[name].append(task)
#     return users
#
# def save_to_json(data, output_filename):
#     with open(output_filename, "w") as out_file:
#         json.dump(data, out_file, indent=2)
#
# data = load_data("C:\\Users\\eliza\\Desktop\\Python\\pycharm projects\\GIT\\json.py")
# filtered_data = filter_json(data)
# save_to_csv(filtered_data, "to-> <-do.csv")


# Zadanie 6
# Korzystając z wyrażenia regularnego napisz funkcję, która sprawdzi, czy
# liczba jest podzielna przez 4

# import re       Nie działa
#
# def is_divisible_by_four(number_str):
#     pattern = r"^-?([048|\d*([023468][048][13579][26]))$"
#     return bool(re.search(pattern, number_str))
#
# test = ["8", "42", "757465", "2036", "1100", "-12"]
# for number in test:
#         print(number, is_divisible_by_four(number))


# Zadanie 7
# Typowym błędem przy szybkim wpisywaniu tekstu jest pisanie drugiej litery
# wyrazu dużą literą, np. SZczecin (zamiast Szczecin) czy POlska (zamiast
# Polska). Napisz program, wykorzystujący funkcję sub i wyrażenia regularne,
# który poprawi wszystkie takie błędy w tekście wprowadzonym przez
# użytkownika. Wyrazy dłuższe niż dwie litery mają być poprawiane
# automatycznie, natomiast o podmianę wyrazu dwuliterowego (np. IT na It)
# program ma pytać użytkownika za każdym razem, gdy na taki natrafi.

# import re
#
# text = "SZczecin TO miasto w POlsce, w wojeództwie ZAchodniopomorskim, NA PObrzezu Szczecińskiem"
#
# pattern_search_long = r"\b[A-Z]{2}[A-Za-z]+\b"
# pattern_search_short = r"\b[A-Z]{2}\b"
# result = re.sub(pattern_search_long, lambda x: x. group().capitalize(), text)
#
# short_replacements = re.findall(pattern_search_short, result)
# for item in short_replacements:
#     user_answer = input(f"Możliwy błąd: {item}. Czy zmienić (T/N) \n")
#     if user_answer == "t":
#         result = re.sub(item, item.capitalize(), result)
#
# print(result)

# print(re.findall(pattern_search_long, text))

"ZAJĘCIA"

# argparse

# import os
# # import re
# # import argparse
# #
# # def parse_arguments():
# #     parser = argparse.ArgumentParser("contins pythob files in given patch")
# #     parser.add_argument("--dir", "-d", type=str, required=True,
# #                         help="patch to the directory form which we would like to count")
# #     args = parser.parse.args()
# #     return args
# #
# # if __name__ == "main__":
# #     args = parse_arguments()
# #     counter = 0
# #     for file in os.listdir(args.dir):
# #         counter +=1
# #
# #     print(counter)

# Zadanie
# Stwórz skrypt, który zwróci pole trójkąta dla długości podstawy i wysokości
# przekazanych jako argumenty w konsoli poleceń.

import os
import re
import argparse

# def parse_arguments():
#     parser = argparse.ArgumentParser("Podaj wysokośc trójkąta")
#     parser.add_argument('-dl', type=float, required=True,
#                         help="Bla bla bla")
#     parser.add_argument('-w', type=float, required=True,
#                         help="Bla bla bla")
#     args = parser.parse_args()
#     return args
#
# if __name__ == "__main__":
#     args = parse_arguments()
#     print("podaj wysokość tr."), args.w
#     print("podaj długość tr."), args.dl
#     print("pole trójkąta wynosi", args.dl * args.w / 2)


# import argparse
#
# def parse_arguments():
#     parser = argparse.ArgumentParser("Liczy pole trójkąta")
#     parser.add_argument("--długosc", '-dl', type=float, required=True,       # można zrobić: "--długosc", '-dl', type=float, required=True,
#                         help="Długość boku tójkąta")
#     parser.add_argument('-w', type=float, required=True,
#                         help="Bla bla bla")
#     return parser.parse_args()
#
#
# if __name__ == "__main__":
#     args = parse_arguments()
#     pole =  args.dl * args.w / 2


# Zadanie
# Stwórz skrypt, w którym przekażesz ścieżkę do pliku tekstowego oraz napis,
# którego liczbę wystąpień w tym pliku chcesz poznać.


# import argparse
#
# def parse_arguments():
#     parser = argparse.ArgumentParser("Program liczy liczbę powtórzeń w tkeście")
#     parser.add_argument("--plik", "-p", type=str, required=True,
#                          help="ścieżka do pliku który będziemy sprawdzać")
#     parser.add_argument("--tekst", '-t', type=str, required=True,
#                         help="napis który mamy spradzwiić")
#     return parser.parse_args()
#
#
# if __name__ == "__main__":
#     args = parse_arguments()
#     with open(args.plik) as file:
#         counter = 0
#         for line in file:
#             for word in line.lower(). split():
#                 if word == args.tekst:
#                     counter += 1
#     print(f'Słowo {args.tekst} pojawiło się w  pliku {args.plik} {counter} razy')



# import logging
#
# # Create and configure logger
# logging.basicConfig(filename="newfile.log", level=logging.INFO)
#
#
# # Creating an object
# logger = logging.getLogger()
#
# # Setting theshold of longer to warning
# logger.setLevel(logging.WARNING)
#
# #Test message
#
# logger.debug("harmless debug Message")
# logger.info("Just an information")
# logger.warning('Its a Warning')
# logger.error("did you try to divide by zerio")
# logger.critical("internet is down")


# SWITCH CASE


# Stwórz Kalkulator

# def dodawanie(a, b):
#     return a+b
#
# def odejmowanie(a,b):
#     return a -b
#
# def mnozenie(a, b):
#     return a *b
#
# def dzielenie(a, b):
#     return a /b
#
# if __name__ == "__main__":
#     switch ={
#         "+": dodawanie,
#         "-": odejmowanie,
#         "*": mnozenie,
#         "/": dzielenie
#     }
#
#     user_input = input("Podaj wyrażenie\n")
#     pattern = r"(\d+)([\+\-\*/])(\d+)"
#     liczba1, dzialanie, liczba2 = re.search(pattern, user_input).groups()
#
#     func = switch[dzialanie]
#     print(func(int(liczba1), int(liczba2)))

# Albo  lambdy

# if __name__ == "__main__":
#     switch ={
#         "+": lambda x, y: x + y,
#         "-": lambda x, y: x - y,
#         "*": lambda x, y: x * y,
#         "/": lambda x, y: x - y
#     }
#
#     user_input = input("Podaj wyrażenie\n")
#     pattern = r"(\d+)([\+\-\*/])(\d+)"
#     liczba1, dzialanie, liczba2 = re.search(pattern, user_input).groups()
#
#     func = switch[dzialanie]
#     print(func(int(liczba1), int(liczba2)))

# Zadanie
# Napisz program do zamiany numeru dnia tygodnia na jego nazwę.


# def day_number_to_string(day_number):
#     switch = {
#         1:"poniedziałek",
#         2:"wtorek",
#         3:"środa",
#         4:"czwartek",
#         5:"piątek",
#         6:"sobota",
#         7:"niedziela"
#     }
#     return switch.get(day_number, "LOL")
#
# if __name__ == "__main__":
#     user_day = input("Podaj numer dnia\n")
#     print(day_number_to_string(int(user_day)))


# Zadanie
# # Korzystając z utworzonej wcześniej klasy Punkt utwórz kilka jej instancji, a
# # następnie spróbuj porównać ze sobą dwa punkty oraz dodać je do siebie.

# from math import sqrt
#
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def show_point(self):
#         return f"Your point's location is: {self.x} on axis X and {self.y} on axis Y."
#
#     def relocate(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#         return f"Your new point's location is: {self.x} on axis X and {self.y} on axis Y."
#
#     def calculate(self, xpoint, ypoint):
#         distance = sqrt((abs(xpoint - self.x))**2 + (abs(ypoint - self.y))**2)
#         return f"Distance from your point to point: {xpoint}, {ypoint} is {distance}"
#
#     def __str__(self):
#         return f"Point({self.x},{self.y})"
#
#     def __eq__(self, other):                               # (Nowa metoda)
#         return self.x == other.x and self.y == other.y
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
#
#
# if __name__ == "__main__":
#     point1 = Point(4, 5)
#     point2 = Point(6, 3)
#     print(point1)
#     # Wymyśl inne przykłady


# Zadanie
# Dokończ implementację tak, by program wykonywał się bez błędu

from math import sqrt

class Wektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dlugosc(self):
        return sqrt(self.x ** 2 + self.y ** 2)


    def __str__(self):
        return f"Wektor({self.x},{self.y} o dłgugości {self.dlugosc()})"

    def __eq__(self, other):                               # (Nowa metoda)
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Wektor(self.x + other.x, self.y + other.y)

    def _

if __name__ == "__main__":
    w1 = Wektor(1, 3)
    w2 = Wektor(2, 5)
    w3 = Wektor(4, 3)

    assert str(w3) == "wektor (4, 3) o długości 5.0"
    assert w1 + w2 == Wektor(3,8)
    assert  w3.dlugosc() == 5.0