from list_data import data_tab, parametric
from func_tab import values_select, parametric_select, str_list_num

deter  = 'Скорость'
improv =  '01. Вес подвижного объекта'

res_str = values_select(data_tab, deter, improv)  # Получение значения из таблицы
res_num_list = str_list_num(res_str)  # Преобразование строки с числами в список с ними
result = parametric_select(res_num_list, parametric)  # Получение списка с параметрами
print((repr(result).strip('[]')).replace('\'', ''))


def do_search():
    res_str = values_select(data_tab, deter, improv)  # Получение значения из таблицы
    res_num_list = str_list_num(res_str)  # Преобразование строки с числами в список с ними
    result = parametric_select(res_num_list, parametric)  # Получение списка с параметрами
    return list_str(result)