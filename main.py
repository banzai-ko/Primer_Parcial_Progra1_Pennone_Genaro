"""
    _summary_ Entrada del programa
    """

from UTN_Heroes_Dataset.utn_pp import get_original_matrix
from interface.interface import menu_principal

if __name__ == '__main__':
    dataset = get_original_matrix()
    menu_principal(dataset)
