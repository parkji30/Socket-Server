"""
The code here is not DEFINITE and must be adjusted to whatever DEVICE 
you are using. The settings below is set to CTC100 device in Vutha Lab.
It should be changed to other device settings.

Step 1) Initialize any directory and device settings. You first need to 
to import your topic_device of choice and import its address link.

Step 2) Initialize topic and port settings which will be used to create
a publishing socket

Step 3) change the parameters and add any extra details to the 
data_dict. 

The format for the data_dict is:
    {some measurement (e.g. Temp): ACTUAL VALUE,
     ...}
     
NOTE
Use time.sleep on line 54 to determine your data upload speed. If your
pub_init time.sleep is < your client_init time.sleep, then your client
socket will read less data than 
"""
import os
import time



##Initialize Directory and Device settings here! 
os.chdir("/home/labuser/Desktop/googledrive/code/Samarium_control/Widgets") # Change this to the directory containing your device code.
from CTC100 import CTC100
topic_device = CTC100("/dev/ttyACM1")   # Change this to whatever device you want to connect with the zmq socket.
if topic_device is None:
    print("No device was loaded.")
    exit()


## Intialize Topic and Port here.
# change this directory to where the zmq_sockets folder is.
os.chdir("/home/labuser/Desktop/googledrive/code/Samarium_control/Widgets/zmq_sockets")  
from zmq_server_socket import zmq_server_socket
topic = "CTC100"                        # Change this to whatever device you're going to use. 
port = 5557                             # If port is in use, enter a different 4 digit port number.


## Create a Publisher for the given Topic and Port.
publisher = zmq_server_socket(port, topic)

while True:
    NitrogenCryostatChannel = 2 
    HeliumCryostatChannel = 1   
    HeTemp = topic_device.read(HeliumCryostatChannel)
    NiTemp = topic_device.read(NitrogenCryostatChannel)
    data_dict = {'HeTemp' : HeTemp, 'NiTemp' : NiTemp}
    publisher.send(data_dict) 
    publisher.print_current_data()    # toggle comment if you want to publisher to print data.
    #time.sleep(0.1)                     # change time.sleep to determine upload speed to the publishing socket.
publisher.close()