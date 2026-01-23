from datetime import datetime

current_time = datetime.now()

print(current_time)        # will print the full date and time

import socket
print(socket.gethostname())

import os
print(os.getlogin())


import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

files = [f for f in os.listdir('.') if os.path.isfile(f)]

print (dir_path)
print (files)