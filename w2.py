# Zadanie 1 (1.py):
# • Dla osób poniżej 4 roku życia wstęp jest bezpłatny.
# • Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.
# • Dla osób powyżej 18 roku życia bilet kosztuje 20zł.
# Przykład: Wprowadź wiek klienta: 5
# # Cena biletu: 10zł

wiek = input ('podaj wiek')
wiek = int(wiek)
if wiek < 4:
    cena = 0
elif wiek <= 18:
    cena = 10
else: cena = 20

print(f"cena biletu {cena} zl")


