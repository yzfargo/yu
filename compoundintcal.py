def calculate_compound_interest(principal, rate, compounding_frequency, time):
    """Calculates the compound interest."""
    amount = principal * (1 + (rate / compounding_frequency))**(compounding_frequency * time)
    interest = amount - principal
    return interest

# Example usage
principal = 1000
rate = 5
compounding_frequency = 12
time = 2

compound_interest = calculate_compound_interest(principal, rate, compounding_frequency, time)
total_amount = principal + compound_interest

print(f"Principal: ${principal}")
print(f"Rate: {rate}%")
print(f"Compounding Frequency: {compounding_frequency} times per year")
print(f"Time: {time} years")
print(f"Compound Interest: ${compound_interest}")
print(f"Total Amount: ${total_amount}")
