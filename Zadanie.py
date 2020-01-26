def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Nie można dzielić przez zero"

check_1 = True
while check_1:
    a = input("wpisz pierwszą liczbę\n")
    try:
        a = float(a)
        check_1 = False
    except ValueError:
        print('Podana wartość nie jest liczbą.')

check_2 = True
while check_2:
    b = input("wpisz drugą liczbę\n")
    try:
        b = float(b)
        check_2 = False
    except ValueError:
        print('Podana wartość nie jest liczbą')

check_3 = True
while check_3:
    dzialanie = input("Podaj jaką operację chcesz wykonać\nDodawanie (1)\nOdejmowanie (2)\nMnożenie (3)\nDzielenie (4)\n")
    if dzialanie == "1" or dzialanie == "2" or dzialanie == "3" or dzialanie == "4":
        check_3 = False

if dzialanie == "1":
    print(dodawanie(a, b))
elif dzialanie == "2":
    print(odejmowanie(a, b))
elif dzialanie == "3":
    print(mnozenie(a, b))
elif dzialanie == "4":
    print(dzielenie(a, b))