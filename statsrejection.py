import math

def calculate_critical_value(alpha, n, clt=True):
    """Calculates the critical value based on alpha and sample size."""
    if clt:
        z_critical = 1.96  # For a 95% confidence level (two-tailed test)
        critical_value = z_critical * math.sqrt(n)
    else:
        t_critical = n - 1
        critical_value = t_critical
    return critical_value

def calculate_cumulative_probability(z):
    """Calculates the cumulative probability for a standard normal distribution."""
    return (1.0 + math.erf(z / math.sqrt(2.0))) / 2.0

def perform_hypothesis_test(sample_mean, population_mean, standard_deviation, alpha, n, alternative='two-sided', clt=True):
    """Performs a hypothesis test based on the given parameters."""
    z = (sample_mean - population_mean) / (standard_deviation / math.sqrt(n))

    if alternative == 'right':
        critical_value = calculate_critical_value(alpha, n, clt)
        p_value = 1 - calculate_cumulative_probability(z)
        reject_null = z > critical_value
    elif alternative == 'left':
        critical_value = calculate_critical_value(alpha, n, clt)
        p_value = calculate_cumulative_probability(z)
        reject_null = z < -critical_value
    else:  # two-sided
        critical_value = calculate_critical_value(alpha / 2, n, clt)
        p_value = 2 * (1 - calculate_cumulative_probability(abs(z)))
        reject_null = abs(z) > critical_value

    return p_value, reject_null

# Example usage
sample_mean = 9.6
population_mean = 10
standard_deviation = 2.5
alpha = 0.05
n = 25
alternative = 'two-sided'
clt = True

p_value, reject_null = perform_hypothesis_test(sample_mean, population_mean, standard_deviation, alpha, n, alternative, clt)

print(f"Sample Mean: {sample_mean}")
print(f"Population Mean: {population_mean}")
print(f"Standard Deviation: {standard_deviation}")
print(f"Alpha: {alpha}")
print(f"Sample Size (n): {n}")
print(f"Alternative: {alternative}")
print(f"Using CLT: {clt}")
print(f"P-value: {p_value}")
print(f"Reject Null Hypothesis: {reject_null}")

