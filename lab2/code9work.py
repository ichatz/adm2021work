"""
Your module description
"""
import pandas as pd

dataset2 = pd.read_json("2020-Jan.json", lines=True, nrows=20)

print(dataset2[dataset2.price > 100])