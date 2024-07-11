import os
import json
import datetime

def parsear_csv(nombre_archivo:str):
    
    lista_parseada = []
    lista_claves = []
    
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding = "utf-8") as archivo:
            primer_linea = archivo.readline()
            primer_linea = primer_linea.replace("\n","")
            lista_claves = primer_linea.split(",")
            
            for linea in archivo:
                linea_aux = linea.replace("\n","")
                linea_aux_uno = linea_aux.replace("-","/")
                lista_valores = linea_aux_uno.split(",")
                dict_proyecto = {}
                
                for i in range(len(lista_claves)):
                    dict_proyecto[lista_claves[i]] = lista_valores[i]
                
                lista_parseada.append(dict_proyecto)
    else:
        print("NO SE ENCONTRO EL ARCHIVO")
    return lista_parseada

def normalizar_csv(lista_parseada:list):
    
    for proyecto in lista_parseada:
            if type(proyecto["id"]) == str:
                valor_clave = int(proyecto["id"])
                proyecto["id"] = valor_clave
                
            if type(proyecto["Presupuesto"]) == str:
                valor_clave = int(proyecto["Presupuesto"])
                proyecto["Presupuesto"] = valor_clave
            if type(proyecto['Fecha de inicio']) == str: 
                valor_clave = datetime.datetime.strptime(proyecto['Fecha de inicio'], '%d/%m/%Y')
            if type(proyecto['Fecha de Fin']) == str: 
                valor_clave = datetime.datetime.strptime(proyecto['Fecha de Fin'], '%d/%m/%Y')
            
    return lista_parseada


def generar_json(nombre_archivo:str,lista:list):
    with open(nombre_archivo,"w") as archivo:
        json.dump(lista,archivo,indent=4)

# def generar_json_reporte(numero_reporte):
#     with open("Numeros Reporte.json","w") as archivo:
#         json.dump(numero_reporte,archivo,indent=4)

# def cargar_reporte():
#     if os.path.exists("numero.json"):
#         with open("numero.json", "r") as archivo:
#             datos = json.load(archivo) #CARGO EL ARCHIVO 
#             return datos.get("reporte", 0)
#     else:
#         with open("numero.json", "w") as archivo:
#             json.dump({"reporte": 0}, archivo)
#         return 0

# def guardar_numero_reporte(numero):
#     # numero = []
#     cantidad_reportes = cargar_reporte()
#     if cantidad_reportes == 0:
#         cantidad_reportes = 1
#     else:
#         cantidad_reportes += 1
#     numero = int(numero) #EN DATO STR
#     with open("numero.json", "w") as archivo:
#         json.dump({"reporte": numero}, archivo)

# def cargar_reporte(numero):
#     if os.path.exists("numero.json"):
#         with open("numero.json", "r") as archivo:
#             try:
#                 datos = json.load(archivo)
#                 return datos.get("reporte", numero)
#             except json.JSONDecodeError:
#                 return numero
#     else:
#         with open("numero.json", "w") as archivo:
#             json.dump({"reporte": numero}, archivo)
#         return numero
def cargar_reporte(numero):
    if os.path.exists("numero.json"):
        with open("numero.json", "r") as archivo:
            datos = archivo.read()
            if datos:
                datos = json.loads(datos)
                return datos.get("reporte", numero)
            else:
                return numero
    else:
        with open("numero.json", "w") as archivo:
            json.dump({"reporte": numero}, archivo)
        return numero

def guardar_numero_reporte(numero):
    cantidad_reportes = cargar_reporte(numero)
    if cantidad_reportes == 0:
        cantidad_reportes = 1
    else:
        cantidad_reportes += 1
    
    with open("numero.json", "w") as archivo:
        json.dump({"reporte": cantidad_reportes}, archivo)
    return cantidad_reportes

def guardar_numero_reporte_nombre(numero):
    cantidad_reportes = cargar_reporte(numero)
    if cantidad_reportes == 0:
        cantidad_reportes = 1
    else:
        cantidad_reportes += 1
    
    with open("numero_nombre.json", "w") as archivo:
        json.dump({"reporte": cantidad_reportes}, archivo)
    return cantidad_reportes

def generar_txt(nombre_archivo:str, informacion:str):
        with open(nombre_archivo,"a", encoding="utf-8") as archivo:
            archivo.write(informacion)

def generar_csv(nombre_archivo:str,lista:list):
    if len(lista) > 0:
        lista_claves = list(lista[0].keys())
        separador = ","
        cabecera = separador.join(lista_claves)
        print(cabecera)
        
        with open(nombre_archivo,"w", encoding="utf-8") as archivo:
            archivo.write(cabecera + "\n")
            for elemento in lista:
                lista_valores = list(elemento.values())
                for i in range(len(lista_valores)):
                    lista_valores[i] = str(lista_valores[i])

                dato = separador.join(lista_valores)
                dato += "\n"
                archivo.write(dato)
    else:
        print("ERROR LISTA VACIA")


print(parsear_csv("Proyectos.csv"))