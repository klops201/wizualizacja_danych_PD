import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

#zad1.
print('------zadanie 1------')
x = np.arange(20, 40, 0.2)
y = (1/x)
plt.plot(x, y, 'r')
plt.title('wykres funkcji f(x) dla x[20,40]')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim([20,40])
plt.ylim([0.02,0.05])
plt.show()

print('\n\n')

#zad2.
print('------zadanie 2------')
x = np.arange(20, 40, 0.9)
y = (1/x)
plt.plot(x, y, 'bo--', label='f(x) = 1/x')
plt.title('wykres funkcji f(x) dla x[20,40]')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim([20,40])
plt.ylim([0.02,0.05])
plt.show()
print('\n\n')



#zad3.
print('------zadanie 3------')
x1 = np.arange(0, 45, 0.1)
x2 = np.arange(0, 45, 0.1)

y1 = np.sin(x1)
y2 = np.cos(x2)



plt.subplot(2, 1, 1)
plt.plot(x1, y1, '-', label="wykres sinusa")
plt.plot(x2, y2, '-', label="wykres cosinusa")
plt.legend()
plt.title('wykres sin(x) i cos(x)')
plt.show()
print('\n\n')

#zad4.
print('------zadanie 4------')

x1 = np.arange(0, 45, 0.1)
x2 = np.arange(0, 45, 0.1)

y1 = np.sin(x1) + 2
y2 = np.sin(x2*-1)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, '-', label="sin(x)")
plt.plot(x2, y2, '-', label="sin(x)")
plt.legend()
plt.title('wykres sin(x), sin(x)')
plt.show()
print('\n\n')


#zad6.
print('------zadanie 6------')
imiona = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(imiona)
# plt.subplot(1, 2, 1)
# print(df)
# w1 = df['Liczba'].sum()
# w1 = df.groupby('Rok', as_index=False)['Liczba'].sum() #-----------------????????
# w1.plot.bar(x=sum, y='Liczba')
# plt.title('suma urodzen w kazdym roku')
# plt.show()


plt.subplot(1, 2, 1)
b = df.loc[df['Plec'] == 'M']
g = df.loc[df['Plec'] == 'K']
# print(b)
b = b.drop('Imie', 1)
b = b.drop('Plec', 1)
# print(b)
g = g.drop('Imie', 1)
g = g.drop('Plec', 1)

b1 = b.groupby('Rok', as_index=False)['Liczba'].sum()
g1 = g.groupby('Rok', as_index=False)['Liczba'].sum()
ax = plt.gca()
b1.plot(x = 'Rok', y = 'Liczba', kind = 'line', color='red', linewidth=2, label='chlopcy', ax=ax)
g1.plot(x = 'Rok', y = 'Liczba', kind = 'line', color='lightblue', linewidth=2, label='dziewczynki', ax=ax)
plt.legend()
# plt.show()

plt.subplot(1, 2, 2)


w3 = df.groupby('Rok', as_index=False)['Liczba'].sum()
w3.plot.bar(x='Rok', y='Liczba')
plt.title('suma urodzen w kazdym roku')
plt.show()

print('\n\n')
