
#clase
#contenedor donde vamos a almacenar diferentes clases. Tambien modelo para crear otros objetos, o clases.
from typing import Any


class Auto:
    marca = '' #creo los atributos de la clase 
    modelo = 0
    placa = ''
taxi = Auto() #creo el objeto que contiene la clase.
# imprimo (objeto.atributo_de_la_clase)
print(taxi.modelo)

#////////////////////////////////////////////////////

#Clases y objetos II

class Persona:
    doctor = 'Christian'
print(Persona.doctor)

class nombre:
    pass

victor = nombre()
maria  = nombre()

#objeto.atributo = valor
victor.edad = 30
victor.sexo = 'masculino' 
victor.pais = 'bolivia'

maria.edad = 30
maria.sexo = 'femenino'
maria.pais = 'Colombia'

print(maria.edad)
print(victor.sexo)

#////////////////////////////////////////////////////////////

#METODO
#Determinar una accion o un comportamiento. 

#CLASS nombre_clase:
#   DEF nomre_del_metodo(SELF)
#SELF.nombre_de_la_variable = algoritmo
#forma 1
class matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 3
s = matematica()
s.suma()
print(s.n1 + s.n2)

#forma 2
#__init__(SEFT) (iniciar)

class calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1- n2
        self.producto = n1 * n2
        self.division = n1 / n2
operacion = calculadora(2,3)
print(operacion.suma) 

#//////////////////////////////////////////
#funciones para atributos.

#getattr

class persona:
    edad = 27
    nombre = 'victor'
doctor = persona()
print(doctor.edad)
print(getattr(doctor, 'edad')) #sacar valores de atributos.

#hasattr

class persona:
    edad = 27
    nombre = 'victor'
doctor = persona()
print("el doctor tiene una edad", hasattr(doctor, 'edad')) #identificar si hay un atributo dentro de una clase.

#setattr

class persona:
    edad = 27
    nombre = 'victor'
doctor = persona()
print(doctor.nombre)
setattr(doctor, 'nombre', 'christian') #cambia el valor de un atributo por el de otro.
print(doctor.nombre) 

#delattr

class persona:
    edad = 27
    nombre = 'victor'
    pais = 'brazil'
doctor = persona()
delattr(persona, 'pais') #elimina un atgributo de la clase.
print(doctor.nombre)

#//////////////////////////////////////////////////////////////////////

#CONSTRUCTORES.
#los metodos en una clase comienzan con un gion bajo doble,. esto quiere decir que estra fucnion tiene una relacion 
# especial, que tiene un significado distinto
#__init__() = constructor

class persona:
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
    def descripcion(self):
        return ' {} tiene {}'.format(self.nombre, self.año)
    def comentario(self, frase):
        return '{} dicce {} '.format(self.nombre, frase)
doctor = persona('chris', '23')
print(doctor.descripcion())
print(doctor.comentario("lucho lo chupa mucho")) 

#modificar un atributo
class email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

s = email
print(s.enviado)

