import pandas as pd
import statistics
import colorsys
import matplotlib.pyplot as plt

df = pd.read_csv('./analysis/tw_colors.csv', index_col=0)
print(df)

# TODO Find the average, median and stdev of S&L for each shade


reds = []
greens = []
blues = []
shades = dict()

for i, row in df.iterrows():
    shades[row['name']] = {}
    shades[row['name']]['hue'] = []
    shades[row['name']]['sat'] = []
    shades[row['name']]['lgt'] = []
    for shade in row.keys():
        if shade == 'name':
            continue
        hexcode = row[shade]
        rgb = tuple(int(hexcode[i+1:i+3], 16) for i in (0, 2, 4))
        hsl = hsl = colorsys.rgb_to_hls(*rgb)
        print(hsl)
        shades[row['name']]['hue'].append(hsl[0])
        shades[row['name']]['sat'].append(hsl[1])
        shades[row['name']]['lgt'].append(hsl[2])
        

for color in df['name']:
    x_values = list(df.columns)[1:]
    y_values1 = [x/256 for x in shades[color]['sat']]
    y_values2 = shades[color]['lgt']
    # # print('sat',y_values1)
    # print('lgt',y_values2)
    color_row = df[df['name'] == color]
    color_500 = color_row['500'].values[0]

    plt.plot(x_values, y_values1, label=f'{color} sat', lw=2, c=color_500)
    # plt.plot(x_values, y_values2, label = f'{color} lgt', lw = 2, c = color_500)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Sat Graph')
plt.grid()
plt.legend()

plt.show()
