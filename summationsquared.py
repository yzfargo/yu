def calculate_sum_of_squares(numbers):
    """Calculates the sum of squares for a given set of numbers."""
    sum_of_squares = sum(x**2 for x in numbers)
    return sum_of_squares

# Example usage
numbers = [2, 4, 6, 8, 10]

sum_of_squares = calculate_sum_of_squares(numbers)

print(f"Numbers: {numbers}")
print(f"Sum of Squares: {sum_of_squares}")
