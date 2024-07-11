from os import *
import datetime
from validaciones import *
from archivos_csv_json import*

lista_original = parsear_csv("Proyectos.csv")
lista_proyectos = normalizar_csv(lista_original)

fecha_hoy = datetime.date.today()
fecha_formato_perzonalizado = fecha_hoy.strftime("%d/%m/%Y")


#ESTADO PROYECTO
ACTIVO = "Activo"
CANCELADO = "Cancelado"
FINALIZADO = "Finalizado"

#ESTADOS BUSQUEDA
CORRECTA = 1
FALLIDA = 2
ANULADA = 3

def devolver_ultimo_id(nombre_archivo):
    csv_parseado = (nombre_archivo)
    if not csv_parseado:
        print("El archivo CSV está vacío o no se encontró.")
        return 1
    lista_largo = len(csv_parseado)
    if lista_largo == 0:
        print("No hay proyectos en el archivo CSV.")
        return 1
    ultima_id = int(csv_parseado[lista_largo - 1]["id"])
    return ultima_id + 1

id_auto_incremental = devolver_ultimo_id(lista_original)

# FUNCIONES MENU
def continuar():
    mensaje = input("Presione ENTER para continuar...")
    print(mensaje)

def mostrar_menu():
    system('cls')
    print("Menu de opciones\n",
        "1) Ingresar proyecto\n",
        "2) Modificar proyecto\n",
        "3) Cancelar proyecto\n",
        "4) Comprobar proyectos\n",
        "5) Mostrar todos\n",
        "6) Calcular presupuesto promedio\n",
        "7) Buscar proyecto por nombre\n",
        "8) Ordenar proyectos\n",
        "9) Retomar proyecto\n",
        "10) Mostar presupuestos mayores\n",
        "11) Mostrar presupuestos finalizados\n"
        " 12) Salir\n")

