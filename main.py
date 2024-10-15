from welcome_function import vienvenida
from input_student_data import ingresar_datos_alumno
from save_student_data import guardar_datos_alumno
from sort_list import ordenar_lista

# Inicializa la lista de alumnos
lista_alumnos = []
# creo mi bucle 
while True:
    #inserto mi funcion vienvenida
    vienvenida() 
    # actualizo mi lista vacia
    lista_alumnos = ingresar_datos_alumno(lista_alumnos)
    # opcion de seguir añadiendo
    opcion = input("¿Desea seguir añadiendo? s/n -> ")
    if opcion.lower() != "s":
        break
# funcion para ordenar lista en filas separadas
ordenar_lista(lista_alumnos)

