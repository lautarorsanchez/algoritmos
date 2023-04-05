""" Escribir una función repite_hola que reciba como parámetro un número entero
n y escriba por pantalla el mensaje "Hola" n veces. Invocarla con distintos valores de n. """

def repite_hola(int):
    for x in range(0,int):
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

def repite_saludo(int:int, greet:str):
     for x in range(0,int):
          print(greet)

# repite_saludo(10,'hola mundo')

""" Escribir otra función repite_saludo que reciba como parámetro un número entero
n y una cadena saludo devuelva el valor de n concatenaciones de saludo. Invocarla con distintos
valores de n y de saludo. """

def repite_saludo(int:int, greet:str):
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
        print("Duracion de llamada", x+1, ':' , duracion, "segundos. Costo:", costo_pesos, 'pesos y', costo_centavos, 'centavos.')
    if(x==0):
        print('Valor total de', x+1 , 'comunicacion: $' ,total)
    else:
        print('Valor total de', x+1 , 'comunicaciones: $' ,total)           

def a_segundos(horas, minutos, segundos):
    return 3600 * horas + 60 * minutos + segundos

# main()