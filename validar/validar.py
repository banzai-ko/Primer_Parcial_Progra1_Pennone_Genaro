def validar_entrada(minimo: int, maximo: int):
    """
     funcion de validacion entrada usuario

    Arguments:
        minimo -- _val minimo_
        maximo -- _valor maximo_

    Returns:
        _description_
    """

    entrada = input(f"Elija una opcion: entre {minimo} y {maximo}: ")
    if not entrada or not entrada.isdigit() or not (minimo <= int(entrada) <= maximo):
        return validar_entrada(minimo, maximo)

    return int(entrada)
