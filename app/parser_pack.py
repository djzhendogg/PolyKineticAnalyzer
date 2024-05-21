import numpy as np
import re


def valid_units(
    table_time_unit: str,
    rate_time_unit: str,
    table_temp_unit: str
):
    rate_time_sec = False
    temp_k = False
    temp_c = False
    min_bool = False
    table_time_sec = False
    if table_time_unit == 'min' and table_time_unit == rate_time_unit:
        min_bool = True
    else:
        if table_time_unit != 'min':
            table_time_sec = True
        elif rate_time_unit != 'min':
            rate_time_sec = True

    if table_temp_unit == "C":
        temp_c = True
    elif table_temp_unit == "K":
        temp_k = True
    return min_bool, table_time_sec, rate_time_sec, temp_c, temp_k


def valid_dsc_unit(dsc_unit):
    dsc_unit_list = dsc_unit.split('/')
    if dsc_unit_list[0][0] == dsc_unit_list[1][0]:
        dsk_unit_ok = True
    return dsk_unit_ok


def parser_2(
    dsc_list: list[str]
):
    for num, i in enumerate(dsc_list):
        if '#RANGE:' in i:
            range_num = num
        elif '##Temp./' in i:
            num_of_table = num
            break
    range_str = dsc_list[range_num]
    range_list = range_str.split('/')
    range_list_1 = range_list[1].split('(')
    rate_time_unit = range_list[2].replace(')', "")
    rate_num = float(range_list_1[0])

    unit_list = dsc_list[num_of_table].split(';')
    measer_units = {}

    symbols_to_remove = "#.()"
    for measer in unit_list:
        spl_un = measer.split('/')
        name = spl_un[0]
        for symbol in symbols_to_remove:
            name = name.replace(symbol, "")
        if name == 'Temp':
            measer_units[name] = spl_un[1][1]
        elif name == 'DSC' or name == 'Sensit':
            val = spl_un[1] + '/' + spl_un[2]
            for symbol in symbols_to_remove:
                val = val.replace(symbol, "")
            measer_units[name] = val
        else:
            measer_units[name] = spl_un[1]

    # dsc_ok = valid_dsc_unit(measer_units['DSC'])

    min_bool, table_time_sec, rate_time_sec, temp_c, temp_k = valid_units(
        measer_units['Time'], rate_time_unit, measer_units['Temp']
    )
    if rate_time_sec:
        rate_num *= 60

    table_rows = dsc_list[num_of_table + 1:]
    rows_in_rows = []
    for i in table_rows:
        row = []
        a = i.split(';')
        if len(a) < 4:
            continue
        for y in a:
            y = re.sub(r"\s+", "", y)
            try:
                y = float(y)
            except:
                z = y.split('e')
                number = float(z[0])
                level = int(z[1])
                y = number ** level
            row.append(y)
        rows_in_rows.append(row)
    rows_array = np.array(rows_in_rows)
    if temp_k:
        rows_array[:, 0] -= float(273.15)
    if table_time_sec:
        rows_array[:, 1] /= 60
    return rate_num, rows_array[:, :3]


if __name__ == "__main__":
    with open(r'data/PBS_10Kmin.txt', 'r', encoding='latin-1') as file:
        table_in_list = [bacteria.replace('\n', '') for bacteria in file]
    rate, table_array = parser_2(table_in_list)
    print(rate)
    print(table_array)

