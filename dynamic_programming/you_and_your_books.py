def max_books(arr, k):
    curr_sum = 0
    max_sum = 0
    for i in range(len(arr)):
        if arr[i] <= k:
            curr_sum += arr[i]
        else:
            max_sum = max(curr_sum, max_sum)
            curr_sum = 0
    return max(curr_sum, max_sum)

