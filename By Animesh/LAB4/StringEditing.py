import time

def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

# Example usage
str1 = "Animesh"
str2 = "Acharya"
start_time = time.time()
result = edit_distance(str1, str2)
end_time = time.time()
print(f"Edit distance is {result}")
print(f"Time taken: {end_time - start_time:.6f} seconds")
print("Program by Animesh")
