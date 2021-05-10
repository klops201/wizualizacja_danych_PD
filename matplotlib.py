#zad1.
print('------zadanie 1------')

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
df1 = df.groupby(['Rok']).agg({'Liczba':['sum']})
df1.plot()
plt.show()
print('\n\n')

#zad2.
print('------zadanie 2------')
df2 = df.groupby(['Plec']).agg({'Liczba':['sum']})

#print(df2)
w1 = df2.plot.bar()

plt.xticks(rotation=0)
plt.title('suma urodzen M i K')
plt.show()
print('\n\n')

#zad3.
print('------zadanie 3------')
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
df3 = df.where(df['Rok'] > 2012).groupby(['Plec']).agg({'Liczba': {'sum'}})

wykres = df3.plot.pie(subplots=True, fontsize=20)
plt.show()