def menu():

    while(True):

        mostrar_menu()
        opcion = int(input("Elija una opción: "))

        match opcion:
            case 1:
                retorno = proyectos_mayor_cincuenta(lista_proyectos, "Activo")
                if retorno == CORRECTA:
                    incrementar_id()
                    if ingresar_proyecto(id_auto_incremental, lista_proyectos):
                        print("SE DIO DE ALTA CORRECTAMENTE")
                    else:
                        decrementar_id()
                        print("ALTA CANCELADA")
                else:
                    print("LA SUPERO LA CANTIDAD MAXIMA DE PROYECTOS\nFINALICE O CANCELE UN PROYECTO PARA AÑADIR OTRO")
            case 2:
                if verificar_proyectos(lista_proyectos):
                    retorno = modificar_proyecto(lista_proyectos)
                    if retorno == CORRECTA:
                        print("SE MODIFICO EL PROYECTO CORRECTAMENTE")
                    elif retorno == ANULADA:
                        print("SE ANULO LA MODIFICACION DEL PROYECTO")
                    else:
                        print("MODIFICACION FALLIDA(NO SE ENCONTRO EL PROYECTO)")
                else:
                    print("NO HAY PROYECTOS INGRESADOS")
            case 3:
                if verificar_proyectos(lista_proyectos):
                    retorno = cancelar_proyecto(lista_proyectos)
                    if retorno == CORRECTA:
                        print("SE CANCELO EL PROYECTO CORRECTAMENTE")
                    elif retorno == ANULADA:
                        print("SE ANULO LA CANCELACION DEL PROYECTO")
                    else:
                        print("CANCELACION FALLIDA(NO SE ENCONTRO EL PROYECTO)")
                else:
                    print("NO HAY PROYECTOS INGRESADOS")
            case 4:
                retorno = comprobar_proyectos(lista_proyectos)
                if retorno == CORRECTA:
                    print("PROYECTOS CUYA FECHA FINALIZARON CAMBIADOS CORRECTAMENTE")
                else:
                    print("NO HAY PROYECTOS CON FECHA FINALIZADA")
            case 5:
                mostrar_proyectos(lista_proyectos, ACTIVO)
            case 6:
                if verificar_proyectos(lista_proyectos):
                    print("PROMEDIO PRESUPUESTOS")
                    calcular_promedios(lista_proyectos)
                else:
                    print("NO HAY PROYECTOS INGRESADOS")
            case 7:
                if verificar_proyectos(lista_proyectos):
                    retorno = buscar_nombre(lista_proyectos)
                    if retorno == CORRECTA:
                        print("SE ENCONTRO EL PROYECTO")
                    else:
                        print("NO SE ENCONTRO EL PROYECTO")
                else:
                    print("NO HAY PROYECTOS INGRESADOS")
            case 8:
                if verificar_proyectos(lista_proyectos):
                    print("ORDENAR PROYECTOS")
                    ordenar_proyecto(lista_proyectos)
                else:
                    print("NO HAY PROYECTOS INGRESADOS")
            case 9:
                if verificar_proyectos(lista_proyectos):
                    retorno = retomar_proyectos(lista_proyectos)
                    if retorno == CORRECTA:
                        print("SE RETOMO EL PROYECTO CORRECTAMENTE")
                    elif retorno == ANULADA:
                        print("SE ANULO LA RETOMACION DEL PROYECTO")
                    else:
                        print("RETOMACION FALLIDA(NO SE ENCONTRO EL PROYECTO)")
                else:
                    print("NO HAY PROYECTOS INGRESADOS")
            case 10:
                if verificar_proyectos(lista_proyectos):
                    retorno = mostrar_presupuestos_mayores(lista_proyectos)
                    if retorno == CORRECTA:
                        print("SE ENCONTRARON PRESUPUESTOS MAYORES CON EXITO")
                    else:
                        print("NO SE ENCONTRARON PRESUPUESTOS MAYORES AL INGRESADO")
                else:
                    print("NO HAY PROYECTOS INGRESADOS")
            case 11:
                if verificar_proyectos(lista_proyectos):
                    retorno = reporte_nombre(lista_proyectos)
                    if retorno == CORRECTA:
                        print("SE ENCONTRARON PRESUPUESTOS MAYORES AL NOMBRE DEL PROYECTO CON EXITO")
                    else:
                        print("NO SE ENCONTRARON PRESUPUESTOS MAYORES AL INGRESADO")
                else:
                    print("NO HAY PROYECTOS INGRESADOS")
            case 12:
                generar_csv("Proyectos.csv",lista_proyectos)
                lista_finalizados = buscar_finalizados(lista_proyectos,FINALIZADO)
                generar_json("Proyectos Finalizados.json",lista_finalizados)
                break
            case 13:
                if verificar_proyectos(lista_proyectos):
                    retorno = mostrar_presupuestos_finalizados(lista_proyectos)
                    if retorno == CORRECTA:
                        print("SE ENCONTRARON PROYECTOS FINALIZADOS MAYORES A 2 AÑOS")
                    else:
                        print("NO HAY NINGUN PROYECYO FINALIZADO MAYOR A 2 AÑOS")
            case 14:
                if verificar_proyectos(lista_proyectos):
                    print("PRESUPUESTOS DE LOS PROYECTOS CON NOMBRE SISTEMAS")
                    retorno = promedio_presupuestos_sistema(lista_proyectos)
                    if retorno == CORRECTA:
                        print("SE ENCONTRARON PROYECTOS CON EXITO")
                else:
                    print("NO HAY PROYECTOS INGRESADOS")
        continuar()
    print("EL PROGRAMA FINALIZO")

#1) ALTA PROYECTOS
def proyectos_mayor_cincuenta(lista_proyectos:list, ESTADO):
    retorno = FALLIDA
    proyectos_activos = []
    for proyecto in lista_proyectos:
        if proyecto["Estado"] == ESTADO:
            proyectos_activos.append(proyecto)
    if len(proyectos_activos) < 50:
        retorno = CORRECTA
    return retorno

def incrementar_id():
    global id_auto_incremental
    id_auto_incremental = devolver_ultimo_id(lista_original)

def decrementar_id():
    global id_auto_incremental
    id_auto_incremental = devolver_ultimo_id(lista_original) - 1

