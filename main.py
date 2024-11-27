from serial import Serial

import settings

import OnRead
import OnWrite


def ReadSerial(ser):
	return ser.read_until(settings.EOF)[:len(settings.EOF)*(-1)]

def main():
	print(f"Trying to open serial port '{settings.PORT}'...")

	try:
		ser = Serial(settings.PORT, settings.PORT_BAUD)
	except Exception as e:
		print("Failed to open serial port.")
		print(e)
		return

	except KeyboardInterrupt:
		print("Exiting...")
		ser.close()
		return


	while True:

		try:
			data = ReadSerial(ser)
		except Exception as e:
			print("Failed to read serial port.")
			print(e)
			return
		except KeyboardInterrupt:
			print("Exiting...")
			ser.close()
			return


		if OnRead.Check(data, ser):
			OnRead.Trigger(data, ser)

		if OnWrite.Check(data, ser):
			OnWrite.Trigger(data, ser)



if __name__ == '__main__':
	main()