import pandas as pd
from pprint import pprint
import colorsys


class PaletteGenerator():
    def __init__(self,hex_input:str) -> None:
        self.input = hex_input
        self.tw_hex = pd.read_csv('./analysis/tw_colors.csv', index_col=0)
        self.tw_int = pd.read_csv('./analysis/tw_colors_int.csv', index_col=0)
        self.tw_hsl = pd.read_csv('./analysis/tw_colors_hsl.csv', index_col=0)
        self.closest = self.findClosest()
        self.shade_list = ["50","100","200","300","400","500","600","700","800","900","950"]
    
    def generatePalette(self):
        #Convert input color to HSL
        hsl_input = tuple(int(self.input[i+1:i+3], 16) for i in (0, 2, 4))
        hsl_input = colorsys.rgb_to_hls(*hsl_input)
        hsl_ref = tuple(int(self.closest['hex'][i+1:i+3], 16) for i in (0, 2, 4))
        hsl_ref = colorsys.rgb_to_hls(*hsl_ref)
        #Get the tw_closest's row of hsl values
        hsl_arr = self.tw_hsl.loc[self.tw_hsl['name']==self.closest['color']]
        hsl_arr = hsl_arr.values.tolist()[0]
        hsl_arr = self.hsl_str_to_tup(hsl_arr)
        hsl_arr.pop(0)
        #Starting with the input shade, create a new list of colors copying the hsl changes from the tw_closest
        diff_list = []
        for hsl in hsl_arr:
            diff = []
            for i, prop in enumerate(hsl):
                diff.append(float(prop)
                            -hsl_ref[i])
            diff_list.append(tuple(diff))
        print(f'{hsl_ref=}')
        pprint(diff_list)
        
        input_hsl_list = []
        for hsl in diff_list:
            diff = []
            for i, prop in enumerate(hsl):
                diff.append(prop + hsl_input[i])
            input_hsl_list.append(tuple(diff))
        print(f'{hsl_input}')
        pprint(input_hsl_list)
        
        palette = []
        for hsl in input_hsl_list:
            #Fix hsl to rgb
            hexcode_str = self.hsl_to_rgb(hsl)
            palette.append(hexcode_str)
        pprint(palette)
    
    def findClosest(self):
        int_input = tuple(int(self.input[i+1:i+3], 16) for i in (0, 2, 4))
        closest = None
        for x,row in self.tw_hex.iterrows(): 
            
            for y,shade in enumerate(row.keys()):
                if shade =='name':continue
                tw_hex = self.tw_hex.iloc[x,y]
                tw_hex = tuple(int(tw_hex[i+1:i+3], 16) for i in (0, 2, 4))
                difference = int()
                for i, rgb in enumerate(int_input):
                    difference += abs(rgb - tw_hex[i])
                if closest is None:
                    closest = {'color':row['name'],'shade':shade,'diff':abs(difference)}
                    continue
                if closest['diff']>abs(difference):
                    closest = {'color':row['name'],'shade':shade,'diff':abs(difference),'hex':self.tw_hex.iloc[x,y]}
                    continue
        return closest
    
    def hsl_str_to_tup(self,str_arr):
        output= []
        for string in str_arr:
            tup = tuple(string.split('/'))
            output.append(tup)
        return output
         
    def hsl_to_rgb(self, hsl_tup):
    #   rgb = tuple(int(color_hex[i+1:i+3],16) for i in (0,2,4))
    #   print(f"{rgb=}")
    #   hsl = colorsys.rgb_to_hls(*rgb)
        hsl = hsl_tup
        new_rgb = colorsys.hls_to_rgb(*hsl)
        rgb = [1,2,3]
        for i in range(3):
            current = new_rgb[i]
            if new_rgb[i] >255:
                current = 255
            current_hex = hex(round(current)).lstrip("0x")
            if len(current_hex) <1:
                current_hex = "00"
            if len(current_hex) < 2:
                current_hex = f"0{current_hex}"
            rgb[i] = current_hex
        # Add left pad if len str == 0
        hexcode = f"#{rgb[0]}{rgb[1]}{rgb[2]}"
        return hexcode 
if __name__ == '__main__':
    x = PaletteGenerator('#17126A')
    print(x.findClosest())
    x.generatePalette()
