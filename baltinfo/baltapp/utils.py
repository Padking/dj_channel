from random import randint


def random_id():
    """ Создаёт ID канала"""
    first = randint(10**7, 90**7)
    last = randint(1, 9)
    return f"-{first}{last}"


def convert(structure, mod_struct=None):

    """
    Преобразует структуру данных
    :param structure: list
    :return mod_struct: list of tuples
    """

    mod_struct = mod_struct or []

    for elem in structure:
        new_elem = (random_id(), f"@{elem}", "proba")
        mod_struct.append(new_elem)
    
    return mod_struct
