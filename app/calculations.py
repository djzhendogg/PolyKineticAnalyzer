import pandas as pd
import numpy as np
import re
from scipy import stats


class Calculations:
    def __init__(self, **kwargs):
        self.filepath = kwargs.get('filepath', '')
        self.cool_speed = kwargs.get('cool_speed', '')
        self.table_in_list = []
        self.table = pd.DataFrame(columns=['Temp', 'Time', 'DSC'])

    def calculate(
        self
    ):
        with open(self.filepath, 'r', encoding='latin-1') as file:
            self.table_in_list = [bacteria.replace('\n', '') for bacteria in file]

        self.cool_speed = self.cool_speed / 60

        self.parser()
        self.find_inflections()

        self.find_area()

        z, n, r2 = self.define_kinetic_param()
        return z, n, r2

    def parser(
        self
    ) -> pd.DataFrame:
        num_of_table = 0
        for i in self.table_in_list:
            if '##Temp./' in i:
                break
            else:
                num_of_table += 1

        table_rows = self.table_in_list[num_of_table + 1:]

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
        self.table['Temp'] = rows_array[:, 0] + 273.15
        self.table['Time'] = rows_array[:, 1]
        self.table['DSC'] = rows_array[:, 2]

    def find_inflections(
            self
    ):
        x = self.table['Temp'].to_numpy()
        y = self.table['DSC'].to_numpy()
        grad = np.gradient(np.gradient(y, x), x)
        self.table['Prois'] = grad
        max_temp_id = self.table[self.table['DSC'] == min(self.table['DSC'])]['Temp'].index[0]
        first_table = self.table.iloc[:max_temp_id]
        second_table = self.table.iloc[max_temp_id:]
        first_min = first_table[abs(first_table['Prois']) == min(abs(first_table['Prois']))].iloc[0].to_frame().T
        second_min = second_table[abs(second_table['Prois']) == min(abs(second_table['Prois']))].iloc[0].to_frame().T
        self.inflection = pd.concat([first_min, second_min])

    def find_area(
            self
    ):
        covered_energy_border_id = self.inflection.index.to_list()
        self.micro_table = self.table[covered_energy_border_id[0]:covered_energy_border_id[1] + 1]
        line_array_len = self.micro_table.shape[0]
        start_x = self.micro_table['Temp'].loc[covered_energy_border_id[0]]
        start_y = self.micro_table['DSC'].loc[covered_energy_border_id[0]]
        stop_x = self.micro_table['Temp'].loc[covered_energy_border_id[1]]
        stop_y = self.micro_table['DSC'].loc[covered_energy_border_id[1]]
        self.micro_table['Temp_bottom'] = np.linspace(start_x, stop_x, num=line_array_len)
        self.micro_table['DSC_bottom'] = np.linspace(start_y, stop_y, num=line_array_len)
        area = 0
        partial_aria = []
        for i in range(line_array_len - 1):
            sample = self.micro_table.iloc[i]
            smaple_plus_one = self.micro_table.iloc[i + 1]
            h = abs(np.average([sample['DSC'], smaple_plus_one['DSC']]) - np.average(
                [sample['DSC_bottom'], smaple_plus_one['DSC_bottom']]))
            a = smaple_plus_one['Temp'] - sample['Temp']
            area += a * h / self.cool_speed
            partial_aria.append(area)
        self.micro_table['Partial_aria'] = [0] + partial_aria
        self.micro_table['Conversion_rate'] = self.micro_table['Partial_aria'] / area
        t_onset = self.micro_table['Time'].iloc[0]

        t_list = []
        for t in self.micro_table['Time'].to_list():
            t_list.append((t_onset - t) / self.cool_speed)

        self.micro_table['t'] = t_list
        return area, self.micro_table

    def define_kinetic_param(
            self
    ):
        self.trimmed = self.micro_table[self.micro_table['Conversion_rate'] >= 0.1]
        self.trimmed = self.trimmed[self.trimmed['Conversion_rate'] <= 0.8]
        self.trimmed['ln_min_ln_Conversion_rate'] = np.log(-np.log(1 - self.trimmed['Conversion_rate']))
        self.trimmed['ln_Time'] = np.log(self.trimmed['t'])
        res = stats.linregress(self.trimmed['ln_Time'].to_numpy(), self.trimmed['ln_min_ln_Conversion_rate'].to_numpy())
        z = np.exp(res.intercept)
        n = res.slope
        r2 = res.rvalue ** 2
        return z, n, r2


if __name__ == "__main__":
    r = Calculations(filepath='data/PBS_20Kmin.txt', cool_speed=20).calculate()
    print(r)
