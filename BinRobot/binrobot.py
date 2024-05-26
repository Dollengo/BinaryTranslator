import time
import pygame
import os

def clear_console():
    # Check the operating system to determine the appropriate command to clear the console
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Other systems (Linux, MacOS)
        os.system('clear')

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Initialize pygame mixer
pygame.mixer.init()

# Load the typing sound
typing_sound = pygame.mixer.Sound(os.path.join(current_dir, 's.wav'))  # Ensure you have a typing sound file

# Load the 'loading' sound
load_sound = pygame.mixer.Sound(os.path.join(current_dir, 'sa.wav'))  # Ensure you have a loading sound file

# Dictionary of error codes and their corresponding messages
errors = {
    "001": "Unknown error",
    "002": "Network error",
    "003": "Compiler error",
    "004": "Syntax error",
    "005": "Runtime error",
    "006": "Memory error",
    "007": "Hardware error",
    "008": "Software error",
    "009": "Python language error",
    "010": "IDE/Code editor error (not expected to occur in .exe)",
    "011": "Code error",
    "012": "Input typing error",
    "013": "Input key error",
    "014": "Input reading error",
    "015": "Data loading error",
    "016": "Unrecognized characters"
}

# Simulates a loading process with delays
def loading():
    time.sleep(1)
    print("system:Loading information...")   # Message indicating loading of information
    load_sound.play()
    time.sleep(1)
    print("system:Importing data...")        # Message indicating importing of data
    load_sound.play()
    time.sleep(2)
    print("system:Decrypting information...") # Message indicating decryption of information
    load_sound.play()
    time.sleep(0.5)
    print("system:Completed!")               # Message indicating completion of loading process
    load_sound.play()
    time.sleep(0.1)

# Simulates typing animation for the robot's response
def type_like_robot(text):
    char_count = 0
    for char in text:
        print(char, end='', flush=True)
        char_count += 1
        if char_count % 2 == 0:  # Play the sound every 3 characters
            typing_sound.play()
        time.sleep(0.05)  # Adjust the delay to control typing speed
    print()  # Move to the next line after the text is fully printed

# Prints text normally or with typing animation if it starts with "Bin: "
def print_with_animation(text):
    if text.startswith("Bin: "):
        type_like_robot(text)
    else:
        print(text)

# Converts an ASCII string to binary
def str_to_bin(string):
    # Converts each character to its corresponding 8-bit binary value
    return ' '.join(format(ord(char), '08b') for char in string.replace('_', ' '))

# Converts a binary string (space-separated) to ASCII
def bin_to_str(binary):
    # Converts each binary byte back to its corresponding ASCII character
    string = ''.join(chr(int(b, 2)) for b in binary.split(' '))
    return string.replace(' ', '_')

# Run the clear console command
clear_console()
# Run the loading simulation
loading()

print_with_animation("Bin: Hello, I am Bin, a robot FLUENT in binary code.")
time.sleep(1)

# Prompts the user to choose a conversion type or exit with typing animation
print_with_animation("Bin: Type '1' for (ASCII -> binary), '2' for (binary -> ASCII) or 'esc' to exit: ")
user = input().lower().strip()

while user != "esc":
    if user == "1":
        time.sleep(0.5)
        print_with_animation("Bin: Enter an ASCII string: ")
        string = input()
        print_with_animation(f"Bin: {str_to_bin(string)}")
        time.sleep(0.7)
    elif user == "2":
        time.sleep(0.5)
        print_with_animation("Bin: Enter a binary code (separate bytes with spaces): ")
        binary = input()
        # Checks if the binary code contains '0' or '1'
        if not any(bit in binary for bit in ('0', '1')):
            print_with_animation("system:error 014, 012\nFor more information, use Bin's 'errors' command.")
        else:
            print_with_animation(f"Bin: {bin_to_str(binary)}")
            time.sleep(0.7)
    elif user == "errors":
        print("###")
        print(errors)
        print("###")
    else:
        time.sleep(0.5)
        print_with_animation("system:error 012\nFor more information, use Bin's 'errors' command.")
    # Prompts the user again for input with typing animation
    print_with_animation("Bin: Type '1' for (ASCII -> binary), '2' for (binary -> ASCII) or 'esc' to exit: ")
    user = input().lower().strip()

print_with_animation("Bin: Exiting...")
clear_console()
