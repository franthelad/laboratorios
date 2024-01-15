'''Scenario
An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.
Note:

assume that two empty strings are not anagrams;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent
Test your code using the data we've provided.
'''

#insertamos el texto original
text = input('introduce un texto: ')
#insertamos un 2º texto para comprobar si es anagrama del primero
text1 = input('introduce un segundo texto a ver si es anagrama del primero: ')

#ponemos en mayus y quitamos parentesis para que estos no influyan
text2 = text.upper().replace(' ', '')

#creamos una lista con las letras del texto
lista = []
for i in text2:
    lista.append(i)

#mayus y no espacios en el segundo texto introducido para que no influyan
text3 = text1.upper().replace(' ', '')

#formamos una lista con las letras del segundo texto introducido en mayus y sin espacios
lista1 = []
for i in text3:
    lista1.append(i)

#importamos la funcion counter que cuenta que cantidad de veces se encuentra cada elemento de un iterable en el mismo
from collections import Counter

#comparamos ambas listas, si los counter son iguales ambas listas tienen las mismas letras la misma cantidad de veces,
#indiferente de la posicion en la lista, ergo, son anagramas
if Counter(lista) == Counter(lista1):
    print('estas dos palabras son anagramas')
else:
    print('estas dos palabras no son anagramas')
