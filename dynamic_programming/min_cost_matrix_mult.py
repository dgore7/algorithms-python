import sys


def min_cost_matrix_mult(dimensions: []):
    n = len(dimensions)
    table = [[0 for j in range(n)] for i in range(n)]
    parens = [[0 for j in range(n)] for i in range(n)]
    for group in range(1, n):
        for i in range(1, n - group):
            j = i + group
            table[i][j] = sys.maxsize
            for k in range(i, j):
                current_cost =  table[i][k] + table[k+1][j] + dimensions[i-1] * dimensions[k] * dimensions[j]
                if current_cost < table[i][j]:
                    table[i][j] = current_cost
                    parens[i][j] = k
    return table




if __name__ == '__main__':
    dim = [40, 20, 30, 10, 30]
    print(min_cost_matrix_mult(dim))