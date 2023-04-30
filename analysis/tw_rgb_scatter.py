import pandas as pd
import statistics
import colorsys
import matplotlib.pyplot as plt

df = pd.read_csv('./analysis/tw_colors.csv', index_col=0)
print(df)

rgb_in_list = []
x_list = []
for i, row in df.iterrows():
    for shade in row.keys():
        if shade == 'name':
            continue
        hexcode = row[shade]
        rgb_int = int(hexcode[1:],16)
        rgb_in_list.append(rgb_int)
        x_list.append(1)
        
x_coords = range(len(rgb_in_list))
plt.scatter(rgb_in_list,x_list)
plt.grid()
plt.show()