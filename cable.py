import sys
import math
import time
import random

def Alambre():
	print '\n\tResistencia en un Alambre\n'
	print 'Resistencia = Ohms'
	print 'Resistividad = Ohms'
	print 'Longitud = cm'
	print 'Area = cm**2'
	print '\n'

	P = float(raw_input("Ingrese la Resistividad: "))
	L = float(raw_input("Ingrese la Longitud del Cable: "))
	A = float(raw_input("Ingrese Area del Cable: "))

	Resistividad = []
	Longitud = []
	Area = []
	Resistencia = []

	R = (P*L/A)


	Resistividad.append(P)
	Longitud.append(L)
	Area.append(A)
	Resistencia.append(R)

	print '\n'

	sep ='|{}|{}|{}|{}|'.format('-'*15,'-'*17,'-'*9,'-'*21)
	print('{0}\n| Resistividad  |    Longitud     |  Area   |     Resistencia     |\n{0}'.format(sep))
	for Resistividad,Longitud,Area,Resistencia in zip(Resistividad,Longitud,Area,Resistencia):
		print ('| {:>13.2f} | {:>15.2f} | {:>7.2f} | {:>19.2f} |\n{}'.format(Resistividad,Longitud,Area,Resistencia,sep))

def Voltaje():
	print '\n\tCalcular Voltaje\n'
	print 'Resistencia = Ohms'
	print 'Corriente = Amperios'
	print 'Voltaje = Volts'
	print '\n'
	R = float(raw_input("Ingrese la Resistencia: "))
	I = float(raw_input("Ingrese la Corriente: "))
	
	Resistencia = []
	Corriente = []
	Voltaje = []

	V = (R*I)


	Resistencia.append(R)
	Corriente.append(I)
	Voltaje.append(V)

	print '\n'


	sep ='|{}|{}|{}|'.format('-'*14,'-'*18,'-'*12,)
	print('{0}\n| Resistencia  |    Corriente     |  Voltaje   |\n{0}'.format(sep))
	for Resistencia,Corriente,Voltaje in zip(Resistencia,Corriente,Voltaje):
		print ('| {:>12.2f} | {:>16.2f} | {:>10.2f} | \n{}'.format(Resistencia,Corriente,Voltaje,sep))

def Corriente():
	print '\n\tCalcular Corriente\n'
	print 'Resistencia = Ohms'
	print 'Corriente = Amperios'
	print 'Voltaje = Volts'
	print '\n'

	V = float(raw_input("Ingrese el Voltaje: "))
	R = float(raw_input("Ingrese la Resistencia: "))
	
	Resistencia = []
	Corriente = []
	Voltaje = []

	I = (V/R)


	Resistencia.append(R)
	Corriente.append(I)
	Voltaje.append(V)

	print '\n'

	sep ='|{}|{}|{}|'.format('-'*10,'-'*20,'-'*14,)
	print('{0}\n| Voltaje  |    Resistencia     |  Corriente   |\n{0}'.format(sep))
	for Voltaje,Resistencia,Corriente in zip(Voltaje,Resistencia,Corriente):
		print ('| {:>8.2f} | {:>18.2f} | {:>12.2f} | \n{}'.format(Voltaje,Resistencia,Corriente,sep))

def Resistencia():
	print '\n\tCalcular Resistencia\n'
	print 'Resistencia = Ohms'
	print 'Corriente = Amperios'
	print 'Voltaje = Volts'
	print '\n'

	V = float(raw_input("Ingrese el Voltaje: "))
	I = float(raw_input("Ingrese la Corriente: "))
	
	Resistencia = []
	Corriente = []
	Voltaje = []

	R = (V/I)


	Resistencia.append(R)
	Corriente.append(I)
	Voltaje.append(V)

	print '\n'


	sep ='|{}|{}|{}|'.format('-'*10,'-'*18,'-'*16,)
	print('{0}\n| Voltaje  |    Corriente     |   Resistencia  |\n{0}'.format(sep))
	for Voltaje,Corriente,Resistencia in zip(Voltaje,Corriente,Resistencia):
		print ('| {:>8.2f} | {:>16.2f} | {:>14.2f} | \n{}'.format(Voltaje,Corriente,Resistencia,sep))
def menu():

	"""

	Funcin que limpia la pantalla y muestra nuevamente el menu

	"""
	print ("\n\tSeleccionar una opcion")

	print ("\t1.- Resistencia en un Alambre ")

	print ("\t2.- Voltaje")

	print ("\t3.- Corriente")

        print ("\t4.- Resistencia")

	print ("\t5.- salir")


while True:

	# Mostramos el menu

	menu()

	# solicituamos una opcin al usuario

	opcionMenu = int (raw_input("\n\tOpcion:"))

 	if (opcionMenu==1):
		Alambre()
	if (opcionMenu==2):
		Voltaje()
 	if (opcionMenu==3):
		Corriente()
	if (opcionMenu==4):
		Resistencia()
        if (opcionMenu==5):
               break


