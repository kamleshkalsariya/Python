def shell_sort(arr):
    size = len(arr)
    gap = size//2
    while gap>0:
        i = gap
        while i<size:
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap]>=anchor:
                if arr[j]  == arr[j-gap]:
                    del arr[j]
                    size -= 1
                    j-=1
                    i-=1
                else:
                    arr[j]  = arr[j-gap]
                    j -= gap
                arr[j] = anchor
            i += gap
        gap = gap//2

if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3,9,10,2,4,5,10,9]
    shell_sort(elements)
    print(elements)