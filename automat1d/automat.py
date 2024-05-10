import random

rule = input("podaj ciag binarny: ")
n = int(input("podaj dlugosc ciagu: "))
k = int(input("podaj liczbe krokow: "))

rand = "".join(random.choice("*_") for _ in range(n))

automat = {"***": "_", "**_": "*", "*_*": "_", "*__": "*", "_**": "*", "_*_": "_", "__*": "*", "___": "_"}

for key, bit in zip(automat.keys(), rule):
    value = "_" if bit == "0" else "*"
    automat[key] = value

for i in range(0, k):
    print(rand)
    result = ""
    for j in range(0, len(rand)):
        if j == 0:
            result += automat[rand[-1] + rand[j] + rand[j + 1]]
        elif j == len(rand) - 1:
            result += automat[rand[j - 1] + rand[j] + rand[0]]
        else:
            result += automat[rand[j - 1] + rand[j] + rand[j + 1]]
    rand = result
print(rand)
