import serial
import adafruit_us100
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
us100 = adafruit_us100.US100(uart)
  
def get_distance():
    return us100.distance

def get_temperature():
    return us100.temperature 

def print_output():
    print(str(get_distance()) + "cm")    
    print(str(get_temperature()) + "C")
