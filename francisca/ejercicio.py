import funcione as fn
nombre=[]
rut=[]
categoria=[]
celular=[] 
correo=[]
fecha_nacimiento=[] 
nom_pareja=[]
op=0
while op!=4:
    op=fn.menu()
    if op==1:
        nombre,rut,categoria,celular,correo,fecha_nacimiento,nom_pareja=fn.ingreso_participantes(nombre,rut,categoria,celular,correo,fecha_nacimiento,nom_pareja)
    elif op==2:
        nombre,rut,categoria,celular,correo=fn.buscar_participante(nombre, rut , categoria , celular , correo )
    elif op==3:
        nombre,rut, nom_pareja=fn.imprimir_parejas(nombre,rut,nom_pareja)
    else:
        fn.salir()