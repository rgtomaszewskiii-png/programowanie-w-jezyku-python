
def wyswietl_parzyste(liczby):
"""Otrzymuje listę 10 liczb i wyświetla tylko te, które są parzyste."""
for x in liczby:
if x % 2 == 0:
print(x)

if name == 'main':

lista = list(range(1, 11)) # 1..10
wyswietl_parzyste(lista)