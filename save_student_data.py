def guardar_datos_alumno(lista_alumnos, id, cui, nombre, apellido, numero_celular, programa_estudio, ciclo_academico, email):
    lista_alumnos.append({
        "id": id,
        "cui": cui,
        "nombre": nombre,
        "apellido": apellido,
        "numero_celular": numero_celular,
        "programa_estudio": programa_estudio,
        "ciclo_academico": ciclo_academico,
        "email": email
    })
