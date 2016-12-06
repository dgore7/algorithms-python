def selection_sort(array):
    n = len(array)
    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if array[j] < array[min_index]:
                min_index = j
        if i != min_index:
            array[min_index], array[i] = array[i], array[min_index]


def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(array, j-1, j)
            j -= 1


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


if __name__ == "__main__":
    arg = [535, 12, 53, 23, 53, 645, 23, 42, 32, 61]
    insertion_sort(arg)
    print(arg)