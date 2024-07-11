import datetime 

def ingresar_nombre (mensaje:str, mensaje_error:str, limite:int) -> str:
    str = input(mensaje).capitalize()
    while str == "" or len(str) > limite or str.isalpha() == False:
        str = input(mensaje_error).capitalize()
    return str

def ingresar_descripcion (mensaje:str, mensaje_error:str, limite:int) -> str:
    str = input(mensaje).capitalize()
    str_aux = str.replace(" ","")
    while str_aux == "" or len(str_aux) > limite or str_aux.isalnum() == False:
        str_aux = input(mensaje_error).capitalize()
        str_aux = str_aux.replace(" ","")
    return str

def ingresar_entero(mensaje:str, mensaje_error:str, minimo:int, maximo:int) -> int:
    num = int(input(mensaje))
    while num < minimo or num > maximo:
        num = int(input(mensaje_error))
    return num

def ingresar_año(mensaje:str, mensaje_error:str) -> int:
    num = int(input(mensaje))
    while num < 1950 or num > 2030:
        num = int(input(mensaje_error))
    return num

def ingresa_fecha(estado:str):
    dia = ingresar_entero(f"Ingrese el dia {estado} : ", f"Ingrese un dia de {estado} valido: ", 1, 31)
    mes = ingresar_entero(f"Ingrese el mes {estado}: ", f"Ingrese un mes de {estado} valido: ", 1, 12)
    año = ingresar_año(f"Ingrese el año {estado}: ", f"Ingrese un año de {estado} valido: ")
    fecha = f"{dia}/{mes}/{año}"
    return fecha

def ingresar_2_str_comparativos (mensaje:str, mensaje_error:str, str_1:str, str_2:str) -> str:
    str = input(mensaje).capitalize()
    while str != str_1 and str != str_2:
        str = input(mensaje_error).capitalize()
    return str

def validar_fechas(fecha_inicio:str, fecha_finalizacion:str) -> str:
    fecha_inicio = fecha_inicio.split("/")
    fecha_inicio.reverse()
    fecha_finalizacion = fecha_finalizacion.split("/")
    fecha_finalizacion.reverse()
    retorno = False
    if fecha_finalizacion < fecha_inicio:
        retorno = True
    return retorno