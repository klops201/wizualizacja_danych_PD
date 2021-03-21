import random
#zad1.
print('------zadanie 1------')
lista = []
a = 1
for a in range(50):
    a = random.randrange(100)
    if a % 4 == 0:
        lista.append(a)
print(lista)
plik = open("zad.txt", "w")
plik.writelines(str(lista))
plik.close()
print('\n\n')

#zad2.
print('------zadanie 2------')
plik = open("zad.txt", "r")
wiersze = plik.readlines()
linia = plik.readline()
plik.close()
print(wiersze)
print('\n\n')

#zad3.
print('------zadanie 3------')
with open('test1.txt', 'a') as a:
    for elem in 'test':
        a.write(elem + '\n')

with open('test1.txt', 'r') as b:
    for elem in b:
        print(elem)
print('\n\n')

#zad4.
print('------zadanie 4------')
class NaZakupy:

    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        return self.nazwa_produktu

    def ile_produktu(self):
         return f'{self.ilosc}  {self.jednostka_miary}'

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

ziemniak = NaZakupy("ziem", 0.5, "kg", 3.2)
marchew = NaZakupy("mar", 3, "szt", 5)

print(ziemniak.wyswietl_produkt())
print(marchew.ile_kosztuje())
print(marchew.ile_produktu())
