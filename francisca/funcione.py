def menu():
    print("1- Registro de personas : ")
    print("2-Buscar participante por rut:")
    print("3-Impresion de parejas: ")
    print("4-Salir ")
    return validanro(int,"Ingrese su opcion: ", 1 , 4)

def validanro(tipo,texto,rmin=None,rmax=None):
    while True:
        try:
            nro=tipo(input(texto))
            if rmin!=None and rmax!=None:
                if rmin<=nro<=rmax:
                    break
                else:
                    print("Fuera de rango ")
            elif rmin!=None:
                if rmin<=nro:
                    break
                else:
                    print(f"El rango minimo es {rmin}")
            elif rmax!=None:
                if nro<=rmax:
                    break
                else:
                    print(f"El rango maximo es {rmax}")
            else:
                break
        except:
            print("Se esperaba un numero")
    return nro

def valida_largo(texto,largo,estricto):
    while True:
        entrada=input(texto)
        if estricto:
            if len(entrada)==largo:
                break
            else:
                print(f"El largo debe ser de {largo}")
        else:
            if len(entrada)>=largo:
                break
            else:
                print(f"El largo debe ser {largo}")
    return entrada
def validar_correo(entrada):
    while True :
        entrada=valida_largo("Ingrese su correo : ",6,False)
        if '@' in entrada:
            print("Correo ingresado con exito ")
            break
        else:
            print("Falta @ en su correo .")


def ingreso_participantes(nombre,rut,categoria,celular, correo , fecha_nacimiento , nom_pareja ):
    nombre.append(valida_largo("Ingrese su nombre :" , 2 , False))
    rut.append(validanro(int , "Ingrese su rut :"  ))
    celular.append(valida_largo("Ingrese su numero de celular ej:(972740245):" , 9 , True)) 
    correo.append(validar_correo("Ingrese su correo electronico : "))
    fecha_nacimiento.append(validanro(int , "Ingrese su año de nacimiento :", 1942 , None))#me falta validar el año 
    nom_pareja.append(valida_largo("Ingrese su nombre de equipo :" , 2 , False ))
    
    while True:
        if rut!=0:
            print("Ingrese su categoria : 1/ Oro  ,  2/Plata , 3/Bronce ")
            opcion=validanro(int,"Opcion:" , 1 , 3)
            if opcion==1:
                categoria.append("Oro")
                break
            elif opcion==2:
                categoria.append("Plata")
                break
            elif opcion==3:
                categoria.append("Bronce")
                break
            else:
                print("Ingreso una categeoria erronea , intente nuevamente ")
        else:
            print("Aun no hay registros por rut")
    return nombre,rut,categoria,celular,correo,fecha_nacimiento,nom_pareja

def buscar_participante(nombre, rut , categoria ,celular , correo):
    if rut!=0:
        buscar=int(input("Ingrese el rut a buscar :"))
        for i in range(len(rut)):
            if buscar==rut[i]:
                print("Nombre:",nombre[i])
                print("Categoria:",categoria[i])
                print("Fono:", celular[i])
                print("Correo:", correo[i]) #No me sale el correo 
            else:
                print("No hay personas ingresadas con ese rut ")
    else:
        print("Aun no hay participantes ingresados en el sistema ")
    return nombre, rut , categoria , celular , correo 

def imprimir_parejas(nombre,rut,nom_pareja):
    if rut!=0:
        buscador=(input("Ingrese nombre del equipo  :"))
        for i in range(len(nom_pareja)):
            if buscador==nom_pareja[i]:
                print("Nombre integrante  :", nombre[i])
            else:
                print("No hay parejas registradas con ese nombre identificador ")
    else:
        print("Aun no hay participantes ingresados en el sistema ")
    return nombre,rut,nom_pareja

def salir():
    print(" SALISTE ")
    print("Francisca Ramirez Soza -PGY1121_015D")