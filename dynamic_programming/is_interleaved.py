# God save me. O(n^2)
def isInterleave(A, B, C):
    if len(A) + len(B) != len(C):
        return False
    # return recursive(A, B, C, 0, 0, 0)
    dp = [[False for i in range(len(B) + 1)] for j in range(len(A) + 1)]
    for i in range(len(A) + 1):
        for j in range(len(B) + 1):
            # empty string is True
            if i == 0 and j == 0:
                dp[i][j] = True
            # if B is empty and the i'th char in A matches the i'th char in C, set dp to previous char i'th char in A.
            elif j == 0 and A[i - 1] == C[i - 1]:
                dp[i][j] = dp[i - 1][j]
            # if A is empty and the j'th char in B matches the j'th char in C, set dp to previous char j'th char in B.
            elif i == 0 and B[j - 1] == C[j - 1]:
                dp[i][j] = dp[i][j - 1]
            # if both string have a match at their respective indices to the value in the i+j-1'th spot in C
            elif A[i - 1] == C[i + j - 1] and B[j - 1] == C[i + j - 1]:
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            # if A matches the value in the i+j-1'th spot in C
            elif C[i + j - 1] == B[j - 1]:
                dp[i][j] = dp[i][j - 1]
            # if B matches the value in the i+j-1'th spot in C
            elif C[i + j - 1] == A[i - 1]:
                dp[i][j] = dp[i - 1][j]

    return dp[len(A)][len(B)]
    # YXY
    # YZX
    # YXYZXY

# recursive version. runs in O(2^n)
def recursive(A, B, C, a_index, b_index, c_index):
    if len(C) == a_index + b_index:
        return True

    if a_index != len(A) and C[c_index] == A[a_index]:
        if recursive(A, B, C, a_index + 1, b_index, c_index + 1):
            return True
    if b_index != len(B) and C[c_index] == B[b_index]:
        if recursive(A, B, C, a_index, b_index + 1, c_index + 1):
            return True
    return False

