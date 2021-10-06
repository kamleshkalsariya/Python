def binary_search(num_list, num_find,left_index,right_index):
    mid_index = 0
    while left_index <= right_index:
        mid_index = (left_index+right_index)//2
        mid_num = num_list[mid_index]
        index_list = []
        if num_find == mid_num:
            for i in range(1,mid_index+1):
                if num_find == num_list[mid_index-i]:
                    index_list.append(mid_index - i)
                else:
                    break
            index_list.append(mid_index)
            for i in range(1,mid_index+1):
                if num_find == num_list[mid_index+i]:
                    index_list.append(mid_index+i)
                else:
                    break
            return index_list
        elif num_find >= mid_num:
            left_index = mid_index+1
        else:
            right_index = mid_index-1
    return -1

if __name__ == '__main__':
    number_list = [1,4,6,9,11,15,15,15,15,17,21,34,34,56]
    number_find = 15
    l = len(number_list)-1
    indices = binary_search(number_list,number_find,0,l)
    print(indices)