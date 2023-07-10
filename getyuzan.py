import random
import string

def generate_random_combination(length):
    """Generates a random combination of characters."""
    symbols = string.ascii_lowercase + string.digits + string.punctuation
    combination = ''.join(random.choice(symbols) for _ in range(length))
    return combination

def play_slot_machine():
    """Simulates a slot machine game with random letter combinations."""
    word = "yuzan"
    guess = generate_random_combination(5)
    
    print("Spinning the reels...")
    print(guess)
    
    if guess == word:
        print("Congratulations! You won!")
    else:
        print("Better luck next time!")

# Example usage
play_slot_machine()
