import os

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

from dynamixel_sdk import *                 # Uses Dynamixel SDK library

# Protocol version
PROTOCOL_VERSION        = 2.0               # See which protocol version is used in the Dynamixel
#/dev/ttyS0 
# Default setting
BAUDRATE                = 57600             # Dynamixel default baudrate : 57600
DEVICENAME              = '/dev/ttyS0'    # Check which port is being used on your controller
                                            # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()


# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()

# Try to broadcast ping the Dynamixel
dxl_data_list, dxl_comm_result = packetHandler.broadcastPing(portHandler)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

print("Detected Dynamixel :")
for dxl_id in dxl_data_list:
    print("[ID:%03d] model version : %d | firmware version : %d" % (dxl_id, dxl_data_list.get(dxl_id)[0], dxl_data_list.get(dxl_id)[1]))

# Close port
portHandler.closePort()