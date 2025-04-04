from time import sleep

# The pyautoGUI module automates windows. It can move the mouse around,
# write some text...
import pyautogui

# I can make it print text where the cursor is, even this file.
# In this example, the '\n' makes the code go on a newline.
sleep(1)
pyautogui.write('print("hello")\n', interval=0.1)
