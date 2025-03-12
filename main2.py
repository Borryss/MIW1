import pandas as pd
import numpy as np

def convert_to_strings(array):
    return np.array([[str(val) for val in row] for row in array])

array = np.array([
    [1, 1, 1, 1, 3, 1, 1],
    [1, 1, 1, 1, 3, 2, 1],
    [1, 1, 1, 3, 2, 1, 0],
    [1, 1, 1, 3, 3, 2, 1],
    [1, 1, 2, 1, 2, 1, 0],
    [1, 1, 2, 1, 2, 2, 1],
    [1, 1, 2, 2, 3, 1, 0],
    [1, 1, 2, 2, 4, 1, 1]
])

string_array = convert_to_strings(array)

# Створення DataFrame
COLUMNS = ["Row1", "Row2", "Row3", "Row4", "Row5", "Row6", "Row7"]
COLUMNS2 = ["Row1", "Row2", "Row3", "Row4", "Row5", "Row6"]
answer = []
blocked_row = []
df = pd.DataFrame(string_array, columns=COLUMNS)
again = True
again2 = True
da = 1




for j in range(len(df)):
    again2 = True
    if j in blocked_row:
        continue
    else:
        for valuek in COLUMNS2:
            first_value = df[valuek].iloc[j]
            first_decision = df[COLUMNS[len(COLUMNS2)]].iloc[j]
            if not again2:
                break
            else:
                if again:
                    print(f"DLA WARTOSCI: {first_value} {first_decision}")
                    again = False
                    for i in range(len(df)):
                        kolumna = df.iloc[i][valuek]
                        decyzja = df.iloc[i][COLUMNS[len(COLUMNS2)]]
                        if kolumna == first_value:
                            print(f"Badanie: Kolumna = {kolumna}, Decyzja = {decyzja}")
                            if decyzja != first_decision:
                                print(f"Nie znaleziono dopasowania: Kolumna = {kolumna}, Decyzja = {decyzja}")
                                print("\n")
                                again = True
                                break

                    if not again:
                        print(f"Znaleziono dopasowanie: Kolumna = {first_value}, Decyzja = {first_decision}")
                        answer.append(first_value + first_decision)
                        for i in range(len(df)):
                            kolumna = df.iloc[i][valuek]
                            decyzja = df.iloc[i][COLUMNS[len(COLUMNS2)]]
                            if kolumna == first_value:
                                if i not in blocked_row:
                                    blocked_row.append(i)
                        again2 = False
                        print("\n")
                        print("\n")
                else:
                    break

            again = True




print("\n")
print(answer)
print("\n")

for j in range(len(df)):
    again2 = True
    if j in blocked_row:
        continue
    else:
        for vi in range(len(COLUMNS2) - 1):
            for vik in range(vi+1,len(COLUMNS2)):
                first_value1 = df[COLUMNS2[vi]].iloc[j]
                first_decision = df[COLUMNS[len(COLUMNS2)]].iloc[j]
                first_value2 = df[COLUMNS2[vik]].iloc[j]
                if not again2:
                    break
                else:
                    if again:
                        print(f"DLA WARTOSCI: {first_value1} {first_value2} {first_decision}")
                        again = False
                        for i in range(len(df)):
                            kolumna1 = df.iloc[i][COLUMNS2[vi]]
                            decyzja = df.iloc[i][COLUMNS[len(COLUMNS2)]]
                            kolumna2 = df.iloc[i][COLUMNS2[vik]]
                            if kolumna1 + kolumna2 == first_value1 + first_value2:
                                print(f"Badanie: Kolumna1 = {kolumna1}, Kolumna2 = {kolumna2}, Decyzja = {decyzja}")
                                if decyzja != first_decision:
                                    print(
                                        f"Nie znaleziono dopasowania: Kolumna1 = {kolumna1}, Kolumna2 = {kolumna2}, Decyzja = {decyzja}")
                                    print("\n")
                                    again = True
                                    break

                        if not again:
                            print(
                                f"Znaleziono dopasowanie: Kolumna1 = {first_value1}, Kolumna2 = {first_value2}, Decyzja = {first_decision}")
                            answer.append(first_value1 + first_value2 + first_decision)
                            for i in range(len(df)):
                                kolumna1 = df.iloc[i][COLUMNS2[vi]]
                                decyzja = df.iloc[i][COLUMNS[len(COLUMNS2)]]
                                kolumna2 = df.iloc[i][COLUMNS2[vik]]
                                if kolumna1 + kolumna2 == first_value1 + first_value2:
                                    if i not in blocked_row:
                                        blocked_row.append(i)
                            again2 = False
                            print("\n")
                            print("\n")

                    else:
                        break

                again = True

print("\n")
print(answer)