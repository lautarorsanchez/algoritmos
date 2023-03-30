""" Escribir un ciclo definido para imprimir por pantalla todos los números entre 10 y 20. """
def counter():
    for x in range(10,20+1):
        print(x)

# counter()

""" Escribir un ciclo definido que salude por pantalla a sus cinco mejores amigos/as. """

def greeter():
    friends=['Angela','María','Roberto','Miguel','Selena']
    for x in range(5):
        print(friends[x])

# greeter()

""" Escribir un programa que use un ciclo definido con rango numérico, que pregunte los
nombres de sus cinco mejores amigos/as, y los salude. """

def greeter2():
    friends=[]
    for x in range(5):
        friends.append(input('Nombre a un amigo/a: '))
    for y in range(5):
        print('Hola ' + friends[y])

# greeter2()

""" Escribir un programa que use un ciclo definido con rango numérico, que averigue a
cuántos amigos quieren saludar, les pregunte los nombres de esos amigos/as, y los salude. """

def greeter3(ammount):
    friends=[]
    for x in range(ammount):
        friends.append(input('Nombre a un amigo/a: '))
    for y in range(ammount):
        print('Hola ' + friends[y])

# greeter3(int(input('Ingrese cuantos amigos quiere saludar: ')))

""" Escribir una función que reciba una cantidad de pesos, una tasa de interés y un
número de años y devuelva el monto final a obtener. La fórmula a utilizar es:  Cn = C × (1 + x
100)**n Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular."""

def finance():
    months = int(input('Cuantos meses desea ingresar su dinero:'))
    money = int(input('Cuanto dinero desea ingresar:'))
    interest = int(input('Tasa de interés:'))
    total = money * (1 + (interest / 100))**months
    totalRound = round(total)
    return str(totalRound)

# print('Usted recibirá: ' + finance())

""" Escribir una función que convierta un valor dado en grados Fahrenheit a grados
Celsius. """

def celToFar(f):
    c = (int(f) - 32) / (9/5)  
    floated = round(c,2)
    print('Celcius: ' + str(floated))


# celToFar(input('Farenheit: '))

""" Escribir un programa que utilice la función anterior para generar una tabla de
conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10. """
def celToFar2(f):
    c = (int(f) - 32) / (9/5)  
    floated = round(c,2)
    print('Celcius: ' + str(floated))

# for x in range(10, 120+1, 10):
#    celToFar2(x)

