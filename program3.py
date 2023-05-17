import math 

""" Escribir una función repite_hola que reciba como parámetro un número entero
n y escriba por pantalla el mensaje "Hola" n veces. Invocarla con distintos valores de n. """


def repite_hola(int):
    for x in range(0, int):
        print('Hola')

# repite_hola(10)


""" Escribir otra función repite_hola que reciba como parámetro un número entero n
y devuelva la cadena formada por n concatenaciones de "Hola". Invocarla con distintos valores
de n. """


def repite_hola(int):
    print('Hola ' * int)

# repite_hola(10)


""" Escribir una función repite_saludo que reciba como parámetro un número entero
n y una cadena saludo y escriba por pantalla el valor de saludo n veces. Invocarla con distintos
valores de n y de saludo. """


def repite_saludo(int: int, greet: str):
    for x in range(0, int):
        print(greet)

# repite_saludo(10,'hola mundo')


""" Escribir otra función repite_saludo que reciba como parámetro un número entero
n y una cadena saludo devuelva el valor de n concatenaciones de saludo. Invocarla con distintos
valores de n y de saludo. """


def repite_saludo(int: int, greet: str):
    print(greet * int)

# repite_saludo(5,' hola')


""" Corregir el programa para que: 
• Informe el costo en pesos y centavos, en lugar de un número decimal.
• Informe cuál fue el total facturado en la corrida. """


def main():
    p = float(input("¿Cuánto cuesta 1 segundo de comunicacion?: "))
    n = int(input("¿Cuántas comunicaciones hubo?: "))
    total = 0
    for x in range(n):
        h = int(input("¿Cuántas horas?: "))
        m = int(input("¿Cuántos minutos?: "))
        s = int(input("¿Cuántos segundos?: "))
        duracion = a_segundos(h, m, s)
        costo = duracion * p
        costo_pesos = round((duracion * p) // 1)
        costo_centavos = round(((duracion * p) % 1)*100)
        total += costo
        print("Duracion de llamada", x+1, ':', duracion, "segundos. Costo:",
              costo_pesos, 'pesos y', costo_centavos, 'centavos.')
    if (x == 0):
        print('Valor total de', x+1, 'comunicacion: $', total)
    else:
        print('Valor total de', x+1, 'comunicaciones: $', total)


def a_segundos(horas, minutos, segundos):
    return 3600 * horas + 60 * minutos + segundos

# main()


""" Escribir dos funciones que permitan calcular:
a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
b) La duración en horas, minutos y segundos de un intervalo dado en segundos. """

# a)


def to_secs():
    h = int(input('Horas:'))
    m = int(input('Minutos:'))
    s = int(input('Segundos:'))
    secs = h*60*60+m*60+s
    return secs

# x = to_secs()
# print(x)

# b)


def to_time(sec):
    h = str(sec // 3600)
    m = str((sec % 3600) // 60)
    s = str((sec % 3600) % 60)
    return h, m, s

# time = to_time(3672)
# print('H:'+time[0]+' M:'+time[1]+' S:'+time[2])


""" Usando las funciones del ejercicio anterior, escribir un programa que pida al
usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y mues-
tre por pantalla la duración total en horas, minutos y segundos. """

def to_secs2():
    h = int(input('Horas:'))
    m = int(input('Minutos:'))
    s = int(input('Segundos:'))
    secs = h*60*60+m*60+s
    return secs

# time1 = to_secs2()
# time2 = to_secs2()

def sum_time(t1, t2):
    total = t1 + t2
    return total

# time3 = sum_time(time1,time2)

def to_time(total):
    h = str(total // 3600)
    m = str((total % 3600) // 60)
    s = str((total % 3600) % 60)
    return h, m, s

# time = to_time(time3)

# print('H:'+time[0]+' M:'+time[1]+' S:'+time[2])

""" Escribir una función que, dados cuatro números, devuelva el mayor producto
de dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto
más grande que se puede obtener entre ellos (8 = −2 × −4). """

def maxProduct(a,b,c,d):
    prod1 = a * b
    prod2 = a * c
    prod3 = a * d
    prod4 = b * c
    prod5 = b * d
    prod6 = c * d
    maxproduct = max([prod1, prod2, prod3, prod4, prod5, prod6])
    return maxproduct

# print(maxProduct(1,-10,5,-7))

""" Escribir una función que reciba las coordenadas de un vector en R3 (x,y,z) y devuelva
la norma del vector """

def normaVector(x,y,z):
    num1 = x**2
    num2 = y**2
    num3 = z**2
    sum = num1 + num2 + num3
    norma = math.sqrt(sum)
    return norma

# print(normaVector(3,2,-4))
