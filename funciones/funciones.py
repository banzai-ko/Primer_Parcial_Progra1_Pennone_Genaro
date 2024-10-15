"""
    _summary_ Archivo de funciones
    """
from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla, clear_console
from auxiliares.auxiliares import (mostrar_menu, mostrar_matriz, cargar_datos, sumar_unidades,
                                   obtener_min, mostrar_uno, obtener_max, mostrar_matriz_recaudacion, contar_mas_de_seis, maximo_porcentaje, mostrar_recaudacion_ordenada)
from validar.validar import validar_entrada

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


def menu_principal(data):
    while True:
        mostrar_menu()
        entrada = validar_entrada(1, 9)
        concesionaria = cargar_datos(data)
        match entrada:
            case 1:
                mostrar_matriz(concesionaria)
                clear_console()
            case 2:
                resultado = sumar_unidades(data)
                mensaje = f"La cant TOTAL de unidades almacenadas es: {
                    resultado} \n"
                print(mensaje)
            case 3:
                minimo = f"El concesionaria con menos unidades es: \n"
                minimo = obtener_min(concesionaria)
                mostrar_uno(concesionaria, minimo)
            case 4:
                mensaje_max = f"El concesionaria con mas unidades es: \n"
                print(mensaje_max)
                maximo = obtener_max(concesionaria)
                mostrar_uno(concesionaria, maximo)
                unidades = f"Con {concesionaria[maximo][3]} unidades\n"
                print(unidades)
            case 5:
                mostrar_matriz_recaudacion(concesionaria)
            case 6:
                mas_de_seis = contar_mas_de_seis(concesionaria)
                mensaje_6 = f"La cantidad de garajes con mas de 6 unidades es: {mas_de_seis}"
                print(mensaje_6)
            case 7:
                porcentaje = maximo_porcentaje(data, concesionaria)
                mensaje_porcentaje = f"El concesionario con el maximo porcentaje {porcentaje[0]:.2f}% es \n"
                print(mensaje_porcentaje)
                mostrar_uno(concesionaria, porcentaje[1])
            case 8:
                mostrar_recaudacion_ordenada(concesionaria)
            case 9:
                print('Saliendo...')
                break
            case _:
                print('Opción inválida')
