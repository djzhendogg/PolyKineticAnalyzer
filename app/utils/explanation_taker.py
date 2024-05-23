from .texts import (
    n_1, n_2, n_3, n_4
)


def n_explanation(n):
    if int(n) <= int(1):
        return n_1
    elif int(n) == int(2):
        return n_2
    elif int(n) == 3:
        return n_3
    elif int(n) >= 4:
        return n_4
