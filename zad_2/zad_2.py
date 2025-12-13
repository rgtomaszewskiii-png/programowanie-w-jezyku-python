
def pomnoz_przez_2_for(liczby):
"""Otrzymuje listę 5 liczb, mnoży każdy element przez 2 i zwraca nową listę."""
wynik = []
for x in liczby:
wynik.append(x * 2)
return wynik

if name == 'main':
lista = [1, 2, 3, 4, 5]
print(pomnoz_przez_2_for(lista)) # [2, 4, 6, 8, 10]