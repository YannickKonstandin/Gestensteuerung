import serial #Serial imported for Serial communication
import time #Required to use delay functions


port = '/dev/ttyUSB0'

ArduinoSerial = serial.Serial(port,9600,timeout=5)
time.sleep(2)

while True:
    user_input = input("Eingabe 1 zum Einschalten oder 0 zum Ausschalten: ")
    
    if (user_input == '1'): #if the value is 1
        ArduinoSerial.write(b'1') #send 1
        print ("LED turned ON")
        time.sleep(1)

    elif (user_input == '0'): #if the value is 0
        ArduinoSerial.write(b'0') #send 0
        print ("LED turned OFF")
        time.sleep(1)
    else:
        print("Ubgültige Eingabe!")
