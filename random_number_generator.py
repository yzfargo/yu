import random

def generate_random_number():
    return random.randint(1, 100)

# Generate a random number between 1 and 100
random_number = generate_random_number()

# ANSI escape code for pink color
pink_color_code = "\033[95m"
reset_color_code = "\033[0m"

# Print the random number in pink color
print(pink_color_code + "Random number: " + str(random_number) + reset_color_code)
