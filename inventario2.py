codigoInt = int(input('Codigo'))
nombreStr = input('Nombre')
existenciasInt = 0
controBln = True
import os
while controBln == True:
    os.system('cls') 
    print ('Codigo: ', codigoInt, '\nNombre: ', nombreStr, '\nExistencias: ', existenciasInt)
    opcionStr = input('1. compras\n2. ventas\n3. Reportes\n-> ')
    cantidadInt = int(input('cantidad: '))
    if opcionStr == '1':
        existenciasInt += cantidadInt
    if opcionStr == '2':
        if cantidadInt <= existenciasInt:
           existenciasInt -= cantidadInt
    else:
        print('\nNo hay suficientes existencias')
    enter = input('<Enter>')
if opcionStr == '3':
        print('Cantidad actual de inventario:', existenciasInt)
if opcionStr == '4':
        controBln = False