import os
os.chdir("/home/labuser/Desktop/googledrive/code/Samarium_control/github zmq")  
from zmq_server_socket import zmq_server_socket
import zmq
import time
import random

publisher = zmq_server_socket(5560, "example")

while True:
    he_ra = 75 + random.randint(-10,10)
    ni_ra = 275 + random.randint(-10, 10)   
    data_dict = {'HeTemp' : he_ra, 'NiTemp' : ni_ra}
    publisher.send(data_dict) 
    publisher.print_current_data()   
    time.sleep(0.1)                     #
publisher.close()