def ingresar_proyecto(id_auto_incremental:int, lista_proyectos:list):

    retorno = False

    nombre = ingresar_nombre("Ingresa nombre del proyecto: ",
    "Ingrese un nombre valido: ", 30)
    descripcion = ingresar_descripcion("Ingresa la descripcion del proyecto: ",
    "Ingrese una descripcion valida: ",200)
    presupuesto = ingresar_entero("Ingrese el presupuesto del proyecto: ",
    "Ingrese un presupuesto valido no menor a 500.000: ", 500000, 1000000000000)
    fecha_inicio = ingresa_fecha("Inicio")
    fecha_finalizacion = ingresa_fecha("Finalizacion")
    while validar_fechas(fecha_inicio, fecha_finalizacion):
        print("LA FECHA DE FINALIZACION NO PUEDE SER MENOR A LA FECHA DE INICIO.\n","Ingrese la fecha de finalizacion nuevamente: ")
        fecha_finalizacion = ingresa_fecha("Finalizacion")


    proyecto = {"id":id_auto_incremental, "Nombre del Proyecto":nombre,"Descripción":descripcion,"Fecha de inicio":fecha_inicio,
                "fecha_finalizacion":fecha_finalizacion, "Presupuesto":presupuesto, "Estado":ACTIVO}

    mostrar_un_proyecto(proyecto)

    if confirmar("Desea confirmar el ingreso del proyecto? S/N: ",
                "Ingrese una opcion valida (S/N), Desea confirmar el ingreso del proyecto? S/N: "):
        lista_proyectos.append(proyecto)
        retorno = True
    else:
        ("ALTA CANCELADA")

    return retorno

#2) MODIFICACION PROYECTOS "Terminar"
def modificar_proyecto(lista_proyectos:list):

    retorno = FALLIDA

    mostrar_proyectos(lista_proyectos, ACTIVO)

    id_a_modificar = ingresar_entero("Ingresa el ID a modificar: ", "Ingrese un ID valido, entre 1 y 50: ", 1, 50)
    indice = buscar_proyecto(id_a_modificar,lista_proyectos, ACTIVO)

    if indice != None:
        print("SE ENCONTRO EL PROYECTO")
        respuesta = True
        while respuesta == True:
            print("Opciones: \n",
                "1) Modificar nombre\n",
                "2) Modificar descripcion\n",
                "3) Modificar presupuesto\n",
                "4) Modificar fecha de inicio\n",
                "5) Modificar fecha de finalizacion\n")
            opcion = ingresar_entero("Ingrese una opcion: ", "Ingrese una opcion valida: ", 1, 5)
            match opcion:
                #Guarda en vriables y despues si confirma subir
                case 1:
                    nombre = ingresar_nombre("Ingresa nombre del proyecto: ",
                    "Ingrese un nombre valido: ", 30)
                    lista_proyectos[indice]["Nombre del Proyecto"] = nombre
                case 2:
                    descripcion = ingresar_descripcion("Ingresa la descripcion del proyecto: ",
                    "Ingrese una descripcion valida: ",200)
                    lista_proyectos[indice]["Descripción"] = descripcion
                case 3:
                    presupuesto = ingresar_entero("Ingrese el presupuesto del proyecto: ",
                    "Ingrese un presupuesto valido no menor a 500.000: ", 500000, 1000000000000)
                    lista_proyectos[indice]["Presupuesto"] = presupuesto
                case 4:
                    fecha_inicio = ingresa_fecha("Inicio")
                    lista_proyectos[indice]["Fecha de inicio"] = fecha_inicio
                case 5:
                    fecha_finalizacion = ingresa_fecha("Finalizacion")
                    lista_proyectos[indice]["fecha_finalizacion"] = fecha_finalizacion

            respuesta = confirmar("Desea modificar otro dato? S/N: ",
                                "Ingrese una opcion correcta (S/N). Desea modificar otro dato? S/N: ")

        mostrar_un_proyecto(lista_proyectos[indice])

        if confirmar("Desea confirmar la modificacion del proyecto? S/N: ",
            "Ingrese una opcion valida (S/N), Desea confirmar la modificacion del proyecto? S/N: "):
                retorno = CORRECTA
        else:
            retorno = ANULADA
    return retorno

#3) BAJA PROYECTOS
def cancelar_proyecto(lista_proyectos:list) -> bool:

    retorno = FALLIDA

    mostrar_proyectos(lista_proyectos, ACTIVO)

    id_a_cancelar = ingresar_entero("Ingresa el ID a cancelar: ", "Ingrese un ID valido, entre 1 y 50: ", 1, 50)
    indice = buscar_proyecto(id_a_cancelar,lista_proyectos, ACTIVO)

    if indice != None:
        print("SE ENCONTRO EL PROYECTO")
        mostrar_un_proyecto(lista_proyectos[indice])
        if confirmar("Desea confirmar la cancelacion del proyecto? S/N: ",
                "Ingrese una opcion valida (S/N), Desea confirmar la cancelacion del proyecto? S/N: "):
                    lista_proyectos[indice]["Estado"] = CANCELADO
                    retorno = CORRECTA
                    decrementar_id()
        else:
            retorno = ANULADA
    return retorno

