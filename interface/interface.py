from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla, clear_console
from auxiliares.auxiliares import mostrar_menu, mostrar_matriz, cargar_datos, mostrar_matriz_recaudacion
from funciones.funciones import (
    calcular_total, calcular_menos_unidades, mostrar_recaudacion_por_garage,
    calcular_mas_unidades, calcular_mas_6_unidades, calcular_porcentaje_max
)
from validar.validar import validar_entrada


def menu_principal(data):
    while True:
        mostrar_menu()
        entrada = validar_entrada(1, 9)
        concesionaria = cargar_datos(data)
        match entrada:
            case 1:
                mostrar_matriz(concesionaria)
            case 2:
                calcular_total(data)
            case 3:
                calcular_menos_unidades(concesionaria)
            case 4:
                calcular_mas_unidades(concesionaria)
            case 5:
                mostrar_matriz_recaudacion(concesionaria)
            case 6:
                calcular_mas_6_unidades(concesionaria)
            case 7:
                calcular_porcentaje_max(data, concesionaria)
            case 8:
                mostrar_recaudacion_por_garage(concesionaria)
            case 9:
                print('Saliendo...')
                break
            case _:
                print('Opción inválida')
        clear_console()
