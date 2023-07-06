import os
import time
os.system('cls')
opcion = ''
numero = 0
efectivo =''
total = 0
#entrada de datos y menu de compra
for x in range(4):
    print ("\tPlasTic")
    print (f'''
                |==================================MENU DE OPCIONES=====================================|
                |Producto                | Valor Unitario    | Cantidad min. mayorista | Valor mayorista|
                |1.- tazon               | $500              | 100 unidades            | $300           |
                |2.-llavero              | $200              | 300 unidades            | $150           |
                |3.- polera estampada    | $3000             | 50 unidades             | $2000          |
                |========================================================================================
                |forma de pago | descuento total de la compra |   Producto: {opcion}  metodo de pago: {efectivo}
                |efectivo      |  10%                         |   Cantidad: {numero}
                ==============================================
                ''')
    if x == 0:
        if opcion == '': 
            while True:
                opcion = (input('Producto: ')).upper()
                if opcion != 'TAZON' and opcion != 'LLAVERO' and opcion != 'POLERA ESTAMPADA':
                    print ('dato incorrecto')
                else:
                    break
            os.system('cls')
    if x == 1:
        if numero == 0:
            while True:
                numero = int (input('Ingrese Cantidad: '))
                if numero < 0:
                    print ('dato incorrecto')
                else:
                    break
            os.system('cls')
    if x == 2:
        if efectivo == '':
            while True:
                efectivo = (input('metodo de pago: (efectivo u otros) ')).upper()
                if efectivo != 'EFECTIVO' and efectivo != 'OTROS':
                    print ('dato incorrecto')
                else:
                    os.system('cls')
                    break
    if x == 3:
        print('Presione enter para imprimir boleta')
        input()
        break

os.system('cls')
#animacion 
a = 'imprimiendo boleta'
c = 0
for x in range (26):
    print(f'{a} {x * 4}%')
    if c == 3:
        a = a[:-3]
        c = 0
    else:    
        a += '.'
        c += 1
    time.sleep(0.2)
    os.system('cls')

#calculamos valor del total
if opcion != 'TAZON':
    if opcion != 'LLAVERO': 
        if numero >= 50:
            total = numero * 2000
        else:
            total = numero * 3000
    else:
        if numero >= 300:
            total = numero * 150
        else:
            total = numero *200
else:
    if numero >= 100:
        total = numero * 300
    else:
        total = numero * 500

#imprimimos boleta
if efectivo == 'EFECTIVO':
    print(f''' 
    ========================BOLETA========================
                         -------------
                        |   PLASTIC   |
                         -------------

    -> PRODUCTO = {opcion}

    -> CANTIDAD = {numero}
                                |TOTAL = {total} |
    Medio de pago = {efectivo}
    ----------------------------------------------
    |Forma de pago | descuento total de la compra |
    |efectivo      |  10%                         |
    ----------------------------------------------

                            |SUBTOTAL = {total} 
                            |DESCUENTO = {total * 0.1} 
                            |TOTAL = {total * 0.9} 
     ---------------------------------------------------
    |####################################################|
    |####################################################|
    |####################################################|
    |####################################################|
     ----------------------------------------------------
    ========================================================
    ''')
else:
    print(f''' 
    ========================BOLETA========================
                         -------------
                        |   PLASTIC   |
                         -------------
    
    -> PRODUCTO = {opcion}

    -> CANTIDAD = {numero}
                                |TOTAL = {total} |
    Medio de pago = {efectivo}
                                |TOTAL = {total} |

     ---------------------------------------------------
    |####################################################|
    |####################################################|
    |####################################################|
    |####################################################|
     ----------------------------------------------------
    ========================================================
    ''')