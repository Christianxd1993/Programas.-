import os
import time
# ----------- variables ----------
opcion = ""  # selección del usuario
tipo_entrada = ""  # --> Tribuna, Galeria o Cancha
valor_entrada = 0
cantidad = 0
tiene_descuento = False
total = 0
# ---variables estadísticas --
cant_ventas = 0
monto_galeria, monto_tribuna, monto_cancha = 0, 0, 0
cant_ventas_con_descuento = 0
# --------- Código Principal ---------
while True:
    os.system("cls")
    opcion = str(input('''
    --------- MENÚ ----------
    1.- Realizar comprar de entradas
    2.- Ver estadísticas
    3-. Salir                     
    \nElija opción:  '''))

    if opcion == "1":
        os.system("cls")
        print("-------- REALIZAR COMPRA --------")
        opcion_entrada=str(input('''
           Tipo Entrada \t Valor Entrada
        1.- Galeria \t $20000
        2.- Tribuna \t $35000
        3.- Cancha \t $30000
        \nElija opción:  '''))
        
        if opcion_entrada=="1":
            tipo_entrada="Galeria"
            valor_entrada=20000
        elif opcion_entrada=="2":
            tipo_entrada="Tribuna"
            valor_entrada=35000
        else:
            tipo_entrada="Cancha"
            valor_entrada=30000
                                    
        cantidad=int(input(f'''
        ¿Qué cantidad de {tipo_entrada} desea? '''))
        while not cantidad>0:
            print("Error, no puede ser negativo")
            cantidad=int(input(f'''
            ¿Qué cantidad de {tipo_entrada} desea? '''))
            
        total= valor_entrada*cantidad
        print(f"--> subtotal ${total}")
        
        opcion_descuento=str(input('''
            ¿Tiene descuento? S/N ''')).upper()
        if opcion_descuento=="S":
            tiene_descuento=True
        else:
            tiene_descuento=False
            
        if tiene_descuento and tipo_entrada=="Galeria":
            total*=0.90
        if tiene_descuento and tipo_entrada=="Tribuna":
            total*=0.95
        if tiene_descuento and tipo_entrada=="Cancha":
            total*=0.95
               
        os.system("cls")                
        print(f'''
            ------------ TICKET DE COMPRA --------
            Tipo entrada: {tipo_entrada}
            ${valor_entrada} X {cantidad} = {total} ''')              
        os.system("pause")
        
        # --------------------  Analisis para las estadísticas  -----------------------------------------------
        # Ya en este punto de ejecución, se esta finalizando la compra, todas las
        # variables están con la información final. Analizaremos los datos, es decir,
        # veremos como serán manejadas las variables de tipo contador y acumulador
        
        cant_ventas+=1  #---> se finaliza compra se incrementa en uno el contador de ventas
        
        # ahora vamos a analizar los monto obtenidos por cada tipo de entrada
        if tipo_entrada.upper()=="GALERIA":
            monto_galeria+=total
            
        if tipo_entrada.upper()=="TRIBUNA":
            monto_tribuna+=total
            
        if tipo_entrada.upper()=="CANCHA":
            monto_cancha+=total
            
        # Ahora vamos a incrementar la ventas realizadas con descuento
        if tiene_descuento:
            cant_ventas_con_descuento+=1            
        
        
    if opcion=="2":        
        os.system("cls")
        print(f'''
                __                              
                |_  _ _|_ _  _| _ _|_ o  _  _  _ 
                |___>  |_(_|(_|_>  |_ | (_ (_|_>       
        =================================================
        Cantidad de ventas: {cant_ventas}
        Monto por ventas de Galeria ${monto_galeria}
        Monto por ventas de Tribuna ${monto_tribuna}
        Monto por ventas de Cancha ${monto_cancha}
        
        Cant. ventas con descuento: {cant_ventas_con_descuento}                          
              ''')
        
        os.system("pause")
        
        
    if opcion == "3":
        os.system("cls")
        print("...cerrando app")
        time.sleep(1)
        break
