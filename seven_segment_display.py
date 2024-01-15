

numbers = [['###','# #','# #','# #','###'],['  #','  #','  #','  #','  #'],
           ['###','  #','###','#  ','###'],['###','  #','###','  #','###'],
           ['# #','# #','###','  #','  #'],['###','#  ','###','  #','###'],
           ['###','#  ','###','# #','###'],['###','  #','  #','  #','  #'],
           ['###','# #','###','# #','###'],['###','# #','###','  #','###']]

def seven_digits():
    while True:
        try:
            num = input('intruduce los numeros(no negativos):')
            if int(num) < 0:
                print('he dicho que no valen numeros negativos!!')
                continue
            break
        except ValueError:
            print('Tiene que ser un numero idiota!')
        
    for line in range(5):
        for number in str(num):
            print(numbers[int(number)][line], end = ' ')
        print()

seven_digits()
