""" El usuario del tarifador nos pide ahora una modificación, ya que no es lo mismo
la tarifa por segundo de las llamadas cortas que la tarifa por segundo de las llamadas largas.
Al inicio del programa se informará la duración máxima de una llamada corta, la tarifa de las
llamadas cortas y la de las largas. Se deberá facturar con alguno de los dos valores de acuerdo
a la duración de la comunicación. """

def tarifador():
    print('Las llamadas cortas duran hasta 2 minutos y cuestan 10 centavos por segundo, las llamadas largas cuestan 12 centavos por segundo')
    n = int(input("¿Cuántas comunicaciones hubo?: "))
    total = 0
    p1 = 10
    p2 = 12
    for x in range(n):
        h = int(input("¿Cuántas horas?: "))
        m = int(input("¿Cuántos minutos?: "))
        s = int(input("¿Cuántos segundos?: "))
        duracion = a_segundos(h, m, s)
        if duracion <= 120:
            costo = duracion * p1
            costo_pesos = round((duracion * p1) // 1)
            costo_centavos = round(((duracion * p1) % 1)*100)
            total += costo
        else:
            costo = duracion * p2
            costo_pesos = round((duracion * p2) // 1)
            costo_centavos = round(((duracion * p2) % 1)*100)
            total += costo
        print("Duracion de llamada", x+1, ':', duracion, "segundos. Costo:",
              costo_pesos, 'pesos y', costo_centavos, 'centavos.')
    if (x == 0):
        print('Valor total de', x+1, 'comunicacion: $', total)
    else:
        print('Valor total de', x+1, 'comunicaciones: $', total)


def a_segundos(horas, minutos, segundos):
    return 3600 * horas + 60 * minutos + segundos

tarifador()