import csv
from pathlib import Path

with open(Path(__file__).parent / './dogs-data.csv', encoding='utf-8') as data_file:
    dog_data = csv.DictReader(data_file)
    dog_data = list(dog_data)

print(dog_data[0])

"""
Zadanie 1

Do listy dog_data zostały wczytane dane o psach i ich właścicielach. Każdy element listy to słownik,
który ma 4 klucze 'OwnerAge', 'Gender', 'Breed', 'DogAge' oznaczające kolejno wiek właściciela (przedział wiekowy), 
płeć psa, rasę psa i wiek psa. 
Przykładowy element listy:
{'OwnerAge': 60, 'Gender': 'M', 'Breed': 'Welsh Terrier', 'DogAge': 3}

a) zapisz do zmiennej listę breeds listę wszystich ras psów zawartych w dog_data. Elementy
    listy powinny być unikatowe i posortowane afalbetycznie (A-Z).
"""
print('\n######################## Zadanie a ############################\n')

breeds = []
for n in range(len(dog_data)):
    if dog_data[n]['Breed'] not in breeds:  #sprawdza, czy dany gatunek nie znajduje się już w liście
        breeds.append(dog_data[n]['Breed'])  #jeśli się nie znajduje to jest dodawany do listy

breeds.sort()  #sortowanie listy
print(breeds)
#print('Łącznie gatunków:',len(breeds))


"""
b) Znajdź najpopularniejszą rasę psa dla każdego przedziały wiekowego (klucz `OwnerAge`) i 
    zapisz wynik jako słownik the_most_popular_breed, którego kluczami będą przedziały wiekowe,
    a wartością najpopularniejsza rasa psa (dla danego przedziału).
"""
print('\n######################## Zadanie b ############################\n')

age = []  #utworzenie listy unikalnych przedziałów wieku (analogicznie do zadania a)
for n in range(len(dog_data)):
    if dog_data[n]['OwnerAge'] not in age:  #sprawdza, czy dany gatunek nie znajduje się już w liście
        age.append(dog_data[n]['OwnerAge'])  #jeśli się nie znajduje to jest dodawany do listy
age.sort()  #sortowanie listy

the_most_popular_breed = {}  #utworzenie pustego słownika

for i in age: #pętla dla wieku 'i
    gatunek_max = ''  #zmienna przechowująca gatunek z max liczbą wystąpień
    wystapien_max = 0  #zmienna przechowująca max liczbę wystąpień
    for j in breeds:  #pętla po gatunku (w ramach wieku)
        liczba = 0  #zmienna przechowująca zliczenia danego gatunku w przedziale wiekowym
        for n in range(len(dog_data)):  #pętla po całym zbiorze danych - przez to operacja jest nieefektywna
            if dog_data[n]['OwnerAge'] == i and dog_data[n]['Breed'] == j:  #sprawdzenie warunku (wiek i gatunek)
                liczba += 1  #zwiększenie licznika
        if liczba > wystapien_max:  #sprawdzenie po zliczeniu czy nowa liczba jest większa od dotychczasowego max (stąd przy równym wyniku zostanie pierwsze wystąpienie)
            gatunek_max = j  #jeśli jest nowy max to zmiana gatunku max
            wystapien_max = liczba  #jeśli jest nowy max to zmiana liczby max
    the_most_popular_breed[i] = gatunek_max  #dodanie do słownika klucza - wieku i gatunku, który dla tego wieku wystąpił najczęściej

print(the_most_popular_breed)


"""
c) Biblioteka statistics (https://docs.python.org/3/library/statistics.html#) pozwala na
    obliczenie podstawowych funkcji statystycznych. Wykorzystaj odpowiednie funkcje i oblicz
    średnią, modę (mode) i wariancję wieku psów.
"""
print('\n######################## Zadanie c ############################\n')
import statistics

wiekPsow = []
for n in range(len(dog_data)):
    wiekPsow.append(int(dog_data[n]['DogAge']))

print('Średni wiek psów:',statistics.mean(wiekPsow))
print('Najczęstszy wiek psów:',statistics.mode(wiekPsow))
print('Wariancja wieku psów:',statistics.pvariance(wiekPsow),'zakładając, że dane to populacja generalna')
print('Wariancja wieku psów:',statistics.variance(wiekPsow),'zakładając, że dane to próbka')


"""
d)  Zapisz do plik `terriers.txt` nazwy wszystkich Terrierów wraz z ich liczebnością, które znajdują się w dog_data.
    Dane zapisz w formacie CSV. Wykorzystaj bibliotekę `csv` (https://docs.python.org/3.8/library/csv.html).
"""

print('\n######################## Zadanie d ############################\n')

terriery = []  #utworzenie listy terrierów
for n in range(len(dog_data)):
    if 'Terrier' in dog_data[n]['Breed']:  #sprawdza, czy dany gatunek zawiera w nazwie Terrier
        if dog_data[n]['Breed'] not in terriery:  #sprawdza, czy ten gatunek terriera nie jest na liście
            terriery.append(dog_data[n]['Breed'])  #jeśli się nie znajduje to jest dodawany do listy
terriery.sort()  #sortowanie listy

print(terriery)
print('Liczba gatunków terrierów:',len(terriery))

zest_terierow = {}
for i in terriery: #pętla po pozycjach listy teriery
    liczba = 0
    for n in range(len(dog_data)):
        if dog_data[n]['Breed'] == i:  # przyrównanie do iterowanego gatunku
            liczba += 1  # zwiększenie licznika
    zest_terierow[i] = liczba  #dodanie do słownika pary klucz-gatunek i wartość-liczba wystąpień

print(zest_terierow)

import csv

with open('terriers.txt', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Gatunek terriera','Liczba'])
    for row in zest_terierow.items():
        writer.writerow(row)
