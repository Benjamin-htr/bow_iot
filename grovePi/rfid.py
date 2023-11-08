# -*- coding:Utf-8 -*-
import serial

def readBadge():
	ser = serial.Serial(
		port='/dev/ttyS0',
		baudrate = 9600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=0.01
	)

	print("Badgez votre carte")
	i=0
	buffer=b''
	octet=ser.read()
	while (i<1000) & (len(buffer)<14) :
		if octet != b'' :
			buffer+=octet
		else :
			i=i+1
		octet=ser.read()
	if buffer != b'':
		id=str(buffer[1:-1],"UTF-8")
		return id
	else:
		return None

if __name__ == "__main__":
	print(readBadge())
