#zad1.
print('------zadanie 1------')
import numpy as np
a = np.array([3, 2, 5])
b = np.array([4, 7, 8])
print(a)
print(b)
print(np.dot(a, b))
print('\n\n')

#zad2.
print('------zadanie 2------')
a = np.array([[3, 2, 5], [34, 1, 11], [34, 0, 11]])
b = np.array([[2, 20, 3, 44], [14, 1, 21, 12], [14, 0, 21, 12], [14, 2, 21, 12]])
print(a)
print('\n')
print(b)

print("minimalne wartosci z kolumn: ", a.min(axis=0), "oraz ", b.min(axis=0))
print("minimalne wartosci z rzedow: ", a.min(axis=1), "oraz ", b.min(axis=1))
print('\n\n')

#za3.
print('------zadanie 3------')
a = np.array([3, 2, 5])
b = np.array([4, 7, 8])
print(a.dot(b))
print('\n\n')


#za4.
print('------zadanie 4------')
a = np.array([3, 4, 6])
b = np.empty(3)
print(a)
print(b)
print(a.dtype)
print(b.dtype)
print("tablice po wymnozeniu: ", a.dot(b))
print('\n\n')

#za5.
print('------zadanie 5------')
x = np.array([[12, 2, 3], [4, 6, 7]])
print(x)
print('\n')
a = np.sin(x)
print(a)
print('\n\n')

#za6.
print('------zadanie 6------')
x = np.array([[12, 2, 3], [4, 6, 7]])
print(x)
print('\n')
b = np.cos(x)
print(b)
print('\n\n')

#za7.
print('------zadanie 7------')
c = a + b
print(c)
print('\n\n')

#za8.
print('------zadanie 8------')
x = np.arange(9).reshape(3, 3)
print(x)
for rzad in x:
    print(rzad)
print('\n\n')

#za9.
print('------zadanie 9------')
x = np.arange(9).reshape(3, 3)
print(x)
for e in x.flat:
    print(e)
    print("")
print('\n\n')

#zad10.
print('------zadanie 10------')
x = np.arange(81).reshape(9, 9)
print(x.shape)
x1 = x.reshape(3,27)
print(x1.shape)
x2 = x1.ravel()
print(x2.shape)
#mozliwosci jest sporo, mozemy tak dlugo zmieniac ksztalt, dopoki iloczyn rzedow i wierszy
#bedzie rowny 81
print('\n\n')

#zad11.
print('------zadanie 11------')
x = np.arange(12)
print(x)
print('\n')
x1 = x.reshape((3, 4))
print("macierz nr1 : \n", x1)
x1s = x1.ravel()
print(x1s)

print('\n')
x2 = x.reshape((4, 3))
print("macierz nr2 : \n", x2)
x2s = x2.ravel()
print(x2s)

print('\n')
x3 = x.reshape((2, 6))
print("macierz nr3 : \n", x3)
x3s = x3.ravel()
print(x3s)

# splaszczone macierze wygladaja na identyczne