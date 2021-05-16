import pandas as pd
import numpy as np
import xlrd
import openpyxl
print('\n\n')

#zad1.
print('------zadanie 1------')
imiona = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(imiona)
# print(df)
print('\n\n')



#zad2.
print('------zadanie 2------')
print('a)--------------------------------------------------------')
#print(imiona.where(imiona.Liczba > 1000))
print(df[df['Liczba']>1000])
print('\n')
print('b)--------------------------------------------------------')
print(df[df['Imie'] == 'BARTOSZ'])
print('\n')
print('c)--------------------------------------------------------')
print(df['Liczba'].sum())
print('\n')
print('d)--------------------------------------------------------')
df1 = df.groupby('Rok', as_index=False)['Liczba'].sum()
print(df1[:6])
# print(df[df['Rok']==2000])
# print(df[df['Rok']==2001])
# print(df[df['Rok']==2002])
# print(df[df['Rok']==2003])
# print(df[df['Rok']==2004])
# print(df[df['Rok']==2005])
print('\n')
print('e)--------------------------------------------------------')
chlopcy = df.loc[df['Plec'] == 'M', 'Liczba'].sum()
print('chlopacy: ', chlopcy)
dziewczyny = df.loc[df['Plec'] == 'K', 'Liczba'].sum()
print('dziewczyny: ', dziewczyny)
print('\n')
print('g)--------------------------------------------------------')
# df2 = df.groupby('Imie', as_index=False).agg({'Liczba': {'sum'}})
# print(df2)
ile = df['Imie'].value_counts()[:5].sort_values(ascending=False)
print(ile)
print('\n\n')



#zad3.
print('------zadanie 3------')
print('a)--------------------------------------------------------')
zam = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
print(zam['Sprzedawca'].unique())
print('\n')
print('b)--------------------------------------------------------')
print(zam.sort_values('Utarg', ascending=False).head(5))
print('\n')
print('c)--------------------------------------------------------')
ile2 = zam.groupby(['Sprzedawca']).agg({'Sprzedawca': {'count'}})
print(ile2)
print('\n')
print('d)--------------------------------------------------------')
kraje = zam.groupby(['Kraj']).agg({'Kraj': {'count'}})
print(kraje)
print('\n')
print('e)--------------------------------------------------------')
PL = zam.loc[(zam['Data zamowienia'] >= '2005-01-01') & (zam['Data zamowienia'] < '2005-12-30')]
#print(PL)
PL1 = PL.loc[zam['Kraj'] == 'Polska']
#print(PL1)
zam1 = PL1.loc[zam['Kraj'] == 'Polska'].agg({'Kraj': {'count'}})
print(zam1)
print('\n')
print('f)--------------------------------------------------------')
o4 = zam.loc[(zam['Data zamowienia'] >= '2004-01-01') & (zam['Data zamowienia'] < '2004-12-30')]
#print(o4)
zam2 = round(o4['Utarg'].mean())
print(zam2)
print('\n')
print('g)--------------------------------------------------------')
d_2004 = zam.loc[(zam['Data zamowienia'] >= '2004-01-01') & (zam['Data zamowienia'] < '2004-12-30')]
d_2005 = zam.loc[(zam['Data zamowienia'] >= '2005-01-01') & (zam['Data zamowienia'] < '2005-12-30')]

d_2004.to_csv('zamowienia-2004.csv', index=False, header=True)
d_2005.to_csv('zamowienia-2005.csv', index=False, header=True)



