import pandas as pd
import numpy as np
from scipy import stats


def find_inflections(
    table: pd.DataFrame
):
    x = table['Temp'].to_numpy()
    y = table['DSC'].to_numpy()
    grad = np.gradient(np.gradient(y, x), x)
    table['Prois'] = grad
    max_temp_id = table[table['DSC'] == min(table['DSC'])]['Temp'].index[0]
    first_min = table[table['Prois'] == min(table.iloc[:max_temp_id]['Prois'])]
    second_min = table[table['Prois'] == min(table.iloc[max_temp_id:]['Prois'])]
    inflection = pd.concat([first_min, second_min])
    return inflection


def find_area(
    inflection,
    table,
    cool_speed
):
    covered_energy_border_id = inflection.index.to_list()
    micro_table = table[covered_energy_border_id[0]:covered_energy_border_id[1] + 1]
    line_array_len = micro_table.shape[0]
    start_x = micro_table['Temp'].loc[covered_energy_border_id[0]]
    start_y = micro_table['DSC'].loc[covered_energy_border_id[0]]
    stop_x = micro_table['Temp'].loc[covered_energy_border_id[1]]
    stop_y = micro_table['DSC'].loc[covered_energy_border_id[1]]
    micro_table['Temp_bottom'] = np.linspace(start_x, stop_x, num=line_array_len)
    micro_table['DSC_bottom'] = np.linspace(start_y, stop_y, num=line_array_len)
    area = 0
    partial_aria = []
    for i in range(line_array_len - 1):
        sample = micro_table.iloc[i]
        smaple_plus_one = micro_table.iloc[i + 1]
        h = abs(np.average([sample['DSC'], smaple_plus_one['DSC']]) - np.average(
            [sample['DSC_bottom'], smaple_plus_one['DSC_bottom']]))
        a = smaple_plus_one['Temp'] - sample['Temp']
        area += a * h / cool_speed
        partial_aria.append(area)
    micro_table['Partial_aria'] = [0] + partial_aria
    micro_table['Conversion_rate'] = micro_table['Partial_aria'] / area
    return area, micro_table


def define_kinetic_param(
micro_table
):
    micro_table = micro_table[micro_table['Conversion_rate'] >= 0.1]
    micro_table = micro_table[micro_table['Conversion_rate'] <= 0.8]
    micro_table['ln_min_ln_Conversion_rate'] = np.log(-np.log(1 - micro_table['Conversion_rate']))
    micro_table['ln_Time'] = np.log(micro_table['Time'])
    res = stats.linregress(micro_table['ln_Time'].to_numpy(), micro_table['ln_min_ln_Conversion_rate'].to_numpy())
    # z = np.exp(res.intercept)
    z = res.intercept
    n = res.slope
    return z, n
