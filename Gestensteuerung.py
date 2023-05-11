import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

port = '/dev/ttyUSB1'

ArduinoConnection = serial.Serial(port,9600,timeout=5)
time.sleep(2)

while 1:

    incoming = str (ArduinoConnection.readline()) #read the serial data and print it as line

    #print(incoming)   

    if 'Play/Pause' in incoming:

        pyautogui.typewrite(['space'], 0.2)

    if 'Rewind' in incoming:

        pyautogui.hotkey('ctrl', 'left')  

    if 'Forward' in incoming:

        pyautogui.hotkey('ctrl', 'right') 

    if 'Vup' in incoming:

        pyautogui.hotkey('ctrl', 'up')

    
    if 'Vdown' in incoming:

        pyautogui.hotkey('ctrl', 'down')

    if 'Vmute' in incoming:

        pyautogui.hotkey('ctrl', 'm')

    incoming = ("")