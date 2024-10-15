from save_student_data import guardar_datos_alumno

def ingresar_datos_alumno(lista_alumnos):
    id=len(lista_alumnos)+1
    cui=int(input("ingrese dni: "))
    nombre=input("ingrese el nombre: ")
    apellido=input("ingrese el apellido: ")
    numero_celular=int(input("ingrese numero de celular: "))
    programa_estudio=input("ingrese el programa de estudio: ")
    ciclo_academico=input("ingrese su ciclo academico: ")
    email=input("ingrese su correo electronico: ")
    guardar_datos_alumno(lista_alumnos,id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email)
    return lista_alumnos