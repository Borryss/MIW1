import pandas as pd
import numpy as np
from collections import Counter

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
answer_array = [[]]
global timer
timer = 0
global nott
nott = False
temp_array1 = [[]]

df = pd.DataFrame(string_array, columns=COLUMNS)

# stworzenie listy z klasami
for i in array:
    value = i[len(array[0]) - 1]
    classes_array.append(int(value))

# stworzenie listy z klasami podzielonymi na grupy
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

# stworzenie listy list list (array x3), aby rozdzielić rzędy na klasy
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

# stworzenie listy list list (array x3), aby rozdzielić klasy na kolumny (+ ostatnia kolumna)
for a in range(len(array_of_groups)):
    do_once = True
    for i in range(len(array_of_groups[a])):
        if do_once:
            temp_array1.append([])
            for h in range(len(array_of_groups[a][0])):
                temp_array1[a].append([])
                do_once = False

        for j in range(len(array_of_groups[a][i])):
            temp_array1[a][j].append(array_of_groups[a][i][j])


# stworzenie listy kolumn do sprawdzenia, czy liczby unikalne się powtarzają
array2 = [list(map(int, col)) for col in array.T]


# główny algorytm, po którym za każdym razem występuje print
def main_recursive_algorithm(column, sublist, group_of_not_banned_indexes, group_of_not_banned_columns, timer):
    global nott
    for t in sublist[:-1]:
        column += 1
        grouped = []
        grouped_indices = []
        # print(t)
        # pętla do znalezienia z [6,1,1,1] => [[6],[1,1,1]]
        for idx, val in enumerate(t):
            if idx in group_of_not_banned_indexes and column in group_of_not_banned_columns:
                added = False
                for i, group in enumerate(grouped):
                    if val in group:
                        group.append(val)
                        grouped_indices[i].append(idx)
                        added = True
                        break
                if not added:
                    grouped.append([val])
                    grouped_indices.append([idx])

        if grouped:
            # przeszukiwanie liczb powtarzających się więcej niż w 50%
            for gr1 in grouped:
                for gr2 in grouped_indices:
                    if len(group_of_not_banned_indexes) <= 2:
                        answer_array[timer].append(column)
                        answer_array[timer].append(gr1[0])
                        result = list((Counter(array2[column]) - Counter(t)).elements())
                        group_of_not_banned_columns.remove(column)
                        if gr1[0] in result:
                            if group_of_not_banned_columns:
                                resultt = main_recursive_algorithm(-1, sublist, group_of_not_banned_indexes, group_of_not_banned_columns, timer)
                                if isinstance(resultt, (int, list)):
                                    return gr2[0]
                            else:
                                nott = True
                                if len(gr2) == 1:
                                    return gr2[0]
                                else:
                                    return gr2

                        else:
                            return gr2[0]

                    if len(gr1) == len(group_of_not_banned_indexes) // 2 + 1 and len(gr2) == len(group_of_not_banned_indexes) // 2 + 1:
                        answer_array[timer].append(column)
                        answer_array[timer].append(gr1[0])
                        result = list((Counter(array2[column]) - Counter(t)).elements())
                        group_of_not_banned_columns.remove(column)
                        if gr1[0] in result:
                            resultt = main_recursive_algorithm(-1, sublist, gr2, group_of_not_banned_columns, timer)
                            if isinstance(resultt, (int, list)):
                                return gr2[0]
                        else:
                            if len(gr2) == 1:
                                return gr2[0]
                            else:
                                return gr2


# główna pętla algorytmu
for sublist in temp_array1:
    continuee = True
    must_break = False
    column = -1
    group_of_not_banned_indexes = []
    if sublist:
        for indx in range(len(sublist[0])):
            group_of_not_banned_indexes.append(indx)

    group_of_not_banned_columns = []
    if sublist:
        for indx in range(len(array2)):
            group_of_not_banned_columns.append(indx)

    if sublist:
        while continuee:
            if group_of_not_banned_indexes:
                answer_array.append([])
                resultt = main_recursive_algorithm(column, sublist, group_of_not_banned_indexes, group_of_not_banned_columns[:-1], timer)
                # nott oznacza, że kombinacja jest całkowicie sprzeczna
                if nott:
                    if isinstance(resultt, list):
                        result = ' ∧ '.join(f"(a{answer_array[timer][i] + 1} = {answer_array[timer][i + 1]})" for i in
                                            range(0, len(answer_array[timer]), 2))
                        d_chain = ' ⇒ '.join(f"(d = {x})" for x in sorted(set(classes_array)))
                        print(f"{result} ⇒ {d_chain}[{len(resultt)}]")
                        for i in resultt:
                            group_of_not_banned_indexes.remove(i)
                    else:
                        result = ' ∧ '.join(f"(a{answer_array[timer][i] + 1} = {answer_array[timer][i + 1]})" for i in
                                            range(0, len(answer_array[timer]), 2))
                        d_chain = ' ⇒ '.join(f"(d = {x})" for x in sorted(set(classes_array)))
                        print(f"{result} ⇒ {d_chain}")

                        group_of_not_banned_indexes.remove(resultt)

                    nott = False

                else:
                    if isinstance(resultt, list):
                        result = ' ∧ '.join(f"(a{answer_array[timer][i] + 1} = {answer_array[timer][i + 1]})" for i in
                                            range(0, len(answer_array[timer]), 2))
                        d_value = sublist[len(sublist) - 1][0]
                        print(f"{result} ⇒ (d = {d_value})[{len(resultt)}]")
                        for i in resultt:
                            group_of_not_banned_indexes.remove(i)
                    else:
                        result = ' ∧ '.join(f"(a{answer_array[timer][i] + 1} = {answer_array[timer][i + 1]})" for i in
                                            range(0, len(answer_array[timer]), 2))
                        d_value = sublist[len(sublist) - 1][0]
                        print(f"{result} ⇒ (d = {d_value})")
                        group_of_not_banned_indexes.remove(resultt)
            else:
                continuee = False

            timer += 1
