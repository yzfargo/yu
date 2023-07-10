import math

def calculate_correlation(x, y):
    """Calculates the correlation coefficient between two variables."""
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x_squared = sum(xi**2 for xi in x)
    sum_y_squared = sum(yi**2 for yi in y)

    numerator = (n * sum_xy) - (sum_x * sum_y)
    denominator = math.sqrt((n * sum_x_squared - sum_x**2) * (n * sum_y_squared - sum_y**2))
    correlation = numerator / denominator

    return correlation

# Example usage
x = [2, 4, 6, 8, 10]
y = [3, 5, 7, 9, 11]

correlation = calculate_correlation(x, y)

print("Correlation Analysis")
print(f"Variable X: {x}")
print(f"Variable Y: {y}")
print(f"Pearson's Correlation Coefficient: {correlation}")
