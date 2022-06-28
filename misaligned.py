printed_output = []

def save_printed_output(value):
    global printed_output
    printed_output.append(value)

def print_color_map():
    pair_num = []
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            #to_print = f'{i * 5 + j+1} | {major} | {minor}'
            to_print = str(i * 5 + j+1) +'\t\t' + major + '\t\t' + minor
            print(to_print)
            save_printed_output(to_print)
            pair_num.append(i * 5 + j+1)
    return len(major_colors) * len(minor_colors),pair_num


result, pair_num = print_color_map()
assert(result == 25)
assert(pair_num[0] == 1)

#For checking the alignment.
#Compare the index of occurences of "|" in first printed output with all the others
if "|" in printed_output[0]:
    for i in range(1,len(printed_output)):
        first_index_of_0 = printed_output[0].index("|")
        first_index_of_i = printed_output[i].index("|")
        second_index_of_0 = printed_output[0].index("|",first_index_of_0 + 1)
        second_index_of_i = printed_output[i].index("|",first_index_of_i + 1)
        assert(first_index_of_0 == first_index_of_i)
        assert(second_index_of_0 == second_index_of_i)
          
print("All is well (maybe!)\n")
