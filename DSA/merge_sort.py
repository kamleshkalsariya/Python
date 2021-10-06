def merge_sort(arr):
    if len(arr)<= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    return merge_two_sorted_list(left,right,arr)

def merge_two_sorted_list(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k] = b[i]
            j += 1
        k += 1
    while i<len_b:
        arr[k]=a[i]
        i += 1
        k += 1
    while j<len_b:
        arr[k] = b[j]
        j += 1
        k += 1
    return arr

if __name__ == '__main__':

    a = [4,3,45,32,67,1,89,5]
    merge_sort(a)
    print(a)