'''
Scenario
Your task is to write a function able to input integer values and to check if they are within a specified range.

The function should:

accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
if the user enters a string that is not an integer value, the function should emit the message Error: wrong input, and ask the user to input the value again;
if the user enters a number which falls outside the specified range, the function should emit the message Error: the value is not within permitted range (min..max) and ask the user to input the value again;
if the input value is valid, return it as a result.
'''

def read_int(prompt, min, max):
    x = False
    while x == False:
        try:
            prompt = float(input(f'Enter a number from {min} to {max}: '))
            if prompt in range(min, max):
                x = True
                return prompt
            else:
                print(f'Error: the value is not within permitted range ({min}, {max})')
        except ValueError:
            print('Error: wrong input')


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
