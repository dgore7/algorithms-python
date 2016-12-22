import random


def randomized_select(arr, lo, hi, target):
    while True:
        pivot_index = random.randint(lo, hi)
        part_point = partition(arr, lo, hi, pivot_index)
        #pivot_dist = part_point - lo
        if part_point == target:
            return arr[part_point]
        elif target < part_point:
            hi = part_point - 1
        else:
            #target -= pivot_dist + 1
            lo = part_point + 1


def select(arr, target):
    random.shuffle(arr)
    return randomized_select(arr, 0, len(arr) - 1, target)


def partition(arr, lo, hi, pivot_index):
    pivot = arr[pivot_index]
    swap(arr, hi, pivot_index)
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            swap(arr, i, j)
            i += 1
    swap(arr, i, hi)
    return i


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

if __name__ == '__main__':
    arr = [1, 64, 324, 73, 23, 37, 24]
    print(select(arr, 1))

