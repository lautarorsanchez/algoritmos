""" 1. Muestra un mensaje de bienvenida por pantalla.
2. Le pide al usuario que introduzca dos números enteros n1 y n2.
3. Imprime el cuadrado de todos los números enteros del intervalo [n1, n2).
4. Muestra un mensaje de despedida por pantalla. """

def sum_square(x,y):
    for z in range(x,y+1):
        print('El cuadrado de ' + str(z) + ' es ' + str(z*z))

def main():
    print('¡Hola usuario! Ingrese 2 números para conocer los cuadrados de los números en ese intervalo')
    a = int(input('Ingrese primer numero: '))
    b = int(input('Ingrese segundo número: '))
    sum_square(a,b)
    print('¡Chau usuario!')

main()

    