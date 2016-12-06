# find the max sum in the array with the constraint that you may not sum adjacent values
def max_sum_skip(arr : list) -> int:
    n = len(arr)
    if n <= 2:
        return max(arr)
    dp = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i < 2:
                dp[i][j] = arr[j]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i][j-2] + arr[j])
    return dp[n-1][n-1]

print(max_sum_skip([-1,-2,3]))