#4) COMPROBAR PROYECTOS
def comprobar_proyectos(lista_proyectos:list):
    retorno = CORRECTA
    for proyecto in lista_proyectos:
        if proyecto["Fecha de Fin"] < fecha_formato_perzonalizado:
            proyecto["Estado"] = "Finalizado"
            retorno = FALLIDA
    return retorno

#5) MOSTRAR
def mostrar_proyectos(lista_proyectos:list, ESTADO) -> str:
    informacion = "PROYECTOS\n ID | NOMBRE | DESCRIPCION | FECHA INICIO | FECHA FINALIZACION | PRESUPUESTO |\n"
    for proyecto in lista_proyectos:
        if proyecto["Estado"] == ESTADO:
            for clave in proyecto:
                    if clave != "Estado":
                        informacion += str(proyecto[clave]) + " | "
            informacion += "\n"
    print(informacion)

#6) PRESUPUESTOS PROMEDIOS
def calcular_promedios(lista_proyectos:list):

    mostrar_proyectos(lista_proyectos, ACTIVO)
    promedios_presupuestos = 0
    for i in range(len(lista_proyectos)):
        if lista_proyectos[i]["Estado"] != CANCELADO:
            promedios_presupuestos += lista_proyectos[i]["Presupuesto"]
    print(f"El promedio de los presupuestos es: {promedios_presupuestos}")

#7) BUSCAR POR NOMBRE
def buscar_nombre(lista_proyectos:list):

    retorno = FALLIDA
    mostrar_proyectos(lista_proyectos, ACTIVO)
    nombre_a_buscar = ingresar_nombre("Ingrese el nombre del proyecto a buscar: ",
                                    "Ingrese un nombre valido: ",30)
    for i in range(len(lista_proyectos)):
        if lista_proyectos[i]["Nombre del Proyecto"] == nombre_a_buscar:
            mostrar_un_proyecto(lista_proyectos[i])
            retorno = CORRECTA
    return retorno

#8) ORDENAR PROYECTOS
def ordenar_proyecto(lista_proyectos:list):

    mostrar_proyectos(lista_proyectos, ACTIVO)
    dato = menu_orden()
    orden = ingresar_2_str_comparativos(
                "Ingrese la condicion a ordenar 1)Ascendente o 2)Descendente: ",
                "Ingrese una condicion valida: ",
                "1", "2")

    if orden == "1":
        #Ordenamineto de A-Z
        for i in range(len(lista_proyectos)):
            for j in range(i+1, len(lista_proyectos), 1):
                if lista_proyectos[i][dato] < lista_proyectos[j][dato]:
                    aux = lista_proyectos[i]
                    lista_proyectos[i] = lista_proyectos[j]
                    lista_proyectos[j] = aux
    else:
        #Ordenamineto de Z-A
        for i in range(len(lista_proyectos)):
            for j in range(i+1, len(lista_proyectos), 1):
                if lista_proyectos[i][dato] > lista_proyectos[j][dato]:
                    aux = lista_proyectos[i]
                    lista_proyectos[i] = lista_proyectos[j]
                    lista_proyectos[j] = aux

    mostrar_proyectos(lista_proyectos, ACTIVO)

def menu_orden():
    respuesta = False
    while respuesta == False:
        print("Ordenar proyectos por:\n",
                "1) Nombre\n",
                "2) Presupuesto\n",
                "3) Fecha de inicio\n")
        opcion = ingresar_entero("Ingrese una opcion: ", "Ingrese una opcion valida: ", 1, 3)
        match opcion:
            case 1:
                dato = "Nombre del Proyecto"
            case 2:
                dato = "Presupuesto"
            case 3:
                dato = "Fecha de inicio"

        respuesta = confirmar(f"Confirma modificar los proyectos por {dato}? S/N: ",
                        f"Ingrese una opcion correcta (S/N). Confirma modificar los proyectos por {dato}? S/N: ")
    return dato

