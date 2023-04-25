#importaciones a utilizar en el proyecto sprint

import random
import string

#Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
def crear_cuenta(id,nombre_paciente):
    nombre_usuario = nombre_paciente.replace(" ", "").lower()

# crear pass y criterios de validacion
    longitud_contraseña = 8
    caracteres_contraseña = string.ascii_letters + string.digits
    while True:
#La contraseña debe ser creada con random y debe cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
      contraseña = ''.join(random.choice(caracteres_contraseña) for i in range(longitud_contraseña))
      if (any(c.islower() for c in contraseña)
            and any(c.isupper() for c in contraseña)
            and sum(c.isdigit() for c in contraseña) >= 1):
        break
    print("Se ha creado la cuenta para el paciente " + nombre_paciente + " con el nombre de usuario " + nombre_usuario + " y la contraseña " + contraseña)

#Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña. 
    cuentas.update({id:{"user":nombre_usuario, "pass": contraseña}})
  
clientes ={
  1:{"nombre": "Juan", "edad": 30},
  2:{"nombre": "María", "edad": 25},
  3:{"nombre": "Pedro", "edad": 40},
  4:{"nombre": "Ana", "edad": 35},
  5:{"nombre": "Carlos", "edad": 28},
  6:{"nombre": "Luisa", "edad": 42},
  7:{"nombre": "Diego", "edad": 27},
  8:{"nombre": "Lucía", "edad": 31},
  9:{"nombre": "Sofía", "edad": 23},
  10:{"nombre": "Miguel", "edad": 38},
}


cuentas = {}
#recorra una lista con los nombres de 10 de sus futuros usuarios de tu aplicación
for key,value in clientes.items():  
  nombre = value["nombre"]
  crear_cuenta(key,nombre)
  
#Por cada cuenta debe pedir un número telefónico para contactarse.
  contacto = input("Ingrese numero de contacto: ")
  while contacto != type(int) and len(contacto)!=8:
     contacto = input("Ingrese una numero de contacto valido de 8 digitos: ")

  contacto= str(contacto)
  clientes[key]["contacto"] = contacto
for key, value in clientes.items():        
  print(f"Usuario {key}: {cuentas[key]['user']} - Pass: {cuentas[key]['pass']} - Nombre: { clientes[key]['nombre']} - Contacto: {clientes[key]['contacto']}")        
