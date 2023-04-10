import pandas as pd
import statistics
import colorsys
import matplotlib.pyplot as plt

df = pd.read_csv('./tw_colors.csv',index_col=0)
print(df)

#TODO Find the average, median and stdev of S&L for each shade




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
        if shade == 'name':continue
        hexcode = row[shade]
        rgb = tuple(int(hexcode[i+1:i+3], 16) for i in (0, 2, 4))
        hsl = hsl = colorsys.rgb_to_hls(*rgb)
        shades[row['name']]['hue'].append(hsl[0])
        shades[row['name']]['sat'].append(hsl[1])
        shades[row['name']]['lgt'].append(hsl[2])

# for color in df['name']:
#     x_values = list(df.columns)[1:]
#     y_values1 = [x/256 for x in shades[color]['sat']]
#     y_values2 = shades[color]['lgt']
#     # # print('sat',y_values1)
#     # print('lgt',y_values2)
#     color_row = df[df['name']==color]
#     color_500 = color_row['500'].values[0]
    
#     plt.plot(x_values, y_values1, label = f'{color} sat', lw = 2, c = color_500)
#     # plt.plot(x_values, y_values2, label = f'{color} lgt', lw = 2, c = color_500)
# plt.xlabel('X values')
# plt.ylabel('Y values')
# plt.title('Two lines on one graph')
# plt.grid()
# plt.legend()

# plt.show()
shade_list = ["50","100","200","300","400","500","600","700","800","900","950"]
hue_dict = { "50": [], "100": [], "200": [], "300": [
], "400": [], "500": [], "600": [], "700": [], "800": [], "900": [], "950": []}
sat_dict = { "50": [], "100": [], "200": [], "300": [
], "400": [], "500": [], "600": [], "700": [], "800": [], "900": [], "950": []}
lgt_dict = { "50": [], "100": [], "200": [], "300": [
], "400": [], "500": [], "600": [], "700": [], "800": [], "900": [], "950": []}


for color in shades.keys():
    for i in range(11):
        hue_dict[shade_list[i]].append(shades[color]['hue'][i])
        sat_dict[shade_list[i]].append(shades[color]['sat'][i])
        lgt_dict[shade_list[i]].append(shades[color]['sat'][i])

for shade in sat_dict.keys():
    
    x_median = statistics.median(sat_dict[shade])
    x_mean = statistics.mean(sat_dict[shade])
    x_stdev = statistics.stdev(sat_dict[shade])
    x_min = min(sat_dict[shade])
    x_max = max(sat_dict[shade])
    print('Stop')
    # plt.plot(shade_list,x_median,label='Median')
    # plt.plot(shade_list,x_mean,label='Median')
    # plt.plot(shade_list,x_min,label='Median')
    # plt.plot(shade_list,x_max,label='Median')
    
    # plt.xlabel('Shade')
    # plt.ylabel('Saturation')
    # plt.title('Saturation stats by shade')
    # plt.grid()
    # plt.legend()
    # plt.show()


