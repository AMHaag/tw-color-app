import colorsys

def sanity(color_hex):
    rgb = tuple(int(color_hex[i+1:i+3],16) for i in (0,2,4))
    print(f"{rgb=}")
    hsl = colorsys.rgb_to_hls(*rgb)
    print(f"{hsl=}")
    new_rgb = colorsys.hls_to_rgb(*hsl)
    rgb = [1,2,3]
    for i in range(3):
        print(hex(round(new_rgb[i])).lstrip('0x'))
        rgb[i] = hex(round(new_rgb[i])).lstrip("0x")
    print(f"{rgb=}")
    # Add left pad if len str == 0
    hexcode = f"#{rgb[0]}{rgb[1]}{rgb[2]}"
    print(f"{rgb=}")
    print(f"{hexcode=}")
    print(f"{new_rgb=}")
sanity('#1022ff')

print(hex(255))
