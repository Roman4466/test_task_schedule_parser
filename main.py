import pandas as pd

from xlxs_parcer import analyze

file_path = 'data/3.xlsx'
df = pd.read_excel(file_path, header=None)

analyze(df)