import math
from scipy.stats import norm

def calculate_rejection_region(alpha, n, clt=True):
    """Calculates the rejection region based on alpha and sample size."""
    if clt:
        z_critical = norm.ppf(1 - alpha)
        rejection_region = (z_critical * math.sqrt(n), float('inf'))
    else:
        t_critical = n - 1
        rejection_region = (t_critical, float('inf'))
    return rejection_region

def perform_hypothesis_test(sample_mean, population_mean, standard_deviation, alpha, n, alternative='two-sided', clt=True):
    """Performs a hypothesis test based on the given parameters."""
    z = (sample_mean - population_mean) / (standard_deviation / math.sqrt(n))

    if alternative == 'right':
        rejection_region = calculate_rejection_region(alpha, n, clt)
        p_value = 1 - norm.cdf(z)
        reject_null = z > rejection_region[0]
    elif alternative == 'left':
        rejection_region = calculate_rejection_region(alpha, n, clt)
        p_value = norm.cdf(z)
        reject_null = z < -rejection_region[0]
    else:  # two-sided
        rejection_region = calculate_rejection_region(alpha / 2, n, clt)
        p_value = 2 * (1 - norm.cdf(abs(z)))
        reject_null = abs(z) > rejection_region[0]

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
