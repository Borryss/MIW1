import pandas as pd
import numpy as np
from itertools import combinations
from collections import Counter

import re


def convert_to_strings(array):
    return np.array([[str(val) for val in row] for row in array])

array = np.array([

        [2, 6, 1, 2, 3, 1],
        [1, 1, 1, 3, 2, 1],
        [2, 1, 1, 2, 3, 1],
        [4, 1, 3, 1, 2, 1],
        [3, 5, 2, 1, 3, 2],
        [3, 1, 3, 1, 1, 2],
        [1, 1, 1, 3, 1, 2]

])


string_array = convert_to_strings(array)

def generate_columns(array):
    return [f"a{i+1}" for i in range(array.shape[1] - 1)] + ["d"]


COLUMNS = generate_columns(array)
COLUMNS2 = COLUMNS[:-1].copy()
classes_array = []
classes_arrays = []
array_of_groups = []
temp_array1 = [[],[], []]

df = pd.DataFrame(string_array, columns=COLUMNS)


# stwozenie listy z klasami
for i in array:
    value = i[len(array[0]) - 1]
    classes_array.append(int(value))



# stwozenie podzielonej na grupy listy z klasami
for i in classes_array:
    added = False
    if not classes_arrays:
        classes_arrays.append([i])
        continue
    else:
        for j in classes_arrays:
            if i in j:
                j.append(i)
                added = True
                break
            else:
                continue
        if not added:
            classes_arrays.append([i])
            continue



# stwozenie listy z listami list (array x3) , zeby rozdzielic na clasy kazdy rzed
for k in range(len(classes_arrays)):
    # print(classes_arrays[k])
    first = True
    for u in range(len(df)):
        if int(df[COLUMNS[len(COLUMNS2)]].iloc[u]) in classes_arrays[k]:
            if first:
                array_of_groups.append([array[u].tolist()])
                first = False
            else:
                array_of_groups[k].append(array[u].tolist())


print(array_of_groups)

for a in range(len(array_of_groups)):
    do_once = True
    # print(array_of_groups[a])

    for i in range(len(array_of_groups[a])):
        # print(array_of_groups[a][i])
        """DOROBY MECHANIZM STWOZENIA DOdATKOWYCH POL DLA TEMP_ARRAY"""
        # if do_once:
        #     for h in range(len(array_of_groups[a]) - 1):
        #         print(f"for ")
        #         print(f"h is : {h}")
        #         temp_array1.append([])
        #         do_once = False
        for j in range(len(array_of_groups[a][i])):
            temp_array1.append([])
            temp_array1[j].append(array_of_groups[a][i][j])


print(temp_array1)





