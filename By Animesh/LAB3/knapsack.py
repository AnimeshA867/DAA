import time

def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][W]

# Input weights and values
weights = [10, 20, 30]
values = [60, 100, 120]
W = 50

# Measure the time taken to execute the Knapsack function
start_time = time.time()
max_value = knapsack(weights, values, W)
end_time = time.time()

# Output the result and time taken
print("Maximum value in Knapsack =", max_value)
print(f"Time taken to execute the Knapsack program: {end_time - start_time:.6f} seconds")
print("Program by Animesh")
