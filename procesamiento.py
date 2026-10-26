from validaciones import alumno_Valido, validacion_Primer_Nota, validacion_Segunda_Nota, cantidad_Alumnos


def cargar_Alumnos():
    alumnos = cantidad_Alumnos()

    nombre_Alumnos = [""] * alumnos
    notas_Parcial1 = [0] * alumnos
    notas_Parcial2 = [0] * alumnos 
    promedio_Alumnos = [0] * alumnos 
    
    for i in range(alumnos):
        
        nombre_Alumnos[i] = alumno_Valido()

        notas_Parcial1[i] = validacion_Primer_Nota()

        notas_Parcial2[i] = validacion_Segunda_Nota()

        promedio_Alumnos[i] = (notas_Parcial1[i] + notas_Parcial2[i])/2

    return nombre_Alumnos, notas_Parcial1, notas_Parcial2, promedio_Alumnos

def mostrar_Alumnos(nombres, notas1, notas2, promedios):
    pass


def mostrar_Estadisticas(nombres, promedios):
    pass


def ver_Ranking():
    pass


def buscar_Alumno(nombres, notas1, notas2, promedios):
    pass

def juegos_Nombre():
    pass
        





