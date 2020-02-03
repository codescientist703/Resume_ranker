import pandas as pd

keyword_dict = pd.read_csv('keywords.csv')

col_name = keyword_dict.columns[0].split(";")
