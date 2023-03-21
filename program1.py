""" 1. Muestra un mensaje de bienvenida por pantalla.
2. Le pide al usuario que introduzca dos números enteros n1 y n2.
3. Imprime el cuadrado de todos los números enteros del intervalo [n1, n2).
4. Muestra un mensaje de despedida por pantalla. """

def sum_square(x,y):
    for z in range(x,y+1):
        print(z*z)

def main():
    print('Hello user!')
    a = int(input('insert first number: '))
    b = int(input('insert second number: '))
    sum_square(a,b)
    print('goodbye user!')

main()

    