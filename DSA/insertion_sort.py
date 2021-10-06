def insertion_sort(elements):
    for i in range(1,len(elements)):
        anchor = elements[i]
        j = i-1
        median(elements[:j + 1])
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor
    median(elements)

def median(array):
    l = len(array)
    if l%2 != 0:
        print(array[l//2])
    else:
        print((array[l//2]+array[l//2-1])/2)

if __name__ == '__main__':
    elements = [2,1,5,7,2,0,5]
    insertion_sort(elements)
    print(elements)