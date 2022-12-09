"""
Zaimplementuj funkcję `obwod`,obliczy i zwróci obwód zadanej figury. 
Szablon funkcji znajduje się poniżej. Funkcja przyjmuje dokładnie 1 argument, będący listą 2-elementowych krotek
oznaczającymi współrzędne x i y wierzchołka.

Przykład:
obwod([(0,0), (0,1), (1,1), (1,0)]) == 4
"""


def obwod(points):
    obw = 0
    for n in points:
        print([n[0]])
        print([n[1]])
       # print([[(n-1)][0]])
      #  obw += n
    return(obw)

print(obwod ([(0,1), (2,3), (4,5), (6,7)]))