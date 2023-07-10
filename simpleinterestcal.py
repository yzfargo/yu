def calculate_simple_interest(principal, rate, time):
    """Calculates the simple interest."""
    interest = (principal * rate * time) / 100
    return interest

# Example usage
principal = 1000
rate = 5
time = 2

simple_interest = calculate_simple_interest(principal, rate, time)
total_amount = principal + simple_interest

print(f"Principal: ${principal}")
print(f"Rate: {rate}%")
print(f"Time: {time} years")
print(f"Simple Interest: ${simple_interest}")
print(f"Total Amount: ${total_amount}")