#9) RETOMAR PROYECTOS
def retomar_proyectos(lista_proyectos:list):
    retorno = FALLIDA
    print("PROYECTOS CANCELADOS")
    mostrar_proyectos(lista_proyectos,CANCELADO)
    id_a_retomar = ingresar_entero("Ingrese el ID del proyecto a retomar: ",
                                "Ingrese una opcion valida, Ingrese el ID del proyecto a retomar: ", 1, 50)
    indice = buscar_proyecto(id_a_retomar, lista_proyectos, CANCELADO)
    if indice != None:
        print("SE ENCONTRO EL PROYECTO")
        mostrar_un_proyecto(lista_proyectos[indice])
        if confirmar("Confirma retomar el proyecto? S/N: ",
                "Ingrese una opcion valida (S/N), Confirma retomar el proyecto? S/N: "):
                    lista_proyectos[indice]["Estado"] = ACTIVO
                    retorno = CORRECTA
                    generar_csv("Progra-1-1er-Cuatrimestre/Primer Parcial\Proyectos.csv",lista_proyectos)
        else:
            retorno = ANULADA
    return retorno
#10
def mostrar_presupuestos_mayores(lista_proyectos:list) -> str:
    numero = 0
    numero_reporte = guardar_numero_reporte(numero)
    retorno = FALLIDA
    cantidad_reportes_concicentes = 0
    presupuesto_a_buscar = ingresar_entero("Ingrese el presupuesto a buscar: ", "Ingrese un presupuesto valido: ", 500000, 1000000000000)
    informacion =f"PROYECTOS SUPERIORES AL PRESUPUESTO DE: {presupuesto_a_buscar}\nID | NOMBRE | DESCRIPCION | FECHA INICIO | FECHA FINALIZACION | PRESUPUESTO |\n"
    for proyecto in lista_proyectos:
        if proyecto["Presupuesto"] > presupuesto_a_buscar:
            for clave in proyecto:
                    if clave != "Estado":
                        informacion += str(proyecto[clave]) + " | "
            informacion += "\n"
            retorno = CORRECTA
            cantidad_reportes_concicentes += 1
    informacion +=  f"Numero de reporte: {numero_reporte}\nFecha de solicitud: {fecha_formato_perzonalizado}\nCantidad de reportes coincidentes: {cantidad_reportes_concicentes}\n\n"
    generar_txt("Presupuestos Mayores.txt", informacion)
    return retorno

#11
def reporte_nombre(lista_proyectos:list):
    numero = 0
    numero_reporte = guardar_numero_reporte_nombre(numero)
    retorno = FALLIDA
    cantidad_reportes_coincidentes = 0
    
    nombre = ingresar_nombre("Ingresa nombre del proyecto: ","Ingrese un nombre valido: ", 30)
    
    informacion = f"PROYECTOS CON NOMBRE: {nombre}\nID | NOMBRE | DESCRIPCION | FECHA INICIO | FECHA FINALIZACION | PRESUPUESTO |\n"
    for proyecto in lista_proyectos:
        if nombre.lower() == proyecto["Nombre del Proyecto"].lower():
            for clave in proyecto:
                if clave != "Estado":
                    informacion += str(proyecto[clave]) + " | "
            informacion += "\n"
            retorno = CORRECTA
            cantidad_reportes_coincidentes += 1
    
    informacion += f"Numero de reporte: {numero_reporte}\nFecha de solicitud: {fecha_formato_perzonalizado}\nCantidad de reportes coincidentes: {cantidad_reportes_coincidentes}\n\n"
    generar_txt("Proyectos por Nombre.txt", informacion)
    return retorno
    # numero = 0
    # numero_reporte = guardar_numero_reporte_nombre(numero)
    # retorno = FALLIDA
    # cantidad_reportes_concicentes = 0
    # nombre = ingresar_nombre("Ingresa nombre del proyecto: ","Ingrese un nombre valido: ", 30)
    # informacion =f"PROYECTOS SUPERIORES AL PRESUPUESTO DEL PROYECTO: {nombre}\nID | NOMBRE | DESCRIPCION | FECHA INICIO | FECHA FINALIZACION | PRESUPUESTO |\n"
    # for proyecto in lista_proyectos:
    #     if proyecto["Nombre del Proyecto"] == nombre:
    #         if proyecto["Presupuesto"] > proyecto["Presupuesto"]:
    #             for clave in proyecto:
    #                     if clave != "Estado":
    #                         informacion += str(proyecto[clave]) + " | "
    #             informacion += "\n"
    #             retorno = CORRECTA
    #             cantidad_reportes_concicentes += 1
    # informacion +=  f"Numero de reporte: {numero_reporte}\nFecha de solicitud: {fecha_formato_perzonalizado}\nCantidad de reportes coincidentes: {cantidad_reportes_concicentes}\n\n"
    # generar_txt("Presupuestos Mayores a nombre.txt", informacion)
    # return retorno

