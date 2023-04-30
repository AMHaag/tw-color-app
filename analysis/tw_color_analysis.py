import pandas as pd
import statistics
import colorsys
import matplotlib.pyplot as plt

df = pd.read_csv('./analysis/tw_colors.csv',index_col=0)
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

for color in df['name']:
    x_values = list(df.columns)[1:]
    y_values1 = [x/256 for x in shades[color]['sat']]
    y_values2 = shades[color]['lgt']
    # # print('sat',y_values1)
    # print('lgt',y_values2)
    color_row = df[df['name']==color]
    color_500 = color_row['500'].values[0]
    
    plt.plot(x_values, y_values1, label = f'{color} sat', lw = 2, c = color_500)
    # plt.plot(x_values, y_values2, label = f'{color} lgt', lw = 2, c = color_500)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Saturation Graph')
plt.grid()
plt.legend()

plt.show()
quit(1)
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
        lgt_dict[shade_list[i]].append(shades[color]['lgt'][i])

for i, shade in enumerate(sat_dict.keys()):
    
    sat_median = statistics.median(sat_dict[shade])
    sat_mean = statistics.mean(sat_dict[shade])
    sat_stdev = statistics.stdev(sat_dict[shade])
    sat_min = min(sat_dict[shade])
    sat_max = max(sat_dict[shade])
    print(f"\033[1m Shade: \033[0m {shade}")
    print(f"Sat Median: {sat_median}  Sat Mean: {sat_mean} Sat StDev: {sat_stdev}\n Sat Min: {sat_min} Sat Max: {sat_max}")

    x = i+1
    # ax.fill_between(sat_median,sat_min,sat_max)
    plt.plot(x,sat_median,color="#000000",label='median')
    plt.plot(x,sat_median-sat_stdev,color="#ff0000",label='lower std')
    plt.plot(x,sat_median+sat_stdev,color='#00ff00',label='upper std')
    plt.plot(x,sat_min,label='min')
    plt.plot(x,sat_max,label='max')
    
    

#     plt.plot(shade_list,sat_median,label='Median')
#     plt.plot(shade_list,sat_mean,label='Mean')
#     plt.plot(shade_list,sat_min,label='Min')
#     plt.plot(shade_list,sat_max,label='Max')
    
#     plt.xlabel('Shade')
#     plt.ylabel('Saturation')
#     plt.title('Saturation stats by shade')
#     plt.grid()
#     plt.legend()
plt.show()


