'''
Scenario
Imagine that you receive a task description of an application that monitors the process of apple packaging before the apples are sent to a shop.

A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.

Write a code that creates objects representing apples as long as both limitations are met. When any limitation is exceeded, than the packaging process is stopped, and your application should print the number of apple class objects created, and the total weight.

Your application should keep track of two parameters:

the number of apples processed, stored as a class variable;
the total weight of the apples processed; stored as a class variable. Assume that each apple's weight is random, and can vary between 0.2 and 0.5 of an imaginary weight unit;
'''

import random

class Apple(object):
    
    def __init__(self):
        self.weight = random.uniform(0.2, 0.5)


class Packing(object):
    total_weight = 0
    quantity = 0
    
    def __init__(self, units_to_deliver: int):
        
        self.box =[]
        self.units_to_deliver = units_to_deliver
        
    def make_pack(self):
        
        while (Packing.total_weight <= 300.0) and (Packing.quantity <= self.units_to_deliver):
            new_apple = Apple()
            self.box.append(new_apple)
            Packing.total_weight += new_apple.weight
            Packing.quantity += 1
        
        if Packing.total_weight > 300:
            self.box.pop()
        
        Packing.total_weight = 0
        Packing.quantity = 0
        
        for apple in self.box:
            Packing.total_weight += apple.weight
            Packing.quantity += 1
                
        print(
            f'''
La cantidad total de manzanas entregadas sera de {Packing.quantity} manzanas.
El peso total del p6edido es de {Packing.total_weight} kg.
            ''')
        
pedido1 = Packing(1000)
pedido1.make_pack()        
        
    