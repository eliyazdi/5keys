import serial
from getch import getch
import sys

print(sys.argv[1])

ser = serial.Serial('/dev/tty.usbserial', sys.argv[1])
