cumple = input('inserta tu fecha de nacimiento en formato DDMMYYYY: ')

if (cumple.isdigit() == False) or (len(cumple) != 8):
    print('algo falla aqui, seguro que has introducido el formato correcto?')
    x = False
elif int(cumple[:2]) > 31 or int(cumple[2:4]) > 12 or int(cumple[4:]) > 2024:
    print('algo falla aqui, seguro que has puesto una fecha correcta?')
    x = False
else:
    
    sum_cumple = 0

    for i in cumple:
        sum_cumple += int(i)

    while True:
    
        if len(str(sum_cumple)) > 1:

            sum_cumple1 = sum_cumple
            sum_cumple = 0
            for i in str(sum_cumple1):
                sum_cumple += int(i)
        else:
            break
    x = True
if x == True:
    print('Your digit of life is: ', sum_cumple)