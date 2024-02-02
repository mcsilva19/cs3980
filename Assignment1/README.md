#Part1: Echo.py
This python script mimics the behavior of an echo. It takes an input for the user and repeats the input with decreasing length (only shows the last 3 indexes) and ends with a "."

## Usage 
1. Run the script by executing the command: `python echo.py`.
2. Enter the desired text when prompted.
3. The program will output the text repeated with decreasing length, followed by a period.

## Implementation Details
- The script takes two parameters:
  - `text`: The string to be echoed.
  - `repetitions`: (Optional) The number of times to repeat the echo. Default is 3.

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
- `echo.py`: Python Script that imitates real-world echo.
- `fib.py`: Python script containing the Fibonacci calculation logic.
- `README.md`: This file providing an overview, usage instructions, and implementation details for both codes for assignment 1 for CS3980.


