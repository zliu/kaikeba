


def find_num(num_list, num_to_find):
    pos = -1
    length = len(num_list)
    if not length:
        return pos
    if num_list[0] > num_to_find or num_to_find > num_list[-1]:
        return pos
    cur_pos = length//2
    if num_to_find == num_list[cur_pos] :
        return cur_pos
    # ordered array in later part
    if num_list[cur_pos] <= num_list[-1]:
        if num_to_find >= num_list[cur_pos] and num_to_find <= num_list[-1]:
            return find_num(num_list[:cur_pos], num_to_find)
        else:
            return cur_pos + find_num(num_list[cur_pos:], num_to_find)
    elif num_list[0] <= num_list[cur_pos]:
    # ordered array in former part
        if num_to_find >= num_list[0] and num_to_find <= num_list[cur_pos]:
            return find_num(num_list[:cur_pos], num_to_find)
        else:
            return cur_pos + find_num(num_list[cur_pos:], num_to_find)
    
array = [8,12,        15,34,2,3,4,5,6,7,]
n = 15

array = [2]
n = 2

pos = find_num(array, n)
print(pos)