'''
Scenario
Do you know what a palindrome is?

It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.

Your task is to write a program which:

asks the user for some text;
checks whether the entered text is a palindrome, and prints result.
Note:

assume that an empty string isn't a palindrome;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent;
there are more than a few correct solutions - try to find more than one.
Test your code using the data we've provided.
'''

#PEDIMOS AL USER QUE INTRODUZCA EL TEXTO
text = input('inserto some text to check if it is a palindrome or not: ')
#PONEMOS TODO EN MAYUSCULAS PARA QUE NO DIFERENCIE
text1 = text.upper()
#QUITAMOS LOS ESPACIOS
text2 = text1.replace(' ', '')

if text2 == text2[::-1]:
    print('"' + text + '"' + ' is a palindrome')
else:
    print('"' + text + '"' + ' is not a palindrome')
