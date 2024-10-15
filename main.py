import pyautogui
from PIL import ImageGrab
import time
import keyboard  # Install with `pip install keyboard`


# Function to capture the screen
def capture_screen():
    img = ImageGrab.grab()  # Captures the entire screen
    return img


# Function to check if a pixel is green (targeting green leaves)
def is_green_leaf(pixel):
    r, g, b = pixel
    return g > 100 and r < 100 and b < 100  # High green, low red and blue


# Function to check if a pixel is black or white
def is_black_or_white(pixel):
    r, g, b = pixel
    return (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)  # Black or white


# Function to automatically click on green leaves and count clicks
def click_on_green_leaves():
    click_count = 0  # Initialize click counter

    while True:
        if keyboard.is_pressed('space'):  # Check if spacebar is pressed
            print("Stopping the program...")
            break

        screen = capture_screen()  # Capture the screen

        # Loop through the screen pixels to find green leaves
        width, height = screen.size
        for y in range(0, height, 10):  # Step by 10 pixels for efficiency
            for x in range(0, width, 10):
                pixel = screen.getpixel((x, y))
                if is_green_leaf(pixel) and not is_black_or_white(pixel):  # Check green leaf and exclude black/white
                    pyautogui.click(x, y)  # Click at the pixel's position
                    click_count += 1  # Increment click counter
                    print(f"Clicked {click_count} times")  # Print click count

        time.sleep(0.1)  # Delay between checks


# Run the green leaf autoclicker
click_on_green_leaves()
