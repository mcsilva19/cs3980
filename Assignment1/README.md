

# Part2: Fib.py

This Python script calculates the Fibonacci sequence up to a given number `n` and measures the execution time for each calculation.

## Usage

1. Run the script by executing the command: `python fib.py`.
2. The script will calculate the Fibonacci sequence up to the specified number (`n = 100` by default).
3. Each Fibonacci calculation is timed, and the script prints the execution time along with the Fibonacci number for each `n` value.

## Implementation Details

- The script uses recursion to calculate Fibonacci numbers.
- It utilizes the `@lru_cache` decorator for caching previously computed values to optimize performance.
- The `@timer` decorator measures the execution time of each Fibonacci calculation.
- Results are printed in the format: `Finished in <execution_time>s: f(<n>) -> <fibonacci_number>`.

## File Structure

- `fib.py`: Main Python script containing the Fibonacci calculation logic.
- `README.md`: This file providing an overview, usage instructions, and implementation details for both codes for assignment 1 for CS3980.


