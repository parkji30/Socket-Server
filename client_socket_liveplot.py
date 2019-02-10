"""
This is the plot client socket, which will live plot data retrieved
from the publishing socket.

You can have multiple client sockets connected to the one publishing 
socket and have them run different refreshment rates and other 
parameters.

WARNING!
- if you set time.sleep in line 72 to be 0 or comment it out, you will
not have any data retrieved. time.sleep must be greater than 0.
"""

import os
os.chdir("/home/labuser/Desktop/googledrive/code/Samarium_control/github zmq") 
import zmq
from zmq_client_socket import zmq_client_socket
import matplotlib.pyplot as plt
import time

update_time = 2 #s

## Initialize Client socket Settings here! (You can run multiple clients on different shells)
connection_settings = {'ip_addr': 'localhost',  # ip address
                       'port': 5557,            # our open port
                       'update_period_ms': 1,                   # Not implemented yet
                       'logdata': False,                        # Not implemented yet
                       'topic': 'CTC100'}       # device

client_socket = zmq_client_socket(connection_settings)
client_socket.make_connection()


## Plot settings go here.
counter = 0
HePlt = plt.subplot(211)
NiPlt = plt.subplot(212) #you can add or remove subplots here.

title = "Cryostate Temperature"
axis_font = {'fontname':'Roboto', 'size':'12'}
title_font = {'fontname':'Roboto', 'size':'18'}

#Helium plot
HePlt.set_title(title, **title_font)
HePlt.set_ylabel('Helium Temperature [K]',**axis_font)

#Nitrogen plot
NiPlt.set_xlabel('Time [s]',**axis_font)
NiPlt.set_ylabel('Nitrogen Temperature [K]',**axis_font)
    
        
## Call this to run the Liveplot
while True:
    
    Time, TemperatureMeasurement = client_socket.read_on_demand()
    HeTemp = TemperatureMeasurement['HeTemp']
    NiTemp = TemperatureMeasurement['NiTemp']
    
    if counter == 0:
        t0 = Time
        counter = 1
    real_time = Time - t0 #starts the time count from 0.
    
    HePlt.grid()
    HePlt.plot(real_time, HeTemp, '.', color = 'b')
    NiPlt.grid()
    NiPlt.plot(real_time, NiTemp, '.', color = 'b')
    
    plt.pause(1e-9) #Pause time not important, just as small as possible
    time.sleep(update_time) #global variable defined above.
