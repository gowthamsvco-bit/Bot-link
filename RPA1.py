import pyautogui
import subprocess
import time

# Small pause between PyAutoGUI actions
pyautogui.PAUSE = 0.3

# Fail-safe: move mouse to top-left corner to stop the script
pyautogui.FAILSAFE = True

# 1. Open Notepad
subprocess.Popen("notepad.exe")
time.sleep(1.5)  # Wait for Notepad to open

# 2. Create a New file
pyautogui.hotkey("ctrl", "n")
time.sleep(0.5)

# If a "Save" dialog appears (because an unsaved file was open),
# press "Don't Save" using keyboard shortcut.
pyautogui.press("right")
pyautogui.press("enter")
time.sleep(0.5)

# 3. Type slowly
message = "I am a BOT controlling your NOTEPAD"

pyautogui.write(message, interval=0.12)
