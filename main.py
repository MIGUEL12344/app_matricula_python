"""- registrar alumnos.
- generar fichas de matricula
- mostrar la lista de todos los matriculados
- filtrar matriculados por programa de estudio """
#lista alumnos 
lista_alumnos=[]
while True:
    nombre=input("ingrese el nombre: ")
    apellido=input("ingrese el apellido: ")
    opcion=input("desea seguir añadiendo? s/n-> ")
    if opcion == "s":
        lista_alumnos.append({"nombre":nombre,"apellido":apellido})
    for alumnos in lista_alumnos:
        print(alumnos)