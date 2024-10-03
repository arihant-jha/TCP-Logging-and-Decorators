import logging
import time
from functools import wraps

# Set up logging
logging.basicConfig(level=logging.INFO)

# Dictionary to hold the call graph
call_graph = []

class NamedLogger:
    def __init__(self, logger_name):
        self.logger = logging.getLogger(logger_name)

    def __call__(self, function):
        @wraps(function)
        def wrapped_function(*args, **kwargs):
            start = time.perf_counter()
            func_name = function.__name__
            try:
                result = function(*args, **kwargs)
                execution_time = (time.perf_counter() - start) * 1_000_000  # Execution time in microseconds
                
                # Log the execution time
                self.logger.info(f"{func_name} executed in {execution_time:.1f}μs")
                
                # Update the call graph
                call_graph.append((func_name, execution_time))
                
                return result
            except Exception as ex:
                execution_time = (time.perf_counter() - start) * 1_000_000
                self.logger.error(f"Error: {ex}, {func_name} failed in {execution_time:.1f}μs")
                raise
        return wrapped_function

# Example functions
@NamedLogger("logger")
def function_a(median, sample):
    time.sleep(0.1)  # Simulate processing time
    return abs(sample - median)

@NamedLogger("logger")
def function_b(value):
    time.sleep(0.05)  # Simulate processing time
    return value ** 2

@NamedLogger("logger")
def function_c(median, sample):
    # Calls function_a
    result_a = function_a(median, sample)
    # Calls function_b
    result_b = function_b(result_a)
    return result_b

@NamedLogger("logger")
def main_function(median, sample):
    # Calls function_c
    return function_c(median, sample)

# Run the main function
main_function(10, 20)

# Print the call graph
print("\nCall Graph:")
for func, time_taken in call_graph:
    print(f"{func}: {time_taken//1000:.1f}ms")
    print('      |')
    print('      |')
    print('      V')
