# list operations
x = int(input())
l = [1, 2, 3]
if x in l:
    print("yes")
else:
    print("no")
l = {True, True, False}
all(l)

z = int(input())
x = z if z > 5 else 10 * z
print(x)
z = int(input())
print(x := z if z > 5 else 10 * z)

# for loop operations
s = "ala ma kota"
for i in s:
    print(i)
for i in [1, 2, 3, 4, 5]:
    print(i ** 2)
for i in range(1, 10, 2):  # poczatek, koniec(n-1), krok
    print(i)
for i in range(10, 0, -1):
    print(i)

# list
l2 = [i ** 2 for i in range(1, 21) if i % 2 == 1]
print(l2)
l3 = [i / 3 for i in l2]
print(l3)

# embeded list
lz1 = [[i * j for i in range(j)] for j in range(10)]  # list of lists
print(lz1)

k = (i ** 2 for i in range(10))  # generator type
type(k)

# map
dl = dict((("a", 1), ("b", 2), ("c", 3)))
print(dl)
print(dl["a"])  # for key show val
print(dl.get("c", "null"))  # for key show val, if out of bands show null

import string

tekst = "Ala ma kota Mruczka".lower()
d = dict([[i, tekst.count(i)] for i in string.ascii_lowercase])
print(d)
