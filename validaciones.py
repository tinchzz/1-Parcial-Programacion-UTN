def cantidad_Alumnos():
    cantidad_Alumnos = int(input("Ingresar cantidad de alumnos \n"))
    return cantidad_Alumnos

def alumno_Valido():
    validez = False

    while validez == False:
        nombre_Alumno = input("Ingresar nombre de alumno. Debe contener minimo 5 caracteres. Solo letras (a-z, A-Z) y espacios: ")

        if len(nombre_Alumno) >= 5:
            for caracter in nombre_Alumno:
                if "a" <= caracter <= "z" or "A" <= caracter <= "Z" or caracter == " ":
                    validez = True
                else:
                    print("Nombre con caracteres invalidos")
                    validez = False
                    break
        else:
            print("Nombre con menos de 5 caracteres")
            validez = False

    return nombre_Alumno



def validacion_Primer_Nota():
    validez = False

    while validez == False:
        nota_Alumno = int(input("Nota primer parcial:"))
        if 0 <= nota_Alumno <= 10:
            validez = True
        else:
            validez = False
            
    
    return nota_Alumno


def validacion_Segunda_Nota():
    validez = False

    while validez == False:
        nota_Alumno = int(input("Nota segunda parcial:"))
        if 0 <= nota_Alumno <= 10:
            validez = True
        else:
            validez = False
            
    
    return nota_Alumno




