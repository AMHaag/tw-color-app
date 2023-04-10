import pandas as pd

with open('./raw_scrape.txt') as f:
    raw_text = f.read()

raw_text = raw_text.split(";")

cols = {"name":[],"50":[],"100":[],"200":[],"300":[],"400":[],"500":[],"600":[],"700":[],"800":[],"900":[],"950":[]}

df = pd.DataFrame(cols)

for i, raw_color in enumerate(raw_text):
    if i == 242:break
    color_name = raw_color.split("\t")[0]
    shade = color_name.split("-")[2]
    color_name = color_name.split('-')[1]
    
    hex_code = raw_color.split("\t")[1]
    hex_code = hex_code.split(" ")[1]
    # hex_code = hex_code[:-1]
    
    if not df['name'].isin([color_name]).any():
        new_row = {"name":color_name,shade:hex_code}
        df.loc[len(df)] = new_row
    else:
        df.loc[df['name'] == color_name, shade] = hex_code
    

print(df)
df.to_csv('./tw_colors.csv')