from functions import (
    find_area,
    find_inflections,
    define_kinetic_param
)
from parser import parser


def calculate(
    file_name: str
):
    with open(file_name, 'r', encoding='latin-1') as file:
        common_bacterias = [bacteria.replace('\n', '') for bacteria in file]

    cool_speed = 20
    cool_speed = cool_speed / 60

    table = parser(common_bacterias)
    inflection_table = find_inflections(table)

    area, final_table = find_area(
        inflection_table,
        table,
        cool_speed
    )

    z, n, r2 = define_kinetic_param(final_table)
    return z, n, r2


if __name__ == "__main__":
    r = calculate('data/PBS_20Kmin.txt')
    print(r)