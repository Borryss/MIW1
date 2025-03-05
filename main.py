import itertools
import numpy as np
import pandas as pd

# Dane systemu decyzyjnego
data = [
    ["Deszczowa", "Goraco", "Wysoka", "Slaby", "Tak"],
    ["Pochmurna", "Lagodnie", "Wysoka", "Slaby", "Tak"],
    ["Sloneczna", "Chlodno", "Wysoka", "Mocny", "Tak"],
    ["Sloneczna", "Goraco", "Wysoka", "Mocny", "Tak"],
    ["Pochmurna", "Goraco", "Normalna", "Mocny", "Tak"],
    ["Sloneczna", "Chlodno", "Wysoka", "Slaby", "Tak"],
    ["Deszczowa", "Goraco", "Wysoka", "Mocny", "Tak"],
    ["Deszczowa", "Chlodno", "Wysoka", "Mocny", "Tak"],
    ["Deszczowa", "Lagodnie", "Normalna", "Mocny", "Tak"],
    ["Deszczowa", "Lagodnie", "Wysoka", "Mocny", "Nie"],
    ["Sloneczna", "Chlodno", "Normalna", "Mocny", "Nie"],
    ["Deszczowa", "Lagodnie", "Normalna", "Slaby", "Nie"],
    ["Pochmurna", "Goraco", "Wysoka", "Slaby", "Nie"],
    ["Sloneczna", "Goraco", "Normalna", "Mocny", "Nie"]
]


attributes = ["Pogoda", "Temperatura", "Wilgotnosc", "Wiatr", "Decyzja"]
df = pd.DataFrame(data, columns = attributes)


# Algorytm pokrywający (Sequential Covering)
def covering_algorithm(df):

    rules = []
    used_rows = set()

    for index, row in df.iterrows():
        print(f"Row{index}: {row}")
        if index in used_rows:
            print(f"Index in used ROWS!: {index}")
            continue

        conditions = [(attr, row[attr]) for attr in attributes[:-1]]
        print(f"Conditions{index}: {conditions}")
        decision = row["Decyzja"]

        rule = {"conditions": conditions, "decision": decision}
        print(f"Rule{index}: {rule}")
        rules.append(rule)

        used_rows.add(index)

    return rules


# Algorytm wyliczania reguł decyzyjnych
def decision_rules(df):
    rules = []

    for index, row in df.iterrows():
        conditions = [(attr, row[attr]) for attr in attributes[:-1]]
        decision = row["Decyzja"]
        rule = {"conditions": conditions, "decision": decision}
        rules.append(rule)

    return rules


# Wyniki
print("Reguły pokrywające:")
print(covering_algorithm(df))

print("Reguły decyzyjne:")
print(decision_rules(df))

def
