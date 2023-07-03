# 1
s = 'Ala ma kota'
lz = list(s)
print(lz)
for i in range(len(lz)):
    print(lz[i], end='')
print('\n')
for i in lz:
    print(i, end='')

print('\n')
# 2
s = input('Wprowadź zdanie: ')
ls = list(s)
ile = ls.count('a')
print('Ilość literek a:', ile)

print('\n')
# 3
from math import factorial
n = factorial(2000)
s = str(n)
l = list(s)
ile = l.count('9')
print('Ilość cyfr 9:', ile)
for i in range(0, 10):
    znak = str(i)
    ile = l.count(znak)
    print('Ilość cyfr', i, ile)

print('\n')
# 4
lz = list('Alamakota')
print(lz.index('a'))
print(lz.index('m'))
print(lz.index('k'))
l = []
for i in range(0, 31):
    l.append(3**i-2**i)
print('Pozycja liczby 1161737179:', l.index(1161737179))
print('3^19-2^19=', 3**19-2**19)

print('\n')
# 5
l = []
for i in range(0, 31):
    l.append(3**i-2**i)
l2=[]
for i in range(0, 31):
    l2.append(l[i] % 19)
print(10 in l2)
print(11 in l2)
liczba = int(input('Wprowadź liczbę z zakresu 0-18: '))
while(liczba < 0 or liczba > 18):
    print('Wprowadzono liczbę spoza zakresu!')
    liczba = int(input('Wprowadź liczbę z zakresu 0-18: '))
    test = 10 in l2
    print(test)
if liczba in l2:
    print('Ta liczba występuje w l2', l2.count(liczba), 'razy')
else:
    print('Nie ma tej liczby w l2')

print('\n')
# 6
from math import factorial
l = []
for i in range(1, 101):
    l.append(1/i)
print(sum(l))
print(min(l))
print(max(l))

n = factorial(1000)
s = str(n)
lz = list(s)
for i in range(len(lz)):
    lz[i] = int(lz[i])
print('Suma cyfr 1000! :', sum(lz))

print('\n')
# 7
from math import factorial
n = factorial(1000)
s = str(n)
lz = list(s)
ld = []
for i in range(0, len(lz), 2):
    ld.append(lz[i]+lz[i+1])
for i in range(0, 100):
    if i < 10:
        s = '0' + str(i)
    else:
        s = str(i)
    print(s, '- występuje', ld.count(s), 'razy')
