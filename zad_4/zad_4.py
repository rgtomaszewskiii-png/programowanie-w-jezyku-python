def wyswietl_co_drugi(liczby):
"""Otrzymuje listę 10 liczb i wyświetla co drugi element (indeksy 0,2,4,...)."""

for i in range(0, len(liczby), 2):
print(liczby[i])

if name == 'main':
lista = list(range(10)) # 0..9
wyswietl_co_drugi(lista)