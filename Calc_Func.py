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
