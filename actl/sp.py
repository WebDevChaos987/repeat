import sys
from .wait import wait

def sp(text, speed=100000):
    """
    Prints text one character at a time like a video game dialogue box.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        wait(speed)  # Uses your custom wait loop between letters
    print()  # Moves to a new line at the end
