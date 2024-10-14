"""- registrar alumnos.
- generar fichas de matricula
- mostrar la lista de todos los matriculados
- filtrar matriculados por programa de estudio """
#lista alumnos 
lista_alumnos=[]
while True:
    print("""\n         ___¡VIENVENIDO!___
:::REALIZE LA MATRICULA DEL ALUMNO:::\n""")
    nombre=input("ingrese el nombre: ")
    apellido=input("ingrese el apellido: ") 
    lista_alumnos.append({"nombre":nombre,"apellido":apellido})
    opcion=input("desea seguir añadiendo? s/n-> ") 
    if opcion.lower() != "s":
        break
for alumnos in lista_alumnos:
    print(alumnos)