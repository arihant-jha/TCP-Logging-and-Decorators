from math import factorial
from functools import lru_cache
import time

# With lru_cache
@lru_cache(maxsize=128)  # Caches the last 128 results
def binom_with_cache(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Without lru_cache
def binom_without_cache(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Test parameters
n_values = [1000, 2000, 3000]  # Larger values for n
k = 10  # A smaller k
num_calls = 1000  # Number of calls to test

# Measure performance with lru_cache
start_time = time.time()
for n in n_values:
    for _ in range(num_calls):
        binom_with_cache(n, k)
end_time = time.time()
cache_time = end_time - start_time

# Measure performance without lru_cache
start_time = time.time()
for n in n_values:
    for _ in range(num_calls):
        binom_without_cache(n, k)
end_time = time.time()
no_cache_time = end_time - start_time

# Results
print(f"Time with lru_cache: {cache_time:.6f} seconds")
print(f"Time without lru_cache: {no_cache_time:.6f} seconds")
