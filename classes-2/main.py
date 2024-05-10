# functions

def kwadrat(x):
    return x ** 2


# print(kwadrat(15))

def concat(s1, s2=' nie ma', s3=' nic'):
    return s1 + s2 + s3


# print(concat("Ala", s3=" kota"))

def rozszerz(l=[], element=['x']):  # each execute adds to the end
    l.append(element)
    return l


# print(rozszerz())

def rozszerz2(l=None, element=['x']):  # each execute adds to the end but only once
    if l == None:
        l = []
    l.append(element)
    return l


def f(a, b=None):
    if b == None:
        b = a
    print(a)
    print(b)


# f("marek")

def dlugosc(x):
    if type(x) in {str, list, tuple}:
        return len(x)
    elif type(x) in (int, float, complex):
        return abs(x)
    else:
        return None


# print(dlugosc(-1000))

def fun(*args):
    print(args)


# lambda functions
lambda x: x ** 3
# print(szescian(7))

funkcja = lambda a, b, c=2: (a + b) ** c
# print(funkcja(1,2,4))


# functional programming
l = [i for i in range(1, 11)]


# print(list(map(lambda x:x**3,l)))

def select(x):
    if x > 0: return True
    return False


l = "Ala ma kota psa i chomika".split()


# print(sorted(l, key = lambda s:len(s)))

def iloczyn_skalarny(a, b):
    return sum(map(lambda i: i[0] * i[1], zip(a, b)))


l = list(range(1, 31))  # zadanie: usun elementy podzielne przez 3, nieparzyste pomnoz *2
print([2 * i if i % 2 != 0 else i for i in l if i % 3 != 0])  # rozwiazanie 1
print(list(map(lambda i: i * 2 if i % 2 != 0 else i, filter(lambda i: i % 3, l))))  # rozwiazanie 2
