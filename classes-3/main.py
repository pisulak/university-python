# ex 8
lista = [2, 5, 8, 9, 12, 15, 18, 21, 24, 27, 3, 6]

wynik = [x for x in lista if x % 3 != 0]
for i in range(0, len(wynik)):
    if wynik[i] % 2 != 0:
        wynik[i] *= 2
print(wynik)

# ex 9
list = ["32a12adsf", "54b32434", "65c12asdv"]
wynik = [''.join(filter(str.isalpha, element)) for element in list]
print(wynik)

# ex 10
list = ['a', 'b', 'c', '123d', 'gef', '45a6', '!@#1', '1423hge']

przeksztalcenie = [int(''.join(filter(str.isdigit, element))) for element in list if
                   ''.join(filter(str.isdigit, element))]

print(przeksztalcenie)

# ex 11
l = [(1,), (2, 3), (4, 5, 6), (7, 8, 9, 10)]

cut = [krotka[:2] for krotka in l if len(krotka) >= 2]

print(cut)

# ex 12
list = [(1, 2), (2, 4), (4, 5), (7, 7), (6, 9)]

wynik = [krotka for krotka in l if sum(krotka) % 2 == 0]

print(wynik)

# ex 13
list = [(3, 6, 9), (2, 6, 12), (9, 18, 27), (4, 8, 16)]

wynik = [krotka for krotka in l if all(element % 3 == 0 for element in krotka)]

print(wynik)

# ex 14
list = [(3, 6, 9), (2, 6, 12), (9, 18, 27), (4, 8, 16)]

wynik = [krotka for krotka in list if any(element % 3 == 0 for element in krotka)]

print(wynik)

# ex 15
list = ['hellou', 'hello world', 'Python is great', 'kocham pythona']

wynik = [słowo.split()[0] for słowo in list if len(słowo.split()) > 1]

print(wynik)


# ex 21
def pole(*args):
    if len(args) == 1:
        return args[0] ** 2
    elif len(args) == 2:
        return args[0] * args[1]
    elif len(args) == 3:
        a, b, h = args
        return 0.5 * (a + b) * h
    else:
        return "Niepoprawna liczba argumentów"


print(pole(5))  # pole kwadratu (5x5)
print(pole(3, 4))  # pole prostokąta (3x4)
print(pole(3, 5, 4))  # pole trapezu (podstawa1=3, podstawa2=5, wysokość=4)
