import random

def generate_wholesome_message():
    messages = [
        "You are capable of amazing things!",
        "Your hard work is paying off. Keep going!",
        "You're making a positive impact on the world!",
        "Believe in yourself, you can achieve anything!",
        "Your kindness inspires others. Thank you!",
        "Take a moment to appreciate how far you've come.",
        "You are loved and appreciated!",
        "Your efforts make a difference. Keep pushing forward!",
        "You have the power to make someone's day brighter.",
        "Remember to be kind to yourself. You deserve it!"
    ]

    message = random.choice(messages)
    return message

# Prompt for a wholesome message
message = generate_wholesome_message()
print(message)
