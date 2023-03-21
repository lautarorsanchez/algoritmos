import math

""" Escribir una función que reciba dos números y devuelva su producto. """
def multiply():
    print('Elija dos números para multiplicarlos entre si')
    x = int(input('Ingrese primer número: '))
    y = int(input('Ingrese segundo número: '))
    print('El resutlado es: ' + str(x * y))

""" Calcular el área de un rectángulo dada su base y su altura. """
def rectangle():
    print('Calcula el perímetro de un rectángulo según altura y ancho')
    x = int(input('Ingrese altura: '))
    y = int(input('Ingrese ancho: '))
    print('El perímetro es: ' + str((x + y)*2))

""" Calcular el perímetro de un círculo dado su radio. """
def circlePerimeter():
    print('Ingrese el radio del círculo para obtener su perimetro')
    x = int(input('Ingrese radio:'))
    print( 2* math.pi * x)

""" Calcular el area de un círculo dado su radio. """
def circleArea():
    print('Ingrese el radio del círculo para obtener su area')
    x = int(input('Ingrese radio:'))
    print( math.pi * x**2)

""" Calcular el volumen de una esfera dado su radio. """
def sphereVolume():
    print('Ingrese el radio de la esfera para obtener su volumen')
    x = int(input('Ingrese radio:'))
    print( 4/3 * math.pi * x**3)

""" Dados los catetos de un triángulo rectángulo, calcular su hipotenusa. """
def pitagoras():
    print('ingrese el largo de cada cateto para conocer el largo de la hipotenusa')
    x = int(input('primer cateto: '))
    y = int(input('segundo cateto: '))
    z = x**2 + y**2
    print('hipotenusa: ' + str(z**0.5))

""" Escribir una función que, dado un número entero n, permita calcular su facto-
rial. """
def factorial(x):
    fact=1
    for y in range(1,x+1):
        fact = fact * y
    return fact

# print(factorial(6))

""" Dados dos números, imprimir la suma, resta, división y multiplicación de ambos. """

def calculator(x,y):
    print(x + y)
    print(x - y)
    print(x / y)
    print(x * y)

# calculator(1,2)

""" Dado un número natural n, imprimir su tabla de multiplicar. """

def tablas(x):
    for i in range(1,10):
        print(x * i)

# tablas(2)

""" Escribir un programa que le pida una palabra al usuario, para luego imprimirla
1000 veces, en una única línea, con espacios intermedios. """

def inputx1000():
   x = input('salude: ')
   for i in range(1000):
        print(x, end=" ")

# inputx1000()



