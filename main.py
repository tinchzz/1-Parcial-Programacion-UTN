from procesamiento import cargar_Alumnos, mostrar_Alumnos

salir = True

while salir == True:
    opcion = int(input("===== NOTAFÁCIL ===== \n" 
    "1. Cargar alumnos \n" 
    "2. Mostrar listado \n" 
    "3. Mostrar estadísticas \n" 
    "4. Ver ranking (ordenado) \n" 
    "5. Buscar alumno \n" 
    "6. Juegos con un nombre \n" 
    "0. Salir: "))



    match(opcion):
        case 1:
            nombres, notas1, notas2, promedios = cargar_Alumnos()
        case 2:
            mostrar_Alumnos(nombres)
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 0:
            salir = False
        case _:
            print("Opcion Inválida")
            
    



