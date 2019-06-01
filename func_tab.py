from list_data import data_tab, parametric


# Todo 1) function values_select
def values_select(didict: dict, deter: str, improv: str) -> str:
    """ #Функция выбора значения из словаря словарей, на входе словарь словарей и две строки,
    #на выходе срока со значением словар
    >>> values_select({'1': {'2': 'dva'}}, '1', '2' )
    'dva'
    >>> values_select(data_tab, 'Вес подвиж-ного объекта', '03. Длина подвижного объекта')
    '8, 15, 29, 34'
    >>> values_select(data_tab, 'Сила', '10. Сила')
    ''
    >>> values_select(data_tab, 'Сила', 'Сила')
    'not found'
    >>> values_select(data_tab, "10. Сила", "Сила")
    'not found'
    """
    if deter in didict and improv in didict[deter]:
        return didict[deter][improv]
    return 'not found'


# Todo 2) function parametric_select
def parametric_select(lst: list, parametr: dict) -> list:
    """# Выборка значения из словаря по нескольким ключам
    # на входе лист с ключами и словарь, а выходе список ключей словаря
    >>> parametric_select([8, 15, 29, 34], {8: 'd', 15: 'f', 29: 'g', 34: 'h'})
    ['d', 'f', 'g', 'h']
    >>> parametric_select([1, 2], parametric)
    ['Дробление', 'Вынесение']
    >>> parametric_select([''], parametric)
    ['not values']
    >>> parametric_select(['-'], parametric)
    ['not values']
    >>> parametric_select([], parametric)
    ['not values']
    >>> parametric_select([41, 51], parametric)
    ['not values', 'not values']
    """
    issue_list = []
    if lst:
        for i in lst:
            try:
                if i in list(parametr.keys()):
                    issue_list.append(parametr[i])

                else:
                    issue_list.append('not values')
            except KeyError:
                issue_list.append('not values')
    else:
        issue_list.append('not values')

    return issue_list


# Todo 3) function str_list_num

def str_list_num(string: str) -> list:
    """ # Функция преобразует строку с цифрами в список, на входе строка, на выходе список
    >>> str_list_num('8, 15, 29, 34')
    [8, 15, 29, 34]
    >>> str_list_num('8')
    [8]
    >>> str_list_num('8. 12, 13')
    [8, 12, 13]
    >>> str_list_num('-')
    []
    >>> str_list_num('')
    []
    """
    l = []
    string = string.replace('.', ',')
    if string in ('-', ''):
        l = []
    else:
        l = string.split(', ')
        for i in range(len(l)):
            if l[i].isdigit():
                l[i] = int(l[i])
            else:
                return l

    return l


# Todo 4) func Преобразует список параметров в строку без апострофов
def list_str(result):
    return (repr(result).strip('[]')).replace('\'', '')

def search_tab(deter, improv):
    res_str = values_select(data_tab, deter, improv)  # Получение значения из таблицы
    res_num_list = str_list_num(res_str)  # Преобразование строки с числами в список с ними
    result = parametric_select(res_num_list, parametric)  # Получение списка с параметрами
    return list_str(result)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
