"""
    _summary_ Archivo de funciones
    """
from auxiliares.auxiliares import (
    mostrar_menu, mostrar_matriz, cargar_datos, sumar_unidades,
    obtener_min, mostrar_uno, obtener_max, mostrar_matriz_recaudacion,
    contar_mas_de_seis, maximo_porcentaje, mostrar_recaudacion_ordenada
)

# 1. Obtener existencias: para ello deberá crear una función que cargue la existencia de cada vehículo en todos los garajes y mostrarlos.
# 2. Calcular cantidad total de unidades almacenadas entre todos los vehículos de la concesionaria.
# 3. Datos completos del garaje que almacena menos unidades de vehículos.
# 4. Máxima cantidad de unidades que almacenana el concesionaria con mas unidades.
# 5. Obtener recaudación: para ello deberás crear una función que calcule la recaudación de cada garaje,
# teniendo en cuenta su precio unitario y cantidad de unidades almacenadas en cada garaje.
# 6. Cantidad de garajes que hayan almacenado 6 o más unidades de vehículos.
# Porcentaje de unidades de cada marca de vehículo sobre el total de vehículos almacenados entre todos los garajes de la sede matriz.
# 7. Además mostrar todos los datos del garaje con el máximo porcentaje de vehículos almacenados.
# 8. Generar un informe con la recaudación de cada garaje, ordenada de mayor a menor.


def calcular_total(data: list[list]) -> None:
    resultado = sumar_unidades(data)
    mensaje = f"La cant TOTAL de unidades almacenadas es: {resultado} \n"
    print(mensaje)


def calcular_menos_unidades(data: list[list]) -> None:
    minimo = "El concesionario con menos unidades es: \n"
    minimo = obtener_min(data)
    mostrar_uno(data, minimo)


def calcular_mas_unidades(data: list[list]) -> None:
    mensaje_max = f"El concesionario con mas unidades es: \n"
    print(mensaje_max)
    maximo = obtener_max(data)
    mostrar_uno(data, maximo)
    unidades = f"Con {data[maximo][3]} unidades\n"
    print(unidades)


def calcular_mas_6_unidades(data: list[list]) -> None:
    mas_de_seis = contar_mas_de_seis(data)
    mensaje_6 = f"La cantidad de garajes con mas de 6 unidades es: {
        mas_de_seis}"
    print(mensaje_6)


def calcular_porcentaje_max(data: list[list], concesionaria: int) -> None:
    porcentaje = maximo_porcentaje(data, concesionaria)
    mensaje_porcentaje = f"El concesionario con el maximo porcentaje {
        porcentaje[0]:.2f}% es \n"
    print(mensaje_porcentaje)
    mostrar_uno(concesionaria, porcentaje[1])


def mostrar_recaudacion_por_garage(data: list[list]) -> None:
    mensaje_rec_ordenada = "Lista recaudacion por Garage: "
    print(mensaje_rec_ordenada)
    mostrar_recaudacion_ordenada(data)
