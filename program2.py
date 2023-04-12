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
#    celToFar2 (x)

""" Escribir una función que dado un número entero devuelva 1 si el mismo
es impar y 0 si fuera par. """

def pair():
    x = int(input('Ingrese un número: '))
    y = x % 2
    print(str(y))
        

# pair()

""" Escribir una función que dado un número entero devuelva 0 si el mismo es impar y 1 si
fuera par. """

def pair2():
    x = int(input('Ingrese un número: ')) % 2
    if x == 0:
        print(1)
    else:
        print(0)

# pair2()

""" Escribir una función que dado un número entero devuelva el dígito de las unidades. Por
ejemplo, para 153 debe devolver 3."""

def units():
    x = int(input('Número: '))
    unit = x % 10
    print(unit)

# units()

""" Escribir una función que dado un número devuelva el primer número múltiplo de 10
inferior a él. Por ejemplo, para 153 debe devolver 150. """

def rounder():
    x = int(input('Número: '))
    unit = (x // 10) * 10
    print(unit)
    
# rounder()

""" Escribir un programa que imprima todos los números pares entre dos números
que se le pidan al usuario. """

def pairer(x,y):
    for z in range(x,y+1):
        if z % 2 == 0:
            print(z)

# pairer(int(input('Número: ')),int(input('Número: ')))

""" Escribir un programa que le pregunte al usuario un número N e imprima los
primeros N números triangulares, junto con su índice. Los números triangulares se obtienen
mediante la suma de los números naturales desde 1 hasta n: """ 

def triangular():
    tri = int(input('Ingrese un número para conocer los X primeros números triángulares: '))
    for x in range(1,tri+1):
        n = str(round((x**2+x) / 2))     
        print(str(x) + " - " + n)

# triangular()

""" Escribir un programa que tome una cantidad m de valores ingresados por el
usuario, a cada uno le calcule el factorial e imprima el resultado junto con el número 
de orden correspondiente. """

def factorial(x):
    fact=1
    for y in range(1,x+1):
        fact = fact * y
    return fact

def factorials():
    n = int(input('Ingrese la cantidad de números a calcular su factorial: '))
    for x in range(n):
        f = int(input('Factorial de: '))
        result = factorial(f)
        print(f,'-',result)

# factorials()


""" Escribir un programa que imprima por pantalla todas las fichas de dominó, de
una por línea y sin repetir. """

def imprimir_fichas_domino():
    for i in range(7):
        for j in range(i,7):
            print(i,"/",j,end=" | ")
        print()

# imprimir_fichas_domino()

""" Modificar el programa anterior para que pueda generar fichas de un juego que
puede tener números de 0 a n. """

def imprimir_custom_domino():
    n = int(input('Cantidad de fichas: '))
    for i in range(n+1):
        for j in range(i,n+1):
            print(i,"/",j,end=" | ")
        print()

# imprimir_custom_domino()