import time

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n]

# Example usage
p = [30, 35, 15, 5, 10, 20, 25]
start_time = time.time()
result = matrix_chain_order(p)
end_time = time.time()
print(f"Minimum number of multiplications is {result}")
print(f"Time taken: {end_time - start_time:.6f} seconds")
print("Program by Animesh")
