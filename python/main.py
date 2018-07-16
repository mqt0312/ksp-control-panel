import sys, time, os
import krpc as ksp
import serial as ser

game = None
panel = None

def initKSP():
    print("Initiate connection between client and game")
    for attempt in range(10):
        try:
            game = ksp.connect()
            print("Game connected. kRPC version", game.krpc.get_status().version)

            return 1
        except:
            time.sleep(1)
            print('Attempt ' + str(attempt+1) + ' failed')
            time.sleep(1)
    return 0

def initArduino():
    print("Initiate connection between client and controller")
    for attempt in range(10):

        '''
        for port in ["COM" + str(num) for num in range(256)]:
            try:
                panel = ser.Serial(port, 9600)
                panel.write('A')
                if panel.read().decode("utf-8") == "A":
                    print("Panel connected on port", port)
                    panel.timeout = None
                    return 1
            except:
                pass
        '''
        panel = ser.Serial('COM5', 9600)
        panel.write(b'A')
        if panel.read().decode("utf-8") == "A":
            print("Panel connected on port", port)
            panel.timeout = None
            return 1
        time.sleep(1)
        print('Attempt ' + str(attempt + 1) + ' failed')
        time.sleep(1)
    return 0




def com(data, read_timeout=None, write_timeout=None):
    panel.timeout = read_timeout
    panel.write_timeout = write_timeout
    panel.write(data.encode())
	
    return panel.read()


def init():
    print("KSP Control Panel v0.1")
    print("Copyright (c) 2018 Minh Truong. All right reserved")
    if not initKSP():
        print("Unable to establish connection with the game; perhaps check to see if kRPC server is on?")
    if not initArduino():
        print("unable to establish connection with the panel; perhaps check to see if panel is connected to the computer?")
    #print(com('Hello World'))

print(os.name)

if __name__ == "__main__":
    init()