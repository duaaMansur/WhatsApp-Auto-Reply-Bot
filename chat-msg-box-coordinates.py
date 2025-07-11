import pyautogui

print("Move your mouse to the desired spot and press Enter in the console.")
print("Press Ctrl+C to exit.")

try:
    while True:
        input("Press Enter to record mouse position...")
        x, y = pyautogui.position()
        print(f"Mouse position: ({x}, {y})")
except KeyboardInterrupt:
    print("\nDone.")