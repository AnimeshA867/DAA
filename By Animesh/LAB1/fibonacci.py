import time

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Input value
n = 10

# Measure the time taken to execute the Fibonacci function
start_time = time.time()
result = fibonacci(n)
end_time = time.time()

# Output the result and time taken
print(f"The {n}th Fibonacci number is: {result}")
print(f"Time taken to compute Fibonacci number: {end_time - start_time} seconds")
print("Program by Animesh")