#13
def mostrar_presupuestos_finalizados(lista_proyectos:list):
    contador = 0
    presupuesto_total = 0
    for proyecto in lista_proyectos:
        mas_de_dos_años = False
        if proyecto['Estado'] == 'Finalizado':
            fecha_inicio =  proyecto['Fecha de inicio']
            fecha_finalizacion = proyecto['Fecha de Fin']
            if (fecha_inicio.year + 2) < fecha_finalizacion.year:
                mas_de_dos_años = True
            if (fecha_inicio.year + 2) <= fecha_finalizacion.year:
                if fecha_inicio.month < fecha_finalizacion.month:
                    mas_de_dos_años = True
                if fecha_inicio.month == fecha_finalizacion.month:
                    if fecha_inicio.day <= fecha_finalizacion.day:
                        mas_de_dos_años = True
            if mas_de_dos_años == True:
                contador += 1
                presupuesto_total += proyecto['Presupuesto']
    if contador == 0:
        retorno = FALLIDA
    else:
        promedio_proyectos_finalizados = presupuesto_total / contador
        print(f'El promedio de los proyectos finalizados con más de dos años es: ${promedio_proyectos_finalizados:,.2f}')
        retorno = CORRECTA
    return retorno

#14
def promedio_presupuestos_sistema(lista_proyectos:list):
    retorno = FALLIDA
    proyetos_sistemas = []
    proyectos_activos = []
    suma_presupuestos = 0
    nombre = "Sistema"
    for i in range(len(lista_proyectos)):
        if buscar_nombre_sistema(lista_proyectos[i]["Nombre del Proyecto"], nombre):
            proyetos_sistemas.append(lista_proyectos[i])
    if len(proyetos_sistemas) < 1:
        print("NO HAY PROYECTOS CON EL NOMBRE SISTEMA")
    else:
        for i in range(len(proyetos_sistemas)):
            if proyetos_sistemas[i]["Estado"] == ACTIVO:
                proyectos_activos.append(proyetos_sistemas[i])
                suma_presupuestos += proyetos_sistemas[i]["Presupuesto"]
        promedios_presupuestos = suma_presupuestos / len(proyectos_activos)
        print(f"El promedio de los presupuestos es: {promedios_presupuestos}")
        retorno = CORRECTA
    return retorno

def buscar_nombre_sistema(cadena:str, nombre:str) -> str:
    cadena_nueva = ""
    retorno = False
    if len(cadena) > 6:
        for i in range(7):
            cadena_nueva += cadena[i]
        if nombre == cadena_nueva:
            retorno = True
    return retorno

#FUNCIONES PROYECTOS
def verificar_proyectos(lista_proyectos:list):
    retorno = False
    for i in range(len(lista_proyectos)):
        if i > -1:
            retorno = True
            break
    return retorno

def mostrar_un_proyecto(proyecto:dict) -> str:
    informacion = "PROYECTOS\n ID | NOMBRE | DESCRIPCION | FECHA INICIO | FECHA FINALIZACION | PRESUPUESTO |\n"
    for clave in proyecto:
        if clave != "estado":
            informacion+= str(proyecto[clave]) + "|"
    print(informacion)

def confirmar(mensaje:str, mensaje_error:str):
    confirmacion = input(mensaje).upper()
    retorno = False

    while confirmacion != "S" and confirmacion != "N":
        confirmacion = input(mensaje_error).upper()

    if confirmacion == "S":
        retorno = True

    return retorno

def buscar_proyecto( id_a_buscar:int, lista_proyectos:list, ESTADO):
    retorno = None
    for i in range(len(lista_proyectos)):
        if lista_proyectos[i]["id"] == id_a_buscar and lista_proyectos[i]["Estado"] == ESTADO:
            retorno = i
            break

    return retorno


#ARCHIVOS
def buscar_finalizados(lista_proyectos:list, ESTADO) -> list:
    lista_finalizados = []
    for proyecto in lista_proyectos:
        if proyecto["Estado"] == ESTADO:
            lista_finalizados.append(proyecto)
    return lista_finalizados