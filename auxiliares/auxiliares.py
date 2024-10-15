"""
    _summary_ Funciones auxiliares
    """
from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla
from menu import MENU_OPCIONES


def mostrar_menu() -> None:
    print(MENU_OPCIONES)


def cargar_datos(data: list[list]) -> list[list]:
    largo = 20
    dataset = []
    for i in range(largo):
        garage = i + 1
        marca = data[0][i]
        modelo = data[1][i]
        unidades = data[2][i]
        precio = data[3][i]
        ganancia = data[3][i] * data[2][i]
        elemento = [
            garage,
            marca,
            modelo,
            unidades,
            precio,
            ganancia
        ]
        dataset.append(elemento)
    return dataset


def mostrar_matriz(dataset: list[list]) -> None:
    """Muestra la matriz de forma tabular.

    Args:
        dataset: La matriz a mostrar.
    """
    print(f"{'Garage ':<4}{'Marca':<15}{'Modelo':<10}{'Cantidad ':<8}{
          'Precio Unitario':<18}{'Precio Total':<18}")
    print("="*60)

    for vehiculo in dataset:
        garage = vehiculo[0]
        marca = vehiculo[1]
        modelo = vehiculo[2]
        cantidad = vehiculo[3]
        precio_unitario = vehiculo[4]
        precio_total = vehiculo[5]

        print(f"{garage:<8}{marca:<15}{modelo:<10}{cantidad:<8}{
              precio_unitario:<15}{precio_total:<15}")


def sumar_unidades(data: list[list]) -> int:
    """Suma las existencias de todos los vehículos de la concesionaria.

    Args:
        data: La matriz de datos.

    Returns:
        int: La suma de las existencias.
    """
    suma = 0
    for i in range(len(data[2])):
        suma += data[2][i]

    return suma


def mostrar_uno(dataset: list[list], ubicacion: int) -> None:
    """Muestra la matriz de forma tabular.

    Args:
        dataset: La matriz a mostrar.
    """
    print(f"{'Garage ':<4}{'Marca':<15}{'Modelo':<10}{'Cantidad ':<8}{
          'Precio Unitario':<18}{'Precio Total':<18}")
    print("="*60)

    vehiculo = dataset[ubicacion]
    garage = vehiculo[0]
    marca = vehiculo[1]
    modelo = vehiculo[2]
    cantidad = vehiculo[3]
    precio_unitario = vehiculo[4]
    precio_total = vehiculo[5]

    print(f"{garage:<8}{marca:<15}{modelo:<10}{cantidad:<8}{
        precio_unitario:<15}{precio_total:<15}")


def obtener_min(dataset: list[list]) -> int:
    """Obtiene el garage con menos unidades.

    Args:
        dataset: La matriz de datos.

    Returns:
        int: El garage con menos unidades.
    """
    indice_minimo = 0
    cantidad_minima = dataset[0][3]

    for i in range(1, len(dataset)):
        if dataset[i][3] < cantidad_minima:
            cantidad_minima = dataset[i][3]
            indice_minimo = i

    return indice_minimo


def obtener_max(dataset: list[list]) -> int:
    """Obtiene el garage con menos unidades.

    Args:
        dataset: La matriz de datos.

    Returns:
        int: El garage con mas unidades.
    """
    indice_max = 0
    cantidad_max = dataset[0][3]

    for i in range(1, len(dataset)):
        if dataset[i][3] > cantidad_max:
            cantidad_max = dataset[i][3]
            indice_max = i

    return indice_max


def mostrar_matriz_recaudacion(dataset: list[list]) -> None:
    """Muestra la matriz de forma tabular.

    Args:
        dataset: La matriz a mostrar.
    """
    print(f"{'Garage ':<4}{'Recaudación':<18}")
    print("="*20)

    for vehiculo in dataset:
        garage = vehiculo[0]
        precio_total = vehiculo[5]

        print(f"{garage:<8}{precio_total:<15}")


def contar_mas_de_seis(dataset: list[list]) -> int:
    cantidad = 0
    for elem in dataset:
        if elem[3] >= 6:
            cantidad += 1
    return cantidad


def maximo_porcentaje(dataset: list[list], garages) -> None:
    total_unidades = sumar_unidades(dataset)
    max_indice = obtener_max(garages)
    porcentaje = garages[max_indice][3] / total_unidades * 100
    return [porcentaje, max_indice]


def ordenar_recaudacion(dataset, n=None):
    if n is None:
        n = len(dataset)

    if n == 1:
        return dataset

    for i in range(len(dataset)-1):
        if dataset[i][5] < dataset[i + 1][5]:
            dataset[i], dataset[i + 1] = dataset[i + 1], dataset[i]
    return ordenar_recaudacion(dataset, n - 1)



def mostrar_recaudacion_ordenada(dataset: list[list]) -> None:
    reca = ordenar_recaudacion(dataset)
    mostrar_matriz_recaudacion(reca)
