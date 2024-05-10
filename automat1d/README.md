Jednowymiarowy automat komórkowy
Teoria
Dany jest przykładowy zestaw reguł określony w następujący sposób:
*** **_ *_* *__ _** _*_ __* ___
_ * _ * * _ * _
0 1 0 1 1 0 1 0
Oznaczony ten zestaw reguł jako “Rule 90” (01011010), który każdym kolejnym
trzem elementom ciągu złożonego z * i _ przyporządkowuje te elementy w
pokazany sposób tworząc nowy ciąg. Koolejny cią tworzony jest na podstawie
poprzedniego. (jednowymiarowa przestrzeń ma topologię okręgu)
Program
Napisać program automat, który:
1. przyjmuje argumenty podczas uruchamiania:
• rule - ciąg binarny,
• n - długość ciągu,
• k - liczba kroków,
• plik - nazwa pliku z wynikami,
2. tworzy losowy ciąg o długości n składający się * i _
3. Zapisuje w pliku automat.txt wynik działania w postaci:
regula: 01010010
liczba kroków: k
*_*_*_**__**__*_*_**_**__*__**
**___**_*_*_**__**_***_*___*_*
...
Sprawdzić działanie programu dla różnych warunków początkowych i
różnych warunków brzegowych.
4. Rozbudować program o możliwość odczytywania pliku z danymi początko-
wymi automat.cfg w formacie:
regula: 01010011
dlugosc ciagu: 80
*__*_*_*_*_******__**_*_**_**...
5. Zbadać wynik działania programu dla ciągu o długości 80 znaków, dla
ciągu początkowego postaci:
1
___..._*_...___
to znaczy element * jest w “środku ciągu”.
2
