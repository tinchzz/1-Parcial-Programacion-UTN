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
    print("====== ALUMNOS DISPONIBLES ======")
    for i in range(len(nombres)):
        print(f"ID: {i} - Nombre: {nombres[i]}")


def mostrar_estadisticas(nombres, promedios):
    promedio_general = 0
    mejor_promedio = 0
    nombre_mejor_promedio = ""
    peor_promedio = 10
    nombre_peor_promedio = ""

    for i in range(len(promedios)):
        promedio_general += promedios[i] 

        
        if mejor_promedio < promedios[i]:
            mejor_promedio = promedios[i]
            nombre_mejor_promedio = nombres[i]

        
        if peor_promedio > promedios[i]:
            peor_promedio = promedios[i]
            nombre_peor_promedio = nombres[i]

    promedio_general = promedio_general / len(promedios)

    print("====== PROMEDIOS GENERALES, MEJOR Y PEOR ======")
    print(f"Promedio General: {promedio_general}")
    print(f"Mejor Promedio: {nombre_mejor_promedio} con {mejor_promedio}")
    print(f"Peor Promedio: {nombre_peor_promedio} con {peor_promedio}")


def ver_ranking(nombres, promedios):
    nombres_ranking = nombres.copy()
    promedios_ranking = promedios.copy()
    for i in range(len(promedios_ranking) - 1):
        for j in range(len(promedios_ranking) - 1 - i): 
            if promedios_ranking[j] < promedios_ranking[j+1]:
                aux = promedios_ranking[j + 1]
                promedios_ranking[j + 1] = promedios_ranking[j]
                promedios_ranking[j] = aux
                aux_nombre = nombres_ranking[j+1]
                nombres_ranking[j + 1] = nombres_ranking[j]
                nombres_ranking[j] = aux_nombre
                
    print("====== RANKING MAYOR A MENOR ======")
    for i in range(len(nombres_ranking)):
        
        print(f"{i + 1}. {nombres_ranking[i]} - Promedio: {promedios_ranking[i]}")


def buscar_alumno(nombres, notas1, notas2, promedios):
    pass

def juegos_nombre():
    pass
        





