import time

def knapSack(W, weight, value, n):
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weight[i - 1] <= w:
                dp[i][w] = max(value[i - 1] + dp[i - 1][w - weight[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Example usage
value = [60, 100, 120]
weight = [10, 20, 30]
W = 50
n = len(value)
start_time = time.time()
result = knapSack(W, weight, value, n)
end_time = time.time()
print(f"Maximum value in knapsack = {result}")
print(f"Time taken: {end_time - start_time:.6f} seconds")
print("Program by Animesh")
