# [-1, 5, 2, -3, 8]
t = int(input())
for i in range(t):
    n = int(input())
    if n == 0:
        print(0)
        continue
    array = [int(i) for i in input().strip().split(" ")]
    max_sum = array[0]
    curr_sum = array[0]
    for j in range(1, n):
        curr_sum = max(array[j], curr_sum + array[j])
        max_sum = max(curr_sum, max_sum)
    print(max_sum)
