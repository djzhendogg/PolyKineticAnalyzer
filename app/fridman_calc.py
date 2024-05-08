import pandas as pd
import numpy as np
from scipy import stats


def fridman_calculations(calculation_results: list[dict]):
    fin_dict: dict[str, dict[str, list]] = {}
    conv_rate_base = np.arange(0.1, 0.8 + 0.01, 0.05)
    for conv_rate_base_id in conv_rate_base:
        fin_dict[str(round(conv_rate_base_id, 2))] = {
            'x': [],
            'y': [],
            'm': [],
            'energy': []
        }

    for pull in calculation_results:
        x_conrate = pull['cl'].trimmed['Conversion_rate'].to_numpy()
        y_temp = pull['cl'].trimmed['Temp'].to_numpy()

        conrate_temp_polifit_param = np.polyfit(x_conrate, y_temp, 4)
        conrate_temp_polifit_param_func = np.poly1d(conrate_temp_polifit_param)
        y_temp_new = conrate_temp_polifit_param_func(conv_rate_base)
        db_new = pd.DataFrame()
        db_new['Conversion_rate'] = conv_rate_base
        db_new['Temp'] = y_temp_new

        x_temp = 1000 / y_temp_new
        y_ln_area_per_time = pull['cl'].trimmed['ln_Partial_aria_per_Time'].to_numpy()

        ln_area_per_time_temp_polifit_param = np.polyfit(x_temp, y_ln_area_per_time, 3)
        ln_area_per_time_temp_polifit_param_func = np.poly1d(ln_area_per_time_temp_polifit_param)
        x_new = 1000 / db_new['Temp'].to_numpy()
        y_new = ln_area_per_time_temp_polifit_param_func(x_new)

        for num, (y_num, x_num) in zip(conv_rate_base, (zip(y_new, x_new))):
            str_num = str(round(num, 2))
            fin_dict.get(str_num).get('x').append(x_num)
            fin_dict.get(str_num).get('y').append(y_num)
    out_energy = 0
    for key, value in fin_dict.items():
        x = value.get('x')
        y = value.get('y')
        m, b = np.polyfit(x, y, 1)
        res = stats.linregress(x, y)
        energy = res.slope / 8.314
        out_energy += energy
        fin_dict.get(key).get('m').append(m)
        fin_dict.get(key).get('b').append(b)
        fin_dict.get(key).get('energy').append(energy)
    return fin_dict, out_energy
