import pandas as pd
import numpy as np
import re
from scipy import stats
from parser_pack import parser_2
import time


class Calculations:
    """
    indexes for array:
    0 - temp
    1 - time
    2 - dsc
    3 - poris(grad)
    4 - partial_aria
    5 - conversion_rate
    6 - real_time (t)
    7 - ln(-ln(1-conversion_rate))
    8 - ln(t)
    9 - ln(d(partial_aria)/dt)
    """
    def __init__(self, **kwargs):
        self.filepath = kwargs.get('filepath', '')

        self.cool_speed = 0
        self.cool_speed_units = 'K/min'

        self.table_in_list = []
        self.temp_array = None
        self.table_array = None

        self.cristal_temp: int = 0
        self.area: int = 0

    def calculate(
        self
    ):
        with open(self.filepath, 'r', encoding='latin-1') as file:
            self.table_in_list = [bacteria.replace('\n', '') for bacteria in file]

        self.take_df()
        self.find_inflections()

        self.find_area()

        z, n, r2 = self.define_kinetic_param()
        return z, n, r2

    def take_df(
        self
    ):
        self.cool_speed, self.cool_speed_units, self.table_array = parser_2(self.table_in_list)
        self.temp_array = self.table_array[:, 0]
        self.time_array = self.table_array[:, 1]
        self.dsc_array = self.table_array[:, 2]

    def find_inflections(
            self
    ):
        grad = np.gradient(np.gradient(self.dsc_array, self.temp_array), self.temp_array)
        # 3 - grad
        self.table_array = np.c_[self.table_array, grad]
        top_mask = self.table_array[:, 2] == min(self.dsc_array)
        cristal_temp_row = self.table_array[top_mask, :][:, 0]
        self.cristal_temp = cristal_temp_row[0]
        max_temp_id = np.asarray(top_mask).nonzero()[0][0]
        first_table = self.table_array[:max_temp_id]
        second_table = self.table_array[max_temp_id:]
        firs_grad_min = min(abs(first_table[:, 3]))
        sec_grad_min = min(abs(second_table[:, 3]))
        first_min_top_mask = abs(first_table[:, 3]) == firs_grad_min
        second_min_top_mask = abs(second_table[:, 3]) == sec_grad_min
        self.first_min = first_table[first_min_top_mask]
        first_min_id = np.asarray(first_min_top_mask).nonzero()[0][0]
        self.second_min = second_table[second_min_top_mask]
        second_min_id = first_table.shape[0] + np.asarray(second_min_top_mask).nonzero()[0][0]
        self.inflection = np.r_[self.first_min, self.second_min]
        self.micro_table = self.table_array[first_min_id:second_min_id + 1]

    def find_area(
            self
    ):
        start_x = self.first_min[:, 0]
        start_y = self.first_min[:, 2]
        stop_x = self.second_min[:, 0]
        stop_y = self.second_min[:, 2]
        line_array_len = self.micro_table.shape[0]
        temp_bottom = np.linspace(start_x[0], stop_x[0], num=line_array_len)
        dsc_bottom = np.linspace(start_y[0], stop_y[0], num=line_array_len)
        partial_aria = []
        for i in range(line_array_len - 1):
            sample = self.micro_table[i]
            smaple_plus_one = self.micro_table[i + 1]
            h = abs(np.average([sample[2], smaple_plus_one[2]]) - np.average(
                [dsc_bottom[i], dsc_bottom[i+1]]))
            a = smaple_plus_one[0] - sample[0]
            self.area += a * h
            partial_aria.append(self.area)
        partial_aria = np.append([0], np.asarray(partial_aria))
        # 4 - partial_aria
        self.micro_table = np.c_[self.micro_table, partial_aria]
        conversion_rate = 1 - partial_aria / self.area
        # 5 - conversion_rate
        self.micro_table = np.c_[self.micro_table, conversion_rate]

        t_onset = self.micro_table[:, 1][-1]
        t_list = self.micro_table[:, 1] - t_onset
        # 6 - real_time
        self.micro_table = np.c_[self.micro_table, t_list]
        return self.area, self.micro_table

    def define_kinetic_param(
            self
    ):
        self.micro_table = self.micro_table[1:-1]
        ln_min_ln_conversion_rate = np.log(-np.log(1 - self.micro_table[:, 5]))
        ln_time = np.log(abs(self.micro_table[:, 6]))
        # 7 - ln_min_ln_conversion_rate
        # 8 - ln_time
        self.micro_table = np.c_[self.micro_table, ln_min_ln_conversion_rate, ln_time]
        self.micro_table = self.micro_table[~np.isinf(self.micro_table).any(1)]
        res = stats.linregress(self.micro_table[:, 8], self.micro_table[:, 7])
        z = np.exp(res.intercept/self.cool_speed)
        n = res.slope
        r2 = res.rvalue ** 2
        time = self.micro_table[:, 1]
        con_rate = self.micro_table[:, 5]
        grad = np.gradient(con_rate, time)
        ln_partial_aria_per_time = np.log(abs(grad))
        # 9 - ln_Partial_aria_per_Time
        self.micro_table = np.c_[self.micro_table, ln_partial_aria_per_time]
        return z, n, r2


if __name__ == "__main__":
    start_time = time.time()
    r = Calculations(filepath='data/PBS_15Kmin.txt').calculate()
    end_time = time.time()
    print(end_time - start_time)
