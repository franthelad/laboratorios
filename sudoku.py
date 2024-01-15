'''
Scenario
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
If you need more details, you can find them here.

Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
'''
#GENERAMOS LA FUNCION DEL SUDOKU

def sudoku1():
    
#GENERAMOS LA TABLA Y CONTADOR PARA BUCLE EN QUE PEDIREMOS LOS 9 NUMEROS
#DE 1 DIGITO Y COMPROBAREMOS QUE SON CANTIDAD CORRECTA SIN LETRAS
#SI METEN ALGO MAL SALE MENSAJE Y PIDE NUEVAMENTE

    table = []

    counter_ok = True

    counter = 0
    while counter < 9:
        rows = input('inserta una linea de numeros: ')
        if (rows.isdigit() == True) and (len(rows) == 9):
            counter += 1
            table.append(rows)
        else:
            print('Algo has insertado mal en esta ultima, seguro que son 9 numeros entre el 1-9?')

#GENERAMOS UNA LISTA CON LOS NUMEROS DEL 1 AL 9 PARA REALIZAR LAS COMPROBACIONES
    list = [i for i in range(1,10)]

#COMPROBAMOS SI LOS MUMEROS INTRODUCIDOS SON CORRECTOS POR FILAS
    for number in table:
    
        list = [i for i in range(1,10)]

        for digit in number:
            if int(digit) in list:
                list.remove(int(digit))
            else:
                counter_ok = False

#COMPROBAMOS SI LOS NUMEROS INTRODUCIDOS SON CORRECTOS POR COLUMNAS
    k = 0
    while k < 9:
    
        list = [i for i in range(1,10)]

        for number in table:
    
            if int(number[k]) in list:
                list.remove(int(number[k]))
            else:
                counter_ok = False
        k += 1

#GENERO UNA FUNCION QUE ME PERMITA COMPROBAR LAS 9 CUADRICULAS

    list = [i for i in range(1,10)]

    def square_check(x, y, z, l):

        list1 = []

        for number in table[x:y]:
            for digit in number[z:l]:
                list1.append(int(digit))
        list1.sort()
        if list1 != list:
            counter_ok = False

#UTILIZAMOS LA FUNCION PARA CADA CUADRIXULA 3X3
    square_check(0, 3, 0, 3)
    square_check(0, 3, 3, 6)
    square_check(0, 3, 6, 9)
    square_check(3, 6, 0, 3)
    square_check(3, 6, 3, 6)
    square_check(3, 6, 6, 9)
    square_check(6, 9, 0, 3)
    square_check(6, 9, 3, 6)
    square_check(6, 9, 6, 9)

#COMPROBAMOS EL CONTADOR_OK QUE CREAMOS AL PRINCIPIO. EN UN PRINCIPIO LO DEFINIMOS
#COMO TRUE, SI ALGUN CHECKEO DE LINEAS, COLUMNAS O CUADRICULAS NO ES OK PARA
#EL SUDOKU, ESTA VARIABLE SE VUELVE FALSE.
#CHECKEAMOS, SI ES FALSE, LOS NUMEROS NO VALES Y VICEVERSA.

    if counter_ok == True:
        print('estos numeros forman un sudoku correcto!!')
    else:
        print('estos numeros no solucionan un sudoku ceporro!!')

