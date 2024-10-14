"""- registrar alumnos.
- generar fichas de matricula
- mostrar la lista de todos los matriculados
- filtrar matriculados por programa de estudio """
#lista alumnos 
lista_alumnos=[]
def vienvenida():
    print("""\n         ___¡VIENVENIDO!___
:::REALIZE LA MATRICULA DEL ALUMNO:::\n""")
def ingresar_datos_alumno():
    id=len(lista_alumnos)+1
    cui=int(input("ingrese dni: "))
    nombre=input("ingrese el nombre: ")
    apellido=input("ingrese el apellido: ")
    numero_celular=int(input("ingrese numero de celular: "))
    programa_estudio=input("ingrese el programa de estudio: ")
    ciclo_academico=input("ingrese su ciclo academico: ")
    email=input("ingrese su correo electronico: ")
    guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email)
def guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email):
    lista_alumnos.append({"id":id,"cui":cui,"nombre":nombre,"apellido":apellido,"numero_celular":numero_celular,"programa_estudio":programa_estudio,"ciclo_academico":ciclo_academico,"email":email})
def ordenar_lista():
    for alumnos in lista_alumnos:
        print(alumnos)
while True:
    vienvenida() 
    ingresar_datos_alumno()
    opcion=input("desea seguir añadiendo? s/n-> ")
    if opcion.lower() != "s":
        break
ordenar_lista()