#!/usr/bin/python3

#MASTERSOP = 'a5'
#SLAVESOP = '5a'
#IDLE = 'ff'
#sendbuff = b'\xfe\x51'
#binbuf = bytes.fromhex(sendbuff)
test_buffer =  b'\xfe\x51'
#  here is how you prepare a buffer for 8 hex chars
#  buf = bytes.fromhex('dead beef')  
# notice how bytes.fromhex will ignore white space

# now you would need to open the comm port which is board specific:
# in my case I'm using WiringPi on a RPi

#import RPi.GPIO as wpi
import serial
import datetime
import time
from time import strftime
com = serial.Serial('/dev/ttyS2', 9600)
x = 1
while True:
	today1 = datetime.date.today()
	dt1 = str(today1)
	today2 = strftime('%H:%M')
	dt2 = str(today2)
#for b in test_buffer:
#    serial.serialPutchar(com, b)
#    time.sleep(0.010)    # 10mS per char if device cannot keep up
#x = 1
#while True:
	com.write(b'\xfe\x51')
	com.write(b'\xfe\x46')
	com.write(b'\xfe\x45\x05')
	com.write(dt1.encode())
	com.write(b'\xfe\x46')
	com.write(b'\xfe\x45\x48')
	com.write(dt2.encode())
	time.sleep(60)
