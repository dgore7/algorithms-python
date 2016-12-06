def find_min_insertion_DP(string):
    n = len(string)
    dp = [[0 for j in range(n)] for i in range(n)]
    for gap in range(1, n):
        lo = 0
        hi = gap
        while hi < n:
            print("({}, {})".format(lo, hi))
            if string[lo] == string[hi]:
                dp[lo][hi] = dp[lo+1][hi-1]
            else:
                dp[lo][hi] = min(dp[lo+1][hi], dp[lo][hi-1]) + 1
            hi += 1
            lo += 1
    return dp

for i in find_min_insertion_DP("pizza"):
    print(i)