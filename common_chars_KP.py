#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Napisz funkcję common_chars(string1, string2), która zwraca alfabetycznie
uporządkowaną listę wspólnych liter z lańcuchów string1 i string2.
Oba napisy będą składać się wyłacznie z małych liter.
"""


def common_chars(string1, string2):
    wspolne_litery = [] # utworzenie pustej listy
    for char1 in string1: #pętla iterująca po znaku, bo po in jest zmienna typu string
        for char2 in string2: #druga pętla iterująca po drugim ciągu - w ten sposób sprawdzam każdy znak z każdym
            if char1 == char2: #gdy znak się powtarza
                if char1 not in wspolne_litery: #wykluczenie duplikatów
                    if char1 != ' ': #wykluczenie 'spacji'
                        wspolne_litery.append(char1) # dodanie do listy elementu
    return(wspolne_litery)

input1 = "this is a string"
input2 = "ala ma kota"
print(common_chars(input1,input2))
#output = ['a', 't']

