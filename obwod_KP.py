"""
Zaimplementuj funkcję `obwod`,obliczy i zwróci obwód zadanej figury. 
Szablon funkcji znajduje się poniżej. Funkcja przyjmuje dokładnie 1 argument, będący listą 2-elementowych krotek
oznaczającymi współrzędne x i y wierzchołka.

Przykład:
obwod([(0,0), (0,1), (1,1), (1,0)]) == 4
"""


def obwod(points):
    obw = 0
    X = []  #lista ze współrzędnymi x
    Y = []  #lista ze współrzędnymi y
    for n in points:  # pętla po krotkach (które są kolejnymi pozycjami listy)
        X.append(n[0])
        Y.append(n[1])
    X.append(points[0][0])  # dodanie na końcu listy pierwszego elementu do obliczenia długości ostatniego odcinka
    Y.append(points[0][1])

    for m in range(len(points)):  # pętla dla każdej krotki obliczająca odległość do następnego punktu
        dl_odc = ( (X[m+1]-X[m])**2 + (Y[m+1]-Y[m])**2 )**0.5
        obw += dl_odc
    return(obw)

print('Obwód figury z przykładu')
print(obwod ([(0,0), (0,1), (1,1), (1,0)]))
print('Obwód trójkąta pitagorejskiego')
print(obwod ([(0,0), (0,3), (4,0)]))