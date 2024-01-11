'''
ALGORITMO DEL CIFRADO DE CAESAR ORIGINAL

 Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

Scenario
You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you recently.

The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
prints out the encoded text.
Test your code using the data we've provided.
'''

text = input("Enter your message: ")
move = input('Enter your index move for the cipher: ')
cipher = ''

for char in text:
    
    #MAYUSCULAS
    if ord(char) in range(65, 91):
        code = ord(char) + int(move)
        if code > ord('Z'):
            code = ord('A') + (int(move) - (ord('Z') - ord(char)))-1
    #MINUSCULAS
    elif ord(char) in range(97, 123):
        code = ord(char) + int(move)
        if code > ord('z'):
            code = ord('a') + (int(move) - (ord('z') - ord(char)))-1
    #OTROS CARACTERES
    else:
        code = ord(char)
    
    cipher += chr(code)

print(cipher)

