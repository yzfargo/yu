import random
import time

def play_slot_machine():
    """Simulates a slot machine game."""
    symbols = ["♥", "♣", "♦", "♠", "7"]
    reels = [random.choice(symbols) for _ in range(3)]
    
    print("Spinning the reels...")
    time.sleep(2)  # Adds a delay of 2 seconds
    
    print(" ".join(reels))
    time.sleep(1)  # Adds a delay of 1 second
    
    if reels.count("7") == 3:
        print("Congratulations! You won!")
    else:
        print("Better luck next time!")

# Example usage
play_slot_machine()
