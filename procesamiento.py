from validaciones import alumno_valido, validacion_primer_nota, validacion_segunda_nota, cantidad_alumnos


def cargar_alumnos():
    alumnos = cantidad_alumnos()

    nombre_alumnos = [""] * alumnos
    notas_parcial1 = [0] * alumnos
    notas_parcial2 = [0] * alumnos 
    promedio_alumnos = [0] * alumnos 
    
    for i in range(alumnos):
        
        nombre_alumnos[i] = alumno_valido()

        notas_parcial1[i] = validacion_primer_nota()

        notas_parcial2[i] = validacion_segunda_nota()

        promedio_alumnos[i] = (notas_parcial1[i] + notas_parcial2[i])/2

    return nombre_alumnos, notas_parcial1, notas_parcial2, promedio_alumnos

def mostrar_alumnos(nombres):
    for i in range(len(nombres)):
        print(f"ID: {i} - Nombre: {nombres[i]}")


def mostrar_estadisticas(nombres, promedios):
    for i in range(len(promedios)):
        promedio_general += promedios[i] 
    promedio_general = promedio_general / len(promedios)


    return promedio_general



def ver_ranking():
    pass


def buscar_alumno(nombres, notas1, notas2, promedios):
    pass

def juegos_nombre():
    pass
        





