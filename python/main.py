import sys, time, os
import krpc as ksp
import serial as ser


conn = None

def initKSP():
	print("Initiate connection between client and game")
	for attempt in range(10):
		try:
			conn = ksp.connect()
			print(conn.krpc.get_status().version)
			return 1
		except:
			time.sleep(2)
			print('Attempt ' + str(attempt+1) + ' failed')
	return 0

def initArduino():
	print("Initiate connection between client and controller")

def com(data):
	
	return 0


def main():
	print("KSP Control Panel v0.1")
	print("Copyright (c) 2018 Minh Truong. All right reserved")
	if ~initKSP():
		print("Unable to establish connection with the game; perhaps check to see if kRPC server is on?")

print(os.name)

if __name__ == "__main__":
	main()