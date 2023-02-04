# dla danego stringa x stwórz słownik
# przechowujący informację ile razy dana litera wystąpiła w stringu

x = "myszydokazujągdykotanieczują"

x_dict = {}

for let in x:
    if let not in x_dict.keys():
        x_dict[let] = 1
    else:
        x_dict[let] += 1

#for a, b in x_dict.items():
#    print(a, b == 3)

print(4 in x_dict.values())

pensje = {'ksiegowa': 5000, 'kierowca': 4500, 'recepcjonistka': 4000}


print(sum(pensje.values()))

#####################################################

jezyki = ["Python", "Java", "C#", "Ruby"]
print(f"Przed: \n{jezyki}")
print("Po:")

# 1)
#jezyki.reverse()
#jezyki_odwrocone = jezyki

# 2)
#jezyki_odwrocone = list(reversed(jezyki))

# 3) 

jezyki_odwrocone = jezyki[::-1]

print(jezyki_odwrocone)

odwroc_mnie = ['trudne', 'takie', 'bylo', 'nie', 'To']

odwrocona = odwroc_mnie[::-1]

print(' '.join(odwrocona))


def palindrom(słowo):
    return słowo.lower() == słowo[::-1].lower()

print(f'Kajak: {palindrom("Kajak")} \nAnakonda: {palindrom("anakonda")}')


def sprawdzian(word):
    poczatek = 0
    koniec = len(word) -1

    while poczatek <= koniec:
        if word[poczatek] != word[koniec]:
            return False
        else:
            poczatek += 1
            koniec -= 1
    return True

def sprawdz_czy_palindrom(slowo):
    poczatek = 0                              # stwórz indeks poczatkowy równy 0
    koniec = len(slowo) - 1                   # stwórz indeks końcowy równy długości stringa zmniejszonej o 1

    while poczatek <= koniec:                 # wykonuj pętlę dopóki indeks poczatkowy jest mniejszy lub równy indeksowi końcowemu
        if slowo[poczatek] != slowo[koniec]:  # jeśli wartosc zmiennej slowo od indeksu początkowego jest różna od wartości od indeksu końcowego
            return False                      # zwróć False
        else:                                 # w przeciwnym wypadku
            poczatek += 1                     # zwiększ indeks początkowy o 1
            koniec -= 1                       # zmniejsz indeks końcowy o 1
    return True                               # jeśli funkcja dotarła do tego miejsca, to znaczy że słowo jest palindromem i funkcja zwraca True

print(sprawdzian("anna"))

zdanie = "kobyła ma mały bok"
print(zdanie.replace(' ', ''))

print(sprawdz_czy_palindrom(zdanie.replace(' ', '')))

lista_A = list(range(1,11))
lista_B = list(range(100, 0, -3))
lista_C = list(reversed(range(1, 101, 3)))
print(lista_A)
print(lista_B)
print(lista_C)

R = list(range(-5, 6, 2))
print(R)

# 
# Wypisz pierwsze 5 elementów listy L.
# Wypisz co drugą literę stringa s, zaczynając od ostatniej i cofając się do poczatku.

L = [11, 22, 33, 44, 55, 66, 77, 88, 99, 1010]
s = 'a nMozh^tKysPW 9ęxi b$uML'

print(L[:5])
print(s[-1::-2])

#  napisz funkcję, która sprawdzi czy podany string
# zaczyna się słowem "python" i kończy rozszerzeniem ".py"
# Przetestuj nią stringi:
a = "python_moj_kod.py"
b = "python_notatki.txt"

def startEnd(st):
    return st[:6] == "python" and st[-3:] == ".py"

print(startEnd(a))
print(startEnd(b))

z = "In the face of ambiguity, refuse the temptation to guess."

print(z[-6:])

imiona = ['Adam', 'Stanisław', 'Maria', 'Zofia', 'Mikołaj']

for numer_i, imie in enumerate(imiona, start=1):
    print(f"{numer_i}. {imie}")

#  znajdź różnicę między największą a najmniejszą wartością
# na poniższej liście.
# Zadbaj o to aby rozwiązanie było efektywne.

A = [4, 5, 7, -3, 2, 8, -10, 15]

roznica = max(A) - min(A)
print(roznica)


#Sprawdź i wypisz (True lub False) czy największy element na liście A = [x**2 + 3 for x in range(10)] jest większy niż liczba 99.

A = [x**2 + 3 for x in range(10)]

print(max(A) > 99)

def podzielnosc(liczba_1, liczba_2):
    return (liczba_1 % liczba_2 == 0)

print(f"Podzielność: {podzielnosc(4, 2)}")

a = 123454321

b = 11111

print(podzielnosc(a, b))


def dodaj_do_listy(n, lista=[]):  # lista=[] - argument domyślny funkcji
    lista.append(n)               # dodaj n do końca listy lista
    print(lista)

# Argument domyślny, w tym wypadku pusta lista, zostaje utworzona RAZ
# podczas definiowania funkcji i nie jest tworzona od nowa podczas kolejnych jej wywołań
# dlatego modyfikacja argumentu domyślnego podczas wywołania funkcji, spowoduje zapisanie tego stanu
# i zmodyfikowana lista trafi jako argument do kolejnego wywołania funkcji
# w którym zostanie użyty argument domyślny.

dodaj_do_listy(1)
dodaj_do_listy(2,[4,5])
dodaj_do_listy(3)

def nowe_dodanie(element_dod, lista_n=None):
    if lista_n == None:
        lista_n = []
    lista_n.append(element_dod)
    return lista_n

print(nowe_dodanie(1))
print(nowe_dodanie(3))

# co otrzymamy w wyniku wydrukowania zawartości poniższych zmiennych?

L = [1,2,3,4,5,6]

L1 = [x for x in range(5)]        # wpisz do listy L1 elementy z zakresu od 0 do 4
L2 = [x**2 for x in L]            # wpisz do listy L2 elementy z listy L podniesione do kwadratu
L3 = [x for x in L if x % 2 == 0] # wpisz do listy L3 elementy z listy L, tylko jeśli dany element jest podzielny przez 2
L4 = ['Parzysta' if x%2 == 0 else 'Nieparzysta' for x in range(5)]
                                  # wpisz do listy L4 'Parzysta' lub 'Nieparzysta' w zależności od tego czy kolejny element
                                  # z zakresu 0 do 4 jest podzielny lub nie jest podzielny przez 2
L5 = [(x, x+10) for x in L]       # wpisz do listy L5 dwuelementowe tuple, które na indeksie 0 mają kolejny element z lsty L
                                  # a na indeksie 1 ten sam element zwiększony o 10
D1 = {x: x % 2 == 0 for x in L}    # wpisz do słownika D1 pary klucz:wartość, gdzie kluczem są elementy z listy L
                                  # a wartościami True lub False, w zależności od tego czy dany klucz jest podzielny przez 2

print(L1)
print(L2)
print(L3)
print(L4)
print(L5)
print(D1)

A1 = [x+1 for x in range(5,11)]
print(A1)

##################
# SŁOWNIK Z LIST #
##################

keys_list = ['A', 'B', 'C']
values_list = ['blue', 'red', 'bold']

dictionary = dict(zip(keys_list, values_list))
print(dictionary)

dictionary_com = {key: value for key, value in zip(keys_list, values_list)}
print(dictionary_com)

dictionary_enu = {key: value for key, value in enumerate(values_list, start=1)}
print(dictionary_enu)