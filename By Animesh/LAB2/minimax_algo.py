import time

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
    
    if maximizingPlayer:
        best = float('-inf')
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# Input values
values = [3, 5, 2, 9, 12, 5, 23, 23]
initial_depth = 0
initial_node_index = 0
initial_maximizing_player = True
initial_alpha = float('-inf')
initial_beta = float('inf')

# Measure the time taken to execute the Minimax function
start_time = time.time()
optimal_value = minimax(initial_depth, initial_node_index, initial_maximizing_player, values, initial_alpha, initial_beta)
end_time = time.time()

# Output the result and time taken
print(f"Optimal value is: {optimal_value}")
print(f"Time taken to compute optimal value using Minimax: {end_time - start_time:.6f} seconds")
print("Program by Animesh")
