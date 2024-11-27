"""  
	Trigger Function get executed when serial data is received from serial port
	& Read check returns True

	Used to handle data reading, generally sending to api or other modules

	Parameters:
		data: bytes (data received from serial port)
		serial: Serial object (serial port object)

	Returns:
		No Need to return anything

"""


def Trigger(data: bytes, serial):
	##

	## Your code here

	##
	print("Recieved data: '{}'".format(data.decode("utf-8")))
