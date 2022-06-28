
def print_color_map():
    pair_num = []
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j+1} | {major} | {minor}')
            pair_num.append(i * 5 + j+1)
    return len(major_colors) * len(minor_colors),pair_num

 
result, pair_num = print_color_map()
assert(result == 25)
assert(pair_num[0] == 1)
print("All is well (maybe!)\n")
