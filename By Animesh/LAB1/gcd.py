import time

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Input values
a = 48
b = 18

# Measure the time taken to execute the GCD function
start_time = time.time()
result = gcd(a, b)
end_time = time.time()

# Output the result and time taken
print(f"GCD of {a} and {b} is: {result}")
print(f"Time taken to compute GCD: {end_time - start_time} seconds")
print("Program by Animesh")
