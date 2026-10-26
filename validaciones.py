def cantidad_alumnos():
    validez = False
    while not validez:
        cantidad_alumnos = input("Ingresar cantidad de alumnos: ")
        if len(cantidad_alumnos) > 0:
            validez = True
            for caracter in cantidad_alumnos:
                if "0" <= caracter <= "9":
                    continue
                else:
                    print("Caracter no numerico")
                    validez = False
                    break
            if validez:
                cantidad_alumnos = int(cantidad_alumnos)  
                if cantidad_alumnos > 0:
                    validez = True
                else:
                    print("Ingresar un número mayor que 0")
                    validez = False  
    return cantidad_alumnos

def alumno_valido():
    validez = False

    while not validez:
        nombre_alumno = input("Ingresar nombre de alumno. Debe contener minimo 5 caracteres. Solo letras (a-z, A-Z) y espacios: ")

        if len(nombre_alumno) >= 5:
            for caracter in nombre_alumno:
                if "a" <= caracter <= "z" or "A" <= caracter <= "Z" or caracter == " ":
                    validez = True
                else:
                    print("Nombre con caracteres invalidos")
                    validez = False
                    break
        else:
            print("Nombre con menos de 5 caracteres")
            validez = False

    return nombre_alumno



def validacion_nota(nota):
    validez = False
    cual_nota = nota

    while not validez:
        if cual_nota == "primera":
            nota_alumno = int(input("Nota primer parcial: "))
        else:
            nota_alumno = int(input("Nota segundo parcial: "))
        if 0 <= nota_alumno <= 10:
            validez = True
        else:
            validez = False
            
    
    return nota_alumno



def hay_alumnos(nombres):
    if len(nombres) == 0:
        print("No hay alumnos cargados. Cargar alumnos primero.")
        return False
    else:
        return True

