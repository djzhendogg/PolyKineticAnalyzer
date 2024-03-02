import pandas as pd
import numpy as np
import re

def parser(
    common_bacterias: list[str]
) -> pd.DataFrame:
    num_of_table = 0
    for i in common_bacterias:
        if '##Temp./' in i:
            break
        else:
            num_of_table += 1

    table = pd.DataFrame(columns=['Temp', 'Time', 'DSC', 'Sensit'])

    table_rows = common_bacterias[num_of_table + 1:]

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
    table['Temp'] = rows_array[:, 0] + 273.15
    table['Time'] = rows_array[:, 1]
    table['DSC'] = rows_array[:, 2]
    return table
