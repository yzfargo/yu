def calculate_love_meter(name1, name2):
    """Calculates the compatibility percentage between two names."""
    combined_names = name1.lower() + name2.lower()
    letters = list(set(combined_names))
    love_meter_value = len(letters) * 10
    return min(love_meter_value, 100)

# Prompt user to enter two names
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Calculate love meter value
love_percentage = calculate_love_meter(name1, name2)

# Display result
print(f"Love Meter Result: {love_percentage}%")

