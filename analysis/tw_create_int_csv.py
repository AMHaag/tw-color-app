import pandas as pd
import statistics
import colorsys
import matplotlib.pyplot as plt

df = pd.read_csv('./analysis/tw_colors.csv', index_col=0)
# print(df)
df2 = pd.read_csv('./analysis/tw_colors.csv', index_col=0)

for x, row in df.iterrows():

    print(row['name'])
    for y, shade in enumerate(row.keys()):
        if shade == 'name':
            continue
        hexcode = row[shade]
        int_code = int(hexcode[1:], 16)
        print(f'{hexcode} -- {int_code}')
        df2.iloc[x,y] = int_code
print(df2)
df2.to_csv('./analysis/tw_colors_int.csv')

