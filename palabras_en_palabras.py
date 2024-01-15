'''
Scenario
Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.

Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

For example:

if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)
Hints:

you should use the two-argument variants of the pos() functions inside your code;
don't worry about case sensitivity.
Test your code using the data we've provided.
'''

word = input('insert a word: ')
word1 = word.upper()
text = input('insert a string of characters: ')
text1 = text.upper()

start = 0
check = ''

for letter in word1:
    pos = text1.find(letter, start)
    if pos != -1:
        check += letter
        start = pos +1

if check == word1:
    print('ok')
else:
    print('not ok')
        
    
